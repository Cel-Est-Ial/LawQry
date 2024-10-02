from tkinter import *
from functions import *  # Ensure this file exists and contains necessary functions

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

        #heart image
        add_image(self.header_frame, 'pngwing.com1.png', relx=0.925, rely=0.49, relwidth=0.3, relheight=0.4, bg_color="#18191a")

        #no. of hearts
        add_label(self.header_frame, "3", relx=0.85, rely=0.5, relwidth=0.028, relheight=1, bg_color="#18191a", font_size=49, font_color="white")

        # Bind F11 key for toggling fullscreen
        self.bind("<F11>", lambda event: toggle_fullscreen(event, self))
        # Bind Escape key for exiting fullscreen
        self.bind("<Escape>", lambda event: exit_fullscreen(event, self))
    
    def makeHomeFrame(self):
        self.Home_frame = create_custom_frame(self, relheight=0.7417, relwidth=1, relx=0, rely=0.2583, bg_color="#25282b")
        #add label
        add_label(self.Home_frame, "Know Your Laws!", relx=0.5, rely=0.1, relwidth=1, relheight=0.25, bg_color="#25282b", font_size=30, font_color="white")
        # Add an image button in the makeHomeFrame method
        self.image_button = add_image_button(self.Home_frame, "newlogo.png", relx=0.2, rely=0.3, relwidth=0.25, relheight=0.2, command=self.button_action)
        self.image_button = add_image_button(self.Home_frame, "newlogo.png", relx=0.5, rely=0.3, relwidth=0.25, relheight=0.2, command=self.button_action)
        self.image_button = add_image_button(self.Home_frame, "newlogo.png", relx=0.8, rely=0.3, relwidth=0.25, relheight=0.2, command=self.button_action)
   
       



    def button_action(self):
     print("Button clicked!")
if __name__ == '__main__':
    window = GUI()
    window.makeHomeFrame()
    window.mainloop()
