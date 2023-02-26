import datetime
import itertools
import os.path

from image_operator import ImageOperator
from logger import Display


def get_layout_size() -> tuple[int, int]:
    s = Display.ask("请输入总列数")
    if not s.isdigit() or int(s) <= 0:
        Display.warning("不正确的列数 ${}，请重试", [s])
        return get_layout_size()
    _col = int(s)
    s = Display.ask("请输入总行数")
    if not s.isdigit() or int(s) <= 0:
        Display.warning("不正确的行数 ${}，请重试", [s])
        return get_layout_size()
    _row = int(s)
    return _col, _row


def get_layout_align() -> str:
    # TODO: get input here
    return "lt"


def load_image(_x, _y) -> tuple[int, int]:
    path = Display.ask(f"第 {_x + 1} 列，第 {_y + 1} 行").strip("'\"")
    _size = image_op.insert_image(_x, _y, path)
    if _size == (0, 0):
        Display.warning("无法加载图片 ${}，清重试", [path])
        return load_image(_x, _y)
    return _size


if __name__ == "__main__":
    col, row = get_layout_size()
    align = get_layout_align()
    image_op = ImageOperator(col, row, align)

    for y, x in itertools.product(range(row), range(col)):
        size = load_image(x, y)
        Display.info("成功打开图片，图片尺寸: ${}", [f"{size[0]}x{size[1]}"])

    Display.info("图片生成中...")
    output_path = f"out{int(datetime.datetime.now().timestamp())}.jpg"

    size = image_op.get_size()
    Display.info("生成图片尺寸: ${}", [f"{size[0]}x{size[1]}"])

    image_op.do_action(output_path)
    Display.info("图片保存成功！位于: ${}", [os.path.abspath(output_path)])
