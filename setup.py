#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(
    name='giti-cli',
    version='0.0.2',
    description="Automatically generate .gitignore/readme/license file CLI",
    url="https://github.com/chenjiandongx/giti-cli",
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    license="MIT",
    packages=find_packages(),
    py_modules=['giti'],
    keywords=["git", "cli"],
    zip_safe=False,
    include_package_data=True,
    entry_points={
        'console_scripts':['giti-cli=giti:command_line_runner']
    }
)
