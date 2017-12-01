# 自动生成 .gitignore 文件命令行工具

[![PyPI version](https://badge.fury.io/py/giti-cli.svg)](https://badge.fury.io/py/giti-cli) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

鉴于现在每次写 Python 项目都需要自己导入 .gitignore 文件，有点麻烦，就打包了一个命令行工具用于自动生成对应语言的 .gitignore 文件。

### 安装
#### pip 安装
```
$ pip install giti-cli
```

#### 源码安装
```
 $ git clone https://github.com/chenjiandongx/giti-cli.git
 $ cd giti-cli
 $ python setup.py install
```


### 用法
```
C:\Users\chenjiandongx>giti-cli --help
usage: giti-cli [-l LANGUAGE] [-o OUTPUT] [-v] [-h]

自动生成 .gitignore 文件命令行工具

optional arguments:
  -l LANGUAGE, --language LANGUAGE
                        需要生成 .gitignore 文件的语言.(默认为 Python)
  -o OUTPUT, --output OUTPUT
                        .gitignore 保存路径.(默认为根目录)
  -v, --version         版本信息
  -h, --help            帮助页面
```

**温馨提示：** 语言不区分大小写，如 `Python/python/PYTHON` 均可。

如果是要生成 Python 对应的 .gitignore 文件的话，只需在根目录直接运行 giti-cli 即可

**提供语言列表请参考 [git-ignore](https://github.com/chenjiandongx/giti-cli/tree/master/git-ignore) 文件夹**

### MIT 许可证
