import numpy as np
import math
import pathlib
import sys
from math import pi
import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core_ext.camera import Camera
from core.attribute import Attribute
from core.uniform import Uniform
from core.matrix import Matrix
from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.movement_rig import MovementRig
from extras.movementobj import MovementObj
from geometry.spatula import SpatulaGeometry
from geometry.fork import ForkGeometry
from geometry.frigi import FrigiGeometry
from material.surface import SurfaceMaterial
from material.texture import TextureMaterial
from core_ext.texture import Texture

class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add camera movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        vs_code = """
            in vec3 position;
            uniform mat4 projectionMatrix;
            uniform mat4 modelMatrix;
            void main()
            {
                gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
            }
        """
        fs_code = """
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(0.5, 0.5, 0.5, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)

        ### Set up uniforms ###
        m_matrix = Matrix.make_translation(0, 0, -1)
        self.model_matrix = Uniform('mat4', m_matrix)
        self.model_matrix.locate_variable(self.program_ref, 'modelMatrix')
        p_matrix = Matrix.make_perspective()
        self.projection_matrix = Uniform('mat4', p_matrix)
        self.projection_matrix.locate_variable(self.program_ref, 'projectionMatrix')
        # movement speed, units per second
        self.move_speed = 0.5
        # rotation speed, radians per second
        self.turn_speed = 90 * (pi / 180)

        #garfo
        fork_geometry = ForkGeometry()
        fork_material = TextureMaterial(
            texture=Texture(file_name="images/st3.jpg"),
            property_dict={"repeatUV": [5,5]}
        )
        fork_mesh = Mesh(fork_geometry, fork_material)
        fork_mesh.translate(-1.5, 0, 0)
        self.scene.add(fork_mesh)

        #espatula
        spatula_geometry = SpatulaGeometry()
        spatula_material = TextureMaterial(
            texture=Texture(file_name="images/st.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        spatula_mesh = Mesh(spatula_geometry, spatula_material)
        spatula_mesh.translate(1.5, 0, 0)
        self.scene.add(spatula_mesh)

        #frigideira
        frigi_geometry = FrigiGeometry()
        frigi_material = TextureMaterial(
            texture=Texture(file_name="images/frig.jpg"),
            property_dict={"repeatUV": [10, 10]}
        )
        frigi_mesh = Mesh(frigi_geometry, frigi_material)
        frigi_mesh.translate(0, 0, 0)
        self.scene.add(frigi_mesh)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0.5, 1, 5])

        self.mov = MovementObj()
        self.mov.add(spatula_mesh)

        self.meshs = frigi_mesh
        self.meshf = fork_mesh
        self.meshsp = spatula_mesh

        self.additional_rotationy = 0
        self.additional_rotationx = 0


    def update(self):
        self.meshf.rotate_y(0 + self.additional_rotationy)
        self.meshf.rotate_x(0 + self.additional_rotationx)
        self.meshs.rotate_y(0 + self.additional_rotationy)
        self.meshs.rotate_x(0 + self.additional_rotationx)
        self.meshsp.rotate_y(0 + self.additional_rotationy)
        self.meshsp.rotate_x(0 + self.additional_rotationx)
        self.rig.update(self.input, self.delta_time)
        self.mov.update(self.input, self.delta_time)

        move_amount = self.move_speed * self.delta_time
        turn_amount = self.turn_speed * self.delta_time
        tamount = 0.01

        if self.input.is_key_pressed('space'):
            m = Matrix.make_rotation_y(tamount)
            self.meshf._model_matrix.set_data(m @ self.model_matrix.data)

            # Adicione o seguinte código para mover o garfo em um círculo
        radius = 2  # Raio do círculo
        angular_speed = 0.05  # Velocidade angular do movimento circular
        time = self.time  # Tempo decorrido desde o início da execução

        # Calcula a posição do garfo no círculo
        fork_position = [
            radius * math.cos(angular_speed * time),
            radius * math.sin(angular_speed * time),
            0
        ]
        self.meshf.set_translation(*fork_position)
        

        self.renderer.render(self.scene, self.camera)

        for keys in self.input.key_pressed_list:
            if keys == '+':
                    self.additional_rotationy += 0.01
                    self.additional_rotationx += 0.01
            if keys == '-':
                    self.additional_rotationy -= 0.01
                    self.additional_rotationx -= 0.01

Example(screen_size=[800, 600]).run()
