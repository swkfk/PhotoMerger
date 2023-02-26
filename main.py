import os
import sys
from typing import Any, Iterable

try:
    from termcolor import cprint
except ImportError:
    print("[W]无法导入彩色模块，可以使用 `pip install termcolor` 进行安装", file=sys.stderr)


    def cprint(
            text: str,
            color: str | None = None,
            on_color: str | None = None,
            attrs: Iterable[str] | None = None,
            **kwargs: Any,
    ) -> None:
        print(text, **kwargs)

try:
    from PIL import Image
except ImportError:
    cprint("[C]无法导入图片处理模块，请使用 `pip install Pillow` 进行安装",
           color="red", attrs=["bold"], file=sys.stderr)
    os.system("pause>nul")
    sys.exit(1)
