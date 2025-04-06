from manim import *
import math

class ChallengeScene(Scene):
    def construct(self):
        # Setup
        # Create base
        base = Square(side_length=1.0, fill_opacity=1, color=BLUE)
        base.move_to(DOWN * 2)
        initial_base_pos = base.get_center()

        # Create object to balance
        object_to_balance = Line(
            start=base.get_top(),
            end=base.get_top() + UP * 3,
            stroke_width=8,
            color=WHITE
        )

        # Create ground line
        ground = Line(
            start=LEFT * 7,
            end=RIGHT * 7,
            color=GRAY
        ).next_to(base, DOWN, buff=0.5)

        # Create text
        challenge_text = Text("Problem: Learning to balance the rod").move_to(UP * 2.5)

        # Fade in elements
        self.play(
            FadeIn(base),
            FadeIn(object_to_balance),
            FadeIn(ground)
        )
        self.wait(0.5)

        # Attempt 1 - Instability & Fall
        rotation_point = base.get_top()
        
        # Animation group for instability
        self.play(
            AnimationGroup(
                Rotate(object_to_balance, angle=PI/3, about_point=rotation_point),
                Succession(
                    base.animate(rate_func=linear).shift(LEFT*0.3),
                    base.animate(rate_func=linear).shift(RIGHT*0.4),
                    base.animate(rate_func=linear).shift(LEFT*0.2),
                    base.animate(rate_func=linear).shift(RIGHT*0.1),
                ),
                lag_ratio=0.5
            ),
            run_time=1.5
        )

        # Fall completely
        self.play(
            Rotate(object_to_balance, angle=PI/2 - PI/3, about_point=rotation_point),
            run_time=0.5
        )
        self.wait(0.5)

        # Attempt 2 - Reset & Different Fall
        # Reset system
        self.play(
            base.animate.move_to(initial_base_pos),
            Rotate(object_to_balance, angle=-PI/2, about_point=rotation_point),
            run_time=0.5
        )

        # Second instability animation
        self.play(
            AnimationGroup(
                Rotate(object_to_balance, angle=-PI/3.5, about_point=rotation_point),
                Succession(
                    base.animate(rate_func=linear).shift(RIGHT*0.2),
                    base.animate(rate_func=linear).shift(LEFT*0.3),
                    base.animate(rate_func=linear).shift(RIGHT*0.1),
                    base.animate(rate_func=linear).shift(LEFT*0.2),
                ),
                lag_ratio=0.5
            ),
            run_time=1.5
        )

        # Second fall
        self.play(
            Rotate(object_to_balance, angle=PI/2 - PI/3.5, about_point=rotation_point),
            run_time=0.5
        )
        self.wait(0.5)

        # Show text
        self.play(Write(challenge_text))
        self.wait(2)
