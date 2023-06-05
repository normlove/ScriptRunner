import tkinter as tk
from tkinter import ttk
from random import randint


class DiceRollerGUI:
    def __init__(self):
        self.dice = []  # List to store the dice
        self.total = 0  # Variable to store the total sum
        self.roll_results = []  # List to store individual roll results

        self.root = tk.Tk()
        self.root.title("Dice Roller")

        # Create GUI elements
        self.frame_dice = tk.Frame(self.root)
        self.frame_dice.pack()

        self.label_total = tk.Label(self.root, text="Total: 0", font=("Arial", 24))
        self.label_total.pack()

        self.label_large_total = tk.Label(self.root, text="0", font=("Arial", 72), pady=20)
        self.label_large_total.pack()

        self.frame_rolls = tk.Frame(self.root)
        self.frame_rolls.pack()

        self.label_rolls = tk.Label(self.frame_rolls, text="Rolls: ")
        self.label_rolls.pack(side=tk.LEFT)

        self.button_roll = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.button_roll.pack()

        self.button_add_dice = tk.Button(self.root, text="Add Dice", command=self.add_dice)
        self.button_add_dice.pack()

        self.button_remove_dice = tk.Button(self.root, text="Remove Dice", command=self.remove_dice)
        self.button_remove_dice.pack()

        self.label_add = tk.Label(self.root, text="Add: ")
        self.label_add.pack()

        self.add_value = tk.StringVar()
        self.add_value.set("0")
        self.dropdown_add = ttk.Combobox(self.root, textvariable=self.add_value, values=list(range(1, 101)))
        self.dropdown_add.pack()

        self.button_add = tk.Button(self.root, text="Add", command=self.add_value_to_total)
        self.button_add.pack()

    def add_dice(self):
        # Create a new dice widget
        dice_widget = tk.Scale(self.frame_dice, from_=1, to=20, orient=tk.HORIZONTAL, length=200)
        dice_widget.pack()

        self.dice.append(dice_widget)

    def remove_dice(self):
        if self.dice:
            dice_widget = self.dice.pop()
            dice_widget.pack_forget()

    def roll_dice(self):
        self.total = 0
        self.roll_results.clear()

        for dice_widget in self.dice:
            sides = dice_widget.get()
            roll = randint(1, sides)
            self.total += roll
            self.roll_results.append(roll)

        self.label_total.config(text="Total: {}".format(self.total))
        self.label_large_total.config(text=self.total)
        self.update_roll_results()

    def add_value_to_total(self):
        value = int(self.add_value.get())
        self.total += value
        self.label_total.config(text="Total: {}".format(self.total))
        self.label_large_total.config(text=self.total)

    def update_roll_results(self):
        rolls_text = "Rolls: "
        for i, roll in enumerate(self.roll_results):
            rolls_text += str(roll)
            if i < len(self.roll_results) - 1:
                rolls_text += ", "
        self.label_rolls.config(text=rolls_text)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    dice_roller = DiceRollerGUI()
    dice_roller.run()
