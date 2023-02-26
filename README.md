# PhotoMerger

~~为了顺利地交上数分作业！~~

使用方法应该要简单，正如这个程序的体量一样。我觉得暂时不需要使用方法的介绍。哦对了，程序入口在 `main.py` 中。

依照目前的体量，没必要使用 `requirements.txt` 描述依赖库，大家就自己装一装吧。 ~~还不是我懒得写安装方法~~

后续会使用 `PyQt` 库制作图形化界面，并使用 `pyinstaller` 制作发行版程序。

## Python 版本选择

代码中使用了 3.9 版本新增的功能，因此程序不支持 Windows7 及以下版本系统。推荐使用 3.10 版本的 Python。

## 第三方依赖（如无特殊说明，库名即为安装名）

- pillow 图形处理库
- termcolor 彩色控制台输出（因为 Windows 的控制台对彩色文字支持不佳，**建议不要装**，除非你使用的控制台支持彩色，程序对缺失此库的情况作了特殊处理）

## 第三方库安装方式及镜像站的使用教程

（打开命令行总知道的吧，cmd）

通常情况，使用

```commandline
pip install xxx
```

可以安装名为 `xxx` 的第三方库，如果遇到网速问题，可以通过

```commandline
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple
```

使用清华大学的镜像站。

同时，可以通过修改全局配置文件，达到“一劳永逸”的目的：

1. 打开或创建文件夹 `C:\Users\<你的用户名>\AppData\Roaming\pip` 或者是 `%APPDATA%\pip`
2. 创建一个名为 `pip.ini` 的文件
3. 在其中写入如下内容：

```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
format = columns
```
