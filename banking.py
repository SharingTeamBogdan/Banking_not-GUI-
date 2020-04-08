import time
import sys
import random
import Continue
from PIN_Gen import Gen
from Code_Ver import verify_code as ver
code=Gen()
file=open('PIN.txt','w')
file.write(code)
file.close()
bal=0
if(ver(code)==True):
	while(True):
		op=input()
		if(op=="CheckBalance"):
			time.sleep(1)
			print(f"Your balance is {bal} $")
			time.sleep(1)
			print(f"Checked {time.asctime()}")
			Continue.want_to_continue()
		if(op=="Deposit"):
			amount=int(input())
			bal+=amount
			time.sleep(1)
			print(f"You deposited {amount} $ succsessfully {time.asctime()}")
			Continue.want_to_continue()
		if(op=="Withdraw"):
			amount=int(input())
			if(bal-amount<0):
				time.sleep(1)
				print("Insufficient funds")
			else:
				time.sleep(1)
				print(f"You retrieved {amount} $ successfully {time.asctime()}")
			Continue.want_to_continue()
		if(op=="quit"):
			quit()
else:
	quit()

