from pyfiglet import figlet_format
from termcolor import colored



def print_art(msg,color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan")

    if color not in valid_colors:
        color = "magenta"
        
    result = figlet_format(msg)
    result_color = colored(result, color=color)
    print(result_color)

msg = input("What would you like to print?")
color = input("What color?")
print_art(msg,color)
