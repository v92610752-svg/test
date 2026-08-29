import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

selected_app = None

def choose_app():
    global selected_app

    # На Mac приложения — это .app (на самом деле папка),
    # поэтому используем askdirectory, а не askopenfilename.
    path = filedialog.askdirectory(
        title="Выберите приложение (.app)"
    )

    if path and path.endswith(".app"):
        selected_app = path
        file_label.config(text=os.path.basename(path))
    elif path:
        messagebox.showwarning("Ошибка", "Нужно выбрать файл с расширением .app")

def launch_app():
    if not selected_app:
        messagebox.showwarning("Ошибка", "Сначала выберите приложение (.app)")
        return

    try:
        # "open" — стандартная команда macOS для запуска .app
        subprocess.Popen(["open", selected_app])
    except Exception as e:
        messagebox.showerror("Ошибка запуска", str(e))


root = tk.Tk()
root.title("App Launcher")
root.geometry("400x220")
root.resizable(False, False)

title = tk.Label(
    root,
    text="App Launcher",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

choose_button = tk.Button(
    root,
    text="Выбрать приложение",
    command=choose_app,
    width=25,
    height=2
)
choose_button.pack()

file_label = tk.Label(
    root,
    text="Приложение не выбрано",
    fg="gray"
)
file_label.pack(pady=10)

launch_button = tk.Button(
    root,
    text="▶ Запустить",
    command=launch_app,
    width=25,
    height=2
)
launch_button.pack()

root.mainloop()
