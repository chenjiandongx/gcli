#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(
    name='gcli',
    version='0.0.1',
    description="Automatically generate .gitignore/readme/license files cli",
    url="https://github.com/chenjiandongx/gcli",
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    license="MIT",
    packages=find_packages(),
    py_modules=['gcli'],
    keywords=["git", "cli"],
    zip_safe=False,
    include_package_data=True,
    entry_points={
        'console_scripts': ['gcli=gcli:command_line_runner']
    }
)
