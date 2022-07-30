from PIL import Image



def background(image_wh: tuple, background_color: str) -> Image:
    return Image.new('RGBA', image_wh, background_color)

