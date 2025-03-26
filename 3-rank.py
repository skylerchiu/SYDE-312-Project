from manim import *
import numpy as np

class RankVisualizationFixed(ThreeDScene):
    def construct(self):
        # Set up 3D axes with float coordinates
        axes = ThreeDAxes(x_range=[-4,4], y_range=[-4,4], z_range=[-4,4])
        title = Text("Matrix Rank Visualization").to_edge(UL)
        self.add_fixed_in_frame_mobjects(title)

        # Create 3D grid
        grid = self.get_3d_grid(axes)

        # Create vectors with explicit float coordinates
        vectors = VGroup(
            Arrow3D(start=[0.0,0.0,0.0], end=[1.0,1.0,1.0], color=RED),
            Arrow3D(start=[0.0,0.0,0.0], end=[2.0,-1.0,0.0], color=BLUE),
            Arrow3D(start=[0.0,0.0,0.0], end=[-1.0,2.0,-1.0], color=YELLOW)
        )

        # Store initial states with float preservation
        grid.save_state()
        axes.save_state()
        vectors.save_state()

        # Initial setup
        self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)
        self.play(Create(axes), Create(grid), Create(vectors))
        self.wait()

        # Rank 1 transformation with float-safe operations
        rank1_text = Text("Rank 1", color=RED).to_edge(UR)
        self.add_fixed_in_frame_mobjects(rank1_text)
        rank1_matrix = np.array([
            [1.0, 0.5, 0.5],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0]
        ], dtype=np.float64)
        self.play(
            grid.animate.apply_matrix(rank1_matrix),
            axes.animate.apply_matrix(rank1_matrix),
            vectors.animate.apply_matrix(rank1_matrix),
            run_time=3
        )
        self.wait(2)

        # Safe reset using preserved states
        self.play(
            grid.animate.restore(),
            axes.animate.restore(),
            vectors.animate.restore(),
            FadeOut(rank1_text),
            run_time=2
        )

        # Rank 2 transformation with explicit float casting
        rank2_text = Text("Rank 2", color=GREEN).to_edge(UR)
        self.add_fixed_in_frame_mobjects(rank2_text)
        rank2_matrix = np.array([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.5, 0.5, 0.1]
        ], dtype=np.float64)
        self.play(
            grid.animate.apply_matrix(rank2_matrix),
            axes.animate.apply_matrix(rank2_matrix),
            vectors.animate.apply_matrix(rank2_matrix),
            run_time=3
        )

        # Float-safe camera rotation
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()

    def get_3d_grid(self, axes):
        grid = VGroup()
        
        # Create XY plane
        xy_plane = Rectangle(
            width=axes.x_range[1] - axes.x_range[0],
            height=axes.y_range[1] - axes.y_range[0],
            fill_opacity=0.2,
            stroke_width=1,
            stroke_opacity=0.6,
            stroke_color=BLUE_D
        ).move_to(axes.c2p(0, 0, 0))
        
        # Create YZ plane
        yz_plane = Rectangle(
            width=axes.y_range[1] - axes.y_range[0],
            height=axes.z_range[1] - axes.z_range[0],
            fill_opacity=0.2,
            stroke_width=1,
            stroke_opacity=0.6,
            stroke_color=BLUE_D
        ).move_to(axes.c2p(0, 0, 0)).rotate(90*DEGREES, RIGHT)
        
        # Create XZ plane
        xz_plane = Rectangle(
            width=axes.x_range[1] - axes.x_range[0],
            height=axes.z_range[1] - axes.z_range[0],
            fill_opacity=0.2,
            stroke_width=1,
            stroke_opacity=0.6,
            stroke_color=BLUE_D
        ).move_to(axes.c2p(0, 0, 0)).rotate(90*DEGREES, UP)
        
        grid.add(xy_plane, yz_plane, xz_plane)
        return grid

