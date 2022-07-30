from images import background
from font import Font



class StoryImageGenerator:
    def __init__(self, story_wh: tuple, story_color: str, font_name: str, font_size: int, lines_spacing: int, text_align: str) -> None:

        self.story_wh = story_wh
        self.story_color = story_color
        self.font_name = font_name
        self.font_size = font_size
        self.lines_spacing = lines_spacing
        self.text_align = text_align

        self.font = self.get_font()
        self.background = self.generate_background()

    def get_font(self) -> Font:
        return Font(self.font_name, self.font_size, spacing=self.lines_spacing, align=self.text_align)

    def generate_background(self):
        return background(self.story_wh, self.story_color)

    def show(self) -> None:
        self.background.show()