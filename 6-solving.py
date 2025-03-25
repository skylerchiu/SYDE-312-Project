from manim import *

class RowReductionScene(Scene):
    def construct(self):
        # Title
        title = Text("Solving for Rank", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Initial Matrix
        matrix_1 = MathTex(r"\begin{bmatrix} 1 & 2 & 0 & 3 \\ 2 & 4 & 1 & 6 \\ 0 & 0 & 1 & 1 \end{bmatrix}")
        matrix_1.scale(1.2)
        self.play(Write(matrix_1, run_time=0.8))

        step_1_text = Text("Convert to Row Echelon Form", font_size=36)
        step_1_text.next_to(matrix_1, DOWN)
        self.play(Write(step_1_text))

        step_2_text = Text("R2 → R2 - 2R1", font_size=36)
        step_2_text.to_edge(DOWN)
        self.play(Write(step_2_text))
        matrix_2 = MathTex(r"\begin{bmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 \end{bmatrix}")
        matrix_2.scale(1.2)
        self.play(Transform(matrix_1, matrix_2))
        self.play(FadeOut(step_2_text, run_time=0.5))

        step_3_text = Text("R3 → R3 - R2", font_size=36)
        step_3_text.to_edge(DOWN)
        self.play(Write(step_3_text))

        matrix_3 = MathTex(r"\begin{bmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}")
        matrix_3.scale(1.2)
        self.play(Transform(matrix_1, matrix_3))
        self.play(FadeOut(step_3_text))

        # Get the center of each row by splitting the matrix into rows manually
        # row_1 = matrix_3[0:4]  # First row
        # row_2 = matrix_3[5:9]  # Second row
        # row_3 = matrix_3[10:14]  # Third row

        #         # Create circles around each row's center
        # circle_1 = Circle(radius=0.5).move_to(row_1.get_center())
        # circle_2 = Circle(radius=0.5).move_to(row_2.get_center())
        # circle_3 = Circle(radius=0.5).move_to(row_3.get_center())
        
        # # Add the matrix and circles to the scene
        # self.play(Transform(matrix_1, matrix_3))
        # self.play(FadeOut(step_3_text))

        # # Display circles around the rows
        # self.play(Create(circle_1), Create(circle_2), Create(circle_3))