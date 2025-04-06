from manim import *

class HierarchyScene(Scene):
    def construct(self):
        # Cleanup: Fade out previous scene elements
        if self.mobjects:
            self.play(FadeOut(Group(*self.mobjects)))
            self.wait(0.5)

        # Create initial centered Team A
        team_a = Circle(radius=0.5, color=BLUE)
        team_a.move_to(LEFT * 2)  # Move left to make room for arrow
        team_a_label = Text("Team A", font_size=24).next_to(team_a, UP, buff=0.2)

        # Create initial action
        initial_action = Square(side_length=0.5, color=RED)
        initial_action.move_to(RIGHT * 2)  # Move right to make room for arrow
        initial_action_label = Text("Action", font_size=24).next_to(initial_action, DOWN, buff=0.2)

        # Create initial arrow
        initial_arrow = Arrow(
            start=team_a.get_right(),
            end=initial_action.get_left(),
            buff=0.2,
            color=GREEN
        )

        # Center the entire group
        initial_group = VGroup(team_a, team_a_label, initial_action, initial_action_label, initial_arrow)
        initial_group.move_to(ORIGIN)

        # Animation 1: Show initial simple structure
        self.play(
            Create(team_a),
            Write(team_a_label),
            Create(initial_action),
            Write(initial_action_label),
            run_time=1
        )
        self.play(
            GrowArrow(initial_arrow),
            run_time=1
        )
        self.wait(0.5)

        # Create teams at different levels
        # Level 1 (Top) - Move Team A up
        team_a_target = Circle(radius=0.5, color=BLUE)
        team_a_target.move_to(UP * 2)
        team_a_label_target = Text("Team A", font_size=24).next_to(team_a_target, UP, buff=0.2)

        # Level 2 (Middle)
        team_b = Circle(radius=0.5, color=BLUE)
        team_b.move_to(ORIGIN + LEFT * 1.5)
        team_b_label = Text("Team B", font_size=24).next_to(team_b, LEFT, buff=0.2)

        team_c = Circle(radius=0.5, color=BLUE)
        team_c.move_to(ORIGIN + RIGHT * 1.5)
        team_c_label = Text("Team C", font_size=24).next_to(team_c, RIGHT, buff=0.2)

        # Level 3 (Bottom)
        team_d = Circle(radius=0.5, color=BLUE)
        team_d.move_to(DOWN * 2)
        team_d_label = Text("Team D", font_size=24).next_to(team_d, DOWN, buff=0.2)

        # Final Action Icon
        final_action = Square(side_length=0.5, color=RED)
        final_action.move_to(DOWN * 2 + RIGHT * 3)
        final_action_label = Text("Action", font_size=24).next_to(final_action, DOWN, buff=0.2)

        # Create hierarchical arrows
        arrow1 = Arrow(
            start=team_a_target.get_bottom(),
            end=team_b.get_top(),
            buff=0.2,
            color=GREEN
        )
        arrow2 = Arrow(
            start=team_a_target.get_bottom(),
            end=team_c.get_top(),
            buff=0.2,
            color=GREEN
        )
        arrow3 = Arrow(
            start=team_b.get_bottom(),
            end=team_d.get_top(),
            buff=0.2,
            color=GREEN
        )
        arrow4 = Arrow(
            start=team_c.get_bottom(),
            end=team_d.get_top(),
            buff=0.2,
            color=GREEN
        )
        arrow5 = Arrow(
            start=team_d.get_right(),
            end=final_action.get_left(),
            buff=0.2,
            color=GREEN
        )

        # Animation 2: Transform to hierarchical structure
        self.play(
            # Move Team A up
            team_a.animate.move_to(team_a_target.get_center()),
            Transform(team_a_label, team_a_label_target),
            # Fade out initial action and arrow
            FadeOut(initial_action),
            FadeOut(initial_action_label),
            FadeOut(initial_arrow),
            run_time=1
        )

        # Animation 3: Add second level teams
        self.play(
            Create(team_b),
            Write(team_b_label),
            Create(team_c),
            Write(team_c_label),
            run_time=1
        )
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            run_time=1
        )
        self.wait(0.5)

        # Animation 4: Add third level team
        self.play(
            Create(team_d),
            Write(team_d_label),
            run_time=1
        )
        self.play(
            GrowArrow(arrow3),
            GrowArrow(arrow4),
            run_time=1
        )
        self.wait(0.5)

        # Animation 5: Add final action and connection
        self.play(
            Create(final_action),
            Write(final_action_label),
            run_time=1
        )
        self.play(
            GrowArrow(arrow5),
            run_time=1
        )
        self.wait(0.5)

        # Animation 6: Show information flow using MoveAlongPath
        # Create a dot to move along the paths
        dot = Dot(color=YELLOW, radius=0.1)
        dot.move_to(team_a_target.get_center())

        # Create smooth paths using VMobject
        def create_path(*arrows):
            path = VMobject()
            points = []
            for arrow in arrows:
                points.extend(arrow.points)
            path.set_points_as_corners(points)
            return path

        # Create paths for both routes
        path1 = create_path(arrow1, arrow3, arrow5)
        path2 = create_path(arrow2, arrow4, arrow5)

        # Animate along paths
        self.play(
            MoveAlongPath(dot, path1, rate_func=rate_functions.ease_in_out_sine),
            run_time=3
        )
        self.wait(0.5)
        self.play(
            MoveAlongPath(dot, path2, rate_func=rate_functions.ease_in_out_sine),
            run_time=3
        )
        self.play(FadeOut(dot))

        # Hold final state
        self.wait(3)
