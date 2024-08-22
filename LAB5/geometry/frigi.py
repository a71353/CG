from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader

class FrigiGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        # vertices
        
        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-
        c1, c2 = [0.5,0.5,0.5], [0.5, 0.5, 0.5]
        c3, c4 = [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]
        c5, c6 = [1, 1, 0], [0, 1, 0]
        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles
        position_data = my_obj_reader('frigideira.obj')

        color_data = []
        print(len(position_data))

        for i in range (len(position_data)):
            if i < 20000:
                color_data.append(c1)
            elif i < 22500:
                color_data.append(c2)
            elif i < 25000:
                color_data.append(c3)
            else:
                color_data.append(c4)
         
        uv_data = [t0, t1, t3, t0, t3, t2] * 100000
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()
