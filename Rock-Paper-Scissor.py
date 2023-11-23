from tkinter import *
import random
from PIL import Image, ImageTk
background_color = "#83A2FF"


def play_game(user_choice, p_score, c_score):
    img = [rock_image, paper_image, scissor_image]
    choose = random.choice(img)
    # rock_button.grid(row=1, column=0)
    if (user_choice == rock_image and choose == rock_image) or (user_choice == paper_image and choose == paper_image) or (user_choice == scissor_image and choose == scissor_image):
        player_score = Label(
            Window, text=f"Player:{p_score}", font=("Ariel", 20, "bold"))
        player_score.grid(row=0, column=0)

        computer_score = Label(
            Window, text=f"Computer:{c_score}", font=("Ariel", 20, "bold"))
        computer_score.grid(row=0, column=4, padx=100)

        image = Label(Window, image=choose)
        image.grid(row=1, column=4, padx=100)

        output = Label(
            Window, text=f"It's draw", font=("Ariel", 20, "bold"))
        output.grid(row=1, column=5, padx=20)

    if (user_choice == rock_image and choose == scissor_image) or (user_choice == scissor_image and choose == paper_image) or (user_choice == paper_image and choose == rock_image):
        p_score += 1
        player_score = Label(
            Window, text=f"Player:{p_score}", font=("Ariel", 20, "bold"))
        player_score.grid(row=0, column=0)

        computer_score = Label(
            Window, text=f"Computer:{c_score}", font=("Ariel", 20, "bold"))
        computer_score.grid(row=0, column=4, padx=100)

        image = Label(Window, image=choose)
        image.grid(row=1, column=4, padx=100)

        output = Label(
            Window, text=f"You won!", font=("Ariel", 20, "bold"))
        output.grid(row=1, column=5, padx=20)

    if (user_choice == rock_image and choose == paper_image) or (user_choice == scissor_image and choose == rock_image) or (user_choice == paper_image and choose == scissor_image):
        c_score += 1
        player_score = Label(
            Window, text=f"Player:{p_score}", font=("Ariel", 20, "bold"))
        player_score.grid(row=0, column=0)

        computer_score = Label(
            Window, text=f"Computer:{c_score}", font=("Ariel", 20, "bold"))
        computer_score.grid(row=0, column=4, padx=100)

        image = Label(Window, image=choose)
        image.grid(row=1, column=4, padx=100)

        output = Label(
            Window, text=f"You lose!", font=("Ariel", 20, "bold"))
        output.grid(row=1, column=5, padx=20)


Window = Tk()
Window.title("Rock Paper Scissor")
Window.config(padx=50, pady=50, bg=background_color)

p_score = 0
c_score = 0
canvas = Canvas(width=300, height=400)
rock_image = PhotoImage(
    file="Task 3/img/raise-hand.png")

paper_image = PhotoImage(
    file="Task 3/img/hand-paper.png")

scissor_image = PhotoImage(
    file="Task 3/img/scissors.png")

rock_button = Button(image=rock_image, width=200, height=150,
                     command=lambda: play_game(rock_image, p_score, c_score))
canvas.create_image(150, 207, image=rock_image)
rock_button.grid(row=1, column=0, pady=20)

paper_button = Button(image=paper_image, width=200,
                      height=150, command=lambda: play_game(paper_image, p_score, c_score))
canvas.create_image(50, 70, image=paper_image)
paper_button.grid(row=2, column=0, pady=20)

scissor_button = Button(image=scissor_image, width=200,
                        height=150, command=lambda: play_game(scissor_image, p_score, c_score))
canvas.create_image(50, 70, image=scissor_image)
scissor_button.grid(row=3, column=0, pady=20)

player_score = Label(
    Window, text=f"Player:{p_score}", font=("Ariel", 20, "bold"))
player_score.grid(row=0, column=0)

computer_score = Label(
    Window, text=f"Computer:{c_score}", font=("Ariel", 20, "bold"))
computer_score.grid(row=0, column=4, padx=100)


Window.mainloop()
