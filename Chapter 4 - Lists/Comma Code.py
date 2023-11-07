"""
Comma Code
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
and a space, with and inserted before the last item. For example, passing the previous spam list to the function
would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed
to it. Be sure to test the case where an empty list [] is passed to your function.
"""

spam = ['apples', 'bananas', 'tofu', 'cats']


def comma_code(anything: list):
    if len(anything) == 0:
        return ""
    elif len(anything) == 1:
        return anything[0]
    else:
        all_but_last = ", ".join(anything[:-1])
        return f"{all_but_last}, and {anything[-1]}"
