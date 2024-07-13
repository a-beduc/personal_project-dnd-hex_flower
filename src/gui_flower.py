import ast
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from class_hex_flower import HexGrid, random_move


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(background="#2b2d30")
        self.root.geometry("800x650")
        self.root.title("Hex Flower")
        self.root.resizable(False, False)

        self.frame = tk.Frame(self.root, padx=10, pady=10, bg="white")
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.configure_grid(self.frame)

        self.hex_grid = HexGrid(init_file="weather_flower.json")

        self.img_tk = None
        self.title = None
        self.current_pos = None
        self.combo = None
        self.current_duration = None
        self.current_sight = None
        self.current_earing = None
        self.current_ranged_attack = None
        self.current_flame = None
        self.current_flight = None
        self.current_dc = None
        self.current_tiredness = None
        self.current_temporary_hp = None
        self.description = None

        self.create_widgets()
        self.update_position_label()

    @staticmethod
    def configure_grid(frame):
        for col in range(4):
            frame.columnconfigure(col, weight=1)
        for row in range(13):
            frame.rowconfigure(row, weight=1, minsize=47)
        frame.rowconfigure(13, weight=1, minsize=10)

    def create_widgets(self):
        img_bloc = tk.Frame(self.frame, padx=5, pady=5)
        img_bloc.grid(row=0, rowspan=9, column=0, sticky="nw")

        self.canvas = tk.Canvas(img_bloc, width=400, height=400)
        self.canvas.pack()

        base_img = Image.open("Fleur_Climat_cleaned-coord.png")
        base_img.thumbnail((400, 400), Image.Resampling.LANCZOS)
        self.base_img_tk = ImageTk.PhotoImage(base_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.base_img_tk)

        dot = Image.open("dot.png")
        dot.thumbnail((8, 8), Image.Resampling.LANCZOS)
        self.dot_tk = ImageTk.PhotoImage(dot)
        self.dot_id = self.canvas.create_image(200, 130, anchor=tk.CENTER, image=self.dot_tk)

        self.title = tk.Label(self.frame, text="Fleur du temps")
        self.title.grid(row=0, column=1, columnspan=3, sticky="nsew")

        self.current_pos = tk.Label(self.frame, text="")
        self.current_pos.grid(row=1, column=1, sticky="nsew")

        forced_position = ["(2, 0)", "(1, -1)", "(2, 1)", "(0, -2)", "(1, 0)",
                           "(2, 2)", "(0, -1)", "(1, 1)", "(-1, -2)", "(0, 0)",
                           "(1, 2)", "(-1, -1)", "(0, 1)", "(-2, -2)", "(-1, 0)",
                           "(0, 2)", "(-2, -1)", "(-1, 1)", "(-2, 0)"]

        self.combo = ttk.Combobox(self.frame, values=forced_position)
        self.combo.grid(row=1, column=2, sticky="nsew")

        go_button = tk.Button(self.frame, text="go", command=self.go_action)
        go_button.grid(row=1, column=3, sticky="nsew")

        return_button = tk.Button(self.frame, text="back", command=self.back_action)
        return_button.grid(row=2, column=1, sticky="nsew")

        next_button = tk.Button(self.frame, text="next", command=self.next_action)
        next_button.grid(row=2, column=2, columnspan=2, sticky="nsew")

        effect_title = tk.Label(self.frame, text="Liste des effets")
        effect_title.grid(row=3, column=1, columnspan=3, sticky="nsew")

        effect_duration = tk.Label(self.frame, text="Durée :")
        effect_duration.grid(row=4, column=1, sticky="nsew")

        self.current_duration = tk.Label(self.frame, text="")
        self.current_duration.grid(row=4, column=2, columnspan=2, sticky="nsew")

        effect_sight = tk.Label(self.frame, text="Vue :")
        effect_sight.grid(row=5, column=1, sticky="nsew")

        self.current_sight = tk.Label(self.frame, text="")
        self.current_sight.grid(row=5, column=2, columnspan=2, sticky="nsew")

        effect_earing = tk.Label(self.frame, text="Audition :")
        effect_earing.grid(row=6, column=1, sticky="nsew")

        self.current_earing = tk.Label(self.frame, text="")
        self.current_earing.grid(row=6, column=2, columnspan=2, sticky="nsew")

        effect_ranged_attack = tk.Label(self.frame, text="Attaque à distance :")
        effect_ranged_attack.grid(row=7, column=1, sticky="nsew")

        self.current_ranged_attack = tk.Label(self.frame, text="")
        self.current_ranged_attack.grid(row=7, column=2, columnspan=2, sticky="nsew")

        effect_flame = tk.Label(self.frame, text="Flame :")
        effect_flame.grid(row=8, column=1, sticky="nsew")

        self.current_flame = tk.Label(self.frame, text="")
        self.current_flame.grid(row=8, column=2, columnspan=2, sticky="nsew")

        effect_flight = tk.Label(self.frame, text="Vol :")
        effect_flight.grid(row=9, column=1, sticky="nsew")

        self.current_flight = tk.Label(self.frame, text="")
        self.current_flight.grid(row=9, column=2, columnspan=2, sticky="nsew")

        effect_dc = tk.Label(self.frame, text="DC :")
        effect_dc.grid(row=10, column=1, sticky="nsew")

        self.current_dc = tk.Label(self.frame, text="")
        self.current_dc.grid(row=10, column=2, columnspan=2, sticky="nsew")

        effect_tiredness = tk.Label(self.frame, text="Épuisement :")
        effect_tiredness.grid(row=11, column=1, sticky="nsew")

        self.current_tiredness = tk.Label(self.frame, text="")
        self.current_tiredness.grid(row=11, column=2, columnspan=2, sticky="nsew")

        effect_temporary_hp = tk.Label(self.frame, text="PdV Temp :")
        effect_temporary_hp.grid(row=12, column=1, sticky="nsew")

        self.current_temporary_hp = tk.Label(self.frame, text="")
        self.current_temporary_hp.grid(row=12, column=2, columnspan=2, sticky="nsew")

        self.description = tk.Label(self.frame, text="", justify="left", wraplength=300)
        self.description.grid(row=9, rowspan=4, column=0, sticky="nsew")

    def update_position_label(self, direction=""):
        self.current_pos.config(text=direction + " " + str(self.hex_grid.current_position))
        hex_tile=self.hex_grid.get_hex(self.hex_grid.current_position)
        self.title.config(text=str(hex_tile.title))
        self.current_duration.config(text=str(hex_tile.effect.duration))
        self.current_sight.config(text=str(hex_tile.effect.sight))
        self.current_earing.config(text=str(hex_tile.effect.earing))
        self.current_ranged_attack.config(
            text=str(hex_tile.effect.ranged_attack))
        self.current_flame.config(text=str(hex_tile.effect.flame))
        self.current_flight.config(text=str(hex_tile.effect.flight))
        self.current_dc.config(text=str(hex_tile.effect.dc_concentration))
        self.current_tiredness.config(text=str(hex_tile.effect.tiredness))
        self.current_temporary_hp.config(
            text=str(hex_tile.effect.temporary_hp))
        self.description.config(text=str(hex_tile.description))

        self.canvas.coords(self.dot_id, hex_tile.small_image_coords[0], hex_tile.small_image_coords[1])

    def go_action(self):
        selected_value = self.combo.get()
        if selected_value:
            selected_position = ast.literal_eval(selected_value)
            self.hex_grid.forced_position(selected_position)
            self.update_position_label("")

    def back_action(self):
        self.hex_grid.move_previous_position()
        self.update_position_label("")

    def next_action(self):
        direction = random_move()
        self.hex_grid.move_current_position(direction)
        self.update_position_label(direction)




def main():
    root = tk.Tk()
    GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
