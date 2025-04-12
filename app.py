# from helpers import *

# SETTINGS_DRAWER_CHILDREN = [
#     # Dark/Light Mode
#     dmc.Switch(
#         id = 'dark-mode--swtich',
#         label = 'Dark Mode',
#         thumbIcon = dmc.Image(src = DARK_MODE_ICON, w = ICON_SIZE),
#         size = 'lg',
#         color = SWITCH_COLOR,
#         checked = False,
#     ),
    
#     # ColorInput for Bar fill
#     dmc.ColorInput(
#         id = 'bar--colorinput',
#         label = BAR_COLORINPUT_LABEL,
#         value = DASH_NICE_BLUE,
#         w = 250,
#         format = 'hex',
#         withPicker = True,
#         withPreview = True,
#         withEyeDropper = True,
#         disallowInput = False,
#         swatches = DEFAULT_SWATCH,
#         className = 'settings-colorinput',
#     ),

#     # ColorInput for Outline
#     dmc.ColorInput(
#         id = 'outline--colorinput',
#         label = OUTLINE_COLORINPUT_LABEL,
#         value = DEFUALT_LINE_COLOR,
#         w = 250,
#         format = 'hex',
#         withPicker = True,
#         withPreview = True,
#         withEyeDropper = True,
#         disallowInput = False,
#         swatches = DEFAULT_SWATCH,
#         className = 'settings-colorinput',
#     ),
    
#     html.Div(children = [
#         dmc.Text(WIDTH_SLIDER_LABEL, size = 'sm'),
#         # Marker Size
#         dmc.Slider(
#             id = 'stroke-width--slider',
#             min = 0, 
#             max = 5,
#             value = DEFAULT_LINE_WIDTH,
#             step = 0.5,
#             marks = [{'value': i, 'label': i} for i in range(1, 6)],
#             color = SLIDER_COLOR,
#         )
#     ], className = 'settings-slider'),
    
# ] # END SETTINGS_DRAWER

# TOOL_TAB = [    
#     # Container div for all content
#     html.Div(className = 'content-div', children = [
#         dmc.Title('Tool', order = 1),

#         dcc.Markdown("This tool lets you visualize any expenditures made on a Square device. It only works if you for purchases for which you have an email receipt from Square (from: `messenger@messaging.squareup.com`). The tool also assumes your email address if Gmail."),

#         dcc.Markdown("Enter your Gmail address and an \"App Password\" to start. See the `Help` tab if you run into issues."),

#         dmc.Stack(children=[
#             dmc.TextInput(
#                 id = 'gmail-address--textinput', 
#                 description = 'Please include the @gmail.com',
#                 label = 'Your Gmail address:', 
#                 placeholder = 'user@gmail.com',
#                 w = 250, 
#                 required = True, 
#                 leftSection = dmc.Image(src = EMAIL_ICON, w = ICON_SIZE)
#             ),
#             dmc.PasswordInput(
#                 id = 'app-password--textinput', 
#                 description = 'This will be a 16-character passcode',
#                 label = 'Your app password:', 
#                 w = 250, 
#                 required = True,
#                 placeholder = 'abcd efgh ijkl mnop', 
#                 leftSection = dmc.Image(src = PASSWORD_ICON, w = ICON_SIZE)
#             ),
#             dmc.Button(
#                 'Search for Square Receipts',
#                 id = 'search--button',
#                 loading = False,
#                 className = 'search-button',
#                 leftSection = dmc.Image(src = SEARCH_ICON, w = ICON_SIZE),
#                 color = BUTTON_COLOR
#             ),
#         ]),

#         # Hidden until valid dataframe obtained
#         html.Div(id = 'valid-query--div', className = 'valid-div', children = [

#             # Divider
#             dmc.Divider(size = 'xs', label = 'Generated Output', className = 'divider'),  

#             # Graph component to display the interactive Plotly chart.
#             dcc.Graph(id = 'spending-graph', className = 'plot'), 

#             # Grid
#             dmc.Grid(className = 'components-grid', style = {'margin': '0px 40px 0px 40px'}, children = [
#                 dmc.GridCol(span = 'auto', children = [
#                     dmc.Stack(children = [
#                         dmc.Select(
#                             id = 'by-time--select',
#                             label = 'Select Time Aggregation',
#                             data = [{'value': 'day', 'label': 'Group by Day'}, {'value': 'week', 'label': 'Group by Week'}, {'value': 'month', 'label': 'Group by Month'},],
#                             value = 'week', # base-64 still
#                             clearable = False,
#                             searchable = False,
#                             allowDeselect = False
#                         ),
#                         dmc.Grid(children = [
#                             dmc.GridCol(span = 4, children = [
#                                 dmc.Button(
#                                     'Export Data', 
#                                     leftSection = dmc.Image(src = EXPORT_ICON, w = ICON_SIZE),
#                                     id = 'export-data--button',
#                                     className = 'export-button',
#                                     color = BUTTON_COLOR,
#                                     fullWidth = True,
#                                 ),
#                                 dcc.Download(id = 'export-data--download'),
#                             ]),
#                             dmc.GridCol(span = 8, children = [
#                                 dmc.Select(
#                                     id = 'export--select',
#                                     label = 'Select Export Type',
#                                     data = [{'value': 'csv', 'label': 'CSV (.csv)'}, {'value': 'xlsx', 'label': 'Excel (.xlsx)'},],
#                                     value = 'csv', # base-64 still
#                                     clearable = False,
#                                     searchable = False,
#                                     allowDeselect = False
#                                 ),
#                             ])
#                         ]),
#                     ]),
#                 ]),
#                 dmc.GridCol(span = 6, children = [
#                     # Table component to show summary stats.
#                     dmc.Table(
#                         id = 'summary-table',
#                         striped = True,
#                         horizontalSpacing = 10,
#                         highlightOnHover = True,
#                         withColumnBorders = True,
#                         data = {'caption': 'Quick insights into your expenditures', 'head': [], 'body': []},
#                         className = 'summary-table',
#                     ),
#                 ]),
#             ]),            
        
