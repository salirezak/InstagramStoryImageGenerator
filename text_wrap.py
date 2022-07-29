def line_wrap(line: str, max_len: int) -> str:
    words = line.strip().split()
    lines, line = [], ''

    while words:
        word = words.pop(0)
        if len(line + ' ' + word) > max_len:
            lines.append(line)
            line = word
        else:
            line += ' ' + word
            line = line.strip()

    if line:
        lines.append(line)

    return '\n'.join(lines)