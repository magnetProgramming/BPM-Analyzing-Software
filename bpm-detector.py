import customtkinter
import librosa

app = customtkinter.CTk()

appVersion = "Version 1.0"

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app.geometry("400x500")
app.resizable(width=False, height=False)

app.title("BPM Detector " + appVersion)


def chooseSongFileDialog():
    return

def detectBPM():
    try:

    ecept:
        return error

def about():
    aboutWindow = customtkinter.CTkToplevel()
    aboutWindow.geometry("400x280")
    aboutWindow.title("about")

    developedByLabel = customtkinter.CTkLabel(master=aboutWindow, text="Developed by magnetProgramming")
    developedByLabel.pack()

    appName_VersionNameLabel = customtkinter.CTkLabel(master=aboutWindow, text="BPM Detector " + appVersion)
    appName_VersionNameLabel.pack()


chooseSongButton = customtkinter.CTkButton(master=app, text="Choose Song")
chooseSongButton.pack()

detectBPM_Button = customtkinter.CTkButton(master=app, text="Detect BPM")
detectBPM_Button.pack()

aboutButton = customtkinter.CTkButton(master=app, text="about", command=about)
aboutButton.pack()







app.mainloop()