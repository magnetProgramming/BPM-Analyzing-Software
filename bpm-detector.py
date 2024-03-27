import customtkinter
import librosa
import threading
import pygame


app = customtkinter.CTk()

appVersion = "Version 1.0"
audioFile = None
pygame.mixer.init()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app.geometry("400x500")
app.resizable(width=False, height=False)

app.title(f"BPM Detector {appVersion}")


def playSong():
    global audioFile
    try:
        pygame.mixer.music.load(audioFile)
        pygame.mixer.music.play()

    except Exception as e:
        print(f"Error playing song: {e}")

def stopSong():
    pygame.mixer.music.stop()
    

def chooseSongFileDialog():
    global audioFile
    chosenSong = customtkinter.filedialog.askopenfilename()
    audioFile = chosenSong

def detectBPM():
    try:
        global audioFile
        y, sr = librosa.load(audioFile)
        BPM, _ = librosa.beat.beat_track(y=y, sr=sr)
        detectedBPM_Label.configure(text="BPM Detected is {}".format(BPM))




    except Exception as e:
        detectedBPM_Label.configure(text=f"Error: {e}")

def about():
    aboutWindow = customtkinter.CTkToplevel()
    aboutWindow.geometry("400x280")
    aboutWindow.title("about")

    developedByLabel = customtkinter.CTkLabel(master=aboutWindow, text="Developed by magnetProgramming")
    developedByLabel.pack()

    appName_VersionNameLabel = customtkinter.CTkLabel(master=aboutWindow, text="BPM Detector " + appVersion)
    appName_VersionNameLabel.pack()


detectedBPM_Label = customtkinter.CTkLabel(master=app, text="")
detectedBPM_Label.pack()

playMusicButton = customtkinter.CTkButton(master=app, text="Play selected song", command=lambda: threading.Thread(target=playSong).start())
playMusicButton.pack(padx=20, pady=20)

stopMusicButton = customtkinter.CTkButton(master=app, text="Stop selected song", command=lambda: threading.Thread(target=stopSong).start())
stopMusicButton.pack(padx=20, pady=20)

chooseSongButton = customtkinter.CTkButton(master=app, text="Choose Song", command=chooseSongFileDialog)
chooseSongButton.pack(padx=20, pady=20)

detectBPM_Button = customtkinter.CTkButton(master=app, text="Detect BPM", command=lambda: threading.Thread(target=detectBPM).start())
detectBPM_Button.pack(padx=20, pady=20)

aboutButton = customtkinter.CTkButton(master=app, text="about", command=about)
aboutButton.pack(padx=20, pady=20)




app.mainloop()