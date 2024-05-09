import random
def input_user():
    user_input=input("Enter rock/paper/scissors:")
    while user_input not in ['rock','paper','scissor']:
        print("ERROR!! PLEASE ENTER ROCK/PAPER/SCISSOR!!!")
        user_input=input("Enter rock/paper/scissor:")
    return user_input 
def comput_input():
    return random.choice(["rock","paper","scissor"])
def win(user,computer):
    if user==computer:
        return "tie"
    elif(user=="rock" and computer=="paper") or (user=="paper" and computer=="scissor") or (user=="scisssor" and computer=="rock"):
        return "computer wins" 
    else:
        return "user wins"        
         
         
def game():
    print("let's play ROCK/PAPER/SCISSOR!!")
    user_input=input_user()
    computer_choice=comput_input()
    print("user=",{user_input})
    print("computer",{computer_choice})
    result=win(user_input,computer_choice)
    print(result)
game()


         
         
         
         
         
         
         
         
         
         
         
  

  