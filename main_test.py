from tkinter import *
from functions import *  # Ensure this file exists and contains necessary functions
import json 

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Full Screen App")
        
        # Make the window full screen
        self.attributes("-fullscreen", True)
        self.configure(bg="#25282b")
        
        # Create a custom frame
        self.header_frame = create_custom_frame(self, relheight=0.2583, relwidth=1, relx=0, rely=0, bg_color="#18191a")
        
        # Logo image
        add_image(self.header_frame, 'newlogo.png', relx=0.15, rely=0.45, relwidth=0.5, relheight=1, bg_color="#18191a")

        # Heart image
        add_image(self.header_frame, 'pngwing.com1.png', relx=0.925, rely=0.49, relwidth=0.3, relheight=0.4, bg_color="#18191a")

        # No. of hearts
        add_label(self.header_frame, "3", relx=0.85, rely=0.5, relwidth=0.028, relheight=1, bg_color="#18191a", font_size=49, font_color="white")

        # Bind F11 key for toggling fullscreen
        self.bind("<F11>", lambda event: toggle_fullscreen(event, self))
        # Bind Escape key for exiting fullscreen
        self.bind("<Escape>", lambda event: exit_fullscreen(event, self))

        # Load questions from the JSON file
        self.questions = load_json_file('questions.json')
        self.current_question_index = 0
        self.selected_option = StringVar()

    def makeHomeFrame(self):
        self.Home_frame = create_custom_frame(self, relheight=0.7417, relwidth=1, relx=0, rely=0.2583, bg_color="#25282b")
        
        # Add label
        add_label(self.Home_frame, "Know Your Laws!", relx=0.5, rely=0.1, relwidth=1, relheight=0.25, bg_color="#25282b", font_size=30, font_color="white")

        # Add image buttons in the makeHomeFrame method
        self.image_button_quiz = add_image_button(self.Home_frame, "newlogo.png", relx=0.2, rely=0.4, relwidth=0.25, relheight=0.2, command=self.button_action_quiz)
        self.image_button_read = add_image_button(self.Home_frame, "newlogo.png", relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2, command=self.button_action_read)
        self.image_button_watch = add_image_button(self.Home_frame, "newlogo.png", relx=0.8, rely=0.4, relwidth=0.25, relheight=0.2, command=self.button_action_watch)

    def button_action_quiz(self):
        print("Quiz button clicked!")
        self.make_Quiz_Frame()
   
    def button_action_read(self):
        print("Read button clicked!")
        destroy_frame(self.Home_frame)

    def button_action_watch(self):
        print("Watch button clicked!")  
        destroy_frame(self.Home_frame)
    
    def make_Quiz_Frame(self):
        destroy_frame(self.Home_frame)
        self.Quiz_frame = create_custom_frame(self, relheight=0.7417, relwidth=1, relx=0, rely=0.2583, bg_color="#25282b")

        self.display_question_and_options()

        # Add the "Next" button
        add_standard_button(self.header_frame, text="Next", relx=0.5, rely=0.5, command=self.next_question, bg_color="#25282b", fg_color="white", relwidth=0.2, relheight=0.05)


    def display_question_and_options(self):
        # Get the current question and options
        question_data = self.questions[self.current_question_index]
        question_text = question_data["question"]
        options = question_data["options"]

        # Add question text inside the rectangle
        add_rectangle_with_text_to_frame(self.Quiz_frame, rel_x=0, rel_y=0, rel_height=0.3, rel_width=1, bg_color="#25282b", border_color="white", text=question_text, font_size=35, font_color="white", padding=50)

        # Create 4 radio buttons for the options
        self.selected_option.set(None)  # Reset the selected option
        for i, option in enumerate(options):
                 add_radio_button(self.Quiz_frame, 
                     variable=self.selected_option, 
                     value=option, 
                     text=option, 
                     relx=0.1, 
                     rely=0.6 + i * 0.1, 
                     relwidth=0.5,  # Customize width here
                     relheight=0.15)  # Customize height here


    def next_question(self):
        # Increment the question index and display the next question if available
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            destroy_frame(self.Quiz_frame)  # Clear the frame
            self.make_Quiz_Frame()  # Display the next question
        else:
            add_label(self.Quiz_frame, "Quiz Completed!", relx=0.5, rely=0.5, relwidth=1, relheight=0.1, bg_color="#25282b", font_size=20, font_color="white")

if __name__ == '__main__':
    window = GUI()
    window.makeHomeFrame()
    window.mainloop()

if __name__ == '__main__':
    window = GUI()
    window.makeHomeFrame()
    window.mainloop()
