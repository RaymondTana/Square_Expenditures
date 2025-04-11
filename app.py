import os
from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for production

@app.route('/', methods=['GET'])
def index():
    # Render the main page with file upload form.
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash("No file part in the request")
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash("No file selected")
        return redirect(request.url)
    
    try:
        # Read the CSV file. We assume the CSV has columns: date, total_price, business_name.
        df = pd.read_csv(file, parse_dates=["date"])
        df['datetime'] = pd.to_datetime(df['date'])
        
        # Determine aggregation type based on form selection: day or month.
        agg_by = request.form.get('aggregation', 'day')
        if agg_by == 'month':
            # Aggregate by month (convert to first day of month)
            df['period'] = df['datetime'].dt.to_period('M').dt.to_timestamp()
        else:
            # Aggregate by day (use the date part)
            df['period'] = df['datetime'].dt.date
        
        # Create a receipt info string for hover details.
        df['receipt_info'] = df.apply(
            lambda row: f"{row['datetime'].strftime('%b %d, %Y')}: {row['business_name']} - ${row['total_price']:.2f}", axis=1
        )
        
        # Group by period: sum total spending and concatenate top 3 receipt infos.
        grouped = df.groupby('period').agg({
            'total_price': 'sum',
            'receipt_info': lambda x: "<br>".join(x.head(3)) + ("<br>..." if len(x) > 3 else "")
        }).reset_index()
        
        # Create an interactive Plotly bar chart.
        fig = px.bar(
            grouped,
            x='period',
            y='total_price',
            hover_data={'receipt_info': True},
            labels={'total_price': 'Total Spending ($)', 'period': 'Date'},
            title=f"Spending Over Time ({agg_by.title()} Aggregation)"
        )
        
        # Customize the hover text.
        fig.update_traces(
            hovertemplate='<b>Date:</b> %{x}<br>'
                          '<b>Total:</b> $%{y:.2f}<br>'
                          '<b>Receipts:</b><br>%{customdata[0]}<extra></extra>'
        )
        
        # Convert the Plotly figure to an HTML snippet.
        graph_html = pio.to_html(fig, full_html=False)
        
        return render_template('chart.html', graph_html=graph_html)
    
    except Exception as e:
        flash(f"Error processing file: {e}")
        return redirect(url_for('index'))

if __name__ == '__main__':
    # For local development; in production, Render will use gunicorn as per the Procfile.
    app.run(debug=True)
