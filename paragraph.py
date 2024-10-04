
from tkinter import *


class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.configure(bg="#25282b")
        self.title("LawQry")

        # Frame for the header
        self.mainframe = Frame(self, width=1280, height=150, bg="#18191a")
        self.mainframe.pack(fill=X)

        # Canvas for the rectangle and images
        self.canvas = Canvas(self.mainframe, width=1280, height=150, bg="#18191a", highlightthickness=0)
        self.canvas.pack(fill=BOTH)
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

        # Add the Next button, initially disabled
        self.nextButton = Button(
            self.mainframe,
            text="Next",
            font=("Comic Sans MS", 20),
            bg="#25282b",
            fg="white",
            state=DISABLED,  # Initially disabled
            command=self.nextQuestion  # Command to move to the next question
        )
        self.nextButton.place(x=1000, y=45, anchor="ne")

        # Initialize questions and options with correct answers
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Berlin", "London", "Paris", "Rome"],
             "answer": "Paris"},
            {"question": "Which legal act did Anita rely on to challenge the government's decision?",
             "options": ["Indian Penal Code, 1860", " Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013", "Transfer of Property Act, 1882", "Indian Contract Act, 1872"],
             "answer": "Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013"},
            {"question": "What was Anita’s primary concern with the government’s land acquisition??",
             "options": ["The government’s refusal to acquire her land", "The low compensation offered", "The location of the highway", " The environmental impact of the highway"],
             "answer": "The low compensation offered"},
            {"question": "If Anita is dissatisfied with the District Court’s ruling, where can she appeal next?",
             "options": ["Supreme Court", "Magistrate Court", "High Court", "Consumer Court"], "answer": "High Court"}
        ]
        self.current_question_index = 0
        self.selected_option = StringVar(value="")
        self.score = 0  # Initialize score

        # Create and display the passage frame
        self.createPassageFrame()

        # Bind the "n" key to the Next button, but only enable it when the button is enabled
        self.bind("<KeyPress-n>", self.onKeyPressN)

        # Handle window close event
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def createPassageFrame(self):
        # Frame for the passage section
        self.passageFrame = Frame(self, bg="#25282b", width=1280, height=570)
        self.passageFrame.place(x=0, y=150)

        # Create a Canvas inside the passage frame
        self.passageCanvas = Canvas(self.passageFrame, bg="#25282b", width=1280, height=570,
                                    highlightthickness=0)
        self.passageCanvas.pack(fill=BOTH, expand=True)

        # Draw the rectangle border in the passage frame
        self.drawRectangleBorder(self.passageCanvas)

        # Set up the text for typing animation
        self.text = ("Case Study: Anita, a young school teacher from a small village,\n"
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
                     "and eventually, if necessary, to the Supreme Court.")

        # Create the label with the text variable
        self.typing_label = Label(self.passageCanvas, text="", font=("Arial", 20, "bold"),
                                  bg="#25282b", fg="white",
                                  anchor="nw", justify=LEFT)
        self.typing_label.place(x=30, y=30)  # Slightly inset from rectangle borders

        # Start typing animation
        self.typing_index = 0
        self.typing_speed = 10  # milliseconds
        self.newline_count = 0  # Count the number of newlines
        self.typewriter(self.text)

    def drawRectangleBorder(self, canvas):
        # Draw the rectangle border
        left_padding = 20
        right_padding = 20
        bottom_padding = 80
        top_padding = 20

        rect_x1, rect_y1 = left_padding, top_padding
        rect_x2, rect_y2 = 1280 - right_padding, 570 - bottom_padding

        canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline="white", width=2, fill="")

    def typewriter(self, message):
        if self.typing_index < len(message):
            current_char = message[self.typing_index]

            # Count newlines
            if current_char == '\n':
                self.newline_count += 1

            # Check if 12 newlines have been encountered
            if self.newline_count >= 12:
                # Enable the Next button and change its color to green
                self.nextButton.config(state=NORMAL, bg="green")
                return  # Stop the animation

            # Update label with the current character
            current_text = self.typing_label.cget("text") + current_char
            self.typing_label.config(text=current_text)
            self.typing_index += 1

            # Continue the animation
            self.after(self.typing_speed, self.typewriter, message)

    def clearText(self):
        # Clear the text from the typing_label
        self.typing_label.config(text="")
        # Disable the Next button until an option is selected
        self.nextButton.config(state=DISABLED, bg="#25282b")
        # Display the question and options
        self.displayQuestion()

    def displayQuestion(self):
        # Destroy old passage frame
        if hasattr(self, 'passageFrame'):
            self.passageFrame.destroy()

        # Create a new frame for questions and options
        self.questionFrame = Frame(self, bg="#25282b", width=1280, height=570)
        self.questionFrame.place(x=0, y=150)

        # Create a Canvas inside the question frame
        self.questionCanvas = Canvas(self.questionFrame, bg="#25282b", width=1280, height=570,
                                     highlightthickness=0)
        self.questionCanvas.pack(fill=BOTH, expand=True)

        # Draw the rectangle border in the question frame
        self.drawRectangleBorder(self.questionCanvas)

        # Get the current question and options
        question = self.questions[self.current_question_index]
        question_text = question["question"]
        options = question["options"]

        # Create question label (centered)
        self.question_label = Label(self.questionCanvas, text=question_text, font=("Arial", 20, "bold"),
                                    bg="#25282b", fg="white", wraplength=1200, justify=CENTER)
        self.question_label.place(x=640, y=60, anchor="center")  # Centered position for the question label

        # Coordinates for buttons
        start_x = 20  # Left padding
        start_y = 100  # Starting y-coordinate for buttons
        y_offset = 20  # Space between each button

        # List to hold button widgets
        self.option_buttons = []

        for index, option in enumerate(options):
            button = Button(self.questionCanvas,
                            text=option,
                            font=("Arial", 18),
                            bg="#25282b",
                            fg="white",
                            activebackground="#25282b",
                            activeforeground="green",
                            padx=10,  # Horizontal padding
                            pady=10,  # Vertical padding
                            command=lambda opt=option: self.selectOption(opt))
            button.place(x=start_x, y=start_y + index * (y_offset + button.winfo_reqheight()), anchor="nw", width=1240)
            self.option_buttons.append(button)

        # Update the Next button state
        self.nextButton.config(state=DISABLED, bg="#25282b")

    def selectOption(self, option):
        # Change the color of the selected button
        for button in self.option_buttons:
            if button.cget('text') == option:
                button.config(bg="green", fg="white")
            else:
                button.config(bg="#25282b", fg="white")

        # Check if the selected option is correct
        correct_answer = self.questions[self.current_question_index]["answer"]
        if option == correct_answer:
            self.score += 1  # Increase score for correct answer

        # Enable the Next button when an option is selected
        self.enableNextButton()

    def enableNextButton(self):
        # Enable the Next button when an option is selected
        self.nextButton.config(state=NORMAL, bg="green")
        # Update the command of Next button to proceed further
        self.nextButton.config(command=self.nextQuestion)

    def nextQuestion(self):
        # Increment the question index
        self.current_question_index += 1

        # Check if there are more questions
        if self.current_question_index < len(self.questions):
            # Display the next question
            self.displayQuestion()
        else:
            # Display end message if there are no more questions
            self.displayEndMessage()

    def displayEndMessage(self):
        # Destroy the question frame
        if hasattr(self, 'questionFrame'):
            self.questionFrame.destroy()
        # Create and show an end message in a new window
        end_window = Toplevel(self)
        end_window.title("Quiz Over")
        end_window.geometry("300x200")
        end_window.configure(bg="#25282b")

        end_message = Label(end_window, text=f"You answered {self.score} questions correctly!",
                            font=("Arial", 20, "bold"),
                            bg="#25282b", fg="white", wraplength=280)
        end_message.pack(pady=50)

        # Add a styled OK button to close the end message window
        ok_button = Button(end_window, text="OK", font=("Arial", 14, "bold"),
                           bg="#18191a", fg="white",
                           padx=20, pady=10,  # Increase padding
                           activebackground="green", activeforeground="white",  # Style when active
                           borderwidth=2, relief="raised",  # Add a border
                           command=lambda: self.onEndWindowClose(end_window))
        ok_button.pack(pady=10)

        # Keep reference to the end window
        self.end_window = end_window

    def onEndWindowClose(self, end_window):
        # Enable the main window and destroy the end message window
        self.attributes('-disabled', False)
        end_window.destroy()

    def onKeyPressN(self, event):
        # Check if the Next button is enabled before executing its command
        if self.nextButton.cget('state') == NORMAL:
            self.nextButton.invoke()

    def on_close(self):
        # Ensure end window is closed properly before quitting
        if hasattr(self, 'end_window') and self.end_window.winfo_exists():
            self.end_window.destroy()
        self.destroy()  # Call destroy to close the main window


if __name__ == '__main__':
    window = GUI()
    window.mainloop()