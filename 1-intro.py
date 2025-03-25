from manim import *


class Intro(Scene):
    def construct(self):
        title = Text("Rank and Nullity").scale(1.2)
        subtitle = Text("SYDE 362 Final Project").scale(0.6)
        subtitle.next_to(title, DOWN)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(subtitle))
        self.wait(2)