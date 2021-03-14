# pyinstaller-Ameliorate
pyinstaller改良脚本。解决使用pyinstaller打包时，各种不方便的问题。

> 1.使用pyinstaller -F打包时，会生成dist、build等无用文件，需要手动删除。
> 
> 2.可执行文件名不可自定义。

本脚本自动化此流程。

可自定义可执行文件名，自动根据本地时间加上版本号。方便将可执行文件直接发送给客户。

## 使用方法：
下载脚本后，添加到PATH。

在需要打包的软件根目录下运行
在pyinstaller执行无误的情况下，会直接在根目录生成可执行文件，并自动清理dist、build、.spec等文件

例：
```bash
pyinstaller_ameliorate.py .\main.py 清理无流量
```

生成的文件名 例：
> 清理无流量v210314213909.exe
