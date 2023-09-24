powers_of_3 = [59050, 19684, 6562, 2188, 730, 244, 82, 28, 10, 4, 2]

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


def triangle_simple(row):
    if len(row) == 1:
        return row
    next_row = ''
    for i in range(len(row)-1):
        next_row += next_colour[row[i:i+2]]
    return triangle_simple(next_row)


def triangle(row):
    if row_length := len(row) == 1:
        return row
    if row_length in powers_of_3:
        return next_colour[row[0] + row[-1]]
    return triangle(triangle_simple(row))
