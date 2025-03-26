from manim import *

class MatrixTransformationScene(Scene):
    def construct(self):
        # Title
        title = Text("What is a Matrix, Really?")
        title.to_edge(UP)

        # Define the matrix M
        matrix = MathTex(
            r"\mathbf{M} = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}"
        )

        # Define the input vector x
        input_vector = MathTex(
            r"\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}"
        )

        # Define the matrix-vector multiplication
        multiplication = MathTex(
            r"\mathbf{M} \cdot \mathbf{x} =",
            r"x_1 \begin{bmatrix} a \\ d \\ g \end{bmatrix} +"
            r"x_2 \begin{bmatrix} b \\ e \\ h \end{bmatrix} +"
            r"x_3 \begin{bmatrix} c \\ f \\ i \end{bmatrix}"
        )

        # Position elements
        matrix.shift(UP * 1.5)
        input_vector.next_to(matrix, RIGHT, buff=1)
        multiplication.next_to(matrix, DOWN, buff=1)

        # Play animations
        self.play(Write(title))
        self.play(Write(matrix))
        self.wait(1)

        self.play(Write(input_vector))
        self.wait(1)

        self.play(Transform(matrix, multiplication))
        self.wait(3)
