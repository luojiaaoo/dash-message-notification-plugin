from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
setup(
    name="dash-message-notification-plugin",
    version="0.1.0",
    install_requires=[
        "dash>=3.1.1",
        "feffery-antd-components",
    ],
    packages=["dash_message_notification_plugin"],
    author="luojiaaoo",
    author_email="675925864@qq.com",
    description="A plugin to feedback by message or notification for Dash applications using Dash Hooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luojiaaoo/dash-message-notification-plugin",
)
