# 自动生成 .gitignore 文件命令行工具

[![PyPI version](https://badge.fury.io/py/gitignore-cli.svg)](https://badge.fury.io/py/gitignore-cli) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

鉴于现在每次写 Python 项目都需要自己导入 .gitignore 文件，有点麻烦，就打包了一个命令行工具用于自动生成对应语言的 .gitignore 文件。

### 安装
#### pip 安装
```
$ pip install gitignore-cli
```

#### 源码安装
```
 $ git clone https://github.com/chenjiandongx/gitignore-cli.git
 $ cd gitignore-cli
 $ python setup.py install
```


### 用法
```
C:\Users\chenjiandongx>gitignore-cli --help
usage: gitignore-cli [-l LANGUAGE] [-o OUTPUT] [-v] [-h]

自动生成 .gitignore 文件命令行工具

optional arguments:
  -l LANGUAGE, --language LANGUAGE
                        需要生成 .gitignore 文件的语言.(默认为 Python)
  -o OUTPUT, --output OUTPUT
                        .gitignore 保存路径.(默认为根目录)
  -v, --version         版本信息
  -h, --help            帮助页面
```

### 提供语言列表请参考 [git-ignore]() 文件夹

