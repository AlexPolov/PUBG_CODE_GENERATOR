import pyautogui
import keyboard
import random
import time
import os
import json

# Reduce the default pause between PyAutoGUI commands
pyautogui.PAUSE = 0.01

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

def load_config():
    """Load configuration from config.json."""
    try:
        with open(config_path, "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print("Configuration file not found! Please run 'setup.py' to create it.")
        exit(1)
    except json.JSONDecodeError:
        print("Configuration file is corrupted! Please run 'setup.py' to regenerate it.")
        exit(1)

def generate_code(base):
    """Generates a full code based on the base code."""
    part1 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4))
    part2 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4))
    part3 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=5))
    return f"{base}-{part1}-{part2}-{part3}"

def input_code(code, coordinates):
    """Inputs the generated code and presses enter."""
    pyautogui.click(x=coordinates['input_field'][0], y=coordinates['input_field'][1])
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(code, interval=0.02)
    pyautogui.click(x=coordinates['redeem_button'][0], y=coordinates['redeem_button'][1])

def main():
    # Load configuration
    config = load_config()
    base_code = config['base_code']
    coordinates = config['coordinates']
    delay = config['default_delay']

    print("Press 'F' to start script or hold 'P' to pause")
    print("Press 'Q' to quit the program")

    running = False

    while True:
        if keyboard.is_pressed('F'):
            print("Started loop...")
            running = True
            time.sleep(0.2)
        
        if running:
            code = generate_code(base_code)
            print(f"Generated Code: {code}")
            input_code(code, coordinates)
            time.sleep(delay)
        
        if keyboard.is_pressed('P'):
            print("Stopped loop.")
            running = False
            time.sleep(0.2)

        if keyboard.is_pressed('Q'):
            print("Program closed.")
            break

if __name__ == "__main__":
    main()
