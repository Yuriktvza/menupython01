import time
print ("\n\t\t--------Choose your destiny !! --------")
print(" ______   ____    ___  ____________ ")
print(" |  __ \ / __ \| |  | |  _ \__   __|")
print(" | |  | | |  | | |  | | |_) | | |   ")
print(" | |  | | |  | | |  | |  _ <  | | ")
print(" | |__| | |__| | |__| | |_) | | |  ") 
print(" |_____/ \____/ \____/|____/  |_|")
for i in range(1,5):
	print("\t\tWELCOME TO DOUBT")
	time.sleep(1)
def xmenu():
	print("\n1-Colors")
	print("2-ASCII")
	print("3-Binary")
	print("4-Hexa")
	print("5-Exit")
	while True:
		try:
			select = int(input("\n Choose the number:"))
			if select==1:
				first()
				break
			elif select==2:
				second()
				break
			elif select==3:
				third()
				break
			elif select==4:
				foour()
				break
			elif select==5:
				exiit()
			else:
				print("\t\nInvalid - Choose 1-5")
				xmenu()
		except ValueError:
			print("\t\nInvalid choice - Chosse 1-5")
	exit
def first():
	print("\t\nMath Operations > ")
	keyboard=input("\nPress ENTER to respect :")
	xmenu()
def second():
	print("\n OKAY 2")
	keyboard=input("\nPress ENTER to respect :")
	xmenu()
def third():
	print("\nOKAY 3")
	keyboard=input("\nPress ENTER to respect :")
	xmenu()
def foour():
	print("\nOKAY 4")
	keyboard=input("\nPress ENTER to respect :")
	xmenu()	
xmenu()
