import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


def main():
    gui = tk.Tk()
    gui.configure(bg="#2b2d30")
    gui.geometry("800x600")
    gui.title("Weather Flower GUI")

    frame = tk.Frame(gui, padx=10, pady=10, bg="white")
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=1)
    frame.rowconfigure(5, weight=1)
    frame.rowconfigure(6, weight=1)
    frame.rowconfigure(7, weight=1)
    frame.rowconfigure(8, weight=1)
    frame.rowconfigure(9, weight=1)
    frame.rowconfigure(10, weight=1)
    frame.rowconfigure(11, weight=1)
    frame.rowconfigure(11, weight=1)
    frame.rowconfigure(12, weight=1)


    img_bloc = tk.Frame(frame, padx=5, pady=5)
    img_bloc.grid(row=0, rowspan=10, column=0)

    img = Image.open("Fleur_Climat_cleaned-coord.png")
    img.thumbnail((400, 400), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    display = tk.Label(img_bloc, image=img_tk)
    display.pack(expand=True)

    title = tk.Label(frame, text="Fleur du temps")
    title.grid(row=0, column=1, columnspan=3, sticky="nsew")

    position = "(1, -1)"
    current_pos = tk.Label(frame, text=position)
    current_pos.grid(row=1, column=1, sticky="nsew")

    forced_position = ["(2, 0)", "(1, -1)", "(2, 1)", "(0, -2)", "(1, 0)",
                       "(2, 2)", "(0, -1)", "(1, 1)", "(-1, -2)", "(0, 0)",
                       "(1, 2)", "(-1, -1)", "(0, 1)", "(-2, -2)", "(-1, 0)",
                       "(0, 2)", "(-2, -1)", "(-1, 1)", "(-2, 0)"]

    combo = ttk.Combobox(frame, values=forced_position)
    combo.grid(row=1, column=2, sticky="nsew")

    go_button = tk.Button(frame, text="go")
    go_button.grid(row=1, column=3, sticky="nsew")

    return_button = tk.Button(frame, text="back")
    return_button.grid(row=2, column=1, sticky="nsew")

    next_button = tk.Button(frame, text="next")
    next_button.grid(row=2, column=2, columnspan=2, sticky="nsew")

    effect_title = tk.Label(frame, text="Liste des effets")
    effect_title.grid(row=3, column=1, columnspan=3, sticky="nsew")

    effect_duration = tk.Label(frame, text="Durée :")
    effect_duration.grid(row=4, column=1, sticky="nsew")

    effect_sight = tk.Label(frame, text="Vue :")
    effect_sight.grid(row=5, column=1, sticky="nsew")

    effect_earing = tk.Label(frame, text="Audition :")
    effect_earing.grid(row=6, column=1, sticky="nsew")

    effect_ranged_attack = tk.Label(frame, text="Attaque à distance :")
    effect_ranged_attack.grid(row=7, column=1, sticky="nsew")

    effect_flame = tk.Label(frame, text="Flame :")
    effect_flame.grid(row=8, column=1, sticky="nsew")

    effect_flight = tk.Label(frame, text="Vol :")
    effect_flight.grid(row=9, column=1, sticky="nsew")

    effect_dc = tk.Label(frame, text="DC :")
    effect_dc.grid(row=10, column=1, sticky="nsew")

    effect_tiredness = tk.Label(frame, text="Épuisement :")
    effect_tiredness.grid(row=11, column=1, sticky="nsew")

    effect_temporary_hp = tk.Label(frame, text="PdV Temp :")
    effect_temporary_hp.grid(row=12, column=1, sticky="nsew")

    description_title = tk.Label(frame, text="Description :")
    description_title.grid(row=10, column=0, sticky="nsew")

    description = ("Le vent se lève et des rafales de vents glaciales s'abattent sur le groupe, des gerbes de neige "
                   "sont soulevés des conggères et se mélangent aux nombreux flocons tombant du ciel. Il devient "
                   "difficile de voir devant soi, et vous arrivez à peine à entendre ce qui se passe autour de vous. "
                   "Un blizzard s'est levé.")
    text_description = tk.Label(frame, text=description, justify="left", wraplength=300)
    text_description.grid(row=11, rowspan=2, column=0, sticky="nsew")


    gui.mainloop()


if __name__ == '__main__':
    main()
