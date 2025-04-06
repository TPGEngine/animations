from manim import *
import math
import numpy as np

class ChallengeScene(Scene):
    def construct(self):
        # Setup
        # Create base
        base = Square(side_length=1.0, fill_opacity=1, color=BLUE)
        base.move_to(DOWN * 3 + UP * 0.5)
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
        ).move_to(DOWN * 3)

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

        # Solution text
        solution_text = Text("Solution: TPG - Tangled Program Graphs", color=GREEN).move_to(UP * 2.5)
        explanation_text = Text("A team-based approach where programs work together\nto learn optimal balancing strategies", font_size=24).next_to(solution_text, DOWN)

        # Transform challenge text to solution text
        self.play(
            Transform(challenge_text, solution_text),
            Write(explanation_text)
        )
        self.wait(2)

        # Create team circle
        team_circle = Circle(radius=1.5, color=BLUE)
        team_circle.move_to(ORIGIN)
        team_label = Text("Decision Team", font_size=24).move_to(team_circle.get_center())

        # First transform the rod into a tree structure
        tree_branches = VGroup()
        main_branch = Line(
            start=base.get_top(),
            end=base.get_top() + UP * 2,
            stroke_width=6,
            color=GREEN
        )
        side_branches = VGroup(
            Line(
                start=main_branch.get_center(),
                end=main_branch.get_center() + RIGHT * 0.5 + UP * 0.5,
                stroke_width=4,
                color=GREEN
            ),
            Line(
                start=main_branch.get_center(),
                end=main_branch.get_center() + LEFT * 0.5 + UP * 0.5,
                stroke_width=4,
                color=GREEN
            )
        )
        tree_branches.add(main_branch, side_branches)

        # Transform rod to tree
        self.play(
            Transform(object_to_balance, tree_branches),
            FadeOut(explanation_text),
            run_time=1.5
        )
        self.wait(1)

        # Then fade tree into team circle and remove original elements
        self.play(
            Transform(tree_branches, team_circle),
            FadeIn(team_label),
            FadeOut(base),
            FadeOut(ground),
            FadeOut(object_to_balance),
            run_time=1.5
        )
        self.wait(3)
