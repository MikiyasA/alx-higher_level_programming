#!/use/bin/python3
""" The module that prints a text with 2 new lines
after each of these characters: ., ? and :
using def text_indentation(text): function
"""


def text_indentation(text):
    """ The functuin to ptint with 2 new line after charactets . ? and :
    Args:
       test - the text to split
    Exception:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n_text = text.replace('. ', '.\n\n').replace('? ', '?\n\n')\
                                        .replace(': ', ':\n\n')

    print(n_text, end="")
