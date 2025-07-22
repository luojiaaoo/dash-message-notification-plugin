from dash import hooks, set_props
import feffery_antd_components as fac
from typing import Literal
from functools import wraps

PACKAGE_NAME = 'dash-message-notification-plugin'


_globel_message_container = fac.Fragment(id=f'{PACKAGE_NAME}/global-message-container')  # 注入全局消息提示容器
_globel_notification_container = fac.Fragment(id=f'{PACKAGE_NAME}/global-notification-container')  # 注入全局通知信息容器


def setup_message_notification_plugin():
    """Setup the message notification plugin"""

    @hooks.layout()
    def update_layout(layout):
        """注入layout"""
        common_components = [
            _globel_message_container,
            _globel_notification_container,
        ]
        if isinstance(layout, list):
            layout = [*layout, *common_components]
        else:
            layout = [layout, *common_components]
        return layout


def _show_message(
    type: Literal['default', 'success', 'error', 'info', 'warning'],
    content: str,
    maxCount: int,
    duration: int,
) -> None:
    """显示消息"""
    message = fac.AntdMessage(
        type=type,
        content=content,
        duration=duration,
        maxCount=maxCount,
    )
    set_props(_globel_message_container.id, {'children': message})


def _show_notification(
    type: Literal['default', 'success', 'error', 'info', 'warning'],
    content: str,
    description: str,
    duration: int,
    showProgress: bool,
    placement: Literal['top', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'],
) -> None:
    """显示消息"""
    notification = fac.AntdNotification(
        type=type,
        message=content,
        description=description,
        placement=placement,
        duration=duration,
        showProgress=showProgress,
    )
    set_props(_globel_notification_container.id, {'children': notification})


class UtilMessage:
    """消息工具"""

    @staticmethod
    def default(content: str, /, *, maxCount: int = 3, duration: int = 3) -> None:
        """显示默认消息"""
        _show_message('default', content, maxCount, duration)

    @staticmethod
    def success(content: str, /, *, maxCount: int = 3, duration: int = 3) -> None:
        """显示成功消息"""
        _show_message('success', content, maxCount, duration)

    @staticmethod
    def error(content: str, /, *, maxCount: int = 3, duration: int = 3) -> None:
        """显示错误消息"""
        _show_message('error', content, maxCount, duration)

    @staticmethod
    def info(content: str, /, *, maxCount: int = 3, duration: int = 3) -> None:
        """显示提示消息"""
        _show_message('info', content, maxCount, duration)

    @staticmethod
    def warning(content: str, /, *, maxCount: int = 3, duration: int = 3) -> None:
        """显示警告消息"""
        _show_message('warning', content, maxCount, duration)


class UtilNotification:
    """消息工具"""

    @staticmethod
    def default(
        content: str,
        /,
        *,
        description: str = None,
        duration: int = 4,
        showProgress: bool = False,
        placement: Literal['top', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'] = 'topRight',
    ) -> None:
        """显示默认消息"""
        _show_notification('default', content, description, duration, showProgress, placement)

    @staticmethod
    def success(
        content: str,
        /,
        *,
        description: str = None,
        duration: int = 4,
        showProgress: bool = False,
        placement: Literal['top', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'] = 'topRight',
    ) -> None:
        """显示成功消息"""
        _show_notification('success', content, description, duration, showProgress, placement)

    @staticmethod
    def error(
        content: str,
        /,
        *,
        description: str = None,
        duration: int = 4,
        showProgress: bool = False,
        placement: Literal['top', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'] = 'topRight',
    ) -> None:
        """显示错误消息"""
        _show_notification('error', content, description, duration, showProgress, placement)

    @staticmethod
    def info(
        content: str,
        /,
        *,
        description: str = None,
        duration: int = 4,
        showProgress: bool = False,
        placement: Literal['top', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'] = 'topRight',
    ) -> None:
        """显示提示消息"""
        _show_notification('info', content, description, duration, showProgress, placement)

    @staticmethod
    def warning(
        content: str,
        /,
        *,
        description: str = None,
        duration: int = 4,
        showProgress: bool = False,
        placement: Literal['top', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'] = 'topRight',
    ) -> None:
        """显示警告消息"""
        _show_notification('warning', content, description, duration, showProgress, placement)
