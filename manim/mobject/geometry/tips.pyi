import numpy as np
from _typeshed import Incomplete

from manim.mobject.geometry.arc import Circle
from manim.mobject.geometry.polygram import Square, Triangle
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.types.vectorized_mobject import VMobject
from manim.typing import Point3D, Vector3D

# from manim.constants import *

__all__ = [
    "ArrowTip",
    "ArrowCircleFilledTip",
    "ArrowCircleTip",
    "ArrowSquareTip",
    "ArrowSquareFilledTip",
    "ArrowTriangleTip",
    "ArrowTriangleFilledTip",
    "StealthTip",
]

class ArrowTip(VMobject, metaclass=ConvertToOpenGL):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def base(self) -> Point3D: ...
    @property
    def tip_point(self) -> Point3D: ...
    @property
    def vector(self) -> Vector3D: ...
    @property
    def tip_angle(self) -> float: ...
    @property
    def length(self) -> np.floating: ...

class StealthTip(ArrowTip):
    start_angle: Incomplete
    def __init__(
        self,
        fill_opacity: int = 1,
        stroke_width: int = 3,
        length=...,
        start_angle=...,
        **kwargs,
    ) -> None: ...
    @property
    def length(self): ...

class ArrowTriangleTip(ArrowTip, Triangle):
    width: Incomplete
    def __init__(
        self,
        fill_opacity: float = 0,
        stroke_width: float = 3,
        length: float = ...,
        width: float = ...,
        start_angle: float = ...,
        **kwargs,
    ) -> None: ...

class ArrowTriangleFilledTip(ArrowTriangleTip):
    def __init__(
        self, fill_opacity: float = 1, stroke_width: float = 0, **kwargs
    ) -> None: ...

class ArrowCircleTip(ArrowTip, Circle):
    start_angle: Incomplete
    width: Incomplete
    def __init__(
        self,
        fill_opacity: float = 0,
        stroke_width: float = 3,
        length: float = ...,
        start_angle: float = ...,
        **kwargs,
    ) -> None: ...

class ArrowCircleFilledTip(ArrowCircleTip):
    def __init__(
        self, fill_opacity: float = 1, stroke_width: float = 0, **kwargs
    ) -> None: ...

class ArrowSquareTip(ArrowTip, Square):
    start_angle: Incomplete
    width: Incomplete
    def __init__(
        self,
        fill_opacity: float = 0,
        stroke_width: float = 3,
        length: float = ...,
        start_angle: float = ...,
        **kwargs,
    ) -> None: ...

class ArrowSquareFilledTip(ArrowSquareTip):
    def __init__(
        self, fill_opacity: float = 1, stroke_width: float = 0, **kwargs
    ) -> None: ...
