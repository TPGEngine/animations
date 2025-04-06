from manim import *
import random

class HierarchyScene(Scene):
    def create_complex_node(self, position, node_id, colors=None):
        """Create a complex node with multiple color segments."""
        if colors is None:
            # Default colors if none provided
            colors = [BLUE, RED, YELLOW, GREEN, PURPLE]
            random.shuffle(colors)
            colors = colors[:random.randint(2, 5)]  # Use 2-5 colors
        
        # Create circle with segments
        radius = 0.25  # Reduced radius for better fit
        circle = Circle(radius=radius)
        segments = VGroup()
        
        # Create pie segments
        num_segments = len(colors)
        for i, color in enumerate(colors):
            angle_start = i * TAU / num_segments
            angle_end = (i + 1) * TAU / num_segments
            segment = AnnularSector(
                inner_radius=0,
                outer_radius=radius,
                angle=angle_end - angle_start,
                start_angle=angle_start,
                color=color,
                fill_opacity=1
            )
            segments.add(segment)
        
        # Add node ID
        node_id_text = Text(str(node_id), font_size=14, color=WHITE)  # Smaller font
        node_id_text.move_to(circle.get_center())
        
        # Group everything
        node = VGroup(segments, node_id_text)
        node.move_to(position)
        return node

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
        self.wait(0.5)

        # Store the current hierarchy state
        hierarchy_group = VGroup(
            team_a, team_a_label,
            team_b, team_b_label,
            team_c, team_c_label,
            team_d, team_d_label,
            final_action, final_action_label,
            arrow1, arrow2, arrow3, arrow4, arrow5
        )
        
        # Transition text
        transition_text = Text("Evolving into a complex program graph...", font_size=32)
        transition_text.to_edge(UP)
        
        # Show transition text
        self.play(
            Write(transition_text),
            run_time=1
        )
        self.wait(0.5)
        
        # Create complex nodes
        nodes = VGroup()
        
        # Define clear hierarchical levels
        LEVEL_SPACING = 1.25  # Vertical spacing between levels
        NODE_SPACING = 1.5    # Horizontal spacing between nodes
        
        # Level 1 (Top) - Root node
        level1_y = 2.5
        node_positions = [
            ORIGIN + UP * level1_y,  # Node 1 (root)
        ]
        
        # Level 2
        level2_y = level1_y - LEVEL_SPACING
        level2_nodes = 3
        for i in range(level2_nodes):
            x = (i - 1) * NODE_SPACING
            node_positions.append(RIGHT * x + UP * level2_y)  # Nodes 2-4
        
        # Level 3
        level3_y = level2_y - LEVEL_SPACING
        level3_nodes = 4
        for i in range(level3_nodes):
            x = (i - 1.5) * NODE_SPACING
            node_positions.append(RIGHT * x + UP * level3_y)  # Nodes 5-8
        
        # Level 4
        level4_y = level3_y - LEVEL_SPACING
        level4_nodes = 5
        for i in range(level4_nodes):
            x = (i - 2) * NODE_SPACING
            node_positions.append(RIGHT * x + UP * level4_y)  # Nodes 9-13
        
        # Level 5 (Bottom)
        level5_y = level4_y - LEVEL_SPACING
        level5_nodes = 5
        for i in range(level5_nodes):
            x = (i - 2) * NODE_SPACING
            node_positions.append(RIGHT * x + UP * level5_y)  # Nodes 14-18
        
        # Create nodes with random color segments
        for i, pos in enumerate(node_positions, 1):
            node = self.create_complex_node(pos, i)
            nodes.add(node)
        
        # Create arrows between nodes ensuring hierarchical structure
        arrows = VGroup()
        connections = [
            # From root (Node 1) to Level 2
            (0, 1), (0, 2), (0, 3),
            
            # From Level 2 to Level 3
            (1, 4), (1, 5), 
            (2, 5), (2, 6),
            (3, 6), (3, 7),
            
            # From Level 3 to Level 4
            (4, 8), (4, 9),
            (5, 9), (5, 10),
            (6, 10), (6, 11),
            (7, 11), (7, 12),
            
            # From Level 4 to Level 5
            (8, 13), (8, 14),
            (9, 14), (9, 15),
            (10, 15), (10, 16),
            (11, 16), (11, 17),
            (12, 17),
            
            # Additional cross-connections for complexity
            (2, 4), (2, 7),
            (5, 8), (6, 12),
            (9, 13), (10, 17),
            (14, 16), (15, 17)
        ]
        
        for start_idx, end_idx in connections:
            start_node = nodes[start_idx]
            end_node = nodes[end_idx]
            arrow = Arrow(
                start=start_node.get_center(),
                end=end_node.get_center(),
                buff=0.2,
                color=GREEN,
                max_tip_length_to_length_ratio=0.08,  # Smaller arrowheads
                stroke_width=1.5  # Thinner arrows
            )
            arrows.add(arrow)
        
        # Create the complex graph group
        complex_graph = VGroup(nodes, arrows)
        
        # Fade out hierarchy while fading in complex graph
        self.play(
            FadeOut(hierarchy_group),
            FadeIn(complex_graph),
            run_time=2
        )
        self.wait(0.5)
        
        # Fade out transition text
        self.play(
            FadeOut(transition_text),
            run_time=1
        )
        
        # Hold final state
        self.wait(3)
