from PIL import Image, ImageDraw, ImageFilter



def background(image_wh: tuple, background_color: str) -> Image:
    return Image.new('RGBA', image_wh, background_color)


def center_xy(main_wh: tuple, sub_wh: tuple) -> tuple:
    return (
       (main_wh[0]-sub_wh[0])/2, #x0
       (main_wh[1]-sub_wh[1])/2, #y0
       (main_wh[0]-sub_wh[0])/2+sub_wh[0], #x1
       (main_wh[1]-sub_wh[1])/2+sub_wh[1], #y1
    )


def text_box(story_wh: tuple, box_wh: tuple, box_color: str, box_radius: int, box_shadow_radius: int, box_shadow_color: str) -> Image:
    box_xy = center_xy(story_wh, box_wh)
    box_image = Image.new('RGBA', story_wh)
    #shadow
    ImageDraw.Draw(box_image).rounded_rectangle(box_xy, box_radius, box_shadow_color)
    box_image = box_image.filter(ImageFilter.GaussianBlur(box_shadow_radius))
    #box
    ImageDraw.Draw(box_image).rounded_rectangle(box_xy, box_radius, box_color)

    return box_image


def merge(image_1: Image, image_2: Image) -> Image:
    image_1.alpha_composite(image_2)
    return image_1