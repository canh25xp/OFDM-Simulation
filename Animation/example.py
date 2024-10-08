from manim import *

config.background_color = WHITE

class Example(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(LEFT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))
        
        
with tempconfig({"quality": "medium_quality", "preview": False}):
    scene = Example()
    scene.render()