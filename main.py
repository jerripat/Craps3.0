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
        self.game_id = logic.get_game_id()
        # Initialize game variables

        self.die1 = 0
        self.die2 = 0
        self.score = 0
        self.is_match = False
        self.GAME_POINT = 0  # Point to beat before the deadly 7
        self.wager = 100



        # Load dice images
        self.dice_images = self.load_dice_images()

        # Setup UI
        self.create_menu()  # Add the menu
        self.create_widgets()

    def load_dice_images(self):
        """Load dice images into a dictionary."""
        images = {}
        for i in range(1, 7):
            images[i] = PhotoImage(file=os.path.join("images", f"dice-{i}.png"))
        return images

    def create_menu(self):
        """Create a File menu with New Game and Exit options."""
        menu_bar = Menu(self.root)  # Create a menu bar

        # Create a File menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New Game", command=self.reset_game)  # New Game option
        file_menu.add_separator()  # Add a separator
        file_menu.add_command(label="Exit", command=self.root.quit)  # Exit option

        # Add the File menu to the menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Configure the root window to use the menu bar
        self.root.config(menu=menu_bar)

    def create_widgets(self):
        """Create and place widgets in the UI."""
        # Insert logo
        self.logo_image = PhotoImage(file="images/dice_W_gold.png")  # Store the image as an instance variable
        self.logo_label = Label(self.root, image=self.logo_image, bg="lightblue")  # Use the instance variable
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
        self.wager_label = Label(self.root, text=f"Wager: ${self.wager}", font=("Arial", 12), bg="lightblue")
        self.wager_label.place(x=10, y=150)

        # Roll Dice button
        self.roll_button = Button(self.root, text="Roll Dice", command=self.roll_dice, bg="gold", font=("Arial", 12))
        self.roll_button.place(x=200, y=300)

    def roll_dice(self):
        global wager
        """Simulate rolling two dice and update the game state."""
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        self.score = self.die1 + self.die2

        # Update the dice labels with the new images
        self.dice1_label.config(image=self.dice_images[self.die1])
        self.dice2_label.config(image=self.dice_images[self.die2])

        # Update the score label
        self.score_label.config(text=f"Score: {self.score}")

        # Check game rules
        if self.GAME_POINT == 0:  # Come-out roll
            if self.score in [7, 11]:
                #wager = wager * 1.10  # Increase wager by 10%
                logic.insert_into_games(self.game_id, self.wager, True, False, self.score)
                self.wager_label.config(text=f"Wager: ${self.wager:.2f}")  # Update wager label

                ans = messagebox.askyesno("Game Result", f"You hit the point! Play again?")
                if ans:
                    self.reset_game()
                else:
                    root.destroy()
            elif self.score in [2, 3, 12]:
                ans = messagebox.askyesno("Game Result", f"You hit the point! Play again?")
                if ans:
                    self.reset_game()
                else:
                    root.destroy()
            else:
                self.GAME_POINT = self.score
                self.game_point_label.config(text=f"Game Point: {self.GAME_POINT}")
        else:  # Point roll
            if self.score == self.GAME_POINT:
                self.wager_label.config(text=f"Wager: ${self.wager:.2f}")  # Update wager label
                ans = messagebox.askyesno("Game Result", f"You hit the point! Play again?")
                if ans:
                    self.reset_game()
                else:
                    root.destroy()
            elif self.score == 7:
                ans = messagebox.askyesno("Game Result", f"You hit the point! Play again?")
                if ans:
                    self.reset_game()
                else:
                    root.destroy()

    def reset_game(self):
        """Reset the game state to start a new round."""
        self.die1 = 0
        self.die2 = 0
        self.score = 0
        self.GAME_POINT = 0
        self.score_label.config(text="Score: 0")
        self.game_point_label.config(text="Game Point: 0")
        self.dice1_label.config(image=None)
        self.dice2_label.config(image=None)


if __name__ == "__main__":
    root = Tk()
    app = DiceRollerApp(root)
    root.mainloop()
