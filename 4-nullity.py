from manim import *
import numpy as np

class VisualNullity(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create the main title
        title = Text("Nullity", font_size=48)
        title.to_edge(UP)
        
        # Create the explanation text
        explanation = Text(
            "The dimension of all vectors mapped to zero (the kernel) by a linear map",
            font_size=32
        )
        explanation.next_to(title, DOWN, buff=0.5)
        
        # Create mathematical representation
        math_text = MathTex(
            "\\text{nullity}(T) = \\dim(\\ker(T))",
            font_size=36
        )
        math_text.next_to(explanation, DOWN, buff=0.5)
        
        # Create a 3D plane to represent the kernel
        kernel_plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.3,
            color=BLUE
        )
        
        # Create a vector that gets mapped to zero
        vector = Arrow3D(
            start=ORIGIN,
            end=[2, 2, 0],
            color=RED
        )
        
        # Animate the text elements one by one
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        
        self.add_fixed_in_frame_mobjects(math_text)
        self.play(Write(math_text))
        
        # Add and animate the 3D elements
        self.add(kernel_plane, vector)
        self.play(Create(kernel_plane), Create(vector))
        
        # Add a rotation animation
        self.begin_ambient_camera_rotation(rate=0.2)
        
        # Wait for a moment
        self.wait(3)
        
        # Stop the rotation
        self.stop_ambient_camera_rotation()
        
        # Final pause
        self.wait(2)
        
        # Clear the scene
        self.clear()

class MatrixExample(Scene):
    def construct(self):
        # Create the matrix title
        title = Text("Transformation Matrix - A", font_size=36)
        title.to_edge(UP)
        
        # Create the matrix using Manim's Matrix class
        matrix = Matrix([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])
        matrix.scale(1.5)  # Make the matrix larger
        
        # Add the "A =" label
        label = MathTex("A =", font_size=40)
        label.next_to(matrix, LEFT, buff=0.5)
        matrix_group = VGroup(label, matrix)
        matrix_group.move_to(ORIGIN)  # Center the matrix group horizontally
        matrix_group.next_to(title, DOWN, buff=1)  # Position relative to title
        
        # Create rank and nullity information
        info = MathTex(
            "\\text{rank}(A) = 2 \\quad \\text{nullity}(A) = 1",
            font_size=32
        )
        info.next_to(matrix_group, DOWN, buff=1)
        
        # Animate the elements
        self.play(Write(title))
        self.play(Write(matrix_group))
        
        # Highlight non-zero rows in red after matrix is rendered
        self.play(
            matrix.get_rows()[0].animate.set_color(RED),
            matrix.get_rows()[1].animate.set_color(RED)
        )
        
        self.play(Write(info))
        
        # Wait for a moment
        self.wait(2)
        
        # Clear the scene
        self.clear()

