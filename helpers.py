# Handling emails
import imaplib
import email
from bs4 import BeautifulSoup
import re

# Handling messages
from inspect import stack

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
def plot_spending_bar_interactive(receipts_df, by='day', max_receipts_displayed=3, bar_color=DASH_NICE_BLUE, marker_line_color=DEFUALT_LINE_COLOR, marker_line_width=DEFAULT_LINE_WIDTH):
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
        title=f"Spending Over Time by ({by.title()})"
    )
    
    fig.update_traces(
        hovertemplate='<b>Date:</b> %{x}<br>' +
                      '<b>Total:</b> $%{y:.2f}<br>' +
                      '<b>Receipts:</b><br>%{customdata[0]}<extra></extra>'
    )
    
    # Update the colors
    fig.update_traces(marker_color=bar_color, marker_line_color=marker_line_color, marker_line_width=marker_line_width)

    fig.update_layout(xaxis_tickangle=-45)
    return fig

def create_dataframe_preview(df: pd.DataFrame):
    # Convert the dataframe header (columns) and body (rows) into a dictionary format for dmc.Table.
    table_data = {
        'caption': f"Data preview (First {MAX_ROWS_DISPLAY_PANDAS} Rows)",
        'head': df.columns,
        'body': df.head(MAX_ROWS_DISPLAY_PANDAS).values.tolist()
    }
    
    # Create a dmc.Table and wrap it in a Div to control its size and scrollability
    preview_table = dmc.Table(
        id = 'df-preview--table',
        className = 'summary-table',
        data = table_data,
        striped = True,
        highlightOnHover = True,
        withColumnBorders = True,
        style = {'--table-caption-side': 'top'}
    )
    
    return preview_table

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