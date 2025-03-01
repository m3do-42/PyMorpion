import tkinter
import tkinter.messagebox
from tkinter.messagebox import YESNO


def clear_board():
    global buttons, current_player, win

    buttons = []
    current_player = 'X'
    win = False

    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50), width=5, height=2,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            button.config(text="")  # Clear button text
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)



def print_winner():
    global win

    if win is False:
        win = True
        reponse = tkinter.messagebox.askquestion(title="Victoire !!!", message = "Le joueur " + current_player + " a gagné, Voulez vous faire une autre partie ??", icon='question', type=YESNO)
        if reponse == 'yes':
            clear_board()
            win = False  # Reset win flag
        else:
            root.quit()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'


def check_win(clicked_row, clicked_col):

    # detecter victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # detecter victoire verticale
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # detecter victoire diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # detecter victoire diagonale inversee
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == 'X' or current_button['text'] == '0':
                    count += 1
        if count == 9:
            reponse = tkinter.messagebox.askquestion(title="Victoire !!!",
                                                     message="Il y a match NULL, Voulez vous faire une autre partie ??",
                                                     icon='question', type=YESNO)
            if reponse == 'yes':
                clear_board()
            else:
                root.quit()


def place_symbol(row, column):

    clicked_button = buttons[column][row]
    if clicked_button['text'] == "":
        clicked_button.config(text=current_player)

        check_win(row, column)
        switch_player()


def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50),
                width=5, height=2,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)


# stockages
buttons = []
current_player = 'X'
win = False

# creer la fenetre du jeu
root = tkinter.Tk()

# personnalisation de la fenetre
root.title("TicTacToe")
root.minsize(500, 500)

draw_grid()
root.mainloop()