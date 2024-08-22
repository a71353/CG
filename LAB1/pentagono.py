import math
import OpenGL.GL as GL
from core.base import Base
from core.utils import Utils
from core.attribute import Attribute


class Example(Base):
    """ Render a regular pentagon """
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
                fragColor = vec4(1.000,0.555,0.270,1.0); // set color to orange
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # Render settings (optional) #
        GL.glLineWidth(5)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attribute #
        radius = 0.9
        center = [0.0, 0.0]
        n_vertices = 5
        angle = 2 * math.pi / n_vertices
        vertices = []
        for i in range(n_vertices):
            x = center[0] + radius * math.cos(i * angle)
            y = center[1] + radius * math.sin(i * angle)
            vertices.append([x, y, 0.0])
        self.vertex_count = len(vertices)
        position_attribute = Attribute('vec3', vertices)
        position_attribute.associate_variable(self.program_ref, 'position')

    def update(self):
        GL.glUseProgram(self.program_ref)
        GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count)

# Instantiate this class and run the program
Example().run()