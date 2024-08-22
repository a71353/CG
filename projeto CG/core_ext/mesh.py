import numpy as np
import OpenGL.GL as GL
from math import sin, cos, tan, pi

from core_ext.object3d import Object3D


class Mesh(Object3D):
    """
    Contains geometric data that specifies vertex-related properties and material data
    that specifies the general appearance of the object
    """
    def __init__(self, geometry, material):
        super().__init__()
        self._geometry = geometry
        self._material = material
        # Should this object be rendered?
        self._visible = True
        # Set up associations between attributes stored in geometry
        # and shader program stored in material
        self._vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self._vao_ref)
        for variable_name, attribute_object in geometry.attribute_dict.items():
            attribute_object.associate_variable(material.program_ref, variable_name)
        # Unbind this vertex array object
        GL.glBindVertexArray(0)

        self._translation = np.zeros(3)
        self._rotation_matrix = np.eye(4)  # Adiciona o atributo _rotation_matrix

    @property
    def geometry(self):
        return self._geometry

    @property
    def material(self):
        return self._material

    @property
    def vao_ref(self):
        return self._vao_ref

    @property
    def visible(self):
        return self._visible
    
    @staticmethod
    def make_rotation_y(angle):
        c = cos(angle)
        s = sin(angle)
        return np.array([[c,  0,  s,  0],
                            [0,  1,  0,  0],
                            [-s, 0,  c,  0],
                            [0,  0,  0,  1]]).astype(float)

    def set_translation(self, x, y, z):
        self._translation[0] = x
        self._translation[1] = y
        self._translation[2] = z
        self._update_model_matrix()

    def _update_model_matrix(self):
        translation_matrix = np.eye(4)
        translation_matrix[0, 3] = self._translation[0]
        translation_matrix[1, 3] = self._translation[1]
        translation_matrix[2, 3] = self._translation[2]
        self._model_matrix = np.matmul(self._rotation_matrix, translation_matrix)
