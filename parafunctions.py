from tkinter import *
from functions import *  # Ensure this file exists and contains necessary functions
import json

def animate_text(canvas, text, x, y, font, root, delay=50):
    """Function to create a typing animation for a given text on a canvas."""
    text_id = canvas.create_text(x, y, text="", font=font, fill="white", anchor="nw")
    
    def type_char(index):
        if index < len(text):
            current_text = canvas.itemcget(text_id, "text")
            canvas.itemconfig(text_id, text=current_text + text[index])
            root.after(delay, type_char, index + 1)
        else:
            # Check if it reached the 14th '\n'
            if current_text.count('\n') >= 14:
                # Clear the text
                canvas.itemconfig(text_id, text="")
                # Start typing again from the top
                root.after(1000, type_char, 0)  # Add a delay before starting again

    type_char(0)  # Start the typing animation

def makePassageFrame(root):
    # Create the passage frame
    passageFrame = Frame(root, bg="#25282b")
    passageFrame.place(relheight=0.7417, relwidth=1, relx=0, rely=0.2583)

    # Create a Canvas to draw the rectangle and animate the text
    canvas = Canvas(passageFrame, bg="#25282b", highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    # Set rectangle dimensions using relx, rely, relwidth, and relheight
    rect_relx = 0.    # 0% from the left
    rect_rely = 0.    # 0% from the top
    rect_relwidth = 1  # 100% of the frame width
    rect_relheight = 1 # 100% of the frame height

    # Update dimensions after the canvas is packed
    passageFrame.update_idletasks()  # Ensure the passageFrame is updated
    width = passageFrame.winfo_width()
    height = passageFrame.winfo_height()

    # Calculate absolute coordinates for the rectangle
    rect_x1 = width * rect_relx
    rect_y1 = height * rect_rely
    rect_x2 = width * (rect_relx + rect_relwidth)
    rect_y2 = height * (rect_rely + rect_relheight)

    # Add the rectangle with the calculated dimensions
    canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline="white", width=2)

    # Define the body text
    body_text = (
        "Case Study: Anita, a young school teacher from a small village,\n"
        "discovered that the government had decided to acquire her ancestral land\n"
        "to build a new highway. The compensation offered was far below the market value,\n"
        "and many villagers, including Anita, felt it was unjust.\n"
        "They feared that losing their land would devastate their livelihoods.\n"
        "Determined to fight for her rights,\n"
        "Anita learned about the right to property and the judicial remedies available in India.\n"
        "She decided to challenge the government's decision in court, seeking fair compensation.\n"
        "Through her journey, Anita discovered the importance of the judiciary in protecting\n"
        "citizens' rights. She approached the District Court, where the judge explained\n"
        "that under the Right to Fair Compensation and Transparency in Land Acquisition,\n"
        "Rehabilitation and Resettlement Act, 2013, she was entitled to fair compensation.\n"
        "If dissatisfied with the District Court’s ruling, she could appeal to the High Court,\n"
        "and eventually, if necessary, to the Supreme Court.\n"
    )

    # Start the typing animation after the rectangle is drawn
    animate_text(canvas, body_text, rect_x1 + 10, rect_y1 + 10, font=("Arial", 23), root=root)

    return passageFrame  # Return the created passageFrame for further use if needed
