from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
from manim.mobject.types.vectorized_mobject import VMobject

__all__ = ['Union', 'Intersection', 'Difference', 'Exclusion']

class _BooleanOps(VMobject, metaclass=ConvertToOpenGL): ...

class Union(_BooleanOps):
    def __init__(self, *vmobjects: VMobject, **kwargs) -> None: ...

class Difference(_BooleanOps):
    def __init__(self, subject: VMobject, clip: VMobject, **kwargs) -> None: ...

class Intersection(_BooleanOps):
    def __init__(self, *vmobjects: VMobject, **kwargs) -> None: ...

class Exclusion(_BooleanOps):
    def __init__(self, subject: VMobject, clip: VMobject, **kwargs) -> None: ...
