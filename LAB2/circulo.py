"""Triangle moves along a circular path"""
import math
import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


class Example(Base):
    """ Animate triangle moving in a circular path around the origin """
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
        # Render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        self.vao_l1 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l1)
        position_data_l1 = [[ -0.3817462491654,0.2849092744913,  0.0],
                                [ -0.3044125494595,0.3058102744118,  0.0],
                                [ -0.241709549698,0.3288013743243,  0.0],
                                [-0.197817449865,0.3455221742607,  0.0],
                                [-0.1727362499604,0.4186756739825,  0.0],
                                [ -0.1622857500001,0.3538825742289,  0.0]]
        self.vertex_count_l1 = len(position_data_l1)
        position_attribute_l1 = Attribute('vec3', position_data_l1)
        position_attribute_l1.associate_variable(self.program_ref, 'position')

        # Set up vertex array object - l2 #
        self.vao_l2 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l2)
        position_data_l2 = [[ -0.1727362499604,0.4186756739825,  0.0],
                            [-0.1,0.4,  0.0],
                            [-0.0536005504135,0.3685132741733,  0.0],
                            [-0.0786817503181,0.3058102744118,  0.0],
                            [-0.1225738501511,0.3371617742925,  0.0],
                            [-0.1622857500001,0.3538825742289,  0.0]]
        self.vertex_count_l2 = len(position_data_l2)
        position_attribute_l2 = Attribute('vec3', position_data_l2)
        position_attribute_l2.associate_variable(self.program_ref, 'position')

         # Set up vertex array object - l2 #
        self.vao_l3 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l3)
        position_data_l3 = [[-0.0536005504135,0.3685132741733,  0.0],
                            [-0.0159787505566,0.3225310743482,  0.0],
                            [0.0007420493798,0.2640082745708,  0.0],
                            [0.0341836492526,0.0030705751829,  0.0],
                            [-0.0222490505327,-0.0199205247297,  0.0],
                            [-0.0515104504214,0.2640082745708,  0.0],
                            [-0.0786817503181,0.3058102744118,  0.0]]
        self.vertex_count_l3 = len(position_data_l3)
        position_attribute_l3 = Attribute('vec3', position_data_l3)
        position_attribute_l3.associate_variable(self.program_ref, 'position')

        self.vao_l4 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l4)
        position_data_l4 = [[0.0341836492526,0.0030705751829,  0.0],
                            [0.2745451483384,0.4249459739586,  0.0],
                            [0.3456085480681,0.3706033741653,  0.0],
                            [0.04672424920491,-0.034551224674,  0.0]]
        self.vertex_count_l4 = len(position_data_l4)
        position_attribute_l4 = Attribute('vec3', position_data_l4)
        position_attribute_l4.associate_variable(self.program_ref, 'position')

        self.vao_l5 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l5)
        position_data_l5 = [[0.0467242492049,-0.034551224674,  0.0],
                            [0.0300034492685,-0.2585167234418,  0.0],
                            [-0.0410599504612,-0.3212197232033,  0.0],
                            [-0.0974926502465,-0.2564266234498,  0.0],
                            [-0.0222490505327,-0.0199205247297,  0.0],
                            [0.0341836492526,0.0030705751829,  0.0]]
        self.vertex_count_l5 = len(position_data_l5)
        position_attribute_l5 = Attribute('vec3', position_data_l5)
        position_attribute_l5.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        """ Update data """
        self.translation.data[0] = 0.50 * math.sin(self.time)
        self.translation.data[1] = 0.50 * math.cos(self.time)
        # Reset color buffer with specified color
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        GL.glBindVertexArray(self.vao_l2)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l2)
        # Draw the square
        GL.glBindVertexArray(self.vao_l1)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l1)

        GL.glBindVertexArray(self.vao_l3)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l3)

        GL.glBindVertexArray(self.vao_l4)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l4)

        GL.glBindVertexArray(self.vao_l5)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l5)

        


# Instantiate this class and run the program
Example().run()