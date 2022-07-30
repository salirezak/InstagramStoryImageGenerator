from images import background



class StoryImageGenerator:
    def __init__(self, story_wh: tuple, story_color: str) -> None:

        self.story_wh = story_wh
        self.story_color = story_color

        self.background = self.generate_background()

    def generate_background(self):
        return background(self.story_wh, self.story_color)