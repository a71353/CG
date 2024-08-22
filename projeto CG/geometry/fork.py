from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader

class ForkGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        
            # azul claro: R=0.6, G=0.8, B=1
        c1, c2 = [0.6, 0.8, 1], [0.4, 0.6, 1]

        # amarelo: R=1, G=0.8, B=0.2
        c3, c4 = [1, 0.8, 0.4], [1, 0.8, 0.2]

        # verde esmeralda: R=0.2, G=0.8, B=0.5
        c5, c6 = [0.2, 0.8, 0.5], [0.2, 0.4, 0.5]
        
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        
        color_data = [c1] * 5487 + [c2] * 5487 + [c3] * 5487 \
                   + [c4] * 5487 + [c5] * 5487 + [c6] * 5487
                   
        uv_data = [t0, t1, t3, t0, t3, t2] * 10000
        position_data = my_obj_reader("fork.obj")
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()
