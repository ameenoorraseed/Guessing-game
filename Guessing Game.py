import random

cpu = ['77','adfdgrdt','@#$#$#'] # list of strings

# number or letter or symbol
# guess what computer has

while True: # main loop
	print(''':::'###:::'##::::'##'########'########'##::: ##:'#######::'#######:'########:::'########::::'###::::'######:'########'########'########::
::'## ##:::###::'###:##.....::##.....::###:: ##'##.... ##'##.... ##:##.... ##:::##.... ##::'## ##::'##... ##:##.....::##.....::##.... ##:
:'##:. ##::####'####:##:::::::##:::::::####: ##:##:::: ##:##:::: ##:##:::: ##:::##:::: ##:'##:. ##::##:::..::##:::::::##:::::::##:::: ##:
'##:::. ##:## ### ##:######:::######:::## ## ##:##:::: ##:##:::: ##:########::::########:'##:::. ##. ######::######:::######:::##:::: ##:
 #########:##. #: ##:##...::::##...::::##. ####:##:::: ##:##:::: ##:##.. ##:::::##.. ##:::#########:..... ##:##...::::##...::::##:::: ##:
 ##.... ##:##:.:: ##:##:::::::##:::::::##:. ###:##:::: ##:##:::: ##:##::. ##::::##::. ##::##.... ##'##::: ##:##:::::::##:::::::##:::: ##:
 ##:::: ##:##:::: ##:########:########:##::. ##. #######:. #######::##:::. ##:::##:::. ##:##:::: ##. ######::########:########:########::
..:::::..:..:::::..:........:........:..::::..::.......:::.......::..:::::..:::..:::::..:..:::::..::......::........:........:........:::'''
                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                           
		)
	choice = int(input("1. play\n2. exit\nenter your choice: "))

	if choice == 1:
		print('Game starts now!!')
		score = 0
		life = 3
		while True:
			cpu_guess = random.choice(cpu)
			user_choice = int(input('1. Letter\n2. Number\n3. Symbol\nEnter your guess: '))
			
			if cpu_guess.isalpha() and user_choice == 1:
				score += 1
				print('you guessed correctly')
			elif cpu_guess.isdigit() and user_choice == 2:
				score += 1
				print('you guessed correctly')
			elif not cpu_guess.isalnum() and user_choice == 3:
				score += 1
				print('you guessed correctly')

			else:
				if life == 0:
					print('you are out!!!!')
					print('your score is', score)
					break
				else:
					life = life - 1
					print('remaining',life)

	elif choice == 2:
		print('good day to you')
		break
	else:
		print('\n')
		print('~'*20)
		print('invalid choice')
		print('^'*20,'\n')


# Guess correctly score ince
# out
