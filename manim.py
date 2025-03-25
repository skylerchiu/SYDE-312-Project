from manim import *

class MatrixScene(Scene):
    def construct(self):
        matrix = MathTex(r"\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}")
        self.play(Write(matrix))
        self.wait(2)