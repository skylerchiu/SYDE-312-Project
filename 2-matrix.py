from manim import *


class MatrixScene(Scene):
    def construct(self):
        # Title text
        title = Text("What Is a Matrix, Really?")
        title.to_edge(UP)  # Position at the top
        
        # Matrix
        matrix = MathTex(r"\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}")
        
        # Play animations
        self.play(Write(title))
        self.play(Write(matrix))
        self.wait(2)