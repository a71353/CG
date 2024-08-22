from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader


class ComidaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]

        
        uv_data = [t0, t1, t2, t3] * 10000

        position_data = my_obj_reader('comida.obj')
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()

    