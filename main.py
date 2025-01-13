from tkinter import *
from tkinter import messagebox
import random
import os
import logic


class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        self.root.geometry("500x400")
        self.root.configure(background="lightblue")
        self.game_id = logic.get_game_id()  # Retrieve a new game ID

        # Initialize game variables
        self.die1 = 0
        self.die2 = 0
        self.score = 0
        self.game_point = 0  # Consolidate to this variable
        self.WAGER = 100
        self.wager = 100
        self.win = 0
        self.comeout = 0
        self.odds = [6, 8]

        # Load dice images and setup UI
        self.dice_images = self.load_dice_images()
        self.create_menu()
        self.create_widgets()

    @staticmethod
    def load_dice_images():
        """Load dice images into a dictionary."""
        images = {}
        for i in range(1, 7):
            images[i] = PhotoImage(file=os.path.join("images", f"dice-{i}.png"))
        return images

    def create_menu(self):
        """Create a File menu with New Game and Exit options."""
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New Game", command=self.reset_game)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def create_widgets(self):
        """Create and place widgets in the UI."""
        # Insert logo
        self.logo_image = PhotoImage(file="images/dice_W_gold.png")
        self.logo_label = Label(self.root, image=self.logo_image, bg="lightblue")
        self.logo_label.place(x=280, y=25)

        # Labels for game info
        self.game_id_label = Label(self.root, text=f"Game ID: {self.game_id}", bg="lightblue", font=("Arial", 12))
        self.game_id_label.place(x=10, y=10)

        self.score_label = Label(self.root, text="Score: 0", bg="lightblue", font=("Arial", 12))
        self.score_label.place(x=10, y=50)

        self.game_point_label = Label(self.root, text="Game Point: 0", bg="lightblue", font=("Arial", 12))
        self.game_point_label.place(x=10, y=90)

        # Dice images and labels
        self.dice1_label = Label(self.root, bg="lightblue")
        self.dice1_label.place(x=150, y=150)

        self.dice2_label = Label(self.root, bg="lightblue")
        self.dice2_label.place(x=300, y=150)

        # Wager label
        self.wager_label = Label(self.root, text=f"Wager: ${self.wager}", font=("Arial", 11), bg="lightblue")
        self.wager_label.place(x=10, y=150)

        # Roll Dice button
        self.roll_button = Button(self.root, text="Roll Dice", command=self.roll_dice, bg="gold", font=("Arial", 12))
        self.roll_button.place(x=200, y=300)

    def roll_dice(self):
        """Simulate rolling two dice and update the game state."""
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        self.score = self.die1 + self.die2

        # Update dice images
        self.dice1_label.config(image=self.dice_images[self.die1])
        self.dice2_label.config(image=self.dice_images[self.die2])

        # Update score label
        self.score_label.config(text=f"Score: {self.score}")

        if self.score in [7, 11]:  # Win case
            self.win = self.wager * 1.1
            logic.insert_into_games(self.game_id, self.wager, self.win, 0, self.score, self.game_point)
            self.wager_label.config(text=f"Win: ${self.win:.2f}")
            self.reset_game()
        elif self.score in [2, 3, 12]:  # Loss case
            logic.insert_into_games(self.game_id, self.wager, 0, self.wager, self.score, self.game_point)
            self.wager_label.config(text=f"Loss: ${self.wager}")
            self.reset_game()
        else:  # Set the game point
            self.game_point = self.score
            self.update_game_point_label()

    def update_game_point_label(self):
        """Update the Game Point label."""
        self.game_point_label.config(text=f"Game Point: {self.game_point}")

    def reset_game(self):
        """Reset the game state to start a new round."""
        self.die1 = 0
        self.die2 = 0
        self.score = 0
        self.game_point = 0  # Reset game point
        self.wager = self.WAGER
        self.score_label.config(text="Score: 0")
        self.update_game_point_label()  # Reset game point label
        self.dice1_label.config(image=None)
        self.dice2_label.config(image=None)
        self.wager_label.config(text=f"Wager: ${self.wager}")
        self.game_id = logic.get_game_id()  # Fetch a new Game ID
        self.game_id_label.config(text=f"Game ID: {self.game_id}")  # Update Game ID label


if __name__ == "__main__":
    root = Tk()
    app = DiceRollerApp(root)
    root.mainloop()