#             # Scrollable DF
#             dmc.Space(id = 'scrollable--space', children=[],
#                 # Use inline style to limit height, force scrolling and control width.
#                 style={'maxHeight': '400px', 'overflowY': 'auto', 'width': '80%', 'margin': '0 auto'}
#             ,)
#         ]), # End hidden div
#     ]) # End div of all the tab's content
# ] # End Tool Tab

# HELP_TAB = [    
#     # Container div for all content
#     html.Div(className = 'content-div', children = [
#         dmc.Title('Help', order = 1),
#         dcc.Markdown(read_markdown('Help'), mathjax = True),
#     ]) # End div with all tab content
# ] # End Help Tab

# APP_CHILDREN = [
#     # invisible email data stored as dictionary
#     dcc.Store(data = {}, id = 'email-data--store'), 

#     # Heading, padding
#     html.Div(children = [
        
#         dmc.Grid(align = 'center', justify = 'space-between', gutter = 'md', children = [
#             dmc.GridCol(span = 'content', children = [
#                 # Heading
#                 dcc.Markdown(f'''
#                     # Square Receipts Visualizer
#                     ''',
#                 ),
#             ]), 
#             dmc.GridCol(span = 'auto', children = [
#             ]), 
#             dmc.GridCol(span = 'content', children = [
#                 # Settings drawer
#                 dmc.Drawer(
#                     id = 'settings--drawer',
#                     position = 'right',
#                     children = SETTINGS_DRAWER_CHILDREN,
#                 ),
#                 dmc.Button(
#                     dmc.Image(src = SETTINGS_ICON, w = ICON_SIZE), 
#                     id = 'settings--button', 
#                     color = BUTTON_COLOR
#                 ),
#             ]),
#         ]),
#     ]), # END HEADER

#     dmc.Divider(size = 'xs'),
        
#     # Tabs Content
#     dmc.Tabs([
#         dmc.TabsList([
#             dmc.TabsTab('Tool', value = 'Tool'),
#             dmc.TabsTab('Help', value = 'Help'),
#         ]),
#         dmc.TabsPanel(TOOL_TAB, value = 'Tool'),
#         dmc.TabsPanel(HELP_TAB, value = 'Help'),
#     ], id = 'tabs', value = 'Tool', color = TABS_COLOR),
# ]

# app = Dash(__name__, external_stylesheets = [EXTERNAL_CSS_SHEET])
# app.layout = html.Div(
#     style = {'margin': '25px', 'padding': '10px'}, 
#     children=[
#         dmc.MantineProvider(
#             forceColorScheme = APP_COLOR_SCHEME,
#             theme = APP_THEME,
#             children = APP_CHILDREN,
#             id = 'app--mantineprovider'
#         )
#     ]
# )

# # --- search button callbacks

# # Search button looks like it's loading once clicked
# clientside_callback(
#     """
#     function updateLoadingState(n_clicks) {
#         return true
#     }
#     """,
#     Output('search--button', 'loading', allow_duplicate=True),
#     Input('search--button', 'n_clicks'),
#     prevent_initial_call = True,
# )

# # Click the search button... query Gmail
# @app.callback(
#     Output('email-data--store', 'data'),
#     Output('search--button', 'loading'),
#     Output('valid-query--div', 'style'),
#     Input('search--button', 'n_clicks'),
#     State('gmail-address--textinput', 'value'),
#     State('app-password--textinput', 'value'),
#     prevent_initial_call = True,
# )
# def check_for_emails(n_clicks, username, password):
#     try:         

#         # set up IMAP connection and attempt login
#         mail = imaplib.IMAP4_SSL(IMAP_SERVER)
#         mail.login(username, password)

#         # specify inbox
#         mail.select(BUZON)

#         # make query
#         typ, data = mail.search(None, f'(FROM "{SENDER}")')

#         # capture hits to the query
#         email_ids = data[0].split()
#         messages = [
#             email.message_from_bytes(mail.fetch(eid, '(RFC822)')[1][0][1])
#             for eid in email_ids
#         ]
#         mail.logout()

#         # build the dataframe by parsing the emails emails
#         receipts_df = pd.DataFrame([
#             extract_data_from_email(message) for message in messages
#         ], columns = ['business_name', 'total_price', 'date'])

