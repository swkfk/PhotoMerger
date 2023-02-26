# PhotoMerger

~~为了顺利地交上数分作业！~~

使用方法应该要简单，正如这个程序的体量一样。我觉得暂时不需要使用方法的介绍。

依照目前的体量，没必要使用 `requirements.txt` 描述依赖库，大家就自己装一装吧。 ~~还不是我懒得写安装方法~~

后续会使用 `PyQt` 库制作图形化界面，并使用 `pyinstaller` 制作发行版程序。

## Python 版本选择

代码中使用了 3.9 版本新增的功能，因此程序不支持 Windows7 及以下版本系统。推荐使用 3.10 版本。

## 第三方依赖（括号中为安装名）

- Pillow(pillow) 图形处理库

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
