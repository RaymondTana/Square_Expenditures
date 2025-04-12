# Handling emails
import imaplib
import email
from bs4 import BeautifulSoup
import re

# Handling messages
import inspect

from time import sleep
import os
from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import plotly.express as px
import plotly.io as pio
from hyperparameters import *

# Pandas
from pandas import set_option, core, DataFrame, concat, read_csv, options
set_option("display.max_rows", MAX_ROWS_DISPLAY_PANDAS)
options.plotting.backend = PLOTTING_BACKEND

# IPython
from IPython.display import HTML
import ipywidgets as widgets

# Plotly
from plotly.graph_objects import Scatter, Figure, Bar
from plotly.subplots import make_subplots

# Dash Mantine
import dash_mantine_components as dmc
from dash import Dash, dcc, html, no_update, clientside_callback
from dash.dependencies import Input, Output, State
import dash.dependencies
dash._dash_renderer._set_react_version(REACT_VERSION)

# Helper function to format prices
def to_price(x):
    return f"${x:,.2f}"

# Finds the business name, receipt total, and date for each email message
def extract_data_from_email(message):
    subject = message['subject']

    payload = message.get_payload(decode = True)

    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == 'text/html':
                payload = part.get_payload(decode = True)
                break

    soup = BeautifulSoup(payload, 'html.parser')
    body_text = soup.get_text()

    # Busines name
    business_name = subject.removeprefix("Receipt from ").strip()

    # Total price
    total_price = float(re.findall(r'\$\d+\.\d{2}', body_text)[0][1:])

    # Date from header
    raw_date = message['Date']

    return business_name, total_price, raw_date

# The plot function that creates the Plotly bar chart.
def plot_spending_bar_interactive(receipts_df, by='day', max_receipts_displayed=3):
    df = receipts_df.copy()
    df['datetime'] = pd.to_datetime(df['datetime'])

    if by == 'month':
        df['period'] = df['datetime'].dt.to_period('M').dt.to_timestamp()
    elif by == 'week':
        df['period'] = df['datetime'].dt.to_period('W').dt.to_timestamp()
    else:
        df['period'] = df['datetime'].dt.date

    # Create a string for each receipt for hover info.
    df['receipt_info'] = df.apply(
        lambda row: f"{row['datetime'].strftime('%b %d %Y')}: {row['business_name']} - ${row['total_price']:.2f}", axis=1
    )

    # Group by the computed period.
    grouped = df.groupby('period').agg({
        'total_price': 'sum',
        'receipt_info': lambda x: "<br>".join(x.head(max_receipts_displayed)) +
                                   ('<br>…' if len(x) > max_receipts_displayed else '')
    }).reset_index()

    fig = px.bar(
        grouped,
        x='period',
        y='total_price',
        hover_data={'receipt_info': True},
        labels={'total_price': 'Total Spending ($)', 'period': 'Date'},
        title=f"Spending Over Time ({by.title()} Aggregation)"
    )
    
    fig.update_traces(
        hovertemplate='<b>Date:</b> %{x}<br>' +
                      '<b>Total:</b> $%{y:.2f}<br>' +
                      '<b>Receipts:</b><br>%{customdata[0]}<extra></extra>'
    )
    
    fig.update_layout(xaxis_tickangle=-45)
    return fig


# ------------------------ Markdown ------------------------

# Handle the Markdown files that fill much of the text found across the tabs
markdown_files = {
    'Help' : MARKDOWN_HELP,
}

# Read a text/Markdown/etc. file's contents, properly opening/closing it 
def get_text(filename):
    """ get_text(filename: str): str | Return complete file contents """
    f = open(filename, encoding = ENCODING)
    read = f.read()
    f.close()
    return read


# Method to get markdown file if exists
def read_markdown(tab):
    return get_text(markdown_files[tab]) if tab in markdown_files else ''

# --------