#         # force the date format to be in a standard datetime format suitable for plotting
#         receipts_df['datetime'] = pd.to_datetime(receipts_df['date'], format = 'mixed')

#         print(f'Found {len(messages)} emails from {SENDER}.')

#         # save the dataframe for use by other components
#         return receipts_df.to_dict('records'), False, {'display': 'inline'}
    
#     except Exception as e:
#         print(f'{CALLBACK_ERROR_MESSAGE}{stack()[0].function}')
#         print(e)
#         return no_update, False, no_update

# # --- callbacks when emails received

# # Callback to update the chart and summary table when the data or radio selection changes.
# @app.callback(
#     Output('spending-graph', 'figure'),
#     Input('email-data--store', 'data'),
#     Input('by-time--select', 'value'),
#     Input('bar--colorinput', 'value'),
#     Input('outline--colorinput', 'value'),
#     Input('stroke-width--slider', 'value'),
#     prevent_initial_call = True
# )
# def update_output(email_data, agg_by, bar_color, marker_line_color, marker_line_width):
#     if email_data is None:
#         return no_update
#     try:
#         # Convert the stored data into a DataFrame.
#         df = pd.DataFrame(email_data)
        
#         # Generate the Plotly bar chart.
#         fig = plot_spending_bar_interactive(df, by = agg_by, bar_color=bar_color, marker_line_color=marker_line_color, marker_line_width=marker_line_width)

#         return fig
#     except Exception as e:
#         import inspect
#         print(f"Error in {inspect.stack()[0].function}: {e}")
#         return no_update
    
# # Callback to update the chart and summary table when the data or radio selection changes.
# @app.callback(
#     Output('summary-table', 'data'),
#     Output('scrollable--space', 'children'),
#     Input('email-data--store', 'data'),
#     prevent_initial_call = True
# )
# def update_output(email_data):
#     if email_data is None:
#         return no_update, no_update
#     try:
#         # Convert the stored data into a DataFrame.
#         df = pd.DataFrame(email_data)
        
#         # Calculate supplementary statistics.
#         total_across_receipts = df['total_price'].sum()
#         average_per_receipt = total_across_receipts / len(df) if len(df) > 0 else 0
#         popular_business = df['business_name'].mode()[0] if not df['business_name'].mode().empty else "N/A"
#         total_popular = df.loc[df['business_name'] == popular_business, 'total_price'].sum()

#         # Create the summary table data.
#         summary_table_data = {
#             'caption': 'Quick insights into your expenditures',
#             'head': ['Insight', 'Value'],
#             'body': [
#                 ["Total money spent across receipts", to_price(total_across_receipts)],
#                 ["Average total per transaction", to_price(average_per_receipt)],
#                 [f"Total spent at {popular_business} all time", to_price(total_popular)]
#             ]
#         }

#         pretty_df = df[['business_name', 'total_price', 'date']].copy().rename(columns = {'business_name': 'Business Name', 'total_price': 'Total ($)', 'date': 'Date'})

#         preview_table = create_dataframe_preview(pretty_df)

#         return summary_table_data, [preview_table]
#     except Exception as e:
#         import inspect
#         print(f"Error in {inspect.stack()[0].function}: {e}")
#         return no_update

# # --- export button

# # Define action of the Export Data button 
# @app.callback(
#     Output('export-data--download', 'data'),
#     Input('export-data--button', 'n_clicks'),
#     State('email-data--store', 'data'),
#     State('export--select', 'value'),
#     State('gmail-address--textinput', 'value'),
#     prevent_initial_call = True
# )
# def export_graph_button(n_clicks, pre_df, export_type, username):
#     try: 
#         df = DataFrame(pre_df)
#         savepath = f'square_expenditures_for_{username.split("@")[0]}.{export_type}'
#         if export_type == 'csv':
#             return dcc.send_data_frame(df.to_csv, savepath, index = False, encoding = ENCODING)
#         elif export_type == 'xlsx':
#             return dcc.send_data_frame(df.to_excel, savepath, index = False)
#         else:
#             return None
    
#     except Exception as e:
#         print(f'{CALLBACK_ERROR_MESSAGE}{stack()[0].function}')
#         print(e)
#         return no_update

# # --- settings callbacks

# # How the drawer updates with settings button interaction
# @app.callback(
#     Output('settings--drawer', 'opened'),
#     Input('settings--button', 'n_clicks'),
#     prevent_initial_call = True,
# )
# def toggle_drawer(n_clicks):
#     return True

# # Toggle dark mode when interact with corresponding switch
# @app.callback(
#     Output('app--mantineprovider', 'forceColorScheme'),
#     Input('dark-mode--swtich', 'checked')
# )
# def toggle_dark_mode(dark_checked):
#     return 'dark' if dark_checked else 'light'

# if __name__ == '__main__':
#     print('''
# ###################
# Restarting the app.
# ###################
#         ''')
#     app.run()

import dash
from dash import html

# Create your Dash app.
app = dash.Dash(__name__)
app.layout = html.Div("Hello from Dash!")

# Explicitly expose the underlying Flask server.
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)