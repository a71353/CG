"""Animation example"""
import OpenGL.GL as GL
import pygame
import numpy as np
from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


class Example(Base):
    """ Render two shapes """

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
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(0.912,0.358,0.009, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)

        # render settings #
        GL.glLineWidth(10)

        GL.glUseProgram(self.program_ref)

        self.vao_l1 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l1)
        position_data_l1 = [[-0.8817462491654,0.4849092744913,0.0],
                                [-0.8044125494595,0.5058102744118,0.0],
                                [-0.741709549698,0.5288013743243,0.0],
                                [-0.697817449865,0.5455221742607,0.0],
                                [-0.6727362499604,0.6186756739825,0.0],
                                [-0.6622857500001,0.5538825742289,0.0]]
        self.vertex_count_l1 = len(position_data_l1)
        position_attribute_l1 = Attribute('vec3', position_data_l1)
        position_attribute_l1.associate_variable(self.program_ref, 'position')

        self.vao_l2 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l2)
        position_data_l2 = [[-0.6727362499604,0.6186756739825,0.0],
                            [-0.6,0.6,0.0],
                            [-0.5536005504135,0.5685132741733,0.0],
                            [-0.5786817503181,0.5058102744118,0.0],
                            [-0.6225738501511,0.5371617742925,0.0],
                            [-0.6622857500001,0.5538825742289,0.0]]
        self.vertex_count_l2 = len(position_data_l2)
        position_attribute_l2 = Attribute('vec3', position_data_l2)
        position_attribute_l2.associate_variable(self.program_ref, 'position')

        self.vao_l3 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l3)
        position_data_l3 = [[-0.5536005504135,0.5685132741733,0.0],
                            [-0.5159787505566,0.5225310743482,0.0],
                            [-0.4992579506202,0.4640082745708,0.0],
                            [-0.4658163507474,0.2030705751829,0.0],
                            [-0.5222490505327,0.1800794752703,0.0],
                            [-0.5515104504214,0.4640082745708,0.0],
                            [-0.5786817503181,0.5058102744118,0.0]]
        self.vertex_count_l3 = len(position_data_l3)
        position_attribute_l3 = Attribute('vec3', position_data_l3)
        position_attribute_l3.associate_variable(self.program_ref, 'position')

        self.vao_l4 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l4)
        position_data_l4 = [[-0.4658163507474,0.2030705751829,0.0],
                            [-0.2254548516616,0.6249459739586,0.0],
                            [-0.1543914519319,0.5706033741653,0.0],
                            [-0.4532757507951,0.165448775326,0.0]]
        self.vertex_count_l4 = len(position_data_l4)
        position_attribute_l4 = Attribute('vec3', position_data_l4)
        position_attribute_l4.associate_variable(self.program_ref, 'position')

        self.vao_l5 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l5)
        position_data_l5 = [[-0.4532757507951,0.165448775326,0.0],
                            [-0.4699965507315,-0.0585167234418,0.0],
                            [-0.5410599504612,-0.1212197232033,0.0],
                            [-0.5974926502465,-0.0564266234498,0.0],
                            [-0.5222490505327,0.1800794752703,0.0],
                            [-0.4658163507474,0.2030705751829,0.0]]
        self.vertex_count_l5 = len(position_data_l5)
        position_attribute_l5 = Attribute('vec3', position_data_l5)
        position_attribute_l5.associate_variable(self.program_ref, 'position')
        self.translation = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')

        self.vao_ellipse = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_ellipse)
        center = [0.4, 0.2]  # center of the ellipse
        a = 0.35  # horizontal radius of the ellipse
        b = 0.3  # vertical radius of the ellipse
        angle = np.linspace(0, 2*np.pi, num=50, endpoint=True)
        x = a * np.cos(angle) + center[0]
        y = b * np.sin(angle) + center[1]
        position_data_ellipse = np.column_stack((x, y, np.zeros_like(x)))
        self.vertex_count_ellipse = len(position_data_ellipse)
        position_attribute_ellipse = Attribute('vec3', position_data_ellipse)
        position_attribute_ellipse.associate_variable(self.program_ref, 'position')

        self.vao_ellipse1 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_ellipse1)
        center = [0.4, 0.2]  # center of the ellipse
        a = 0.32  # horizontal radius of the ellipse
        b = 0.27  # vertical radius of the ellipse
        angle = np.linspace(0, 2*np.pi, num=50, endpoint=True)
        x = a * np.cos(angle) + center[0]
        y = b * np.sin(angle) + center[1]
        position_data_ellipse1 = np.column_stack((x, y, np.zeros_like(x)))
        self.vertex_count_ellipse1 = len(position_data_ellipse1)
        position_attribute_ellipse1 = Attribute('vec3', position_data_ellipse1)
        position_attribute_ellipse1.associate_variable(self.program_ref, 'position')

        self.vao_l6 = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_l6)
        position_data_l6 = [[0.37,0.70,0.0],
                            [0.43,0.75,0.0],
                            [0.43,-0.3,0.0],
                            [0.37,-0.35,0.0]]
        self.vertex_count_l6 = len(position_data_l6)
        position_attribute_l6 = Attribute('vec3', position_data_l6)
        position_attribute_l6.associate_variable(self.program_ref, 'position')
        self.translation1 = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation1.locate_variable(self.program_ref, 'translation')

    def update(self):  

        """debug printing"""
        if len(self.input.key_down_list) > 0:
            print( "Keys down:", self.input.key_down_list )
        if len(self.input.key_pressed_list) > 0:
            print( "Keys pressed:", self.input.key_pressed_list )
        if len(self.input.key_up_list) > 0:
            print( "Keys up:", self.input.key_up_list )

        for keys in self.input.key_pressed_list:
            if keys == 'left':
                    self.translation1.data[0] -= 0.01
            if keys == 'right':
                    self.translation1.data[0] += 0.01
            if keys == 'up':
                    self.translation1.data[1] += 0.01
            if keys == 'down':
                    self.translation1.data[1] -= 0.01
            if keys == 'a':
                    self.translation.data[0] -= 0.01
            if keys == 'd':
                    self.translation.data[0] += 0.01
            if keys == 'w':
                    self.translation.data[1] += 0.01
            if keys == 's':
                    self.translation.data[1] -= 0.01

        self.translation.upload_data()
        
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glBindVertexArray(self.vao_l1)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l1)

        GL.glBindVertexArray(self.vao_l2)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l2)

        GL.glBindVertexArray(self.vao_l3)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l3)

        GL.glBindVertexArray(self.vao_l4)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l4)

        GL.glBindVertexArray(self.vao_l5)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l5)
        
        self.translation1.upload_data()
        GL.glBindVertexArray(self.vao_ellipse)
        GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_ellipse)

        GL.glBindVertexArray(self.vao_ellipse1)
        GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_ellipse1)

        GL.glBindVertexArray(self.vao_l6)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_l6)


# Instantiate this class and run the program
Example().run()