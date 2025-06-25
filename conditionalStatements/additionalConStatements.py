### to check if a given year is a leap year
##a =int(input("enter a year"))
##
##if a%4 ==0 and a%400 ==0:
##   print("the given year is a leap year")
##
##else:
##   print("the given year is not a leap year")
##   
##   
###to check if a number is in the given range
##a=int(input("enter any number"))
##if a>70 and a<100 :
##   print("the given number is in the range")
##
##else:
##   print("the given number is not in the range")
##   
### to find day of the week based on the number
##a=int(input("enter any number between 1 to 7"))
##if a==1:
##   print("Monday")
##   
##elif a==2:
##   print("tuesday")
##
##elif a==3:
##   print("wednesday")         
##
##elif a==4:
##   print("thursday")
##
##elif a==5:
##   print("friday")
##
##elif a==6:
##   print("saturday")
##
##else:
##   print("sunday")
##   
### to check if a given number is a two digit number
##a=int(input("enter a given number"))
##if (a>=10 and a<=99):
##    print("the given number is a two digit number")
##
##elif( a<=-10 and -99<=a):
##   print("the given number is a negative two digit number")
##
##else :
##    print("the given number is not a two digit number")
##    
##
###to compare if the given two strings are equal
##a=input("enter any string")
##b=input("enter any string")
##if a==b:
##   print("string a and b are equal")
##else:
##   print("string a and b are not equal")
##
##   
###to check if the given number is divisible by 2 or 7 or both or none
##a=int(input("enter your number"))
##if a%2==0 and a%7==0 :
##     print("the number is divisible by 2 and  7")
##
##elif a%2==0 :
##   print("the number is divisible by 2")
##
##elif a%7==0 :
##   print("the number is divisible by 7")
##

##
##else:
##     print("the number is not divisible by both 2 and 7")
##     
##### to check if a given string is empty or not
##a=input("enter any string")
##if a=="":
##   print("the given string is empty ")
##
##else :
##   print("the given string is non empty")
##   
### print if the given number is one or two digit 
##a=int(input("enter your number"))
##if a>=1 and a<=9 :
##   print("the given number is positive one digit" )
##elif a<=-1 and -9<=a:
##     print ("the given number is negative one digit")
##elif a>=10 and a<100 :
##    print("the number is  positive two digit ")
##elif a<=-10 and -99<=a:
##     print("the given number is negative two digit ")
##else :
##    print("the given number is more than two digits ")
##    
##    
### to find if the sum of two numbers is odd or even "   
##a=int(input("enter your number"))
##b=int(input("enter your number"))
##
##if a+b%2==0:
##   print("the given number is even")
##
##else :
##    print ("the sum of the numbers is odd")





### clothes based on temperature
##a=int(input( "enter the temperature "))
##
##if a<10 :
##     print("wear a coat ")
##elif a>=10 and a<=20 :
##      print("wear a jacket")
##elif a>=21 and a<=30 :
##      print("wear a t-shirt")
##else:
##      print("stay indoors ")
##
##determining quadrant based on coordinates
a=int(input( "enter  coordinates of x "))
b=int(input ("enter  coordinates of y"))
if a>0 and b>0 :
   print("the coordinates lie in quadrant 1")
elif a<0 and b>0:
   print("the coordinates lie in quadrant 2")
elif a<0 and b<0:       
   print("the coordinates lie in quadrant 3")
else:
   print("the coordinates lie in quadrant 4")
   
   



         
