import sys
import tkinter
import customtkinter
import pyautogui
import os

tab = ["/", "—", "\\", "|"]

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("Kłos Lol Auto Akcept v2")
app.iconbitmap(resource_path("img2.ico"))
app.geometry("400x240")

label = customtkinter.CTkLabel(master=app)
label.configure(text="Wyszukiwanie gry off")

switch_var = tkinter.StringVar()
switch_1 = customtkinter.CTkSwitch(master=app, text="Auto Akcept", variable=switch_var, onvalue=True,
                                   offvalue=False)

label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
switch_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

index = 0


def check():
    if switch_1.get():
        global index
        label.configure(text=f"Wyszukiwanie gry {tab[index]}")
        index = index + 1
        if index == 4:
            index = 0
        if not pyautogui.locateOnScreen(resource_path("img1.png")) is None:
            pyautogui.click(resource_path("img1.png"))
            label.configure(text="Znaleziono mecz!")
            app.after(10000, check)
        else:
            app.after(1000, check)
    else:
        label.configure(text="Wyszukiwanie gry off")
        app.after(1000, check)


app.after(1000, check)
app.mainloop()
