from _typeshed import Incomplete
from typing_extensions import Self

from manim.mobject.geometry.arc import TipableVMobject
from manim.mobject.mobject import Mobject
from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.types.vectorized_mobject import VGroup, VMobject
from manim.typing import Point2D, Point3D, Vector3D
from manim.utils.color import ParsableManimColor

from ..matrix import Matrix

# from manim.constants import *

__all__ = [
    "Line",
    "DashedLine",
    "TangentLine",
    "Elbow",
    "Arrow",
    "Vector",
    "DoubleArrow",
    "Angle",
    "RightAngle",
]

class Line(TipableVMobject):
    dim: int
    buff: Incomplete
    path_arc: Incomplete
    def __init__(
        self,
        start: Point3D | Mobject = ...,
        end: Point3D | Mobject = ...,
        buff: float = 0,
        path_arc: float | None = None,
        **kwargs,
    ) -> None: ...
    def generate_points(self) -> None: ...
    def set_points_by_ends(
        self,
        start: Point3D | Mobject,
        end: Point3D | Mobject,
        buff: float = 0,
        path_arc: float = 0,
    ) -> None: ...
    init_points = generate_points
    def set_path_arc(self, new_value: float) -> None: ...
    start: Incomplete
    end: Incomplete
    def put_start_and_end_on(self, start: Point3D, end: Point3D) -> Self: ...
    def get_vector(self) -> Vector3D: ...
    def get_unit_vector(self) -> Vector3D: ...
    def get_angle(self) -> float: ...
    def get_projection(self, point: Point3D) -> Vector3D: ...
    def get_slope(self) -> float: ...
    def set_angle(self, angle: float, about_point: Point3D | None = None) -> Self: ...
    def set_length(self, length: float) -> Self: ...

class DashedLine(Line):
    dash_length: Incomplete
    dashed_ratio: Incomplete
    def __init__(
        self, *args, dash_length: float = ..., dashed_ratio: float = 0.5, **kwargs
    ) -> None: ...
    def get_start(self) -> Point3D: ...
    def get_end(self) -> Point3D: ...
    def get_first_handle(self) -> Point3D: ...
    def get_last_handle(self) -> Point3D: ...

class TangentLine(Line):
    length: Incomplete
    d_alpha: Incomplete
    def __init__(
        self,
        vmob: VMobject,
        alpha: float,
        length: float = 1,
        d_alpha: float = 1e-06,
        **kwargs,
    ) -> None: ...

class Elbow(VMobject, metaclass=ConvertToOpenGL):
    angle: Incomplete
    def __init__(self, width: float = 0.2, angle: float = 0, **kwargs) -> None: ...

class Arrow(Line):
    max_tip_length_to_length_ratio: Incomplete
    max_stroke_width_to_length_ratio: Incomplete
    initial_stroke_width: Incomplete
    def __init__(
        self,
        *args,
        stroke_width: float = 6,
        buff: float = ...,
        max_tip_length_to_length_ratio: float = 0.25,
        max_stroke_width_to_length_ratio: float = 5,
        **kwargs,
    ) -> None: ...
    def scale(self, factor: float, scale_tips: bool = False, **kwargs) -> Self: ...
    def get_normal_vector(self) -> Vector3D: ...
    normal_vector: Incomplete
    def reset_normal_vector(self) -> Self: ...
    def get_default_tip_length(self) -> float: ...

class Vector(Arrow):
    buff: Incomplete
    def __init__(
        self, direction: Point2D | Point3D = ..., buff: float = 0, **kwargs
    ) -> None: ...
    def coordinate_label(
        self,
        integer_labels: bool = True,
        n_dim: int = 2,
        color: ParsableManimColor | None = None,
        **kwargs,
    ) -> Matrix: ...

class DoubleArrow(Arrow):
    def __init__(self, *args, **kwargs) -> None: ...

class Angle(VMobject, metaclass=ConvertToOpenGL):
    lines: Incomplete
    quadrant: Incomplete
    dot_distance: Incomplete
    elbow: Incomplete
    radius: Incomplete
    angle_value: Incomplete
    dot_radius: Incomplete
    def __init__(
        self,
        line1: Line,
        line2: Line,
        radius: float | None = None,
        quadrant: Point2D = (1, 1),
        other_angle: bool = False,
        dot: bool = False,
        dot_radius: float | None = None,
        dot_distance: float = 0.55,
        dot_color: ParsableManimColor = ...,
        elbow: bool = False,
        **kwargs,
    ) -> None: ...
    def get_lines(self) -> VGroup: ...
    def get_value(self, degrees: bool = False) -> float: ...
    @staticmethod
    def from_three_points(A: Point3D, B: Point3D, C: Point3D, **kwargs) -> Angle: ...

class RightAngle(Angle):
    def __init__(
        self, line1: Line, line2: Line, length: float | None = None, **kwargs
    ) -> None: ...
