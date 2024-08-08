import numpy as np
from _typeshed import Incomplete
from typing_extensions import Self

from manim.constants import *
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.types.vectorized_mobject import VMobject
from manim.typing import Point3D, Point3D_Array
from manim.utils.color import ParsableManimColor

# from manim.constants import *

__all__ = [
    "Polygram",
    "Polygon",
    "RegularPolygram",
    "RegularPolygon",
    "Star",
    "Triangle",
    "Rectangle",
    "Square",
    "RoundedRectangle",
    "Cutout",
]

class Polygram(VMobject, metaclass=ConvertToOpenGL):
    def __init__(
        self, *vertex_groups: Point3D, color: ParsableManimColor = ..., **kwargs
    ) -> None: ...
    def get_vertices(self) -> Point3D_Array: ...
    def get_vertex_groups(self) -> np.ndarray[Point3D_Array]: ...
    def round_corners(
        self,
        radius: float | list[float] = 0.5,
        evenly_distribute_anchors: bool = False,
        components_per_rounded_corner: int = 2,
    ) -> Self: ...

class Polygon(Polygram):
    def __init__(self, *vertices: Point3D, **kwargs) -> None: ...

class RegularPolygram(Polygram):
    def __init__(
        self,
        num_vertices: int,
        *,
        density: int = 2,
        radius: float = 1,
        start_angle: float | None = None,
        **kwargs,
    ) -> None: ...

class RegularPolygon(RegularPolygram):
    def __init__(self, n: int = 6, **kwargs) -> None: ...

class Star(Polygon):
    def __init__(
        self,
        n: int = 5,
        *,
        outer_radius: float = 1,
        inner_radius: float | None = None,
        density: int = 2,
        start_angle: float | None = ...,
        **kwargs,
    ) -> None: ...

class Triangle(RegularPolygon):
    def __init__(self, **kwargs) -> None: ...

class Rectangle(Polygon):
    grid_lines: Incomplete
    def __init__(
        self,
        color: ParsableManimColor = ...,
        height: float = 2.0,
        width: float = 4.0,
        grid_xstep: float | None = None,
        grid_ystep: float | None = None,
        mark_paths_closed: bool = True,
        close_new_points: bool = True,
        **kwargs,
    ) -> None: ...

class Square(Rectangle):
    side_length: Incomplete
    def __init__(self, side_length: float = 2.0, **kwargs) -> None: ...

class RoundedRectangle(Rectangle):
    corner_radius: Incomplete
    def __init__(self, corner_radius: float | list[float] = 0.5, **kwargs) -> None: ...

class Cutout(VMobject, metaclass=ConvertToOpenGL):
    def __init__(self, main_shape: VMobject, *mobjects: VMobject, **kwargs) -> None: ...
