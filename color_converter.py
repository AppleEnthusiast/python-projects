# Program: RGB color to hex color code and display

import tkinter as tk

print("Welcome to the Color Converter!")

# Inputs for red, green, and blue (values 0-255)
r = int(input("Red value (0-255): "))
g = int(input("Green value (0-255): "))
b = int(input("Blue value (0-255): "))

# Convert to hex color code
hex_color = f"#{r:02X}{g:02X}{b:02X}"

print()
print("Your input:")
print(f"Red: {r}, Green: {g}, Blue: {b}")
print(f"Hex color code: {hex_color}")

# Show the color in a window
window = tk.Tk()
window.title("Show Color")

# Set window size and background color
window.geometry("200x200")
window.configure(bg=hex_color)

# Start window loop
window.mainloop()

