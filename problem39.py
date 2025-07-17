# import random
# def game():
#     print("You are playing the game")
#     score = random.randint(1,62)
    

#     with open("highscore.txt","r") as file:
#         content = file.read()
#         if(highscore != ""):
#             highscore = int(highscore)
#         else:
#             highscore = 0

#     print(f"Your score is {score}")
#     if(score>highscore):
#         with open("highscore.txt","w") as file:
#             file.write(str(score))
#             return score
#        game() 



import random

def game():
    print("You are playing the game")
    score = random.randint(1, 62)

    try:
        with open("highscore.txt", "r") as file:
            content = file.read()
            highscore = int(content) if content.strip() != "" else 0
    except FileNotFoundError:
        highscore = 0

    print(f"Your score is {score}")
    if score > highscore:
        print("🎉 New high score!")
        with open("highscore.txt", "w") as file:
            file.write(str(score))
    else:
        print(f"🏆 High score remains {highscore}")

# Start the game
game()