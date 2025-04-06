from manim import *

class TPGScene(Scene):
    def construct(self):
        # Cleanup: Fade out previous scene elements
        if self.mobjects:  # Check if there are any mobjects to fade out
            self.play(FadeOut(Group(*self.mobjects)))
            self.wait(0.5)

        # Create Team Circle and Label
        team_circle = Circle(radius=1.5, color=BLUE)
        team_circle.move_to(ORIGIN + UP * 1.5)
        team_label = Text("Decision Team", font_size=24).move_to(team_circle.get_center())
        
        # Create Action Representations first to position arrows correctly
        action1 = Square(side_length=0.5, color=RED)
        action1.move_to(team_circle.get_right() + RIGHT * 2.5)
        action1_label = Text("Action A", font_size=16).next_to(action1, DOWN, buff=0.1)
        
        action2 = Circle(radius=0.3, color=YELLOW)
        action2.move_to(team_circle.get_bottom() + DOWN * 2.5)
        action2_label = Text("Action B", font_size=16).next_to(action2, DOWN, buff=0.1)
        
        action3 = Triangle(color=PURPLE).scale(0.3)
        action3.move_to(team_circle.get_left() + LEFT * 2.5)
        action3_label = Text("Action C", font_size=16).next_to(action3, DOWN, buff=0.1)

        # Create Program Arrows pointing to the actions
        arrow1 = Arrow(
            start=team_circle.get_right(),
            end=action1.get_left(),
            buff=0.2,  # Add some space between arrow and shape
            color=GREEN
        )
        arrow2 = Arrow(
            start=team_circle.get_bottom(),
            end=action2.get_top(),
            buff=0.2,
            color=GREEN
        )
        arrow3 = Arrow(
            start=team_circle.get_left(),
            end=action3.get_right(),
            buff=0.2,
            color=GREEN
        )

        # Animation Sequence
        # 1. Create Team Circle and Label
        self.play(
            Create(team_circle),
            FadeIn(team_label),
            run_time=1
        )
        self.wait(0.5)

        # 2. Grow Program Arrows
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            GrowArrow(arrow3),
            run_time=1
        )
        self.wait(0.5)

        # 4. Show Actions
        self.play(
            FadeIn(action1),
            FadeIn(action1_label),
            FadeIn(action2),
            FadeIn(action2_label),
            FadeIn(action3),
            FadeIn(action3_label),
            run_time=1
        )
        self.wait(1)

        # Highlight team circle when "Teams" appears
        self.play(
            team_circle.animate.set_fill(BLUE, opacity=0.3),
            run_time=0.5
        )
        self.wait(0.2)

        # Scene 3: The Decision Process - Input and Action
        # 1. Cleanup previous text labels
        self.play(
            FadeOut(team_label),
            FadeOut(action1_label),
            FadeOut(action2_label),
            FadeOut(action3_label),
            run_time=0.5
        )
        self.wait(0.5)

        # 2. Create and animate input
        input_icon = Square(side_length=0.5, color=WHITE)
        input_icon.move_to(LEFT * 4)
        input_text = Text("Input", font_size=16).next_to(input_icon, DOWN, buff=0.1)
        
        self.play(
            FadeIn(input_icon),
            FadeIn(input_text),
            run_time=0.5
        )
        self.wait(0.5)

        # Move input towards team circle and remove text
        self.play(
            input_icon.animate.move_to(team_circle.get_center()),
            FadeOut(input_text),
            run_time=1
        )
        self.wait(0.5)

        # 3. Create and animate suggestion bars
        # Create bars with initial height
        bar1 = Rectangle(height=0.1, width=0.2, color=RED, fill_opacity=0.8)
        bar1.next_to(action1, RIGHT, buff=0.2)
        bar2 = Rectangle(height=0.1, width=0.2, color=YELLOW, fill_opacity=0.8)
        bar2.next_to(action2, RIGHT, buff=0.2)
        bar3 = Rectangle(height=0.1, width=0.2, color=PURPLE, fill_opacity=0.8)
        bar3.next_to(action3, LEFT, buff=0.2)  # Changed to LEFT side

        # First show the bars
        self.play(
            FadeIn(bar1),
            FadeIn(bar2),
            FadeIn(bar3),
            run_time=0.5
        )
        self.wait(0.5)

        # Then animate them growing to different heights
        self.play(
            bar1.animate.stretch_to_fit_height(1.5),
            bar2.animate.stretch_to_fit_height(0.8),
            bar3.animate.stretch_to_fit_height(1.2),
            run_time=1
        )
        self.wait(0.5)

        # Highlight winning bar (bar1)
        self.play(
            Flash(bar1, color=RED, line_length=0.2, flash_radius=0.3),
            run_time=0.5
        )

        # 4. Highlight winning program and action
        self.play(
            arrow1.animate.set_color(YELLOW),
            Indicate(action1),
            run_time=0.5
        )
        self.wait(0.5)
