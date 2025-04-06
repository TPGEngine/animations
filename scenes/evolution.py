from manim import *
import random

class EvolutionScene(Scene):
    def create_team_structure(self, position, color=BLUE):
        """Create a team structure with a circle and 1-2 program arrows."""
        # Create team circle
        team_circle = Circle(radius=0.5, color=color)
        team_circle.move_to(position)
        
        # Create program arrows
        arrow1 = Arrow(
            start=team_circle.get_right(),
            end=team_circle.get_right() + RIGHT * 1.5,
            buff=0.2,
            color=GREEN
        )
        
        # Randomly decide if we should add a second arrow
        if np.random.random() > 0.5:
            arrow2 = Arrow(
                start=team_circle.get_bottom(),
                end=team_circle.get_bottom() + DOWN * 1.5,
                buff=0.2,
                color=GREEN
            )
            return VGroup(team_circle, arrow1, arrow2)
        else:
            return VGroup(team_circle, arrow1)

    def construct(self):
        # Start with Scene 3's final state
        # Create Team Circle with input
        team_circle = Circle(radius=1.5, color=BLUE)
        team_circle.move_to(ORIGIN + UP * 1.5)
        team_circle.set_fill(BLUE, opacity=0.3)
        
        # Create Actions
        action1 = Square(side_length=0.5, color=RED)
        action1.move_to(team_circle.get_right() + RIGHT * 2.5)
        
        action2 = Circle(radius=0.3, color=YELLOW)
        action2.move_to(team_circle.get_bottom() + DOWN * 2.5)
        
        action3 = Triangle(color=PURPLE).scale(0.3)
        action3.move_to(team_circle.get_left() + LEFT * 2.5)

        # Create Program Arrows (all green)
        arrow1 = Arrow(
            start=team_circle.get_right(),
            end=action1.get_left(),
            buff=0.2,
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

        # Create initial state group (without input square and bars)
        initial_state = VGroup(
            team_circle,
            action1, action2, action3,
            arrow1, arrow2, arrow3
        )

        # Show initial state
        self.add(initial_state)
        self.wait(1)

        # Shrink and multiply the team
        small_scale = 0.4
        positions = [
            LEFT * 3 + UP * 2,
            RIGHT * 3 + UP * 2,
            LEFT * 3 + DOWN * 2,
            RIGHT * 3 + DOWN * 2
        ]

        # Create small copies for each position
        teams = VGroup()
        for pos in positions:
            small_team = initial_state.copy().scale(small_scale)
            small_team.move_to(pos)
            teams.add(small_team)

        # Animate transition
        self.play(
            initial_state.animate.scale(small_scale).move_to(positions[0]),
            run_time=1
        )
        
        self.play(
            *[FadeIn(team) for team in teams[1:]],
            run_time=1
        )
        self.wait(0.5)

        # Create generation counter
        generation_text = Text("Generation: ", font_size=24)
        generation_number = Text("1", font_size=24)
        generation_counter = VGroup(generation_text, generation_number)
        generation_counter.arrange(RIGHT, buff=0.2)
        generation_counter.to_corner(UL)

        # Show generation counter
        self.play(
            Write(generation_text),
            Write(generation_number),
            run_time=0.5
        )
        self.wait(0.5)

        # Evolution loop (2 generations)
        for gen in range(2):
            # Increment generation
            new_number = Text(str(gen + 2), font_size=24)
            new_number.move_to(generation_number.get_center())
            
            self.play(
                Transform(generation_number, new_number),
                run_time=0.5
            )
            self.wait(0.5)

            # Store the position of the team to be deleted
            deleted_position = teams[0].get_center()

            # Selection (delete one team)
            team_to_delete = teams[0]
            cross = Cross(team_to_delete, color=RED)
            
            self.play(
                Create(cross),
                run_time=0.5
            )
            self.wait(0.5)
            
            self.play(
                FadeOut(team_to_delete),
                FadeOut(cross),
                run_time=0.5
            )
            teams.remove(team_to_delete)
            self.wait(1)  # Longer wait to emphasize the empty space

            if gen == 0:  # First generation: Crossover
                self.play(
                    FadeOut(initial_state),
                    run_time=0.5
                )
                # Use teams[1] and teams[2] for crossover (avoiding the deleted position)
                parent1 = teams[1]
                parent2 = teams[2]
                
                # Create copies for animation
                parent1_copy = parent1.copy()
                parent2_copy = parent2.copy()
                
                # Store original positions
                parent1_orig_pos = parent1.get_center()
                parent2_orig_pos = parent2.get_center()
                
                # Move parents together
                center_point = ORIGIN + UP * 0.5
                
                # Create "Crossover" text
                crossover_text = Text("Crossover", font_size=20)
                crossover_text.next_to(center_point, UP)
                
                self.play(
                    Write(crossover_text),
                    parent1_copy.animate.move_to(center_point + LEFT),
                    parent2_copy.animate.move_to(center_point + RIGHT),
                    run_time=1
                )
                self.wait(0.5)

                # Create child team (mix of both parents)
                child_team = parent1_copy.copy()
                child_team[0].set_color(PURPLE)  # New color for child
                
                # Move child to final position
                target_pos = center_point + DOWN * 2
                
                # Animate crossover
                self.play(
                    parent1_copy.animate.shift(UP * 0.3),
                    parent2_copy.animate.shift(UP * 0.3),
                    run_time=0.5
                )
                
                # Show arrows connecting parents to child
                arrow_to_child1 = Arrow(parent1_copy.get_bottom(), target_pos + UP * 0.5, color=YELLOW)
                arrow_to_child2 = Arrow(parent2_copy.get_bottom(), target_pos + UP * 0.5, color=YELLOW)
                
                self.play(
                    GrowArrow(arrow_to_child1),
                    GrowArrow(arrow_to_child2),
                    run_time=0.5
                )
                
                self.play(
                    FadeIn(child_team.move_to(target_pos)),
                    run_time=0.5
                )
                self.wait(0.5)

                # Cleanup crossover animation and move child to deleted position
                self.play(
                    FadeOut(VGroup(
                        parent1_copy, parent2_copy,
                        arrow_to_child1, arrow_to_child2,
                        crossover_text
                    )),
                    child_team.animate.move_to(deleted_position),
                    run_time=0.5
                )
                
                teams.add(child_team)

            else:  # Second generation: Mutation
                # Select a successful team to mutate (using teams[1] to avoid the empty space)
                team_to_mutate = teams[1]
                mutated_team = team_to_mutate.copy()
                
                # Create "Mutation" text
                mutation_text = Text("Mutation", font_size=20)
                mutation_text.next_to(team_to_mutate, UP)
                
                self.play(
                    Write(mutation_text),
                    run_time=0.5
                )
                
                # Animate the mutation
                flash = Flash(
                    mutated_team,
                    line_length=0.2,
                    num_lines=20,
                    color=YELLOW,
                    flash_radius=0.5,
                    time_width=0.3
                )
                
                self.play(flash)
                self.wait(0.3)
                
                # Change appearance after mutation
                mutated_team[0].set_color(TEAL)  # Different color than crossover
                
                # Add some random rotation to arrows to show mutation
                for arrow in mutated_team[4:]:  # Arrows start at index 4
                    self.play(
                        arrow.animate.rotate(0.3 * (random.random() - 0.5)),
                        run_time=0.3
                    )
                
                # Move mutated team to deleted position
                self.play(
                    FadeOut(mutation_text),
                    mutated_team.animate.move_to(deleted_position),
                    run_time=0.5
                )
                
                teams.add(mutated_team)
            
            self.wait(0.5)

        self.wait(2)

        # Zoom into bottom left team and transition to simple diagram
        bottom_left_team = teams[2]  # The bottom left team
        
        # Create the target simple diagram
        target_team = Circle(radius=0.5, color=BLUE)
        target_team.move_to(LEFT * 2)
        team_a_label = Text("Team A", font_size=24).next_to(target_team, UP, buff=0.2)
        
        target_action = Square(side_length=0.5, color=RED)
        target_action.move_to(RIGHT * 2)
        action_label = Text("Action", font_size=24).next_to(target_action, DOWN, buff=0.2)
        
        target_arrow = Arrow(
            start=target_team.get_right(),
            end=target_action.get_left(),
            buff=0.2,
            color=GREEN
        )
        
        target_group = VGroup(target_team, team_a_label, target_action, action_label, target_arrow)
        target_group.move_to(ORIGIN)  # Center the entire group
        
        # Fade out other teams and generation counter
        self.play(
            FadeOut(initial_state),  # Add the initial state to fade out
            FadeOut(teams[0]),
            FadeOut(teams[1]),
            FadeOut(teams[3]),
            FadeOut(generation_text),
            FadeOut(generation_number),
            run_time=1
        )
        
        # Zoom into the bottom left team
        self.play(
            bottom_left_team.animate.scale(2.5).move_to(ORIGIN),
            run_time=1.5
        )
        
        # Transform into simple diagram
        self.play(
            Transform(bottom_left_team, target_group),
            run_time=1.5
        )
        
        self.wait(2)
