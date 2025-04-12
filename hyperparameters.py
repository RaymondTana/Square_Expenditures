# This file contains many adjustable hyperparameters for the app

""" Execution settings """
BASE_URL = 'http://127.0.0.1:5000'
DEBUG = False

""" Email settings """
IMAP_SERVER = 'imap.gmail.com'
SENDER = 'messenger@messaging.squareup.com'
BUZON = '"[Gmail]/All Mail"'

"""Local directory structure"""

EXTERNAL_STYLESHEETS = ['/static/css/style.css']
URL_BASE_PATHNAME_WINDOW_APP = '/'

MARKDOWN_HELP = 'assets/markdown/help.md'

DARK_MODE_ICON = 'assets/icons/tdesign--mode-dark.svg'
SETTINGS_ICON = 'assets/icons/solar--settings-linear.svg'
EXPORT_ICON = 'assets/icons/mdi--export.svg'
SAVE_ICON = 'assets/icons/ic--round-save-alt.svg'
EMAIL_ICON = 'assets/icons/ic--round-alternate-email.svg'
PASSWORD_ICON = 'assets/icons/material-symbols--shield-lock-outline.svg'
SEARCH_ICON = 'assets/icons/mdi--sql-query.svg'

"""Library settings"""
MAX_ROWS_DISPLAY_PANDAS = 1000
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

LIGHT_TRANSPARENCY = 0.15
DARK_TRANSPARENCY = 0.2

ERROR_BARS_FILL_COLOR_DARK = 'rgba(68, 68, 68, 0.3)'
NO_COLOR = 'rgba(0, 0, 0, 0)'
ERROR_BARS_HOVERINFO = 'none'
PLOT_MARGIN = {'l': 40, 'b': 40, 't': 10, 'r': 0}
PLOT_HOVERMODE = 'closest'
MARKER_COLOR = DASH_NICE_BLUE
GROUPED_MARKER_COLOR = 'white'
DEFAULT_MARKER_SIZE = 5
DEFAULT_LINE_WIDTH = 2
GROUPED_MARKER_SIZE_SCALAR = 1.9
PREDICTION_FILL = '#ff85af'
PREDICTION_OPACITY = 0.2
FITTED_CURVE_STROKE = '#000000'
FITTED_CURVE_STROKE_2 = DASH_NICE_BLUE

POINT_COLORINPUT_LABEL = 'Color of data points'
CURVE_COLORINPUT_LABEL = 'Color of fitted curve'
CURVE_COLORINPUT_LABEL_2 = 'Color of secondary fitted curve'
PREDICTION_WINDOW_COLORINPUT_LABEL = 'Color of prediction window'
SELECT_CURVE_DASH_LABEL = 'Select Fitting Curve Dash Style'
CURVE_DASHES = ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
DEFAULT_CURVE_DASH = 'dash'

"""Component text"""

WINDOW_TITLE = 'ASML DRGA'

CALLBACK_ERROR_MESSAGE = 'Error in method: '

NO_FILE_SELECTED = 'No csv file(s) selected'

FILE_SELECTION_LABEL = 'Select a file to view'

"""Component colors"""
SLIDER_COLOR = DASH_NICE_BLUE
BUTTON_COLOR = DASH_NICE_BLUE
SWITCH_COLOR = DASH_NICE_BLUE
TABS_COLOR = DASH_NICE_BLUE

"""Component values"""
FITTED_CURVE_TEST_POINTS = 150

STEP_HOLD_INTERVAL = 50
STEP_HOLD_DELAY = 400

SUMMARY_TABLE_DECIMAL_PLACES = 2

TARGET_MTBF_DECIMAL_PLACES = 2

MANUAL_PARAMETER_DECIMAL_PLACES = 5
MANUAL_PARAMETER_STEP = 0.001

FIT_PARAMETERS_DECIMAL_PLACES = 4
FITNESS_DECIMAL_PLACES = 2

CONFIDENCE_LEVEL_DECIMAL_PLACES = 4
CONFIDENCE_LEVEL_STEP = 0.01
CONFIDENCE_LEVEL_DEFAULT = 0.950
CONFIDENCE_LEVEL_MIN = 0
CONFIDENCE_LEVEL_MAX = 1 - 1 / (10 ** CONFIDENCE_LEVEL_DECIMAL_PLACES)

EXTRAPOLATION_TIME_DEFAULT = 10
EXTRAPOLATION_TIME_STEP = 10

TARGET_MTBF_DEFAULT = 100
TARGET_MTBF_STEP = 10

SLIDER_DECIMAL_PLACES = 2
SLIDER_MIN_RANGE = 0.1
SLIDER_STEP = 0.1

EXPORT_NAME_DECIMAL_PLACES = 2

AXIS_DURATION = 300
AXIS_MB = 10

INCLUDE_PREDICTION_DEFAULT = False
INCLUDE_FIT_DEFAULT = True
INCLUDE_ERROR_DEFAULT = True
INCLUDE_INTERPOLATION_DEFAULT = True

ICON_SIZE = 16
NUMBER_ICON_SIZE = 35