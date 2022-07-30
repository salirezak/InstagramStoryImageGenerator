from PIL import ImageFont
from pathlib import Path
from langdetect import DetectorFactory, detect_langs



class Font:
    def __init__(self, font_name: str, font_size: int, spacing=30) -> None:
        self.font_path = str(Path(__file__).resolve().parent / 'fonts' / (font_name+'.ttf'))
        self.font_size = font_size
        self.spacing = spacing

        self.font = self.get_font()

    def get_font(self) -> ImageFont:
        return ImageFont.truetype(self.font_path, self.font_size, encoding='unic')

    def lang_dir(self, text: str) -> None:
        DetectorFactory.seed = 0
        possible_languages = list(map(lambda x: x.lang, detect_langs(text)))
        self.language = 'fa' if any(lang in possible_languages for lang in ['fa', 'ar', 'ur']) else 'en'
        self.direction = 'rtl' if self.language == 'fa' else 'ltr'

    def get_size(self, text: str) -> tuple:
        return self.font.getsize(text)

    def get_size_multiline(self, text: str) -> tuple:
        self.lang_dir(text)
        return self.font.getsize_multiline(text, self.direction, self.spacing, self.language)
