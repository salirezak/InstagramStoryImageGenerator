from PIL import ImageFont



def line_wrap(line: str, max_width: int, font: ImageFont) -> str:
    words = line.strip().split()
    lines, line = [], ''

    while words:
        word = words.pop(0)
        if font.getsize(line + ' ' + word)[0] > max_width:
            # break line and start new line
            if font.getsize(line)[0] > max_width:
                lines.append(line[:max_width].strip())
                line = line[max_width:].strip()
            # start new line
            else:
                if line: lines.append(line)
                line = word
        # add word to line
        else:
            line += ' ' + word
            line = line.strip()

    # add last line
    while line:
        # break line and start new line
        if font.getsize(line)[0] > max_width:
                lines.append(line[:max_width].strip())
                line = line[max_width:].strip()
        # add the true last line
        else:
            if line: lines.append(line)
            line = ''

    return '\n'.join(lines)


def text_wrap(text: str, max_wh: int) -> str:
    font = ImageFont.truetype('fonts/Vazir.ttf', 10, encoding='unic')
    lines = text.strip().split('\n')
    lines = map(lambda line: line_wrap(line, max_wh[0], font), lines)
    text = '\n'.join(lines)

    if font.getsize_multiline(text, 'rtl', 10, 'fa')[1] <= max_wh[1]:
        return text
    raise Exception('Text is too long')