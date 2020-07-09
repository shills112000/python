#!/usr/local/bin/python3.7

#https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming

#while True:
#  print ("Looping")

count = 1
while count <=4:
    print (f"counting : {count}")
    count += 1


count =0
while count < 10:
    if count % 2 == 0:# miss even numbers
        count +=1
        continue
    print (f"were counting odd numbers: {count}")
    count += 1
    count += 1


count = 1
while count < 10:
    if count % 2 == 0:
        break
    print (f"We are counting odd numbers {count}")
    count += 1
