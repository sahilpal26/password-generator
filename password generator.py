#python program to generator password
import random
maximum_length=int(input("enter the number of caharcters you want in password:"))
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
locase_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
  
upcase_character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
  
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  '*', '(', ')', '<'] 
combined=digits+locase_character+upcase_character+symbols
password_random=[]

for x in range(0,maximum_length):
    y=random.choice(combined)
    password_random.append(y)
password_final=""
for x in password_random:
    password_final=password_final+x
print(password_final)


    
        




