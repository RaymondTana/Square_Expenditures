# This file contains many adjustable hyperparameters for the app

""" Execution settings """
BASE_URL = 'http://127.0.0.1:5000'
DEBUG = False

""" Email settings """
IMAP_SERVER = 'imap.gmail.com'
SENDER = 'messenger@messaging.squareup.com'
BUZON = '"[Gmail]/All Mail"'

"""Local directory structure"""
MARKDOWN_HELP = 'assets/markdown/help.md'
DARK_MODE_ICON = 'assets/icons/tdesign--mode-dark.svg'
SETTINGS_ICON = 'assets/icons/solar--settings-linear.svg'
EXPORT_ICON = 'assets/icons/mdi--export.svg'
SAVE_ICON = 'assets/icons/ic--round-save-alt.svg'
EMAIL_ICON = 'assets/icons/ic--round-alternate-email.svg'
PASSWORD_ICON = 'assets/icons/material-symbols--shield-lock-outline.svg'
SEARCH_ICON = 'assets/icons/mdi--sql-query.svg'

"""Library settings"""
MAX_ROWS_DISPLAY_PANDAS = 100
REACT_VERSION = '18.2.0'
PLOTTING_BACKEND = 'plotly'
ENCODING = 'utf-8-sig'

"""Dash theme settings"""
ASML_COLOR = '#10069f'
DASH_NICE_BLUE = '#636efa'
APP_COLOR_SCHEME = 'light'
APP_THEME = {
    'primaryColor': 'indigo',
    'fontFamily': "'Inter', sans-serif",
    'components': {
        'Button': {'defaultProps': {'fw': 400}},
        'Alert': {'styles': {'title': {'fontWeight': 500}}},
        'AvatarGroup': {'styles': {'truncated': {'fontWeight': 500}}},
        'Badge': {'styles': {'root': {'fontWeight': 500}}},
        'Progress': {'styles': {'label': {'fontWeight': 500}}},
        'RingProgress': {'styles': {'label': {'fontWeight': 500}}},
        'CodeHighlightTabs': {'styles': {'file': {'padding': 12}}},
        'Table': {
            'defaultProps': {
                'highlightOnHover': True,
                'withTableBorder': True,
                'verticalSpacing': 'sm',
                'horizontalSpacing': 'md',
            }
        }
    }
}
DEFAULT_SWATCH = [
    '#25262b',
    '#868e96',
    '#fa5252',
    '#e64980',
    '#be4bdb',
    '#7950f2',
    '#4c6ef5',
    '#636efa',
    '#228be6',
    '#12b886',
    '#40c057',
    '#82c91e',
    '#fab005',
    '#fd7e14'
]

"""Plotting settings"""
DEFAULT_LINE_WIDTH = 0
DEFUALT_LINE_COLOR = '#000000'

BAR_COLORINPUT_LABEL = 'Bar color in plot'
OUTLINE_COLORINPUT_LABEL = 'Stroke color in plot'
WIDTH_SLIDER_LABEL = 'Stroke width in plot'

"""Component text"""
CALLBACK_ERROR_MESSAGE = 'Error in method: '

"""Component colors"""
SLIDER_COLOR = DASH_NICE_BLUE
BUTTON_COLOR = DASH_NICE_BLUE
SWITCH_COLOR = DASH_NICE_BLUE
TABS_COLOR = DASH_NICE_BLUE

"""Component values"""
ICON_SIZE = 16