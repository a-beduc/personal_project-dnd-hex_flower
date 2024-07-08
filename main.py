import tkinter as tk
# from PIL import ImageTk, Image


def main():
    gui = tk.Tk()
    gui.configure(bg="#2b2d30")
    gui.geometry("800x600")
    gui.title("Weather Flower GUI")

    frame = tk.Frame(gui, padx=10, pady=10, bg="#4d5056")
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    frame.columnconfigure(0, weight=8)
    frame.columnconfigure(1, weight=3)
    frame.columnconfigure(2, weight=5)
    frame.rowconfigure(0, weight=15)
    frame.rowconfigure(1, weight=15)
    frame.rowconfigure(2, weight=15)
    frame.rowconfigure(3, weight=55)

    img_block = tk.Frame(frame, padx=5, pady=5)
    img_block.grid(row=0, rowspan=45, column=0)

    # img = ImageTk.PhotoImage(Image.open("Fleur_Climat.png"))
    # display = tk.Label(img_block, image = img)
    # display.pack(side="bottom", fill="both", expand = "yes")

    title = tk.Label(frame, text="Fleur du temps")
    title.grid(row=0, column=1, columnspan=2)

    position = "(1, -1)"
    current_pos = tk.Label(frame, text=position)
    current_pos.grid(row=1, column=1, columnspan=2)

    return_button = tk.Button(frame, text="back")
    return_button.grid(row=2, column=1)

    next_button = tk.Button(frame, text="next")
    next_button.grid(row=2, column=2)

    description = ("Le vent se lève et des rafales de vents glaciales s'abattent sur le groupe, des gerbes de neige "
                   "sont soulevés des conggères et se mélangent aux nombreux flocons tombant du ciel. Il devient "
                   "difficile de voir devant soi, et vous arrivez à peine à entendre ce qui se passe autour de vous. "
                   "Un blizzard s'est levé.")
    text_description = tk.Label(frame, text=description, justify="left", wraplength=300)
    text_description.grid(row=3, column=0)

    effect = ("* Le blizzard dure 2d4 heures,* Vision réduite à 9m,* Audition réduite à 30m,* Désavantage aux "
              "jets de perception basé sur la vue ou l'ouïe,* Les flammes s'éteignent immédiatement,* Les traces "
              "dans la neige sont effacées,* Le brouillard se disperse,* Le vol non magique est impossible,\n* "
              "Concentration DC pour ne pas perdre sa concentration")
    text_effect = tk.Label(frame, text=effect, justify="left", wraplength=300)
    text_effect.grid(row=3, column=1, columnspan=2)

    # -------------------

    # frame.columnconfigure(0, weight=1)
    # frame.columnconfigure(1, weight=1)
    # frame.columnconfigure(2, weight=1)
    #
    # label = tk.Label(frame, text="Salut", font=("Calibri", 18))
    # label.grid(row=0, column=0, sticky=tk.W)
    #
    # button = tk.Button(frame, text="New Weather", font=("Calibri", 12))
    # button.grid(row=0, column=1)
    #
    # checkbutton = tk.Checkbutton(frame, text="Hey", font=("Calibri", 12), fg="pink", bg="#282828")
    # checkbutton.grid(row=0, column=2)
    #

    gui.mainloop()


if __name__ == '__main__':
    main()
