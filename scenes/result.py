from manim import *
import numpy as np
import random

class ResultScene(Scene):
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
        # Create ground line that spans the full width
        ground = Line(
            start=LEFT * 8,  # Extended further left
            end=RIGHT * 8,   # Extended further right
            color=GRAY
        ).move_to(DOWN * 3)  # Positioned at a fixed height
        
        # Create successful agent setup (right side)
        base = Square(side_length=1.0, fill_opacity=1, color=BLUE)
        base.move_to(RIGHT * 3 + DOWN * 2.5)  # Adjusted to touch ground line
        initial_base_pos = base.get_center()
        
        # Create rod for successful agent
        rod = Line(
            start=base.get_top(),
            end=base.get_top() + UP * 3,
            stroke_width=8,
            color=WHITE
        )
        
        # Create failing agent setup (left side) - same size as successful agent
        failing_base = Square(side_length=1.0, fill_opacity=1, color=BLUE)
        failing_base.move_to(LEFT * 3 + DOWN * 2.5)  # Adjusted to touch ground line
        failing_base_initial_pos = failing_base.get_center()
        
        failing_rod = Line(
            start=failing_base.get_top(),
            end=failing_base.get_top() + UP * 3,
            stroke_width=8,
            color=WHITE
        )
        
        # Create text labels
        without_tpg_text = Text("without TPG", font_size=24)
        without_tpg_text.move_to(UP * 2.5 + LEFT * 3)  # Positioned higher and aligned with agent
        
        with_tpg_text = Text("with TPG", font_size=24)
        with_tpg_text.move_to(UP * 2.5 + RIGHT * 3)  # Positioned higher and aligned with agent
        
        # Create complex TPG graph
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
        tpg_graph = VGroup(nodes, arrows)
        tpg_graph.scale(0.7)  # Initial scale
        
        # Create result text
        result_text = Text("Result: Efficient AI learns complex skills!", font_size=36)
        result_text.to_edge(UP)
        
        # Animation sequence
        # 1. Show both agents, ground, and labels
        self.play(
            FadeIn(base),
            FadeIn(rod),
            FadeIn(failing_base),
            FadeIn(failing_rod),
            FadeIn(ground),
            Write(without_tpg_text),
            Write(with_tpg_text)
        )
        
        # 2. Animate both agents simultaneously
        def update_rod(mob):
            # Update rod position based on base position
            mob.put_start_and_end_on(
                base.get_top(),
                base.get_top() + UP * 3
            )
            
        def smooth_movement(mob, dt):
            # Smooth movement for successful agent that stays within right side
            # Use a modified sine wave that only moves right and back
            t = self.time * 0.5  # Slower movement
            movement = np.sin(t) * 0.5  # Full range from -0.5 to 0.5
            # Convert to only positive movement (0 to 0.5)
            positive_movement = (movement + 0.5) * 0.5
            # Apply movement only to the right
            mob.move_to(initial_base_pos + RIGHT * positive_movement)
            
        # Add updaters for successful agent
        base.add_updater(smooth_movement)
        rod.add_updater(update_rod)
        
        # Animate failing agent using ChallengeScene animations
        rotation_point = failing_base.get_top()
        
        # First instability and fall
        self.play(
            AnimationGroup(
                Rotate(failing_rod, angle=PI/3, about_point=rotation_point),
                Succession(
                    failing_base.animate(rate_func=linear).shift(LEFT*0.3),
                    failing_base.animate(rate_func=linear).shift(RIGHT*0.4),
                    failing_base.animate(rate_func=linear).shift(LEFT*0.2),
                    failing_base.animate(rate_func=linear).shift(RIGHT*0.1),
                ),
                lag_ratio=0.5
            ),
            run_time=1.5
        )
        
        # First fall completely
        self.play(
            Rotate(failing_rod, angle=PI/2 - PI/3, about_point=rotation_point),
            run_time=0.5
        )
        self.wait(0.5)
        
        # Reset failing agent
        self.play(
            failing_base.animate.move_to(failing_base_initial_pos),
            Rotate(failing_rod, angle=-PI/2, about_point=rotation_point),
            run_time=0.5
        )
        
        # Second instability animation
        self.play(
            AnimationGroup(
                Rotate(failing_rod, angle=-PI/3.5, about_point=rotation_point),
                Succession(
                    failing_base.animate(rate_func=linear).shift(RIGHT*0.2),
                    failing_base.animate(rate_func=linear).shift(LEFT*0.3),
                    failing_base.animate(rate_func=linear).shift(RIGHT*0.1),
                    failing_base.animate(rate_func=linear).shift(LEFT*0.2),
                ),
                lag_ratio=0.5
            ),
            run_time=1.5
        )
        
        # Second fall
        self.play(
            Rotate(failing_rod, angle=PI/2 - PI/3.5, about_point=rotation_point),
            run_time=0.5
        )
        
        # Remove updaters from successful agent
        base.remove_updater(smooth_movement)
        rod.remove_updater(update_rod)
        
        # 3. Remove both agents and focus on "with TPG" text
        self.play(
            FadeOut(failing_base),
            FadeOut(failing_rod),
            FadeOut(base),
            FadeOut(rod),
            FadeOut(without_tpg_text),
            FadeOut(ground),
            with_tpg_text.animate.scale(1.5).move_to(UP * 2.5),
            run_time=1.5
        )
        
        # 4. Show TPG graph and remove "with TPG" text
        self.wait(0.5)  # Pause to emphasize the text
        self.play(
            tpg_graph.animate.scale(1.5).move_to(ORIGIN),  # Center and scale up the TPG graph
            FadeOut(with_tpg_text),  # Remove the text as the graph appears
            run_time=1.5
        )
        
        # 5. Show result text
        self.play(Write(result_text))
        
        # 6. Hold final composition
        self.wait(3)
        
        # 7. Fade out everything for loop transition
        self.play(*[FadeOut(mob) for mob in self.mobjects])
