sales = float(input("Enter sales :"))
bonus = 0
if  fee > 20000 :
    bonus = 200
else:
    bonus = 0
    print("Your Bonus : "+str(bonus ) ) 


 # Nested Decision Structure
salary = int(input("Enter your earning per year :"))
workexperience = float (input("Enter your work experience: "))

if salary > 60000:
 if workexperience >=5:
        print("You are eligibile for loan " )
 else :
        print ("Sorry your work experience is less than 5 years ")
else : 
        print ("Your earning is less than 60000")