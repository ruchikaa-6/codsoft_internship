import random
characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            '#','!','$','@','/','0','9','8','7','6','5','4','3','2','1']
length=int(input("Enter the length of password:"))
password=""
for i in range(0,length):
     char=random.choice(characters)
     password+=char
print("PASSWORD :- ",password)
