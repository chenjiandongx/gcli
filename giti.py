#!/usr/bin/env python
# coding=utf-8

import os
import argparse


HERE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)))

VERSION = "VERSION 0.0.1"


def get_parser():
    """ 解析命令行参数
    """
    parser = argparse.ArgumentParser(
        description='Automatically generate .gitignore/readme/license file CLI')
    parser.add_argument('-g', '--gitignore', action='store_true',
                        help='Whether to generate .gitignore file')
    parser.add_argument('-r', '--readme', action='store_true',
                        help='Whether to generate README.md file')
    parser.add_argument('-l', '--license', action='store_true',
                        help='Whether to generate LICENSE file')
    parser.add_argument('-v', '--version', action='store_true',
                        help='Version info')
    return parser


def command_line_runner():
    """ 执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(VERSION)
        return
    if not (args['license'] or args['readme'] or args['gitignore']):
        parser.print_help()
        return
    save_readme(args['readme'])
    save_license(args['license'])
    save_gitignore(args['gitignore'])


def save_license(license):
    """ 生成 LICENSE 文件
    """
    if license:
        with open(os.path.join(HERE, "dir", "LICENSE"), "r") as fin:
            content = fin.read()
        with open("LICENSE", "w+") as fout:
            fout.write(content)


def save_readme(readme):
    """ 生成 README 文件
    """
    if readme:
        open("README.md", "w+")


def save_gitignore(gitignore):
    """ 生成 .gitignore 文件
    """
    if gitignore:
        with open(os.path.join(
                HERE, "dir", "Python.gitignore"), "r") as fin:
            content = fin.read()
        with open(".gitignore", "w+") as fout:
            fout.write(content)


if __name__ == "__main__":
    command_line_runner()