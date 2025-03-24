from manim import *
import numpy as np

class VisualNullity(ThreeDScene):
    def construct(self):
        # Create 3D axes for reference.
        axes = ThreeDAxes()
        
        # Set the camera orientation for a good 3D perspective.
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create a vector that is not in the kernel.
        vector = Arrow3D(
            start=ORIGIN,
            end=3 * RIGHT + 2 * UP + 2 * OUT,
            color=YELLOW,
        )
        
        # Create a vector that lies entirely in the kernel (along the z-axis).
        kernel_vector = Arrow3D(
            start=ORIGIN,
            end=3 * OUT,
            color=RED,
        )
        # Label the kernel vector.
        kernel_label = Text("Kernel", font_size=24, color=RED).next_to(kernel_vector.get_end(), UP)
        
        # Display nullity information (nullity = dimension of the kernel).
        nullity_info = Text("Nullity = 1", font_size=36).to_corner(DR)
        
        # Add the axes, both vectors, the kernel label, and the nullity info to the scene.
        self.add(axes, vector, kernel_vector, kernel_label, nullity_info)
        self.wait(1)
        
        # Define the projection matrix that projects (x, y, z) to (x, y, 0).
        # This matrix has a nullity of 1 since its kernel is the z-axis.
        proj_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])
        
        # Animate the transformation:
        # - The yellow vector will have its z-component removed.
        # - The red vector lies in the kernel, so it will collapse to the origin.
        self.play(
            ApplyMatrix(proj_matrix, vector),
            ApplyMatrix(proj_matrix, kernel_vector),
            run_time=2
        )
        self.wait(2)