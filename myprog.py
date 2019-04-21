import datetime


CurrentDT = datetime.datetime.now()



while True: 
	try:	
		arg1 = input ("Enter a number: ")
		a=float(arg1) 
	except:
		print("You did not enter a number. Please be sure to enter one number at a time. e.g. 1 or 2 ") 
	else: 
		break
		
while True:
	try: 
		arg2 = input ("Enter a number: ")
		b=float(arg2) 
	except:
		print("You did not enter a number. Please be sure to enter one number at a time. e.g. 1 or 2 ") 
	else:
		break 
		
while True: 
	try:
		arg3 = input ("Enter a number: ") 
		c=float(arg3) 
	except:
		print("You did not enter a number. Please be sure to enter one number at a time. e.g. 1 or 2 ") 
	else:
		break

	
def getHighNumber (a,b,c):
	highNumber = 0
	if (a>=b) and (a>=c):
		highNumber = a
	elif (b>=a) and (b>=c): 
		highNumber = b 
	elif (c>=a) and (c>=b): 
		highNumber = c 
		
	return highNumber

def getLowNumber (a,b,c):
	lowNumber = 0
	if (a<=b) and (a<=c): 
		lowNumber = a 
	elif (b<=a) and (b<=c):
		lowNumber = b 	
	elif (c<=a) and (c<=b):
		lowNumber = c 
		
	
	
	
	
	return lowNumber 
		
highNumber = getHighNumber(a,b,c)  
lowNumber = getLowNumber (a,b,c)  

str(highNumber) 
str(lowNumber) 
print ("======================================") 
print ("High Number:" + str(highNumber)) 
print ("Low Number:" + str(lowNumber))  
print (str(CurrentDT))
print ("======================================") 
