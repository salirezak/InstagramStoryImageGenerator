def line_wrap(line: str, max_len: int) -> str:
    words = line.strip().split()
    lines, line = [], ''

    while words:
        word = words.pop(0)
        if len(line + ' ' + word) > max_len:
            # break line and start new line
            if len(line) > max_len:
                lines.append(line[:max_len].strip())
                line = line[max_len:].strip()
            # start new line
            else:
                if line: lines.append(line)
                line = word
        # add word to line
        else:
            line += ' ' + word
            line = line.strip()

    # add last line
    if line: lines.append(line)

    return '\n'.join(lines)


def text_wrap(text: str, max_len: int) -> str:
    lines = text.strip().split('\n')
    lines = map(lambda line: line_wrap(line, max_len), lines)

    return '\n'.join(lines)