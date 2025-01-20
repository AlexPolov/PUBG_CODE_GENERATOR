import json
import os

# Default configuration
default_config = {
    "base_code": "U03805",
    "coordinates": {
        "input_field": (703, 421),
        "redeem_button": (571, 505)
    },
    "default_delay": 0.3
}

def setup_config():
    """Sets up configuration and saves it to a JSON file."""
    print("Configure the program:")

    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")

    try:
        # Change base code
        base_code = input(f"Enter base code (default '{default_config['base_code']}'): ").strip() or default_config['base_code']
        default_config['base_code'] = base_code

        # Input coordinates for the input field
        input_x = int(input(f"Enter X coordinate for input field (default {default_config['coordinates']['input_field'][0]}): ") or default_config['coordinates']['input_field'][0])
        input_y = int(input(f"Enter Y coordinate for input field (default {default_config['coordinates']['input_field'][1]}): ") or default_config['coordinates']['input_field'][1])
        default_config['coordinates']['input_field'] = (input_x, input_y)

        # Input coordinates for the redeem button
        redeem_x = int(input(f"Enter X coordinate for redeem button (default {default_config['coordinates']['redeem_button'][0]}): ") or default_config['coordinates']['redeem_button'][0])
        redeem_y = int(input(f"Enter Y coordinate for redeem button (default {default_config['coordinates']['redeem_button'][1]}): ") or default_config['coordinates']['redeem_button'][1])
        default_config['coordinates']['redeem_button'] = (redeem_x, redeem_y)

        # Input delay between actions
        delay = float(input(f"Enter delay between actions in seconds (default {default_config['default_delay']}): ") or default_config['default_delay'])
        default_config['default_delay'] = delay

        # Save the configuration to a JSON file
        with open(config_path, "w") as config_file:
            json.dump(default_config, config_file, indent=4)

        print(f"\nConfiguration saved to '{config_path}'!")

    except ValueError as e:
        print(f"Invalid input: {e}. Please run the setup again.")
    except Exception as e:
        print(f"An error occurred: {e}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    setup_config()
