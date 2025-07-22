# dash-message-notification-plugin 中文介绍

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/luojiaaoo/dash-message-notification-plugin/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/dash-message-notification-plugin.svg?color=dark-green)](https://pypi.org/project/dash-message-notification-plugin/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[English](./README.md) | 简体中文

一个基于Dash Hooks实现的消息和通知反馈插件，可以轻松地为Dash应用添加消息提示功能。

## 安装

```bash
pip install dash-message-notification-plugin
```

## 使用方法

```python
import dash

# 导入消息通知插件
from dash_message_notification_plugin import (
    setup_message_notification_plugin,
    UtilMessage,
    UtilNotification,
)

# 为当前应用启用消息通知插件
setup_message_notification_plugin()

app = dash.Dash(__name__)

# 其余应用代码...
```

## 示例

运行示例程序：

```bash
python example.py
```

## API参考

### 1. 激活插件

`setup_message_notification_plugin()`

### 2. 在回调中使用API

`请参考example.py文件`