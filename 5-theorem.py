from manim import *

class RankNullityTheorem(Scene):
    def construct(self):
        # Title
        title = Text("The Rank-Nullity Theorem").scale(1.2).to_edge(UP)
        
        # Theorem statement
        theorem_text = MathTex("\\text{For an } m x n \\text{ matrix } A:").scale(0.8)
        equation = MathTex("\\textbf{\\text{Rank}}(A) + \\textbf{\\text{Nullity}}(A) = \\textbf{n}").scale(1.5)
        condition = Text("(where n = number of columns)")
        
        theorem_text.next_to(title, DOWN, buff=1.0)
        equation.next_to(theorem_text, DOWN, buff=0.5)
        condition.next_to(equation, DOWN, buff = 0.7)
        
        self.play(Write(title))
        self.play(Write(theorem_text))
        self.play(Write(equation))
        self.play(Write(condition))
        self.wait(2)