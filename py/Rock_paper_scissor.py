import random

system_message = """Enter a Input: 
                    Rock: 1                
                    Paper: 2
                    Scissor: 3
Your Input (1-3) :  """

playing_objects = [
    "Rock", "Paper", "Scissor"
]  # storing in a list/ array formate for showing in easy way during per play

status = ""  # update and Store status of per game
user_points = 0
system_points = 0

play_times = 3  ## system have defined 3 time of play
while play_times > 0:

    system_choice = random.randint(1, 3)
    user_input = int(input(system_message))

    if (system_choice == user_input):
        play_times = play_times + 1
        status = "Draw"
        print(
            f"{status}.System picked {system_choice} and you picked {playing_objects[system_choice-1]}. System Point: {playing_objects[system_choice-1]}, your point : {user_points}"
        )

    elif (system_choice == 1 and user_input == 2):
        user_points = user_points + 1
        status = "You won"
        print(
            f"{status}. System picked {playing_objects[0]} and you picked {playing_objects[1]}. System Point: {system_points}, your point : {user_points}"
        )

    elif (system_choice == 1 and user_input == 3):
        system_points = system_points + 1
        status = "System won"
        print(
            f"{status}. System picked {playing_objects[0]} and you picked {playing_objects[2]}. System Point: {system_points}, your point : {user_points}"
        )

    elif (system_choice == 2 and user_input == 1):
        system_points = system_points + 1  ## if draw stating rise to 1 for , in last itaration line update it will decrese 1 times. Only balance perpose
        status = "System won"
        print(
            f"{status}. System picked {playing_objects[1]} and you picked {playing_objects[0]}. System Point: {system_points}, your point : {user_points}"
        )

    elif (system_choice == 2 and user_input == 3):
        user_points = user_points + 1
        status = "You won"
        print(
            f"{status}. System picked {playing_objects[1]} and you picked {playing_objects[2]}. System Point: {system_points}, your point : {user_points}"
        )

    elif (system_choice == 3 and user_input == 1):
        user_points = user_points + 1
        status = "You won"
        print(
            f"{status}. System picked {playing_objects[2]} and you picked {playing_objects[0]}. System Point:             {system_points}, your point : {user_points}"
        )

    elif (system_choice == 3 and user_input == 2):
        system_points = system_points + 1
        status = "System won"
        print(
            f"{status}. System picked {playing_objects[2]} and you picked {playing_objects[1]}. System Point: {system_points}, your point : {user_points}"
        )

    play_times = play_times - 1  ## reversing chances

verdict = ""  # store final output

if (system_points > user_points):
    verdict += f"""POINT TABLE 
                System      : {system_points}
                UserPoint   : {user_points} 
                
                Final Result: Loose :') """
else:
    verdict += f"""POINT TABLE 
                System      : {system_points}
                UserPoint   : {user_points} 
                
                Final Result: Winner!"""

print(verdict)
