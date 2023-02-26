import itertools
import os
import sys

from logger import Display

try:
    from PIL import Image
except ImportError:
    Display.critic("无法导入图片处理模块，请使用 ${} 进行安装", ["pip install pillow"])
    os.system("pause>nul")
    sys.exit(1)


class ImageOperator:
    def __init__(self, col: int, row: int, align: str):
        self.layout_size = (col, row)
        self.size = (0, 0)
        self.align = align
        self.imgs: dict[tuple[int, int], Image.Image] = dict()
        self.widths = list()
        self.heights = list()

    def insert_image(self, col: int, row: int, path: str) -> tuple[int, int]:
        assert 0 <= col < self.layout_size[0] and 0 <= row < self.layout_size[1] and not (col, row) in self.imgs
        try:
            self.imgs[(col, row)] = Image.open(path)
        except FileNotFoundError:
            return 0, 0
        return self.imgs[(col, row)].size

    def get_size(self) -> tuple[int, int]:
        for col in range(self.layout_size[0]):
            img_lst = [self.imgs[col, i] for i in range(self.layout_size[1])]
            self.widths.append(max([img.size[0] for img in img_lst]))
        for row in range(self.layout_size[1]):
            img_lst = [self.imgs[i, row] for i in range(self.layout_size[0])]
            self.heights.append(max([img.size[1] for img in img_lst]))
        self.size = sum(self.widths), sum(self.heights)
        return self.size

    def do_action(self, out_name: str):
        # TODO: add more adaptations
        img = Image.new("RGB", self.size, (255, 255, 255))
        for y, x in itertools.product(range(self.layout_size[1]), range(self.layout_size[0])):
            img.paste(self.imgs[x, y], (sum(self.widths[0:x]), sum(self.heights[0:y])))
        img.save(out_name)
