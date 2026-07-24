import re

def text_normalize(text, operations):
    """
    Returns: str
    """
    result = text 

    # Yes. Because strings are immutable, methods like text.lower() do not change the original string. Instead, they always return a new string with the converted characters.

    # remember! # arraays are mutable so thats why .sort() works 
    for op in operations: 
        if op == 'lowercase':
            result = result.lower()
        elif op == "remove_punctuation":
            result = re.sub(r'[^\w\s]', '', result)
        elif op == 'remove_digits': 
            result = re.sub(r'\d', '', result)
        elif op == "collapse_whitespace":
            result = re.sub(r'\s+', ' ', result)
        elif op == 'strip':
            result = result.strip()

    return result
    pass