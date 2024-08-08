from manim.mobject.geometry.line import Arrow, Line
from manim.mobject.text.tex_mobject import MathTex, Tex
from manim.mobject.text.text_mobject import Text
from manim.utils.color import ParsableManimColor

# from manim.constants import *

__all__ = ["LabeledLine", "LabeledArrow"]

class LabeledLine(Line):
    def __init__(
        self,
        label: str | Tex | MathTex | Text,
        label_position: float = 0.5,
        font_size: float = ...,
        label_color: ParsableManimColor = ...,
        label_frame: bool = True,
        frame_fill_color: ParsableManimColor = None,
        frame_fill_opacity: float = 1,
        *args,
        **kwargs,
    ) -> None: ...

class LabeledArrow(LabeledLine, Arrow):
    def __init__(self, *args, **kwargs) -> None: ...
