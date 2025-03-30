from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class LinearSearchExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Setup for list of numbers and the search target
        list_of_numbers = VGroup(*[Square(side_length=0.75).shift(2 * LEFT + i * RIGHT) for i in range(6)])
        target = Square(side_length=0.75, color=RED).shift(4 * RIGHT)

        # Voiceover explaining the search list
        with self.voiceover(text="We have a list of numbers and a target value to find.") as tracker:
            self.play(LaggedStartMap(Create, list_of_numbers, run_time=tracker.duration))

        # Voiceover explaining what linear search is
        with self.voiceover(text="We will use linear search, which checks each number one by one.") as tracker:
            self.play(Create(target), run_time=tracker.duration)

        # Perform the linear search with voiceover for each step
        for i, square in enumerate(list_of_numbers):
            with self.voiceover(text=f"Checking index {i}...") as tracker:
                self.play(Indicate(square), run_time=tracker.duration)

            if i == 4:  # Let's assume the target is found at index 4
                with self.voiceover(text="Found the target!") as tracker:
                    self.play(Indicate(target), run_time=tracker.duration)
                break

        # Voiceover to emphasize how inefficient linear search is
        with self.voiceover(text="As you can see, we have to check each element one by one. Linear search is inefficient for large lists.") as tracker:
            self.play(Indicate(list_of_numbers), run_time=tracker.duration)

        self.wait()