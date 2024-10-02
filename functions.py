from tkinter import *
import tkinter as tk

def create_custom_frame(root, relwidth, relheight, relx, rely, bg_color):
    frame = tk.Frame(root, bg=bg_color)
    frame.place(relwidth=relwidth, relheight=relheight, relx=relx, rely=rely)
    return frame

def toggle_fullscreen(event, root: tk):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def exit_fullscreen(event, root: tk):
    root.attributes("-fullscreen", False)
    root.geometry("1280x720")  # Optional: Define a default window size

def add_image(root: tk, image_path: str, relx: float, rely: float, relwidth: float, relheight: float, bg_color: str,):
    """Adds an image to the Tkinter window at specified relative position and size."""
    img = PhotoImage(file=image_path)  # Load the image (ensure it's a .png or compatible format)

    # Create a label to hold the image
    label = Label(root, image=img, bg=bg_color)
    label.image = img  # Keep a reference to avoid garbage collection
    label.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="center")  # Position the label with padding

def add_label(root, text, relx, rely, relwidth, relheight, bg_color="#ffffff", font_size=12, font_color="#000000"):     
    label = Label(root, text=text, bg=bg_color, fg=font_color, font=("Helvetica", font_size))
    label.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="center", )  
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