from typing import Any

from _typeshed import Incomplete
from typing_extensions import Self

from manim.mobject.geometry.line import Line
from manim.mobject.geometry.polygram import RoundedRectangle
from manim.mobject.mobject import Mobject
from manim.mobject.types.vectorized_mobject import VGroup
from manim.utils.color import ManimColor, ParsableManimColor

# from manim.constants import *

__all__ = ["SurroundingRectangle", "BackgroundRectangle", "Cross", "Underline"]

class SurroundingRectangle(RoundedRectangle):
    buff: Incomplete
    def __init__(
        self,
        mobject: Mobject,
        color: ParsableManimColor = ...,
        buff: float = ...,
        corner_radius: float = 0.0,
        **kwargs,
    ) -> None: ...

class BackgroundRectangle(SurroundingRectangle):
    original_fill_opacity: Incomplete
    def __init__(
        self,
        mobject: Mobject,
        color: ParsableManimColor | None = None,
        stroke_width: float = 0,
        stroke_opacity: float = 0,
        fill_opacity: float = 0.75,
        buff: float = 0,
        **kwargs,
    ) -> None: ...
    def pointwise_become_partial(self, mobject: Mobject, a: Any, b: float) -> Self: ...
    def set_style(self, fill_opacity: float, **kwargs) -> Self: ...
    def get_fill_color(self) -> ManimColor: ...

class Cross(VGroup):
    def __init__(
        self,
        mobject: Mobject | None = None,
        stroke_color: ParsableManimColor = ...,
        stroke_width: float = 6.0,
        scale_factor: float = 1.0,
        **kwargs,
    ) -> None: ...

class Underline(Line):
    def __init__(self, mobject: Mobject, buff: float = ..., **kwargs) -> None: ...