SETTINGS_DRAWER_CHILDREN = [
    # Dark/Light Mode
    dmc.Switch(
        id = 'dark-mode--swtich',
        label = 'Dark Mode',
        thumbIcon = dmc.Image(src = DARK_MODE_ICON, w = ICON_SIZE),
        size = 'lg',
        color = SWITCH_COLOR,
        checked = False,
    ),
    
    # ColorInput for Points
    dmc.ColorInput(
        id = 'points--colorinput',
        label = POINT_COLORINPUT_LABEL,
        value = MARKER_COLOR,
        w = 250,
        format = 'hex',
        withPicker = True,
        withPreview = True,
        withEyeDropper = True,
        disallowInput = False,
        swatches = DEFAULT_SWATCH,
    ),
    
    # ColorInput for Curves
    dmc.ColorInput(
        id = 'curves--colorinput',
        label = CURVE_COLORINPUT_LABEL,
        value = FITTED_CURVE_STROKE,
        w = 250,
        format = 'hex',
        withPicker = True,
        withPreview = True,
        withEyeDropper = True,
        disallowInput = False,
        swatches = DEFAULT_SWATCH,
        className = 'settings-colorinput',
    ),
    
    # ColorInput for Secondary Curves
    dmc.ColorInput(
        id = 'curves-2--colorinput',
        label = CURVE_COLORINPUT_LABEL_2,
        value = FITTED_CURVE_STROKE_2,
        w = 250,
        format = 'hex',
        withPicker = True,
        withPreview = True,
        withEyeDropper = True,
        disallowInput = False,
        swatches = DEFAULT_SWATCH,
        className = 'settings-colorinput',
    ),
    
    # ColorInput for Prediction Window
    dmc.ColorInput(
        id = 'prediction--colorinput',
        label = PREDICTION_WINDOW_COLORINPUT_LABEL,
        value = PREDICTION_FILL,
        w = 250,
        format = 'hex',
        withPicker = True,
        withPreview = True,
        withEyeDropper = True,
        disallowInput = False,
        swatches = DEFAULT_SWATCH,
        className = 'settings-colorinput',
    ),
    
    html.Div(children = [
        dmc.Text('Marks size', size = 'sm'),
        # Marker Size
        dmc.Slider(
            id = 'marks-size--slider',
            min = 1, 
            max = 15,
            value = DEFAULT_MARKER_SIZE,
            step = 1,
            marks = [{'value': i, 'label': i} for i in range(5, 16, 5)],
            # labelAlwaysOn = True,
            color = SLIDER_COLOR,
        )
    ], className = 'settings-slider'),
    
    html.Div(children = [
        dmc.Text('Curve width', size = 'sm'),
        # Marker Size
        dmc.Slider(
            id = 'curve-width--slider',
            min = 1, 
            max = 15,
            value = DEFAULT_LINE_WIDTH,
            step = 1,
            marks = [{'value': i, 'label': i} for i in range(5, 16, 5)],
            color = SLIDER_COLOR,
        )
    ], className = 'settings-slider'),
    
    # Curve dash type
    dmc.Select(
        id = 'curve-dash--select',
        label = SELECT_CURVE_DASH_LABEL,
        data = CURVE_DASHES,
        value = DEFAULT_CURVE_DASH,
        searchable = False,
        clearable = False,
        className = 'select-dash',
    ),
    
] # END SETTINGS_DRAWER


