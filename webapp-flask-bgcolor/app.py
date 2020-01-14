from flask import Flask, render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "red": "#ff0000",
    "green": "#00ff00",
    "blue": "#0000ff",
    "olive": "#808000",
    "purple": "#800080",
    "navy": "#000080"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
# Generate a random color
COLOR = random.choice(["red", "green", "blue", "olive", "purple", "navy"])


@app.route("/")
def main():
    # return 'Hello'
    return render_template('index.html', name=socket.gethostname(), color=color_codes[COLOR])


if __name__ == "__main__":
    print("This is a simple flask webapp that displays a colored background and a greeting message. \n"
          "The color can be specified in two different ways: \n"
          "    1. As a command line argument with --color as the argument. Accepts one of the following \n"
          "       colors according the list below. \n"
          "    2. As an Environment variable APP_COLOR. Accepts one of the following colors according \n"
          "       the list below.\n"
          "In any other case, a random color is picked from the list below.\n"
          "\n"
          "Note 1: Accepted colors [" + SUPPORTED_COLORS + "] \n"
          "Note 2: Command line argument precedes over environment variable.\n"
          "\n"
          "")


    # Check for Command Line Parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False)
    args = parser.parse_args()

    if args.color:
        print("Color from command line argument =" + args.color)
        COLOR = args.color
        if COLOR_FROM_ENV:
            print("A color was set through environment variable -" + COLOR_FROM_ENV + ". However, color from command line argument takes precendence.")
    elif COLOR_FROM_ENV:
        print("No Command line argument. Color from environment variable =" + COLOR_FROM_ENV)
        COLOR = COLOR_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a Random Color =" + COLOR)

    # Check if input color is a supported one
    if COLOR not in color_codes:
        print("Color not supported. Received '" + COLOR + "' expected one of " + SUPPORTED_COLORS)
        exit(1)

    # Run Flask Application
    app.run(host="0.0.0.0", port=8000)
