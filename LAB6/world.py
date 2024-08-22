import numpy as np
import math
import pathlib
import sys
import time
import pygame
from pygame.locals import *

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.movement_rig import MovementRig
from extras.movementobj import MovementObj
from extras.movementesp import MovementEsp
from geometry.spatula import SpatulaGeometry
from geometry.fork import ForkGeometry
from geometry.frigi import FrigiGeometry
from geometry.comida import ComidaGeometry
from material.texture import TextureMaterial
from core_ext.texture import Texture


class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add camera movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)

        # Garfo
        fork_geometry = ForkGeometry()
        fork_material = TextureMaterial(
            texture=Texture(file_name="images/st3.jpg"),
            property_dict={"repeatUV": [5,5]}
        )
        fork_mesh = Mesh(fork_geometry, fork_material)
        fork_mesh.translate(0, 0, 0)
        self.scene.add(fork_mesh)

        # Espátula
        spatula_geometry = SpatulaGeometry()
        spatula_material = TextureMaterial(
            texture=Texture(file_name="images/st.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        spatula_mesh = Mesh(spatula_geometry, spatula_material)
        spatula_mesh.translate(1.5, 0, 0)
        self.scene.add(spatula_mesh)

        # Frigideira
        frigi_geometry = FrigiGeometry()
        frigi_material = TextureMaterial(
            texture=Texture(file_name="images/frig.jpg"),
            property_dict={"repeatUV": [10, 10]}
        )
        frigi_mesh = Mesh(frigi_geometry, frigi_material)
        frigi_mesh.translate(0, 0, 0)
        self.scene.add(frigi_mesh)

        # Comida
        self.comida_geometry = ComidaGeometry()
        self.comida_material = TextureMaterial(
            texture=Texture(file_name="images/food.jpg"),
            property_dict={"repeatUV": [5,5]}
        )
        self.comida_mesh = Mesh(self.comida_geometry, self.comida_material)
        self.comida_mesh.translate(0, 0, 0)
        self.scene.add(self.comida_mesh)


        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0.5, 1, 5])

        self.mov = MovementObj()
        self.mov.add(fork_mesh)

        self.posesp = MovementEsp()
        self.posesp.add(spatula_mesh)

        self.meshs = frigi_mesh
        self.meshf = fork_mesh
        self.meshsp = spatula_mesh
        self.meshc = self.comida_mesh


        self.additional_rotationy = 0
        self.additional_rotationx = 0

        self.start_time = time.time()

        self.pos_esp = 1.5

    def update(self):
        self.meshf.rotate_y(0 + self.additional_rotationy)
        self.rig.update(self.input, self.delta_time)
        self.mov.update(self.input, self.delta_time)
        self.posesp.update(self.input, self.delta_time)

        for keys in self.input.key_pressed_list:
            if keys == '+':
                self.additional_rotationy = 0.3
            if keys == '-':
                self.additional_rotationy = 0
            if keys == 'k':
                if(self.pos_esp >= 0):
                    self.pos_esp -= 0.03
                if(self.pos_esp <= 0):
                    self.comida_mesh.set_position([2.5, 0, 1.5])

        self.renderer.render(self.scene, self.camera)

Example(screen_size=[800, 600]).run()
