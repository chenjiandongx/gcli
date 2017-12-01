#!/usr/bin/env python
# coding=utf-8

import os
import argparse


HERE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'git-ignore')

VERSION = "VERSION 0.0.1"


def get_parser():
    """ 解析命令行参数
    """
    parser = argparse.ArgumentParser(
        description='自动生成 .gitignore 文件命令行工具',
        add_help=False)
    parser.add_argument('-l', '--language', type=str, default="Python",
                        help='需要生成 .gitignore 文件的语言.(默认为 Python)')
    parser.add_argument('-o', '--output', type=str, default="",
                        help='.gitignore 保存路径.(默认为根目录)')
    parser.add_argument('-v', '--version', action='store_true',
                        help='版本信息')
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='帮助页面')
    return parser


def command_line_runner():
    """ 执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(VERSION)
        return
    save_file(args['language'], args['output'])


def save_file(language, output):
    """ 保存文件到本地

    :param language: 需要生成 .gitignore 文件的语言
    :param output: .gitignore 保存路径
    """
    language = language.title()
    _path = os.path.join(HERE, language + '.gitignore')
    if os.path.exists(_path):
        with open(_path, "r") as fin:
            content = fin.read()
        if output:
            os.chdir(output)
        with open('.gitignore', "w+") as fout:
            fout.write(content)
    else:
        print("找不到该语言对应的 .gitignore 文件")


if __name__ == "__main__":
    command_line_runner()
