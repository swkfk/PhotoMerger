import os

try:
    from PIL import Image
except ImportError:
    print("[C]无法导入图片处理模块，请使用 `pip install Pillow` 进行安装")
    os.system("pause")
