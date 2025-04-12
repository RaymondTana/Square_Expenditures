# Square_Expenditures

This repository helps anyone view their expenditures as reported to their email by Square. It serves as the source code to the deployed app.

The app is hosted by Render at https://square-expenditures.onrender.com.

## Expectations

The tool expects that you receive Square receipts to a Gmail address. The emails detected in this app will be any from the sender: `messenger@messaging.squareup.com`. In order to access your mailboxes, you will need both:

1. Your Gmail address (e.g., `user@gmail.com`)
2. An "App Password" (e.g. `abcd efgh ijkl mnop`)

## Demo

[![Watch the video](https://img.youtube.com/vi/4fTY-ju8dD4/maxresdefault.jpg)](https://youtu.be/4fTY-ju8dD4)

## Implementation

The app is designed as a dashboard using a combination of Plotly Dash and Dash Mantine components. The backend is almost entirely written in Python (version 3.12.8).

All requirements can be found in `requirements.txt`. 