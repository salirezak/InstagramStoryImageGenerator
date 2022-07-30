from PIL import ImageFont
from pathlib import Path



class Font:
    def __init__(self, font_name: str, font_size: int, spacing=30, language='fa', direction='rtl') -> None:
        self.font_path = str(Path(__file__).resolve().parent / 'fonts' / (font_name+'.ttf'))
        self.font_size = font_size
        self.spacing = spacing
        self.language = language
        self.direction = direction

    def get_font(self) -> ImageFont:
        return ImageFont.truetype(self.font_path, self.font_size, encoding='unic')

    def get_size(self, text: str) -> tuple:
        return self.get_font().getsize(text)

    def get_size_multiline(self, text: str) -> tuple:
        return self.get_font().getsize_multiline(text, self.direction, self.spacing, self.language)