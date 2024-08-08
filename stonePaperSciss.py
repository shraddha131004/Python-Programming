import random
item_list = ["Stone", "Paper" ,"Scissor"]
user_choice = input("Enter you move = (Stone,Paper,Scissor) = ")
comp_choice = random.choice(item_list)
print(f"User's choice = {user_choice},Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Tie")
    
elif user_choice == "Stone":
    if comp_choice == "Paper":
        print("Computer wins.")
    else:
        print("User wins.")
        
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Computer wins.")
    else:
        print("User wins.")
        
elif user_choice == "Scissor":
    if comp_choice == "Stone":
        print("computer wins.")
    else:
        print("User wins.")
        