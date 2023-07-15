from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time
from pygame import mixer

# Function to handle button clicks
def quit_game():
    root.destroy()

def start_game():
    global intro_label, continue_button
    # Remove the start button
    start_button.grid_remove()

    # Show the introduction text with typing effect
    intro_text = "In the darkness of Soundless Mountain, an ancient evil stirs. A presence so malevolent, it consumes the souls of those who dare to enter its realm. Legends speak of unspeakable horrors, twisted entities that dwell in the shadows, and tormented spirits seeking vengeance. You play as a lost soul, drawn inexplicably to the mountain's cursed depths. Desperation fuels your quest for answers, as you navigate through a labyrinth of fear and despair. Can you survive the terrors that await within Soundless Mountain, or will you become just another victim of its eternal nightmare?"

    typing_speed = 1500  # Speed of typing effect (characters per minute)
    typing_delay = 60 / typing_speed  # Delay between each character based on typing speed

    def type_intro_text(text, index):
        if index <= len(text):
            intro_label.configure(text=text[:index])
            root.after(int(typing_delay * 1000), lambda: type_intro_text(text, index + 1))
        else:
            # Show continue button after the introduction text
            continue_button.grid(column=0, row=1, columnspan=2, pady=padding * 2)

    intro_label = ttk.Label(frame, text="", font=text_font, foreground="#b7b7b7", background="#1c1c1c", wraplength=600, justify='left')
    intro_label.grid(column=0, row=0, columnspan=2, pady=padding)

    continue_button = ttk.Button(frame, text="Continue", command=progress_to_next_scene, style="GameButton.TButton", width=int(root.winfo_screenwidth() / 100))
    continue_button.grid_remove()  # Initially hide the continue button

    # Typing effect for the introduction text
    type_intro_text(intro_text, 0)

def progress_to_next_scene():
    global scene_label, continue_button2
    # Remove the intro label and continue button
    intro_label.grid_remove()
    continue_button.grid_remove()

    # Show the next scene text with typing effect
    scene_text = "As you step further into the heart of Soundless Mountain, the air grows thick with an otherworldly presence. The surroundings shift and contort, merging reality with nightmares. Shadows dance in the corners of your vision, and whispers echo through the labyrinthine corridors. Every step forward fills you with an unshakeable dread, but turning back is not an option. The mountain demands your presence, and it won't release its grip until it has consumed your very soul."

    typing_speed = 1800  # Speed of typing effect (characters per minute)
    typing_delay = 60 / typing_speed  # Delay between each character based on typing speed

    def type_scene_text(text, index):
        if index <= len(text):
            scene_label.configure(text=text[:index])
            root.after(int(typing_delay * 1000), lambda: type_scene_text(text, index + 1))
        else:
            # Show continue button after the scene text
            continue_button2.grid(column=0, row=2, columnspan=2, pady=padding * 2)

    scene_label = ttk.Label(frame, text="", font=text_font, foreground="#b7b7b7", background="#1c1c1c", wraplength=600, justify='left')
    scene_label.grid(column=0, row=1, columnspan=2, pady=padding)

    continue_button2 = ttk.Button(frame, text="Continue", command=next_scene, style="GameButton.TButton", width=int(root.winfo_screenwidth() / 100))
    continue_button2.grid_remove()  # Initially hide the continue button

    # Typing effect for the scene text
    type_scene_text(scene_text, 0)

def next_scene():
    global next_scene_label, continue_button3
    heartbeat.play()
    # Remove the scene label and continue button
    scene_label.grid_remove()
    continue_button2.grid_remove()

    # Show the next scene text with typing effect
    next_scene_text = "In the dimly lit corridor, a flickering light draws your attention. You cautiously approach, your heart pounding with a mix of curiosity and dread. As you reach the source of the light, you discover a decaying journal, its pages filled with the ravings of a tormented soul. The words speak of unspeakable horrors lurking in the darkness, and a hidden passage that leads deeper into the mountain. With trembling hands, you close the journal and steel yourself for the unknown horrors that lie ahead."

    typing_speed = 2000  # Speed of typing effect (characters per minute)
    typing_delay = 60 / typing_speed  # Delay between each character based on typing speed

    def type_next_scene_text(text, index):
        if index <= len(text):
            next_scene_label.configure(text=text[:index])
            root.after(int(typing_delay * 1000), lambda: type_next_scene_text(text, index + 1))
        else:
            # Show continue button after the next scene text
            continue_button3.grid(column=0, row=3, columnspan=2, pady=padding * 2)

    next_scene_label = ttk.Label(frame, text="", font=text_font, foreground="#b7b7b7", background="#1c1c1c", wraplength=600, justify='left')
    next_scene_label.grid(column=0, row=2, columnspan=2, pady=padding)

    continue_button3 = ttk.Button(frame, text="Continue", command=third_scene, style="GameButton.TButton", width=int(root.winfo_screenwidth() / 100))
    continue_button3.grid_remove()  # Initially hide the continue button

    # Typing effect for the next scene text
    type_next_scene_text(next_scene_text, 0)

