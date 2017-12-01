#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(
    name='gitignore-cli',
    version='0.0.1',
    description="自动生成 .gitignore 文件命令行工具",
    url="https://github.com/chenjiandongx/gitignore-cli",
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    license="MIT",
    packages=find_packages(),
    py_modules=['gitignore'],
    keywords="gitignore",
    zip_safe=False,
    include_package_data=True,
    entry_points={
        'console_scripts':['gitignore-cli=gitignore:command_line_runner']
    }
)
