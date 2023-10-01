def infer_type(context, expression):
    return ''


"""For the sake of simplicity, we are not formally distinguishing between constants and functions but, effectively,
treating constants as zero-argument functions."""


def parse_context(context: str) -> dict:
    lines = [line.strip() for line in context.split('\n') if line.strip()]
    types = {}
    for line in lines:
        [key, val] = line.split(' : ')
        types[key] = tuple(val.split(' -> '))
    print(types)
    return types
