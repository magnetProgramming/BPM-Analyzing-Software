import customtkinter
import librosa

app = customtkinter.CTk()

appVersion = "Version 1.0"

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app.geometry("400x500")

app.title("BPM Detector " + appVersion)







aboutButton = customtkinter.CTkButton(master=app, )







app.mainloop()