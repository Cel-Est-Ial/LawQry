from tkinter import *
from functions import *  # Ensure this file exists and contains necessary functions
import json
from parafunctions import *
from video_player import VideoPlayer

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
        self.make_Quiz_Frame()
   
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

        # Add video player when "Watch" button is clicked
        self.video_player_frame = create_custom_frame(self, relheight=0.7417, relwidth=1, relx=0, rely=0.2583, bg_color="#25282b")

        # Initialize video player with video file 'v1.mp4', and pass the callback to go home
        self.video_player = VideoPlayer(self.video_player_frame, 'v1.mp4', self.makeHomeFrame)
        self.video_player.play()
    
    def make_Quiz_Frame(self):
        destroy_frame(self.Home_frame)
        self.Quiz_frame = create_custom_frame(self, relheight=0.7417, relwidth=1, relx=0, rely=0.2583, bg_color="#25282b")

        self.display_question_and_options()

        # Add the "Next" button
        self.next_button = add_standard_button(self.header_frame, text="Next", relx=0.53, rely=0.5, command=self.next_question, 
                                       bg_color="#25282b", fg_color="white", relwidth=0.25, relheight=0.5, 
                                       font_size=45, font_color="white")

    def display_question_and_options(self):
        # Clear the previous radio buttons
        for rb in self.radio_buttons:
            rb.destroy()
        self.radio_buttons.clear()  # Clear the list of radio buttons

        # Get the current question and options
        question_data = self.questions[self.current_question_index]
        question_text = question_data["question"]
        options = question_data["options"]

        # Add question text inside the rectangle
        add_rectangle_with_text_to_frame(self.Quiz_frame, rel_x=0, rel_y=0, rel_height=0.25, rel_width=1, bg_color="#25282b", border_color="white", text=question_text, font_size=35, font_color="white", padding=50)

        # Create 4 radio buttons for the options
        gap = 0.07  
        
        for i, option in enumerate(options):
            rb = add_radio_button(self.Quiz_frame,
                                  variable=self.selected_option, 
                                  value=option, 
                                  text=option, 
                                  relx=0.005, 
                                  rely=0.35 + i * (0.1 + gap),  
                                  relwidth=0.99,  
                                  relheight=0.15,  
                                  gap=gap,  
                                  font_size=30,  
                                  font_color="white")
            self.radio_buttons.append(rb)  # Add the radio button to the list
    
    def select_radio(self, option_number):
         if option_number <= len(self.radio_buttons):
          self.radio_buttons[option_number - 1].select()

    def next_question(self):
        selected_value = self.selected_option.get()
        correct_answer = self.questions[self.current_question_index]["correct_answer"]

        # Highlight the correct answer in green and the selected answer in red if wrong
        for rb in self.radio_buttons:
            if rb['value'] == correct_answer:
                rb.config(bg="green")  # Correct answer
            elif rb['value'] == selected_value:
                rb.config(bg="red")  # Incorrect answer

        if selected_value == correct_answer:
            self.correct_answers += 1
        else:
            self.heart -= 1
            self.heart_label.config(text=str(self.heart))  # Update heart label

        if self.heart == 0:
            self.show_game_over_popup()
        elif self.current_question_index < len(self.questions) - 1:
            self.selected_option.set("")  # Deselect radio buttons
            self.after(1000, self.show_next_question)  # Call show_next_question after 1 second
        else:
            self.show_popup()  # Show results

    def show_next_question(self):
        self.current_question_index += 1  # Move to the next question
        self.display_question_and_options()  # Update the display with the new question

    def show_popup(self):
        # Create a new window for results
        self.popup = Toplevel()
        self.popup.title("Results")
        self.popup.geometry(f"{300}x{150}+{500}+{290}")
        self.popup.config(background="#25282b")

        # Display the number of correct answers
        label = Label(self.popup, text=f"You got {self.correct_answers} out of {len(self.questions)} correct!", bg="#25282b", fg="white")
        label.pack(pady=10)

        # Add a button to close the pop-up and go home
        close_button = Button(self.popup, text="Close", command=self.go_home)
        close_button.pack(pady=10)

    def go_home(self):
        self.popup.destroy()
        self.next_button.destroy()
        self.makeHomeFrame()
        self.heart = 3
        self.heart_label.config(text=str(self.heart))
          # Go back to home frame
        self.correct_answers = 0
        self.current_question_index = 0

    def show_game_over_popup(self):
        # Create a new window for game over
        self.game_over_popup = Toplevel()
        self.game_over_popup.title("Game Over")
        self.game_over_popup.geometry(f"{300}x{150}+{500}+{290}")
        self.game_over_popup.config(background="#25282b")

        # Display game over message
        label = Label(self.game_over_popup, text="Game Over!", bg="#25282b", fg="white")
        label.pack(pady=10)

        # Add a button to close the pop-up and go home
        close_button = Button(self.game_over_popup, text="Close", command=self.restart_game)
        close_button.pack(pady=10)

    def restart_game(self):
        self.game_over_popup.destroy()
        
        self.heart = 3
        self.correct_answers = 0
        self.current_question_index = 0
        self.next_button.destroy()
        self.makeHomeFrame()  # Restart the quiz
        self.heart_label.config(text=str(self.heart)) 
       
        

if __name__ == "__main__":
    app = GUI()
    app.makeHomeFrame()
    app.mainloop()
