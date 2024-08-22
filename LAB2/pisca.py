import math
import OpenGL.GL as GL
import numpy as np


from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


class Example(Base):
    """ Animate triangle changing its color """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            void main()
            {
                vec3 pos = position + translation;
                gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
            }
        """
        fs_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        GL.glLineWidth(10)
        # render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        # Set up vertex array object - ellipse
        self.vao_ellipse = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_ellipse)
        center = [0.0, 0.0]  # center of the ellipse
        a = 0.35  # horizontal radius of the ellipse
        b = 0.3  # vertical radius of the ellipse
        angle = np.linspace(0, 2 * np.pi, num=50, endpoint=True)
        x = a * np.cos(angle) + center[0]
        y = b * np.sin(angle) + center[1]
        position_data_ellipse = np.column_stack((x, y, np.zeros_like(x)))
        self.vertex_count_ellipse = len(position_data_ellipse)
        position_attribute_ellipse = Attribute('vec3', position_data_ellipse)
        position_attribute_ellipse.associate_variable(self.program_ref, 'position')

        self.vao_ellipse1 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_ellipse1)
        center = [0.0, 0.0]  # center of the ellipse
        a = 0.32  # horizontal radius of the ellipse
        b = 0.27  # vertical radius of the ellipse
        angle = np.linspace(0, 2 * np.pi, num=50, endpoint=True)
        x = a * np.cos(angle) + center[0]
        y = b * np.sin(angle) + center[1]
        position_data_ellipse1 = np.column_stack((x, y, np.zeros_like(x)))
        self.vertex_count_ellipse1 = len(position_data_ellipse1)
        position_attribute_ellipse1 = Attribute('vec3', position_data_ellipse1)
        position_attribute_ellipse1.associate_variable(self.program_ref, 'position')

        self.vao_l6 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l6)
        position_data_l6 = [[-0.03,0.50,  0.0],
                            [0.03,0.55,  0.0],
                            [0.03,-0.5,  0.0],
                            [-0.03,-0.55,  0.0]]
        self.vertex_count_l6 = len(position_data_l6)
        position_attribute_l6 = Attribute('vec3', position_data_l6)
        position_attribute_l6.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.base_color = Uniform('vec3', [0.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        """ Update data """
        # Fast change, note 3 * self.time
        self.base_color.data[0] = (math.sin(3 * self.time) + 1) / 2
        self.base_color.data[1] = (math.sin(3 * self.time) + 1) / 2
        self.base_color.data[2] = (math.sin(3 * self.time) + 1) / 2
        ## Render scene
        # Reset color buffer with specified color
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()

        # render ellipse
        GL.glBindVertexArray(self.vao_ellipse)
        GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_ellipse)
        GL.glBindVertexArray(self.vao_ellipse1)
        GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_ellipse1)
        GL.glBindVertexArray(self.vao_l6)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l6)
        self.base_color.upload_data()

# Instantiate this class and run the program
Example().run()