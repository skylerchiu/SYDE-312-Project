from manim import *

class RankNullityApplications(Scene):
    def construct(self):
        title = Text("Applications of Rank and Nullity", font_size=48).to_edge(UP)
        self.play(Write(title))
        
        # Rank applications
        rank_text = Text("Rank used in:", font_size=36).to_edge(LEFT, buff=1.5).shift(UP*1.5)
        rank_points = BulletedList(
            "Image compression (SVD)",
            "Solving systems of equations",
            "Machine learning (Feature reduction)",
            font_size=30
        ).next_to(rank_text, DOWN, aligned_edge=LEFT)
        
        self.play(FadeIn(rank_text, shift=RIGHT), FadeIn(rank_points, shift=RIGHT))
        
            
        # Illustrations
        image_matrix = ImageMobject("image_compression.jpeg").scale(1).to_edge(RIGHT)
        eqn_system = MathTex("Ax = b", font_size=40).next_to(image_matrix, UP)
        
        self.play(FadeIn(image_matrix), Write(eqn_system))
        self.wait(1)
        
        # Transition to broader applications
        self.play(FadeOut(image_matrix, eqn_system))