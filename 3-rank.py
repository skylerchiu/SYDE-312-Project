from manim import *
import numpy as np

class RankVisualization(Scene):
    def construct(self):
        # Create a NumberPlane as a background grid and scale it down.
        plane = NumberPlane().scale(0.5)
        self.add(plane)
        
        # Define two non-collinear vectors in ℝ² with reduced lengths.
        vector1 = Arrow(ORIGIN, 1.5 * RIGHT + 2.5 * UP, buff=0, color=YELLOW)
        vector2 = Arrow(ORIGIN, -RIGHT + 2 * UP, buff=0, color=BLUE)
        
        # Animate the appearance of the original vectors.
        self.play(GrowArrow(vector1), GrowArrow(vector2))
        self.wait(1)
        
        # Display a label showing the original rank.
        original_rank_label = Tex("Original Rank = 2").to_edge(UP)
        self.play(Write(original_rank_label))
        self.wait(1)
        
        # Display the transformation matrix in the upper left corner.
        matrix = MathTex(
            r"\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}"
        ).to_corner(UL)
        self.play(Write(matrix))
        self.wait(1)
        
        # Define the transformation matrix that maps (x, y) to (x, 0).
        transformation_matrix = np.array([
            [1, 0],
            [0, 0]
        ])
        
        # Animate the transformation:
        # Both vectors will be collapsed onto the x-axis.
        self.play( 
            ApplyMatrix(transformation_matrix, vector1),
            ApplyMatrix(transformation_matrix, vector2),
            run_time=2
        )
        self.wait(1)
        
        # Update the label to indicate the rank of the transformed image.
        new_rank_label = Tex("Transformed Rank = 1").to_edge(UP)
        self.play(Transform(original_rank_label, new_rank_label))
        self.wait(2)