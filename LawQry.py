from tkinter import *
import json

class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.configure(bg="#25282b")
        self.title("LawQry")

        # Frame for the header
        self.mainframe = Frame(self, width=1280, height=150, bg="#18191a")
        self.mainframe.pack()

        # Canvas for the rectangle and images
        self.canvas = Canvas(self.mainframe, width=1280, height=150, bg="#18191a", highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, 1280, 150, fill="#18191a", outline="")

        # Logo Image
        self.logo = PhotoImage(file="newlogo.png")
        self.canvas.create_image(15, 15, image=self.logo, anchor="nw")

        # Heart Image
        self.heart = PhotoImage(file="pngwing.com1.png")
        self.canvas.create_image(1145, 45, image=self.heart, anchor="ne")

        # Heart Number
        self.heartNumber = Label(self.mainframe, text="3", font=("Comic Sans MS", 35, "bold"),
                                 bg="#18191a", fg="white")
        self.heartNumber.place(x=1030, y=38)

        # Load questions from JSON file
        with open("questions.json", "r") as file:
            self.questions = json.load(file)

        # Initialize variables
        self.question_index = 0
        self.correct_answers = 0
        self.selected_option = StringVar()
        self.hearts = 3  # Number of hearts

        # Bind keys for navigation and selection
        self.bind("<KeyPress-n>", lambda event: self.onNextClick())
        self.bind("<KeyPress-1>", lambda event: self.select_option(0))
        self.bind("<KeyPress-2>", lambda event: self.select_option(1))
        self.bind("<KeyPress-3>", lambda event: self.select_option(2))
        self.bind("<KeyPress-4>", lambda event: self.select_option(3))

    def update_heart_number(self):
        # Decrease the heart count and update the label
        if self.hearts > 0:
            self.hearts -= 1
            self.heartNumber.config(text=str(self.hearts))

        # Check if hearts have reached 0
        if self.hearts == 0:
            self.game_over()

    def game_over(self):
        # Destroy the second frame and the "Next" button if they exist
        if hasattr(self, 'secondFrame'):
            self.secondFrame.destroy()
        if hasattr(self, 'nextButton'):
            self.nextButton.destroy()

        # Display a pop-up window with the Game Over message
        game_over_window = Toplevel(self)
        game_over_window.title("Game Over")
        game_over_window.configure(bg="#25282b")

        # Get the window dimensions
        window_width = 300
        window_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position for the pop-up to be centered
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the geometry to open the window in the center
        game_over_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        Label(game_over_window, text="Game Over!", font=("Comic Sans MS", 20), bg="#25282b", fg="white").pack(pady=20)

        Button(game_over_window, text="OK", font=("Comic Sans MS", 15), bg="green", fg="white",
               command=lambda: self.on_game_over_ok(game_over_window)).pack()

    def on_game_over_ok(self, game_over_window):
        # Close the Game Over window and reset the quiz
        game_over_window.destroy()
        self.makehomeFrame()

    def makehomeFrame(self):
        # Reset variables
        self.question_index = 0
        self.correct_answers = 0
        self.hearts = 3  # Reset hearts to 3

        # Update the heart number label
        self.heartNumber.config(text=str(self.hearts))

        # Main frame
        self.homeFrame = Frame(self, width=1280, height=570, bg="#25282b")
        self.homeFrame.place(x=0, y=150)

        # Homepage text
        self.firstTxt = Label(self.homeFrame, text="Know Your Constitution!", font=("Comic Sans MS", 40),
                              bg="#25282b", fg="white")
        self.firstTxt.place(x=370, y=60)

        # Start button
        self.startButton = Button(self.homeFrame, text="Start Quiz!", bg="green", fg="white",
                                  font=("Arial", 20, "bold"), width=30, height=1, borderwidth=3,
                                  relief=RAISED, command=self.makeSecondFrame)
        self.startButton.place(x=400, y=210)

    def makeSecondFrame(self):
        # Destroy the home frame if it exists
        if hasattr(self, 'homeFrame'):
            self.homeFrame.destroy()

        # Frame for content below the header
        self.secondFrame = Frame(self, width=1280, height=570, bg="#25282b")
        self.secondFrame.place(x=0, y=150)

        # Canvas inside the second frame to draw a rectangle and place the radio buttons
        self.canvas2 = Canvas(self.secondFrame, width=1280, height=570, bg="#25282b", highlightthickness=0)
        self.canvas2.pack(fill=BOTH, expand=True)

        # Draw the rectangle with a white border
        width = 1200
        height = 140
        x1 = 40
        y1 = 20
        x2 = x1 + width
        y2 = y1 + height
        self.canvas2.create_rectangle(x1, y1, x2, y2, fill="#25282b", outline="white", width=2)

        # Display the current question
        self.display_question()

        # Create the "Next" button, initially disabled
        self.nextButton = Button(self.mainframe, text="Next", font=("Comic Sans MS", 20),
                                 bg="#25282b", fg="white",
                                 state=DISABLED, command=self.onNextClick)
        self.nextButton.place(x=1000, y=45, anchor="ne")

        # Bind the "N" key to the Next button, but only enable it when an option is selected
        self.bind("<KeyPress-n>", lambda event: self.onNextClick() if self.nextButton.cget('state') == NORMAL else None)

    def display_question(self):
        question_data = self.questions[self.question_index]

        # Add a label inside the rectangle for the question
        self.questionLabel = Label(self.canvas2, text=question_data['question'],
                                   font=("Comic Sans MS", 35),
                                   bg="#25282b", fg="white")
        self.questionLabel.place(x=620, y=90, anchor="center")

        # Define the spacing between radio buttons
        spacing = 75
        self.selected_option.set(None)  # Reset selection
        self.option_selected = False  # Reset the option selected flag

        # Create and place radio buttons for options
        self.radio_buttons = []
        for index, option in enumerate(question_data['options']):
            rb = Radiobutton(self.canvas2, text=option, variable=self.selected_option, value=option,
                             font=("Comic Sans MS", 20), bg="#25282b", fg="white", selectcolor="green",
                             indicatoron=False, relief=RAISED, command=self.enableNextButton)
            rb.place(x=60, y=200 + index * spacing, anchor="nw", width=1120)
            self.radio_buttons.append(rb)

            # Bind keys 1, 2, 3, 4 to select the corresponding options
            self.bind(f"<KeyPress-{index + 1}>", lambda event, idx=index: self.select_option(idx))

    def enableNextButton(self):
        # Enable the Next button when an option is selected
        self.nextButton.config(state=NORMAL, bg="green")

    def select_option(self, index):
        if index < len(self.radio_buttons):
            self.selected_option.set(self.questions[self.question_index]['options'][index])
            self.radio_buttons[index].select()
            self.enableNextButton()

    def onNextClick(self):
        # Check if the selected answer is correct
        if self.selected_option.get() == self.questions[self.question_index]['correct_answer']:
            self.correct_answers += 1
        else:
            self.update_heart_number()  # Decrease heart count if the answer is wrong

        # Check if the number of hearts is 0 and handle game over
        if self.hearts == 0:
            return

        self.question_index += 1

        # If there are more questions, load the next one
        if self.question_index < len(self.questions):
            self.questionLabel.destroy()
            for rb in self.radio_buttons:
                rb.destroy()
            self.display_question()
            self.nextButton.config(state=DISABLED, bg="#25282b")
        else:
            self.show_results()

    def show_results(self):
        # Destroy the second frame and the "Next" button
        self.secondFrame.destroy()
        self.nextButton.destroy()

        # Display a pop-up window with the results
        result_window = Toplevel(self)
        result_window.title("Quiz Results")
        result_window.configure(bg="#25282b")

        # Get the window dimensions
        window_width = 400
        window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position for the pop-up to be centered
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the geometry to open the window in the center
        result_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        Label(result_window, text=f"You got {self.correct_answers} out of {len(self.questions)} correct!",
              font=("Comic Sans MS", 20), bg="#25282b", fg="white").pack(pady=50)

        Button(result_window, text="OK", font=("Comic Sans MS", 15), bg="green", fg="white",
               command=lambda: self.on_result_ok(result_window)).pack()

    def on_result_ok(self, result_window):
        # Close the result window and reset the quiz
        result_window.destroy()
        self.makehomeFrame()

if __name__ == '__main__':
    window = GUI()
    window.makehomeFrame()
    window.mainloop()
