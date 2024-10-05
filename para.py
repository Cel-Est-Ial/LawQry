from tkinter import *
from functions import *  # Ensure this file exists and contains necessary functions
import json
from parafunctions import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Full Screen App")

        # Initialize hearts
        self.heart = 3
        self.radio_buttons = []
        # Make the window full screen
        self.selected_option = StringVar()
        self.attributes("-fullscreen", True)
        self.configure(bg="#25282b")

        # Initialize correct answers counter
        self.correct_answers = 0

        # Create a custom frame for the header
        self.header_frame = create_custom_frame(self, relheight=0.2583, relwidth=1, relx=0, rely=0, bg_color="#18191a")

        # Logo image
        add_image(self.header_frame, 'newlogo.png', relx=0.15, rely=0.45, relwidth=0.5, relheight=1, bg_color="#18191a")

        # Heart image
        add_image(self.header_frame, 'pngwing.com1.png', relx=0.925, rely=0.49, relwidth=0.3, relheight=0.4, bg_color="#18191a")

        # No. of hearts
        self.heart_label = add_label(self.header_frame, str(self.heart), relx=0.85, rely=0.5, relwidth=0.028, relheight=1, bg_color="#18191a", font_size=49, font_color="white")

        # Bind F11 key for toggling fullscreen
        self.bind("<F11>", lambda event: toggle_fullscreen(event, self))
        # Bind Escape key for exiting fullscreen
        self.bind("<Escape>", lambda event: exit_fullscreen(event, self))

        # Load questions from the JSON file
        self.questions = load_json_file('questions.json')
        self.current_question_index = 0

        # Bind 'n' to next_question method
        self.bind("n", lambda event: self.next_question())

        # Bind number keys to select radio buttons
        self.bind("1", lambda event: self.select_radio(1))
        self.bind("2", lambda event: self.select_radio(2))
        self.bind("3", lambda event: self.select_radio(3))
        self.bind("4", lambda event: self.select_radio(4))

    def makeHomeFrame(self):
        self.Home_frame = create_custom_frame(self, relheight=0.7417, relwidth=1, relx=0, rely=0.2583, bg_color="#25282b")

        # Add label
        add_label(self.Home_frame, "Know Your Laws!", relx=0.5, rely=0.1, relwidth=1, relheight=0.25, bg_color="#25282b", font_size=30, font_color="white")

        # Add image buttons
        self.image_button_quiz = add_image_button(self.Home_frame, "newlogo.png", relx=0.2, rely=0.4, relwidth=0.25, relheight=0.2, command=self.button_action_quiz)
        self.image_button_read = add_image_button(self.Home_frame, "newlogo.png", relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2, command=self.button_action_read)
        self.image_button_watch = add_image_button(self.Home_frame, "newlogo.png", relx=0.8, rely=0.4, relwidth=0.25, relheight=0.2, command=self.button_action_watch)

    def button_action_quiz(self):
        print("Quiz button clicked!")

    def button_action_read(self):
        print("Read button clicked!")
        destroy_frame(self.Home_frame)
        self.actualPassageframe = makePassageFrame(self)
        self.nextPassagebutton = add_standard_button(self.header_frame, text="Exit", relx=0.53, rely=0.5, command=lambda: self.end(),
                                       bg_color="#25282b", fg_color="white", relwidth=0.25, relheight=0.5, 
                                       font_size=45, font_color="white")

    def end(self):
        if self.actualPassageframe:
            self.actualPassageframe.destroy()  # Destroy the current passage frame
        if self.nextPassagebutton:
            self.nextPassagebutton.destroy()  # Destroy the next button
        self.makeHomeFrame()  # Or any other function to show the next section

    def button_action_watch(self):
        print("Watch button clicked!")  
        destroy_frame(self.Home_frame)

if __name__ == "__main__":
    app = GUI()
    app.makeHomeFrame()
    app.mainloop()