class GeometricTransformation(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create the kernel plane (larger)
        kernel_plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-3, 3],
            v_range=[-2, 2],
            fill_opacity=0.3,
            color=BLUE
        )
        
        # Create the original vector (in the kernel)
        original_vector = Arrow3D(
            start=ORIGIN,
            end=[1, 1, 1],
            color=RED
        )
        
        # Create the transformed vector (projected onto the kernel plane)
        transformed_vector = Arrow3D(
            start=ORIGIN,
            end=[1, 1, 0],
            color=GREEN
        )
        
        # Add vector value labels
        original_value = MathTex("\\vec{v} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix}", font_size=24)
        original_value.to_edge(UP, buff=0.5)  # Increased top buffer
        original_value.to_edge(LEFT, buff=0.5)
        
        # Add transformation matrix
        matrix_A = Matrix([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])
        matrix_A.scale(0.8)
        
        # Add the "A =" label
        matrix_label = MathTex("A =", font_size=32)
        matrix_label.next_to(matrix_A, LEFT, buff=0.5)
        matrix_group = VGroup(matrix_label, matrix_A)
        matrix_group.next_to(original_value, RIGHT, buff=2)
        
        # Add transformed vector value
        transformed_value = MathTex("A\\vec{v} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix}", font_size=24)
        transformed_value.next_to(matrix_group, RIGHT, buff=2)
        
        # Center all mathematical components horizontally
        math_components = VGroup(original_value, matrix_group, transformed_value)
        math_components.move_to(UP * 2.5)  # Move the entire group up by 1.5 units
        
        # Add geometric labels
        original_label = MathTex("\\vec{v}", font_size=24)
        original_label.next_to(original_vector.get_end(), UP)
        
        transformed_label = MathTex("A\\vec{v}", font_size=24)
        transformed_label.next_to(transformed_vector.get_end(), DOWN)
        
        # Add elements to scene
        self.add(kernel_plane)
        self.play(Create(kernel_plane))
        
        # Show original vector and its value
        self.add_fixed_in_frame_mobjects(original_value)
        self.play(Write(original_value))
        self.play(Create(original_vector))
        self.add_fixed_in_frame_mobjects(original_label)
        self.play(Write(original_label))
        
        # Show transformation matrix
        self.add_fixed_in_frame_mobjects(matrix_group)
        self.play(Write(matrix_group))
        
        # Transform the vector
        self.play(
            Transform(original_vector, transformed_vector),
            Transform(original_label, transformed_label)
        )
        
        # Show transformed value
        self.add_fixed_in_frame_mobjects(transformed_value)
        self.play(Write(transformed_value))
        
        # Add explanation text
        explanation = Text(
            "The matrix A projects vectors onto the xy-plane",
            font_size=24
        )
        explanation.next_to(kernel_plane, DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        
        # Add rotation
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        # Final pause
        self.wait(2)
        
class FullRankTransformation(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create the transformation plane (larger)
        transform_plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-3, 3],
            v_range=[-2, 2],
            fill_opacity=0.3,
            color=BLUE
        )
        
        # Create the original vector
        original_vector = Arrow3D(
            start=ORIGIN,
            end=[1, 1, 1],
            color=RED
        )
        
        # Create the transformed vector (scaled but not projected)
        transformed_vector = Arrow3D(
            start=ORIGIN,
            end=[2, 2, 2],  # Scaled by 2
            color=GREEN
        )
        
        # Add vector value labels
        original_value = MathTex("\\vec{v} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix}", font_size=24)
        original_value.to_edge(UP, buff=0.5)
        original_value.to_edge(LEFT, buff=0.5)
        
        # Add transformation matrix (full rank)
        matrix_A = Matrix([
            [2, 0, 0],
            [0, 2, 0],
            [0, 0, 2]
        ])
        matrix_A.scale(0.8)
        
        # Add the "A =" label
        matrix_label = MathTex("A =", font_size=32)
        matrix_label.next_to(matrix_A, LEFT, buff=0.5)
        matrix_group = VGroup(matrix_label, matrix_A)
        matrix_group.next_to(original_value, RIGHT, buff=2)
        
        # Add transformed vector value
        transformed_value = MathTex("A\\vec{v} = \\begin{pmatrix} 2 \\\\ 2 \\\\ 2 \\end{pmatrix}", font_size=24)
        transformed_value.next_to(matrix_group, RIGHT, buff=2)
        
        # Center all mathematical components horizontally
        math_components = VGroup(original_value, matrix_group, transformed_value)
        math_components.move_to(UP * 2.5)
        
        # Add geometric labels
        original_label = MathTex("\\vec{v}", font_size=24)
        original_label.next_to(original_vector.get_end(), UP)
        
        transformed_label = MathTex("A\\vec{v}", font_size=24)
        transformed_label.next_to(transformed_vector.get_end(), DOWN)
        
        # Add elements to scene
        self.add(transform_plane)
        self.play(Create(transform_plane))
        
        # Show original vector and its value
        self.add_fixed_in_frame_mobjects(original_value)
        self.play(Write(original_value))
        self.play(Create(original_vector))
        self.add_fixed_in_frame_mobjects(original_label)
        self.play(Write(original_label))
        
        # Show transformation matrix
        self.add_fixed_in_frame_mobjects(matrix_group)
        self.play(Write(matrix_group))
        
        # Transform the vector
        self.play(
            Transform(original_vector, transformed_vector),
            Transform(original_label, transformed_label)
        )
        
        # Show transformed value
        self.add_fixed_in_frame_mobjects(transformed_value)
        self.play(Write(transformed_value))
        
        # Add explanation text
        explanation = Text(
            "The matrix A scales vectors by a factor of 2",
            font_size=24
        )
        explanation.next_to(transform_plane, DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        
        # Add rotation
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        # Final pause
        self.wait(2)
        