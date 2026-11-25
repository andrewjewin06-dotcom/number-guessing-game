# Day 72 practice
import random
from datetime import datetime
import json
def play_game(max_attempts,num):
    i=0
    while i<max_attempts:
        try:
            number=int(input("enter a number:"))
        except ValueError:
            print("enter number not letters!")
            continue
        i+=1
        if number==num:
            return True
        if number>num:
            print("too high")
        else:
            print("too low")
    return False
secret=random.randint(1,10)
won=play_game(5,secret)
if won:
    print("you won!")
else:
    print("you lost.number was",secret)
game_result={"date":datetime.now().strftime("%d-%m-%Y %H:%M"),
    "won":won,
    "secret":secret}
def load_history():
    try:
        with open("game_result.json","r") as file:
            return json.load(file)
    except (ValueError,FileNotFoundError):
        return []
def save_history(history):
    with open("game_result.json","w") as file:
        json.dump(history,file)
history=load_history()
history.append(game_result)
save_history(history)
total_result=load_history()
for serial_num,result in enumerate(total_result,start=1):
    print(serial_num,".",result)