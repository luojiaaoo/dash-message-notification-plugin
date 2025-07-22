import dash
from dash import html, Input, ALL, ctx
import feffery_antd_components as fac

# Import the message notification plugin
from dash_message_notification_plugin import (
    setup_message_notification_plugin,
    UtilMessage,
    UtilNotification,
)

# Enable the message notification plugin for the current app
setup_message_notification_plugin()

app = dash.Dash(__name__)

app.layout = fac.AntdCol(
    [
        fac.AntdRow(
            [
                fac.AntdDivider('Message', plain=False, innerTextOrientation='left'),
                fac.AntdFlex(
                    [
                        fac.AntdButton(
                            'Default',
                            id={'type': 'trigger-message', 'index': 'default'},
                            type='default',
                        ),
                        fac.AntdButton(
                            'Info',
                            id={'type': 'trigger-message', 'index': 'info'},
                            type='default',
                        ),
                        fac.AntdButton(
                            'Success',
                            id={'type': 'trigger-message', 'index': 'success'},
                            type='default',
                        ),
                        fac.AntdButton(
                            'Warning',
                            id={'type': 'trigger-message', 'index': 'warning'},
                            type='default',
                        ),
                        fac.AntdButton(
                            'Error',
                            id={'type': 'trigger-message', 'index': 'error'},
                            type='default',
                        ),
                        html.Div(id='message-type-demo'),
                    ],
                    gap='small',
                    align='flex-start',
                ),
            ]
        ),
        fac.AntdRow(
            [
                fac.AntdDivider('Notification', plain=False, innerTextOrientation='left'),
                fac.AntdFlex(
                    [
                        fac.AntdButton(
                            'Default',
                            id={'type': 'trigger-notification', 'index': 'default'},
                            type='default',
                        ),
                        fac.AntdButton(
                            'Info',
                            id={'type': 'trigger-notification', 'index': 'info'},
                            type='default',
                        ),
                        fac.AntdButton(
                            'Success',
                            id={'type': 'trigger-notification', 'index': 'success'},
                            type='default',
                        ),
                        fac.AntdButton(
                            'Warning',
                            id={'type': 'trigger-notification', 'index': 'warning'},
                            type='default',
                        ),
                        fac.AntdButton(
                            'Error',
                            id={'type': 'trigger-notification', 'index': 'error'},
                            type='default',
                        ),
                        html.Div(id='notification-type-demo'),
                    ],
                    gap='small',
                    align='flex-start',
                ),
            ]
        ),
    ]
)


@app.callback(
    Input({'type': 'trigger-message', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def message_type_demo(nClicks):
    triggered_index = ctx.triggered_id.index
    if nClicks:
        if triggered_index == 'default':
            UtilMessage.default('This is a default message.', maxCount=1)
        elif triggered_index == 'info':
            UtilMessage.info('This is an info message.')
        elif triggered_index == 'success':
            UtilMessage.success('This is a success message.', duration=10)
        elif triggered_index == 'warning':
            UtilMessage.warning('This is a warning message.')
        elif triggered_index == 'error':
            UtilMessage.error('This is an error message.')


@app.callback(
    Input({'type': 'trigger-notification', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def notification_type_demo(nClicks):
    triggered_index = ctx.triggered_id.index
    if nClicks:
        if triggered_index == 'default':
            UtilNotification.default('This is a default message.', description='This is a default notification description.')
        elif triggered_index == 'info':
            UtilNotification.info('This is an info message.', duration=1)
        elif triggered_index == 'success':
            UtilNotification.success('This is a success message.', showProgress=True)
        elif triggered_index == 'warning':
            UtilNotification.warning('This is a warning message.', placement='bottom')
        elif triggered_index == 'error':
            UtilNotification.error('This is an error message.')


if __name__ == '__main__':
    app.run()
