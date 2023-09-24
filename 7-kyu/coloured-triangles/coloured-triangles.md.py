next_colour = {
    'RR': 'R',
    'RG': 'B',
    'RB': 'G',
    'GR': 'B',
    'GG': 'G',
    'GB': 'R',
    'BR': 'G',
    'BG': 'R',
    'BB': 'B'
}


def triangle(row):
    if len(row) == 1:
        return row
    next_row = ''
    for i in range(len(row)-1):
        next_row += next_colour[row[i:i+2]]
    return triangle(next_row)
