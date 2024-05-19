# Colored-Text



# Colored Text 

A simple Python script to get user input and print it in different colors using the `colored` module.

## Description

This script prompts the user to enter some text, then prints the entered text in a different color. The `colored` module is used to apply colors to the text displayed in the terminal.

## Prerequisites

Ensure you have the `colored` library installed. You can install it using pip if you don't have it installed already:

```
bash
Copy code
pip install colored
```

## Usage

1. Clone this repository or download the script file to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script to prompt the user for input and print the entered text in cyan:

```
pythonCopy codefrom colored import fg, bg, attr

def get_user_input():
    # Get user input
    user_input = input(fg('green') + "Enter something: " + attr('reset'))

    # Print the user input in a different color
    print(fg('cyan') + "You entered: " + user_input + attr('reset'))

get_user_input()
```

## Example

When you run the script, you will see a prompt in green asking you to "Enter something:". After you input your text, it will be printed in cyan.

```
shCopy code$ python script.py
Enter something: Hello, World!
You entered: Hello, World!
```

## Available Colors and Attributes

### Foreground Colors

- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white

### Background Colors

- on_black
- on_red
- on_green
- on_yellow
- on_blue
- on_magenta
- on_cyan
- on_white

### Attributes

- bold
- dark
- underlined
- blink
- reverse
- concealed

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Colored Library](https://pypi.org/project/colored/) - For handling text styling and coloring in the terminal.