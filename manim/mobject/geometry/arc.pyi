import numpy as np
from _typeshed import Incomplete
from typing_extensions import Self

import manim.mobject.geometry.tips as tips
from manim.mobject.mobject import Mobject
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.text.tex_mobject import SingleStringMathTex, Tex
from manim.mobject.text.text_mobject import Text
from manim.mobject.types.vectorized_mobject import VGroup, VMobject
from manim.typing import CubicBezierPoints, Point3D, Vector3D
from manim.utils.color import ParsableManimColor

# from manim.constants import *

__all__ = [
    "TipableVMobject",
    "Arc",
    "ArcBetweenPoints",
    "CurvedArrow",
    "CurvedDoubleArrow",
    "Circle",
    "Dot",
    "AnnotationDot",
    "LabeledDot",
    "Ellipse",
    "AnnularSector",
    "Sector",
    "Annulus",
    "CubicBezier",
    "ArcPolygon",
    "ArcPolygonFromArcs",
]

class TipableVMobject(VMobject, metaclass=ConvertToOpenGL):
    tip_length: Incomplete
    normal_vector: Incomplete
    tip_style: Incomplete
    def __init__(
        self,
        tip_length: float = ...,
        normal_vector: Vector3D = ...,
        tip_style: dict = {},
        **kwargs,
    ) -> None: ...
    def add_tip(
        self,
        tip: tips.ArrowTip | None = None,
        tip_shape: type[tips.ArrowTip] | None = None,
        tip_length: float | None = None,
        tip_width: float | None = None,
        at_start: bool = False,
    ) -> Self: ...
    def create_tip(
        self,
        tip_shape: type[tips.ArrowTip] | None = None,
        tip_length: float = None,
        tip_width: float = None,
        at_start: bool = False,
    ): ...
    def get_unpositioned_tip(
        self,
        tip_shape: type[tips.ArrowTip] | None = None,
        tip_length: float | None = None,
        tip_width: float | None = None,
    ): ...
    def position_tip(self, tip: tips.ArrowTip, at_start: bool = False): ...
    def reset_endpoints_based_on_tip(
        self, tip: tips.ArrowTip, at_start: bool
    ) -> Self: ...
    start_tip: Incomplete
    tip: Incomplete
    def asign_tip_attr(self, tip: tips.ArrowTip, at_start: bool) -> Self: ...
    def has_tip(self) -> bool: ...
    def has_start_tip(self) -> bool: ...
    def pop_tips(self) -> VGroup: ...
    def get_tips(self) -> VGroup: ...
    def get_tip(self): ...
    def get_default_tip_length(self) -> float: ...
    def get_first_handle(self) -> Point3D: ...
    def get_last_handle(self) -> Point3D: ...
    def get_end(self) -> Point3D: ...
    def get_start(self) -> Point3D: ...
    def get_length(self) -> np.floating: ...

class Arc(TipableVMobject):
    radius: Incomplete
    num_components: Incomplete
    arc_center: Incomplete
    start_angle: Incomplete
    angle: Incomplete
    def __init__(
        self,
        radius: float = 1.0,
        start_angle: float = 0,
        angle: float = ...,
        num_components: int = 9,
        arc_center: Point3D = ...,
        **kwargs,
    ) -> None: ...
    def generate_points(self) -> None: ...
    def init_points(self) -> None: ...
    def get_arc_center(self, warning: bool = True) -> Point3D: ...
    def move_arc_center_to(self, point: Point3D) -> Self: ...
    def stop_angle(self) -> float: ...

class ArcBetweenPoints(Arc):
    radius: Incomplete
    def __init__(
        self,
        start: Point3D,
        end: Point3D,
        angle: float = ...,
        radius: float = None,
        **kwargs,
    ) -> None: ...

class CurvedArrow(ArcBetweenPoints):
    def __init__(self, start_point: Point3D, end_point: Point3D, **kwargs) -> None: ...

class CurvedDoubleArrow(CurvedArrow):
    def __init__(self, start_point: Point3D, end_point: Point3D, **kwargs) -> None: ...

class Circle(Arc):
    def __init__(
        self, radius: float | None = None, color: ParsableManimColor = ..., **kwargs
    ) -> None: ...
    width: Incomplete
    def surround(
        self,
        mobject: Mobject,
        dim_to_match: int = 0,
        stretch: bool = False,
        buffer_factor: float = 1.2,
    ) -> Self: ...
    def point_at_angle(self, angle: float) -> Point3D: ...
    @staticmethod
    def from_three_points(p1: Point3D, p2: Point3D, p3: Point3D, **kwargs) -> Self: ...

class Dot(Circle):
    def __init__(
        self,
        point: Point3D = ...,
        radius: float = ...,
        stroke_width: float = 0,
        fill_opacity: float = 1.0,
        color: ParsableManimColor = ...,
        **kwargs,
    ) -> None: ...

class AnnotationDot(Dot):
    def __init__(
        self,
        radius: float = ...,
        stroke_width: float = 5,
        stroke_color: ParsableManimColor = ...,
        fill_color: ParsableManimColor = ...,
        **kwargs,
    ) -> None: ...

class LabeledDot(Dot):
    def __init__(
        self,
        label: str | SingleStringMathTex | Text | Tex,
        radius: float | None = None,
        **kwargs,
    ) -> None: ...

class Ellipse(Circle):
    def __init__(self, width: float = 2, height: float = 1, **kwargs) -> None: ...

class AnnularSector(Arc):
    inner_radius: Incomplete
    outer_radius: Incomplete
    def __init__(
        self,
        inner_radius: float = 1,
        outer_radius: float = 2,
        angle: float = ...,
        start_angle: float = 0,
        fill_opacity: float = 1,
        stroke_width: float = 0,
        color: ParsableManimColor = ...,
        **kwargs,
    ) -> None: ...
    def generate_points(self) -> None: ...
    init_points = generate_points

class Sector(AnnularSector):
    def __init__(
        self, outer_radius: float = 1, inner_radius: float = 0, **kwargs
    ) -> None: ...

class Annulus(Circle):
    mark_paths_closed: Incomplete
    inner_radius: Incomplete
    outer_radius: Incomplete
    def __init__(
        self,
        inner_radius: float | None = 1,
        outer_radius: float | None = 2,
        fill_opacity: float = 1,
        stroke_width: float = 0,
        color: ParsableManimColor = ...,
        mark_paths_closed: bool = False,
        **kwargs,
    ) -> None: ...
    radius: Incomplete
    def generate_points(self) -> None: ...
    init_points = generate_points

class CubicBezier(VMobject, metaclass=ConvertToOpenGL):
    def __init__(
        self,
        start_anchor: CubicBezierPoints,
        start_handle: CubicBezierPoints,
        end_handle: CubicBezierPoints,
        end_anchor: CubicBezierPoints,
        **kwargs,
    ) -> None: ...

class ArcPolygon(VMobject, metaclass=ConvertToOpenGL):
    arcs: Incomplete
    def __init__(
        self,
        *vertices: Point3D,
        angle: float = ...,
        radius: float | None = None,
        arc_config: list[dict] | None = None,
        **kwargs,
    ) -> None: ...

class ArcPolygonFromArcs(VMobject, metaclass=ConvertToOpenGL):
    arcs: Incomplete
    def __init__(self, *arcs: Arc | ArcBetweenPoints, **kwargs) -> None: ...
