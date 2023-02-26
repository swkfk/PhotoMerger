import sys
from typing import Any, Iterable

try:
    from termcolor import cprint
except ImportError:
    def cprint(
            text: str,
            color: str | None = None,
            on_color: str | None = None,
            attrs: Iterable[str] | None = None,
            **kwargs: Any,
    ) -> None:
        print(text, **kwargs)


    print("[W]无法导入彩色模块，程序将使用控制台默认颜色", file=sys.stderr)


class Display:
    @staticmethod
    def __print(text: str, fmt: list[str], main_clr: str, fmt_clr: str, attrs: list[str], newline=True, **kwargs):
        """
        将文本打印输出，并且赋予其颜色与样式。`fmt` 列表中的元素会被加上反引号，并依次替换 `text` 中的 "${}" 内容。

        :param text: 待输出文本，使用 "${}" 作为占位符
        :param fmt: 替换占位符的字符串列表，会被打上反引号
        :param main_clr: 主体文本的颜色
        :param fmt_clr: 替换文字的颜色
        :param attrs: 其他样式，参考 `termcolor` 中的 `attrs`
        :param newline: 是否换行（默认不换行）
        :param kwargs: **除了"end"** 的 `print` 的其他参数
        :return: None
        """
        if "end" in kwargs:
            del kwargs["end"]
        for idx, sub in enumerate(text.split("${}")):
            cprint(sub, color=main_clr, attrs=attrs, end="", **kwargs)
            if idx < len(fmt) and idx < text.count("${}"):
                cprint("`" + fmt[idx] + "`", color=fmt_clr, attrs=attrs, end="", **kwargs)
        if newline:
            print(**kwargs)

    @staticmethod
    def ask(text: str) -> str:
        Display.__print("[-]" + text, [], "cyan", "", ["underline"], newline=False, flush=True)
        Display.__print(": ", [], "cyan", "", [], newline=False, flush=True)
        return input()

    @staticmethod
    def info(text: str, contents: list[str] | None = None, file=sys.stdout):
        if contents is None:
            contents = list()
        Display.__print("[I]" + text, contents, "light_blue", "cyan", ["bold"], file=file)

    @staticmethod
    def warning(text: str, contents: list[str] | None = None, file=sys.stderr):
        if contents is None:
            contents = list()
        Display.__print("[W]" + text, contents, "yellow", "cyan", ["bold"], file=file)

    @staticmethod
    def critic(text: str, contents: list[str] | None = None, file=sys.stderr):
        if contents is None:
            contents = list()
        Display.__print("[C]" + text, contents, "red", "cyan", ["bold"], file=file)


# test
if __name__ == "__main__":
    Display.info("Hello world! This is ${} speaking.", ["kai_Ker"])
    Display.warning("A warning. This is ${} speaking.", ["kai_Ker", "more args"])
    Display.critic("Fatal error! This is ${} speaking. Less args: ${}.", ["kai_Ker"])
    Display.info("You entered: ${}", [Display.ask("Enter a string")])