def third_scene():
    global third_scene_label, continue_button4
    # Remove the next scene label and continue button
    next_scene_label.grid_remove()
    continue_button3.grid_remove()

    # Show the third scene text with typing effect
    third_scene_text = "A chill runs down your spine as you step into a chamber filled with unsettling artifacts. The walls are adorned with paintings depicting nightmarish creatures and twisted landscapes. In the center of the room, a blood-stained altar stands as a grim reminder of the dark rituals that have taken place here. As you cautiously explore, the air becomes suffocatingly heavy, and whispers fill the room, echoing with a sinister invitation. The choice lies before you: succumb to the madness or find a way to break free from Soundless Mountain's grasp."

    typing_speed = 1800  # Speed of typing effect (characters per minute)
    typing_delay = 60 / typing_speed  # Delay between each character based on typing speed

    def type_third_scene_text(text, index):
        if index <= len(text):
            third_scene_label.configure(text=text[:index])
            root.after(int(typing_delay * 1000), lambda: type_third_scene_text(text, index + 1))
        else:
            # Show continue button after the third scene text
            continue_button4.grid(column=0, row=4, columnspan=2, pady=padding * 2)

    third_scene_label = ttk.Label(frame, text="", font=text_font, foreground="#b7b7b7", background="#1c1c1c", wraplength=600, justify='left')
    third_scene_label.grid(column=0, row=3, columnspan=2, pady=padding)

    continue_button4 = ttk.Button(frame, text="Continue", command=quit_game, style="GameButton.TButton", width=int(root.winfo_screenwidth() / 100))
    continue_button4.grid_remove()  # Initially hide the continue button

    # Typing effect for the third scene text
    type_third_scene_text(third_scene_text, 0)

mixer.init()

# Define your sound and music files paths
heartbeat = "assets/heart_beat.mp3"
background_music_path = "assets/ambience1.mp3"

# Load the sound effect
heartbeat = mixer.Sound(heartbeat)

# Load and play the background music
mixer.music.load(background_music_path)
mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Setting up the root window
root = Tk()
root.title("Soundless Mountain")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Set the window to full-screen
root.configure(bg="#1c1c1c")

# Load the background image
bg_image = Image.open("assets/spooky_mountain.png")
bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.BILINEAR)
bg_image = ImageTk.PhotoImage(bg_image)

# Creating a canvas
canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#1c1c1c", highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)

# Place the background image on the canvas
canvas.create_image(0, 0, anchor=NW, image=bg_image)

# Creating a frame
frame = ttk.Frame(canvas, padding=40, style="GameFrame.TFrame")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Calculate font sizes and padding
text_font_size = max(int(root.winfo_screenwidth() / 100), 15)
button_font_size = max(int(root.winfo_screenwidth() / 60), 20)
padding = 30

# Styling the fonts
text_font = ("Arial", text_font_size, "bold")
button_font = ("Arial", button_font_size, "bold")

# Adding interactive buttons
start_button = ttk.Button(frame, text="Start", command=start_game, style="GameButton.TButton", width=int(root.winfo_screenwidth() / 100))
start_button.grid(column=0, row=0, padx=padding, pady=padding * 2, sticky="w")

# Styling the buttons
style = ttk.Style()
style.configure("GameButton.TButton", font=button_font, foreground="#1c1c1c", background="#e1e1e1", relief="raised")

# Styling the frame
style.configure("GameFrame.TFrame", background="#1c1c1c")

root.mainloop()
