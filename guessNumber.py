import random

def _game():
	start = int(input('Enter starting range:'))
	end = int(input('Enter starting range:'))
	initialized_num = random.randint(start,end)
	user_input = int(input('Guess the number:'))
	if user_input == initialized_num:
		return 'You win the game!'
	else:
		return 'You lose the game.'
		
#print(end_game())

def initialize_game():
	initialized_num = random.randint(1,100)
	for i in range(1,6):
		print(f'Attempt {i}-')
		user_input = int(input('Guess the number:'))
		
		if user_input == initialized_num:
			return f'Rewarded rs.{n-i}'
		elif (user_input-initialized_num)<10:
			print('Number is too small.')
		elif (user_input-initialized_num)<50:
			print("NUmber is small.")
	else:
		return 'Sorry, you lose the game.'
		
print(initialize_game())
