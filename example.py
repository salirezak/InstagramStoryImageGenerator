from main import StoryImageGenerator



fa_text = '''لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است
چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد کتابهای زیادی در شصت و سه درصد گذشته حال و آینده '''
en_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cras euismod,
nisi eu vulputate consectetur, nisl nisi consectetur nisi, euismod ultricies nisl nisi euismod nisl. Nunc euismod, nisi eu vulputate consectetur, nisl nisi consectetur nisi, euismod'''


story = StoryImageGenerator(
    story_wh=(1080, 1920), story_color='#0079b0',
    font_name='Vazir-Medium', font_size=40, lines_spacing=30, text_align='center', text=en_text,
    box_margin_xy=(150, 150), text_margin_xy=(75, 100),
    box_color='#f5f5f5', box_radius=25, box_shadow_radius=10, box_shadow_color='#00000080',
    )


story.show()