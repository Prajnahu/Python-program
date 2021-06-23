BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

##ASCI value of escape character'\' is 27 ir 1B in hex
print(RED,"this will be in red")
print("and so is this")
print(YELLOW,"this wil be in yellow")
print(BLUE,"this will be in blue")


def color_print(text,effect):
    """
    Print 'text' using ANSI sequences to change color
    :param text:The text to print
    :param effect:The effect we want ,One of the constants
    defined at the start of this module.
    """

    output_string="{0}{1}{2}".format(effect,text,RESET)
    print(output_string)

color_print("this will be in red",BLACK)
color_print("and so is this",BLUE)
color_print("this wil be in yellow",YELLOW)
color_print("this will be in blue",RED)
color_print("this will be in blue",REVERSE)