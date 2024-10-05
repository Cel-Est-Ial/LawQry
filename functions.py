from tkinter import*
import tkinter as tk
import json
import os

def create_custom_frame(root, relwidth, relheight, relx, rely, bg_color):
    frame = tk.Frame(root, bg=bg_color)
    frame.place(relwidth=relwidth, relheight=relheight, relx=relx, rely=rely)
    return frame

def toggle_fullscreen(event, root: tk):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def exit_fullscreen(event, root: tk):
    root.attributes("-fullscreen", False)
    root.geometry("1280x720")  # Optional: Define a default window size

def add_image(root: tk, image_path: str, relx: float, rely: float, relwidth: float, relheight: float, bg_color: str):
    """Adds an image to the Tkinter window at specified relative position and size."""
    img = tk.PhotoImage(file=image_path)  # Load the image (ensure it's a .png or compatible format)

    # Create a label to hold the image
    label = tk.Label(root, image=img, bg=bg_color)
    label.image = img  # Keep a reference to avoid garbage collection
    label.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="center")  # Position the label

def add_label(root, text, relx, rely, relwidth, relheight, bg_color="#ffffff", font_size=12, font_color="#000000"):
    label = tk.Label(root, text=text, bg=bg_color, fg=font_color, font=("Helvetica", font_size))
    label.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="center")
    return label

def add_image_button(root: tk, image_path: str, relx: float, rely: float, relwidth: float, relheight: float, 
                     command=None, bg_color: str="#FFFFFF"):
    """Adds an image button to the Tkinter window at specified relative position and size."""
    img = tk.PhotoImage(file=image_path)  # Load the image (ensure it's a PNG file)
    
    # Create a button with the image
    button = tk.Button(root, image=img, command=command, bg=bg_color, borderwidth=0)
    button.image = img  # Keep a reference to avoid garbage collection
    button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="center")  # Position the button
    return button

def destroy_frame(frame):
    """Destroys the given frame."""
    if frame:
        frame.destroy()


def add_radio_button(root, variable, value, text, relx, rely, relwidth=None, relheight=None, command=None, bg_color="#25282b", fg_color="white", gap=0, font_size=10, font_color="white"):
    """Adds a custom radio button to the Tkinter window with customizable size, position, gaps, font size, and font color."""
    # Define the font with size and color
    font = (None, font_size)  # Default font family set to None (system default), adjust as needed
    
    radio_button = tk.Radiobutton(root, text=text, variable=variable, value=value,
                                   command=command, indicatoron=0, relief="raised", 
                                   bg=bg_color, fg=fg_color, selectcolor="green", font=font)

    # Set the font color
    radio_button['fg'] = font_color

    # Place the radio button with optional width, height, and gap
    radio_button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="w")  
    return radio_button



def add_standard_button(root, text, relx, rely, command=None, bg_color="#FFFFFF", fg_color="#000000", relwidth=None, relheight=None, font_size=12, font_color="#000000"):
    """Adds a standard button to the Tkinter window with relative width, height, and customizable font."""
    button = tk.Button(root, text=text, command=command, bg=bg_color, fg=fg_color,
                       font=("Arial", font_size), activebackground="green")
    
    # Place the button with relative dimensions
    button.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="center")
    return button


def load_json_file(file_path):
    """Loads a JSON file and returns its contents."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Parse the JSON file
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
        return None

def add_rectangle_with_text_to_frame(frame, rel_x, rel_y, rel_width, rel_height, bg_color, border_color, text, font_size, font_color, padding=10):
    """Creates a canvas inside a frame, draws a rectangle with a border, and places text inside of it."""
    
    # Create a canvas within the frame
    canvas = tk.Canvas(frame, bg=bg_color,borderwidth=0, highlightthickness=0)
    canvas.place(relx=0, rely=0, relwidth=1, relheight=1)  # Fill the entire frame

    # Force the frame to update its size
    frame.update_idletasks()

    # Calculate absolute dimensions based on relative values
    abs_width = frame.winfo_width() * rel_width
    abs_height = frame.winfo_height() * rel_height
    abs_x = frame.winfo_width() * rel_x
    abs_y = frame.winfo_height() * rel_y

    # Draw the rectangle border
    rectangle = canvas.create_rectangle(abs_x, abs_y, abs_x + abs_width, abs_y + abs_height, fill=bg_color, outline=border_color, width=2)

    # Place the text inside the rectangle, with padding from the top-left corner
    text_x = abs_x + padding  # Add padding to the left
    text_y = abs_y + padding  # Add padding to the top
    text_id = canvas.create_text(text_x, text_y, text=text, fill=font_color, font=("Helvetica", font_size), anchor="nw")  # Anchor at the northwest corner

    return rectangle, text_id, canvas

def show_popup(parent, correct_answers, total_questions):
    # Create a new window
    popup = Toplevel(parent)
    popup.title("Results")
    
    # Set the size of the window
    width = 300
    height = 150
    popup.geometry(f"{width}x{height}")

    # Center the window on the screen
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    popup.geometry(f"{width}x{height}+{x}+{y}")

    # Set background color of the popup
    popup.configure(bg="#25282b")  # Set your desired background color

    # Display the number of correct answers with custom font color
    label = Label(popup, text=f"You got {correct_answers} out of {total_questions} correct!",
                  bg="#25282b", fg="white")  # Set background and font color
    label.pack(pady=10)

    # Add a button to close the pop-up and go home
    close_button = Button(popup, text="Close", command=popup.destroy,
                          bg="#25282b", fg="white")  # Set button background and font color
    close_button.pack(pady=5)