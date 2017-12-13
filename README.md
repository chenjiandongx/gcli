# 自动生成 .gitignore/readme/license 文件命令行工具

[![PyPI version](https://badge.fury.io/py/giti-cli.svg)](https://badge.fury.io/py/giti-cli) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

鉴于现在每次写 Python 项目都需要自己导入 .gitignore/readme/license 文件，有点麻烦，就打包了一个命令行工具用于自动生成这些文件。

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
C:\Users\chenjiandongx>giti-cli
usage: giti-cli [-h] [-g] [-r] [-l] [-v]

Automatically generate .gitignore/readme/license file CLI.

optional arguments:
  -h, --help       show this help message and exit
  -g, --gitignore  Whether to generate .gitignore file.
  -r, --readme     Whether to generate README.md file.
  -l, --license    Whether to generate LICENSE file.
  -v, --version    Version info.
```

生成的 LICENSE 为 MIT，如果一次性要生成这三个文件只需要执行 `giti-cli -grl`

### MIT 许可证
