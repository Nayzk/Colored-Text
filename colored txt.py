from colored import fg, bg, attr

def colored_txt():
    # User txt
    user_input = input(fg('green') + "Enter something: " + attr('reset'))

    # Print the txt in a different color
    print(fg('magenta') + "You entered: " + user_input + attr('bold'))

colored_txt()
