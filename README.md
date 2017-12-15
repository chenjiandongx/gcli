# 自动生成 .gitignore/readme/license 文件小命令行工具

[![PyPI version](https://badge.fury.io/py/gcli.svg)](https://badge.fury.io/py/gcli) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

鉴于现在每次写 Python 项目都需要自己导入 .gitignore/readme/license 文件，有点麻烦，就打包了一个命令行工具用于自动生成这些文件。

### 安装
#### pip 安装
```
$ pip install gcli
```

#### 源码安装
```
 $ git clone https://github.com/chenjiandongx/gcli.git
 $ cd gcli
 $ python setup.py install
```


### 用法
```
C:\Users\chenjiandongx>gcli
usage: gcli [-h] [-g] [-r] [-l] [-a] [-v]

Automatically generate .gitignore/readme/license files cli

optional arguments:
  -h, --help       show this help message and exit
  -g, --gitignore  Whether to generate .gitignore file
  -r, --readme     Whether to generate README.md file
  -l, --license    Whether to generate LICENSE file
  -a, --all        Whether to generate all three files
  -v, --version    Version info

```

生成的 LICENSE 为 MIT，如果一次性要生成这三个文件只需要执行 `gcli -a`

### MIT 许可证
