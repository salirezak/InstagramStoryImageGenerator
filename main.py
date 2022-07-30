from images import background
from font import Font
from text_wrap import text_wrap



class StoryImageGenerator:
    def __init__(self, story_wh: tuple, story_color: str, font_name: str, font_size: int, lines_spacing: int, text_align: str, text: str, box_margin_xy: tuple, text_margin_xy: tuple,
    ) -> None:

        self.story_wh = story_wh
        self.story_color = story_color
        self.font_name = font_name
        self.font_size = font_size
        self.lines_spacing = lines_spacing
        self.text_align = text_align
        self.text = text
        self.box_margin_xy = box_margin_xy
        self.text_margin_xy = text_margin_xy

        self.font = self.get_font()
        self.background = self.generate_background()

    def get_font(self) -> Font:
        return Font(self.font_name, self.font_size, spacing=self.lines_spacing, align=self.text_align)

    def max_box_wh(self) -> tuple:
        return (
            self.story_wh[0]-2*self.box_margin_xy[0],
            self.story_wh[1]-2*self.box_margin_xy[1],
        )

    def max_text_wh(self) -> tuple:
        max_box_wh = self.max_box_wh()
        return (
            max_box_wh[0]-2*self.text_margin_xy[0],
            max_box_wh[1]-2*self.text_margin_xy[1],
        )

    def wrapped_text(self) -> str:
        return text_wrap(self.text, self.max_text_wh(), self.font)

    def generate_background(self):
        return background(self.story_wh, self.story_color)

    def show(self) -> None:
        self.background.show()