import math
import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute


class Example(Base):
    """ Render a blue circle with a vertical line """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            void main()
            {
                gl_Position = vec4(position.x, position.y, position.z, 1.0);
            }
        """
        fs_code = """
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(0.0, 0.0, 1.0, 1.0); 
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # Render settings (optional) #
        GL.glLineWidth(4)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attribute for circle #
        vertex_data_circle = []
        for i in range(360):
            angle_rad = math.radians(i)
            x = 0.5 * math.cos(angle_rad)
            y = 0.5 * math.sin(angle_rad)
            vertex_data_circle.append([x, y, 0.0])
        self.vertex_count_circle = len(vertex_data_circle)
        attribute_circle = Attribute('vec3', vertex_data_circle)
        attribute_circle.associate_variable(self.program_ref, 'position')
        # Set up vertex attribute for line #
        vertex_data_line = [[0.0, -1, 0.0], [0.0, 1, 0.0]]
        self.vertex_count_line = len(vertex_data_line)
        attribute_line = Attribute('vec3', vertex_data_line)
        attribute_line.associate_variable(self.program_ref, 'position')
        # Combine vertex data #
        vertex_data = vertex_data_circle + vertex_data_line
        self.vertex_count = len(vertex_data)
        attribute = Attribute('vec3', vertex_data)
        attribute.associate_variable(self.program_ref, 'position')

    def update(self):
        GL.glUseProgram(self.program_ref)
        GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_circle)
        GL.glDrawArrays(GL.GL_LINES, self.vertex_count_circle, self.vertex_count_line)


# Instantiate this class and run the program
Example().run()