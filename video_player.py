import tkinter as tk
from tkinter import Canvas, Button
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk
import threading
import pygame

class VideoPlayer:
    def __init__(self, master, video_file, home_callback):
        self.master = master
        self.video_file = video_file
        self.home_callback = home_callback  # Callback to return to the home page

        # Initialize pygame mixer for audio control
        pygame.mixer.init()

        # Set background color
        self.master.configure(bg='#25282b')

        # Load video
        self.clip = VideoFileClip(self.video_file)

        # Create canvas for the video
        self.canvas = Canvas(master, width=self.clip.w, height=self.clip.h, bg='#25282b', highlightthickness=0)
        self.canvas.pack()

        # Control variables
        self.is_playing = False
        self.current_frame = 0

        # Load audio from video file and convert it for pygame
        self.audio_file = "temp_audio.mp3"
        self.clip.audio.write_audiofile(self.audio_file)

        # Create Play, Stop, and Exit buttons
        self.play_button = Button(master, text="Play", command=self.play, bg="green", fg="white")
        self.play_button.pack(side="left", padx=10, pady=10)

        self.stop_button = Button(master, text="Stop", command=self.stop, bg="red", fg="white")
        self.stop_button.pack(side="right", padx=10, pady=10)

        self.exit_button = Button(master, text="Exit", command=self.exit, bg="blue", fg="white")
        self.exit_button.pack(pady=20)

        # Store the video frames for playing
        self.frame_image = None

    def play(self):
        if not self.is_playing:
            self.is_playing = True
            self.current_frame = 0

            # Play video frames in a separate thread
            threading.Thread(target=self.update_frame, daemon=True).start()

            # Play audio with pygame
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            pygame.mixer.music.stop()  # Stop the audio

    def update_frame(self):
        if self.is_playing:
            # Get the frame
            frame = self.clip.get_frame(self.current_frame / self.clip.fps)
            # Convert frame to an image
            image = Image.fromarray(frame)
            self.frame_image = ImageTk.PhotoImage(image)

            # Update canvas with the new frame
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.frame_image)

            # Schedule the next frame update
            self.current_frame += 1

            if self.current_frame < self.clip.duration * self.clip.fps:
                self.master.after(int(1000 / self.clip.fps), self.update_frame)
            else:
                self.is_playing = False

    def exit(self):
        # Stop playback and go back to the home page
        self.stop()
        self.canvas.delete("all")  # Clear the canvas
        self.clip.close()  # Properly close the video resource
        pygame.mixer.music.stop()  # Stop the audio
        pygame.mixer.quit()  # Quit pygame mixer

        self.master.destroy()  # Close the video player window
        self.home_callback()  # Call the function to go back to the home page

    def close(self):
        self.clip.close()
        pygame.mixer.quit()  # Close pygame mixer when done


# import tkinter as tk
# from tkinter import Canvas, Button
# from moviepy.editor import VideoFileClip
# from PIL import Image, ImageTk
# import threading
# import pygame

# class VideoPlayer:
#     def __init__(self, master, video_file, home_callback):
#         self.master = master
#         self.video_file = video_file
#         self.home_callback = home_callback  # Callback to return to home page

#         # Initialize pygame mixer for audio control
#         pygame.mixer.init()

#         # Set background color
#         self.master.configure(bg='#25282b')

#         # Load video
#         self.clip = VideoFileClip(self.video_file)

#         # Create canvas with background color and add it to the window
#         self.canvas = Canvas(master, width=self.clip.w, height=self.clip.h, bg='#25282b', highlightthickness=0)
#         self.canvas.pack()

#         # Control variables
#         self.is_playing = False
#         self.current_frame = 0

#         # Load audio from video file and convert it for pygame
#         self.audio_file = "temp_audio.mp3"
#         self.clip.audio.write_audiofile(self.audio_file)

#         # Create Play, Stop, and Exit buttons
#         self.play_button = Button(master, text="Play", command=self.play, bg="green", fg="white")
#         self.play_button.pack(side="left", padx=10, pady=10)

#         self.stop_button = Button(master, text="Stop", command=self.stop, bg="red", fg="white")
#         self.stop_button.pack(side="right", padx=10, pady=10)

#         self.exit_button = Button(master, text="Exit", command=self.exit, bg="blue", fg="white")
#         self.exit_button.pack(pady=20)

#         # Store the video frames for playing
#         self.frame_image = None

#     def play(self):
#         if not self.is_playing:
#             self.is_playing = True
#             self.current_frame = 0

#             # Play video frames in a separate thread
#             threading.Thread(target=self.update_frame, daemon=True).start()

#             # Play audio with pygame
#             pygame.mixer.music.load(self.audio_file)
#             pygame.mixer.music.play()

#     def stop(self):
#         if self.is_playing:
#             self.is_playing = False
#             pygame.mixer.music.stop()  # Stop the audio

#     def update_frame(self):
#         if self.is_playing:
#             # Get the frame
#             frame = self.clip.get_frame(self.current_frame / self.clip.fps)
#             # Convert frame to an image
#             image = Image.fromarray(frame)
#             self.frame_image = ImageTk.PhotoImage(image)

#             # Update canvas with the new frame
#             self.canvas.create_image(0, 0, anchor=tk.NW, image=self.frame_image)

#             # Schedule the next frame update
#             self.current_frame += 1

#             if self.current_frame < self.clip.duration * self.clip.fps:
#                 self.master.after(int(1000 / self.clip.fps), self.update_frame)
#             else:
#                 self.is_playing = False

#     def exit(self):
#         # Stop playback and go back to home page
#         self.stop()
#         self.master.destroy()  # Close the video player window
#         self.home_callback()   # Call the function to go back to home page

#     def close(self):
#         self.clip.close()
#         pygame.mixer.quit()  # Close pygame mixer when done
