from tkinter import Tk, PhotoImage, Label, ttk, messagebox
import subprocess
import os
import shutil
import webbrowser

pfx = "https://llama.pe/convertir-cer-y-key-a-pfx"


def open_directory_explorer():
    script_path = os.path.realpath(__file__)
    target_directory = os.path.join(os.path.dirname(script_path), "certs")
    subprocess.Popen(f'explorer "{target_directory}"', shell=True)


def create_cer(_key: any, _cer: any, _day: any, _name: any):
    key = _key.get()
    cer = _cer.get()

    with open("settings.txt", "r") as _read:
        settings = _read.read()
    subprocess.run(settings, shell=True, check=True)
    path = f"{os.getcwd()}/certs"
    shutil.move(f"{key}.key", path)
    shutil.move(f"{cer}.cer", path)
    _key.config(state="normal")
    _cer.config(state="normal")
    _day.config(state="normal")
    _key.delete(0, "end")
    _cer.delete(0, "end")
    _day.delete(0, "end")
    _name.delete(0, "end")
    _key.config(state="readonly")
    _cer.config(state="readonly")
    _day.config(state="readonly")
    messagebox.showinfo("Info", "Your certificate is ready")
    open_directory_explorer()


def write_json(_key: any, _cer: any, _day: any, _name: any):
    key = _key.get()
    cer = _cer.get()
    day = _day.get()
    name = _name.get()

    command = f'openssl req -nodes -x509 -newkey rsa:4096 -keyout {key}.key -out {cer}.cer -days {day} -subj "/CN={name}"'
    with open("settings.txt", "w") as _write:
        _write.write(str(command))

    create_cer(_key, _cer, _day, _name)


def center_window(window: any, width: int, height: int):
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def valid_information(_key: any, _cer: any, _day: any, _name: any):
    key = _key.get()
    cer = _cer.get()
    day = _day.get()
    name = _name.get()

    if key == "":
        messagebox.showerror("Error", "Data cannot be blank :: KEY")
    elif cer == "":
        messagebox.showerror("Error", "Data cannot be blank :: CER")
    elif day == "":
        messagebox.showerror("Error", "Data cannot be blank :: DAY")
    elif name == "":
        messagebox.showerror("Error", "Data cannot be blank :: APP")
    else:
        write_json(_key, _cer, _day, _name)


class Main:
    def __init__(self):
        # ! settings window
        window = Tk()
        window.withdraw()
        center_window(window, 600, 460)
        window.title("Certificate Applications")
        window.iconbitmap("images/icon-app.ico")

        # ? config panel
        panel_info_bg = Label(window, background="white")
        panel_info_bg.place(width=600, height=84)
        line_panel_info = Label(window, background="#b5b5b5")
        line_panel_info.place(width=600, height=1, y=85)
        logo = PhotoImage(file=r"images/logo-application.png")
        logo_application = Label(window, image=logo, background="white")
        logo_application.place(x=11, y=9)
        inf_application = Label(
            window,
            text="Create Certificates OpenSSL for you applications",
            font=("Aria", 14),
            background="white",
            foreground="black",
        )
        inf_application.place(x=80, y=17)
        sub_inf_application = Label(
            window,
            text="By using the application you are accepting the terms and conditions",
            font=("Aria", 10),
            background="white",
            foreground="grey",
        )
        sub_inf_application.place(x=83, y=47)

        # ? config information and insert information
        name_key = Label(window, text="Key Name", font=("Arial", 14), foreground="grey")
        name_key.place(x=20, y=120)
        insert_name_key = ttk.Combobox(
            window,
            values=["", "Key", "KeySSL", "KeyOpenSSL", "KEY"],
            justify="center",
            font=("Arial", 12),
            state="readonly",
            takefocus=False,
            cursor="hand2",
        )
        insert_name_key.place(width=425, height=35, x=145, y=117)
        name_cer = Label(
            window, text="Certification Name", font=("Arial", 14), foreground="grey"
        )
        name_cer.place(x=20, y=180)
        insert_name_cer = ttk.Combobox(
            window,
            values=["", "Cer", "CerSSL", "CerOpenSSL", "CER"],
            justify="center",
            font=("Arial", 12),
            state="readonly",
            cursor="hand2",
            takefocus=False,
        )
        insert_name_cer.place(width=355, height=35, x=215, y=177)
        day = Label(
            window, text="Certification Days", font=("Arial", 14), foreground="grey"
        )
        day.place(x=20, y=240)
        insert_day = ttk.Combobox(
            window,
            values=["", "365", "730", "1095", "1460", "1825"],
            justify="center",
            font=("Arial", 12),
            state="readonly",
            cursor="hand2",
            takefocus=False,
        )
        insert_day.place(width=355, height=35, x=215, y=237)
        name_application = Label(
            window, text="Name Application", font=("Arial", 14), foreground="grey"
        )
        name_application.place(x=20, y=300)
        insert_name_application = ttk.Entry(
            window,
            justify="center",
            font=("Arial", 12),
            cursor="hand2",
            takefocus=False,
        )
        insert_name_application.place(width=355, height=35, x=215, y=297)

        # ? buttons
        img_folder = PhotoImage(file=r"images/folder.png")
        img_create = PhotoImage(file=r"images/certification.png")
        button_folder = ttk.Button(
            window,
            text="View Certificates  ",
            image=img_folder,
            compound="right",
            padding=(20, 15, 20, 15),
            cursor="hand2",
            takefocus=False,
            command=lambda: [{open_directory_explorer()}],
        )
        button_folder.place(x=30, y=365)
        button_pfx = ttk.Button(
            window,
            text="Create PFX  ",
            image=img_create,
            compound="right",
            padding=(20, 15, 20, 15),
            cursor="hand2",
            takefocus=False,
            command=lambda: [{webbrowser.open(pfx)}],
        )
        button_pfx.place(x=210, y=365)
        button_create = ttk.Button(
            window,
            text="Create Certification SSL  ",
            image=img_create,
            compound="right",
            padding=(20, 15, 20, 15),
            cursor="hand2",
            takefocus=False,
            command=lambda: [
                {
                    valid_information(
                        insert_name_key,
                        insert_name_cer,
                        insert_day,
                        insert_name_application,
                    )
                }
            ],
        )
        button_create.place(x=360, y=365)

        # * version
        ver = Label(window, text="v 1.0.0", font=("Arial", 10), foreground="grey")
        ver.place(x=5, y=435)
        # ! view window
        window.deiconify()
        window.mainloop()


if __name__ == "__main__":
    Main()
