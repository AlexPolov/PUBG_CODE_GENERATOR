import tkinter as tk
import pyautogui
import ctypes
import sys
import os

# Hide the console window (Windows only)
if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Make Python DPI-aware to handle screen scaling
ctypes.windll.user32.SetProcessDPIAware()

# Get the directory where the script is running
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "coordinates.txt")

def update_coordinates():
    """Update and display mouse coordinates in real time."""
    x, y = pyautogui.position()
    coords_label.config(text=f"X: {x}, Y: {y}")
    root.after(50, update_coordinates)  # Refresh every 50ms

def capture_coordinates(event=None):
    """Capture and display the current coordinates when 'C' is pressed."""
    x, y = pyautogui.position()
    print(f"Captured coordinates: X={x}, Y={y}")
    captured_label.config(text=f"Captured: X={x}, Y={y}")

    # Save the captured coordinates to a file
    save_coordinates_to_file(x, y)

def save_coordinates_to_file(x, y):
    """Save the captured coordinates to a text file."""
    try:
        with open(file_path, "a") as file:
            file.write(f"X={x}, Y={y}\n")
        print(f"Coordinates saved to {file_path}.")
    except Exception as e:
        print(f"Failed to save coordinates: {e}")

def close_program(event=None):
    """Close the program when 'Q' is pressed."""
    print("Program closed.")
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Mouse Coordinate Finder")
root.geometry("400x250")
root.resizable(False, False)

# Display instructions
instructions_label = tk.Label(
    root,
    text="Move your mouse to the desired location.\n"
         "Press 'C' to capture coordinates.\n"
         "Press 'Q' to quit the program.",
    font=("Helvetica", 12),
    justify="center"
)
instructions_label.pack(pady=10)

# Display the current coordinates
coords_label = tk.Label(root, text="X: 0, Y: 0", font=("Helvetica", 14))
coords_label.pack(pady=10)

# Display the last captured coordinates
captured_label = tk.Label(root, text="Captured: None", font=("Helvetica", 12))
captured_label.pack(pady=10)

# Bind the 'C' key to capture coordinates and 'Q' key to quit
root.bind('<c>', capture_coordinates)
root.bind('<q>', close_program)

# Start updating coordinates
update_coordinates()

# Run the main loop
root.mainloop()
