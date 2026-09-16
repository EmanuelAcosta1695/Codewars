def greet(name):
    return "Hello " + "".join(x.upper() if i == 0 else x.lower() for i, x in enumerate(name)) + "!"

"""
Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

Example:

"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"
"""