TOOL_TAB = [    
    # Container div for all content
    html.Div(className = 'content-div', children = [
        dmc.Title('Tool', order = 1),

        dcc.Markdown("This tool lets you visualize any expenditures made on a Square device. It only works if you for purchases for which you have an email receipt from Square (from: `messenger@messaging.squareup.com`). The tool also assumes your email address if Gmail."),

        dcc.Markdown("Enter your Gmail address and an \"App Password\" to start. See the `Help` tab if you run into issues."),

        dmc.Stack(
            children=[
                dmc.TextInput(
                    id = 'gmail-address--textinput', 
                    description = 'Please include the @gmail.com',
                    label = 'Your Gmail address:', 
                    placeholder = 'user@gmail.com', 
                    value = 'rayjfriend@gmail.com',
                    w = 250, 
                    required = True, 
                    leftSection = dmc.Image(src = EMAIL_ICON, w = ICON_SIZE)
                ),
                dmc.PasswordInput(
                    id = 'app-password--textinput', 
                    description = 'This will be a 16-character passcode',
                    label = 'Your app password:', 
                    w = 250, 
                    required = True,
                    value = 'rvkl ydwv ukqz trev',
                    placeholder = 'abcd efgh ijkl mnop', 
                    leftSection = dmc.Image(src = PASSWORD_ICON, w = ICON_SIZE)
                ),
                dmc.Button(
                    'Search for Square Receipts',
                    id = 'search--button',
                    loading = False,
                    leftSection = dmc.Image(src = SEARCH_ICON, w = ICON_SIZE),
                    color = BUTTON_COLOR
                ),
            ],
        ),

        html.Div(id = 'valid-query--div', className = 'valid-div', children = [
            dmc.Divider(size = 'xs', label = 'Generated Output'),

            # Radio group to choose aggregation (day, week, month).
            dmc.RadioGroup(
                id='agg-by-radio',
                value='day',
                children=[
                    dmc.Radio(label="Day", value='day'),
                    dmc.Radio(label="Week", value='week'),
                    dmc.Radio(label="Month", value='month')
                ],
                label="Aggregate by:"
            ),
            
            # Graph component to display the interactive Plotly chart.
            dcc.Graph(id='spending-graph', className='plot'),
            
            # Table component to show summary stats.
            dmc.Table(
                id='summary-table',
                striped=True,
                highlightOnHover=True,
                withColumnBorders=True,
                data={"caption": "", "head": [], "body": []},
                className='summary-table'
            )
        ]),

    ]) # END CONTAINER DIV OF ALL CONTENT
] # END DOCUMENTATION

HELP_TAB = [    
    # Container div for all content
    html.Div(className = 'content-div', children = [
        dmc.Title('Help', order = 1),
        dcc.Markdown(read_markdown('Help'), mathjax = True),
    ]) # END CONTAINER DIV OF ALL CONTENT
] # END DOCUMENTATION

APP_CHILDREN = [
    # invisible email data stored as dictionary
    dcc.Store(data = {}, id = 'email-data--store'), 

    # Heading, padding
    html.Div(children = [
        
        dmc.Grid(align = 'center', justify = 'space-between', gutter = 'md', children = [
            dmc.GridCol(span = 'content', children = [
                # Heading
                dcc.Markdown(f'''
                    # Square Receipts Visualizer
                    ''',
                ),
            ]), 
            dmc.GridCol(span = 'auto', children = [
            ]), 
            dmc.GridCol(span = 'content', children = [
                # Settings drawer
                dmc.Drawer(
                    id = 'settings--drawer',
                    position = 'right',
                    children = SETTINGS_DRAWER_CHILDREN,
                ),
                dmc.Button(
                    dmc.Image(src = SETTINGS_ICON, w = ICON_SIZE), 
                    id = 'settings--button', 
                    color = BUTTON_COLOR
                ),
            ]),
        ]),
    ]), # END HEADER

    dmc.Divider(size = 'xs'),
        
    # Tabs Content
    dmc.Tabs([
        dmc.TabsList([
            dmc.TabsTab('Tool', value = 'Tool'),
            dmc.TabsTab('Help', value = 'Help'),
        ]),
        dmc.TabsPanel(TOOL_TAB, value = 'Tool'),
        dmc.TabsPanel(HELP_TAB, value = 'Help'),
    ], id = 'tabs', value = 'Tool', color = TABS_COLOR),
]

app = Dash(__name__, external_stylesheets = EXTERNAL_STYLESHEETS)

app.layout = html.Div(
    style={"margin": "25px", "padding": "10px"},  # Set global margin here
    children=[
        dmc.MantineProvider(
            forceColorScheme=APP_COLOR_SCHEME,
            theme=APP_THEME,
            children=APP_CHILDREN,
            id='window-app--mantineprovider'
        )
    ]
)

# --- search button callbacks

