from manim import *

class RowReductionScene(Scene):
    def construct(self):
        title = Text("Solving for Rank and Nullity", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

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
        self.play(FadeOut(step_3_text, run_time=0.5))
        self.play(FadeOut(step_1_text, run_time=0.5))


        self.wait(1)


        rank_text = MathTex(r"\text{3 non-zero rows, therefore, } \text{rank} = 3")
        rank_text.set_font_size(36)
        rank_text.next_to(matrix_3, DOWN)
        self.play(Write(rank_text))


        row_2_highlight = SurroundingRectangle(matrix_3[0][6:10], color=GREEN, buff=0.15)
        row_1_highlight = row_2_highlight.copy().set_color(YELLOW).shift(UP * 0.7)
        row_3_highlight = row_2_highlight.copy().set_color(BLUE).shift(DOWN * 0.7)
        self.play(Create(row_1_highlight), run_time=0.7)
        self.play(FadeOut(row_1_highlight), run_time=0.3)

        self.play(Create(row_2_highlight), run_time=0.7)
        self.play(FadeOut(row_2_highlight), run_time=0.3)

        self.play(Create(row_3_highlight), run_time=0.7)
        self.play(FadeOut(row_3_highlight), run_time=0.3)


        self.play(FadeOut(rank_text))


        bracket = Brace(matrix_3[:][0], direction=LEFT)
        rank_label = Text("RANK=3", font_size=24).next_to(bracket, LEFT)
        self.play(Create(bracket), Write(rank_label))


        self.wait(2)
        bracket = Brace(matrix_3[0][:], direction=UP)
        columns_label = Text("4 Columns", font_size=24).next_to(bracket, UP)
        self.play(Create(bracket), Write(columns_label))

        theorem = MathTex("\\textbf{\\text{Rank}}(A) + \\textbf{\\text{Nullity}}(A) = \\textbf{n}").scale(1.5)
        theorem.set_font_size(36)
        theorem.next_to(matrix_3, DOWN)
        self.play(Write(theorem))

        theorem2 = MathTex("\\textbf{\\text{3}} + \\textbf{\\text{Nullity}}(A) = \\textbf{4}").scale(1.5)
        theorem2.set_font_size(36)
        theorem2.next_to(matrix_3, DOWN)
        self.play(Transform(theorem, theorem2))

        self.wait(2)


        theorem3 = MathTex("\\textbf{\\text{Nullity}(A)} = \\textbf{\\text{4} -  \\textbf{3} = 1" ).scale(1.5)
        theorem3.set_font_size(36)
        theorem3.next_to(theorem2, DOWN)
        self.play(Write(theorem3))

        self.wait(2)