# Search button looks like it's loading once clicked
clientside_callback(
    """
    function updateLoadingState(n_clicks) {
        return true
    }
    """,
    Output('search--button', 'loading', allow_duplicate=True),
    Input('search--button', 'n_clicks'),
    prevent_initial_call = True,
)

# Click the search button... query Gmail
@app.callback(
    Output('email-data--store', 'data'),
    Output('search--button', 'loading'),
    Output('valid-query--div', 'style'),
    Input('search--button', 'n_clicks'),
    State('gmail-address--textinput', 'value'),
    State('app-password--textinput', 'value'),
    prevent_initial_call = True,
)
def check_for_emails(n_clicks, username, password):
    try: 

        print(f'Starting to search for emails in the mailbox(es) {BUZON} for {username}')

        # set up IMAP connection and attempt login
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(username, password)

        # specify inbox
        mail.select(BUZON)

        # make query
        typ, data = mail.search(None, f'(FROM "{SENDER}")')

        # capture hits to the query
        email_ids = data[0].split()
        messages = [
            email.message_from_bytes(mail.fetch(eid, '(RFC822)')[1][0][1])
            for eid in email_ids
        ]
        mail.logout()

        print(f'Found {len(messages)} emails from {SENDER}')

        # build the dataframe by parsing the emails emails
        receipts_df = pd.DataFrame([
            extract_data_from_email(message) for message in messages
        ], columns = ['business_name', 'total_price', 'date'])

        # force the date format to be in a standard datetime format suitable for plotting
        receipts_df['datetime'] = pd.to_datetime(receipts_df['date'], format = 'mixed')

        # save the dataframe for use by other components
        return receipts_df.to_dict('records'), False, {'display': 'inline'}
    
    except Exception as e:
        print(f'{CALLBACK_ERROR_MESSAGE}{stack()[0].function}')
        print(e)
        return no_update, False, no_update


# --- callbacks when emails received

# Callback to update the chart and summary table when the data or radio selection changes.
@app.callback(
    Output('spending-graph', 'figure'),
    Output('summary-table', 'data'),
    Input('email-data--store', 'data'),
    Input('agg-by-radio', 'value'),
    prevent_initial_call = True
)
def update_dashboard(email_data, agg_by):
    if email_data is None:
        return no_update, no_update
    try:
        # Convert the stored data into a DataFrame.
        df = pd.DataFrame(email_data)
        
        # Generate the Plotly bar chart.
        fig = plot_spending_bar_interactive(df, by=agg_by)
        
        # Calculate supplementary statistics.
        total_across_receipts = df['total_price'].sum()
        average_per_receipt = total_across_receipts / len(df) if len(df) > 0 else 0
        popular_business = df['business_name'].mode()[0] if not df['business_name'].mode().empty else "N/A"
        total_popular = df.loc[df['business_name'] == popular_business, 'total_price'].sum()

        # Create the summary table data.
        summary_table_data = {
            'caption': 'Summary Statistics',
            'head': [["Metric", "Value"]],
            'body': [
                ["Total money spent across receipts", to_price(total_across_receipts)],
                ["Average total per transaction", to_price(average_per_receipt)],
                [f"Total spent at {popular_business} all time", to_price(total_popular)]
            ]
        }
        return fig, summary_table_data
    except Exception as e:
        import inspect
        print(f"Error in {inspect.stack()[0].function}: {e}")
        return no_update, no_update

# --- settings callbacks


# How the drawer updates with settings button interaction
@app.callback(
    Output('settings--drawer', 'opened'),
    Input('settings--button', 'n_clicks'),
    prevent_initial_call = True,
)
def toggle_drawer(n_clicks):
    return True

# Toggle dark mode when interact with corresponding switch
@app.callback(
    Output('window-app--mantineprovider', 'forceColorScheme'),
    Input('dark-mode--swtich', 'checked')
)
def toggle_dark_mode(dark_checked):
    return 'dark' if dark_checked else 'light'

if __name__ == '__main__':
    app.run_server(debug = True, port="5000")