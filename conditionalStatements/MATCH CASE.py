#1)###check if the number is odd or even:
##number=int(input("enter the number")
##match number %2==0:
##      case True :
##           print("the number is even")
##      case False :
##            print("the number is odd")
##                 
2##comparing two numbers and display the largest number
##num1=int(input("enter the number"))
##num2=int(input("enter the number"))
##match  num1>num2:
##         case True :
##             print("num1 is greater")
##             print(num1 )
##         case False :
##              print("num2 is greater")
##              print( num2 )

3## print the grade with the use of percentage             
##a=int(input("enter your percentage"))
##
##match a>90:
##   case True:
##      print("grade A")
##   case False:
##      match a>80:
##         case True:
##            print("grade B")
##         case False:
##            match a>70:
##               case True:
##                   print("grade c")
##               case False:
##                   match a<=70:
##                      case True:
##                       print("grade D")   
                         
                   
            
4#to determine the type of triangle based on side length
##l1 = int(input("enter the number"))
##l2 = int(input("enter the number"))
##l3 = int(input("enter the number"))
##match l1 ==l2 ==l3:
##           case True :
##               print ("the given triangle is equilateral ")
##           case False:
##                match l1==l2 or l2==l3 or l3==l1:
##                    case True :
##                        print ("the given triangle is isoceles triangle ")
##                    
##                    case False :
##                         print (" the given triangle is scalar triangle")

5#determine the season ,based on given month
##a=input("enter the input")
##match a =="december"or a== " january" or a== " february":
##    case True :
##        print("winter")
##    case False:
##        match a =="march"  or a=="april"  or a== "may":
##            case True :
##                print ("spring")
##            case False :
##                match   a=="june" or a== "july" or a== "august" :
##                    case True :
##                        print(" summer")
##                    case False:
##                        match a =="september" or a=="october" or a=="november":
##                            case True :
##                                print ("fall")
##                            case False :
##                                print("invalid")



6###to check if the given number is positive or negative
##a=int(input("enter your number"))
##match a>0:
##    case True :
##        print("positve")
##    case False:
##        match a==0:
##           case True:
##               print(" neither positive nor negative")
##           case False:
##                match a<0:
##                   case True:
##                      print("negative")



7###to compare the salary of three persons and print the minimum salary
##a=int(input("enter your salary "))
##b=int(input("enter your salary "))
##c=int(input("enter your salary "))
##match a<=b<=c:
##     case True:
##        print ("a has the minimum salary")
##     case False :
##         match b<=a<=c:
##             case True:
##                 print("b has the minimum salary")
##             case False:
##                  match c<=b<=a:
##                     case True:
##                         print("c has the minimum salary")

8#to check if a given year is a leap year
##
##a =int(input("enter a year"))
##
##match a%4 ==0 and a%400 ==0:
##    case True:
##         print("the given year is a leap year")
##    case False:
##          match a%4!=0:
##               case True:
##                   print("the given year is not a leap year ")
                   

9#####to check if a number is in the given range
##a=int(input("enter any number"))
##match a>70 and a<100:
##      case True:
##          print("the given number is in the range")
##      case False:    
##          print("the given number is not in the range")
  
               
10##### to find day of the week based on the number
##a=int(input("enter any number between 1 to 7:"))
##match a==1:
##    case True:
##        print("Monday")
##    case False:
##        match a==2:
##            case True:
##                 print("tuesday")   
##            case False:
##                match a==3:
##                   case True:
##                      print("wednesday")  
##                   case False:
##                       match a==4:
##                           case True:
##                               print("thursday")
##                           case False:
##                               match a==5:
##                                   case True:
##                                       print("friday")
##                                   case False:
##                                       match a==6:
##                                           case True:
##                                               print("Saturday")
##                                           case False:
##                                                match a==7:
##                                                    case True:
##                                                        print("sunday")
##                                                    case False:
##                                                        print("invalid")
                                                        
11###to check if a given number is a two digit number
##
##a=int(input("enter a given number"))
##match a>=10 and a<=99:
##      case True:
##          print("the given number is a two digit number")
##      case False:    
##           match a<=-10 and -99<=a:
##             case True:
##                 print("the given number is a negative two digit number")
##             case False:
##                 match a>=100 or a<=-100:
##                     case True:
##                         print("the given number is not a two digit number")

                                                        
12##to compare if the given two strings are equal
##a=input("enter any string")
##b=input("enter any string")
##match a==b:
##      case True:
##            print("both the strings a and b are equal")
##      case False:
##            print("both strings are not equal")


13###to check if the given number is divisible by 2 or 7 or both or none
##a=int(input("enter your number"))
##match a%2==0 and a%7==0:
##      case True:
##          print("the number is divisible by 2 and 7")
##      case False :
##             match a%2==0:
##                   case True:
##                       print("the number is divisible by 2")
##                   case False:
##                         match a%7==0:
##                               case True :
##                                    print("the number is divisible by 7")
##                               case False:
##                                     match a%2!=0 and a%7!=0:
##                                           case True:
##                                                print("the number is  not divisible by 2 and 7" )
##                                          
##                                                       
                                                       
                                                  
                                                
                                                 
14#####print if the given number is one or two digit 
##a=int(input("enter your number"))
##match a>=1 and a<=9:
##      case True:
##            print("the given number is positive one digit" )
##      case False:
##            match a<=-1 and -9<=a:
##                  case True:
##                       print ("the given number is negative one digit")
##                  case False:
##                        match a>=10 and a<100:
##                              case True:
##                                   print("the number is  positive two digit")
##                              case False:
##                                    match a<=-10 and -99<=a:
##                                          case True:
##                                               print("the given number is negative two digit")
##                                          case False:
##                                                 match a>=100 or -100<=a:
##                                                     case True:
##                                                           print("the given number is more than two digits")


##                                               
##                                                
            
            
   
##15#to find if the sum of two numbers is odd or even "   
##a=int(input("enter your number"))
##b=int(input("enter your number"))
##c=a+b
##match c%2==0:
##    case True:
##        print("the sum of the numbers is even")
##    case _:
##        print ("the sum of the numbers is odd")
        
        
                


16### to print if the given character is a vowel or consonant
##a=input("enter letter")
##match a=="a" or a=="e" or a=="i" or a=="o" or a=="u" or  a=="A" or a=="E" or a=="I" or a=="U" or a=="U":
##   case True:
##       print("vowel")
##   case False:
##       print("constant")



17# to check if a given string is empty or not
##a=input("enter any string")
##match a=="":
##   case True:
##     print("the given string is empty ")
##   case False:
##      print("the given string is non empty")
      
      

   
##18#to classify the person age group based on age input
##a=int(input("enter your age"))
##match a<=1:
##   case True:
##      print("baby")
##   case False:
##      match a<=5:
##         case True:
##            print("toddler")
##         case False:
##            match a<=10:
##               case True:
##                  print("kid")
##               case False:
##                match a<=18:
##                   case True:
##                       print("teen")
##                   case False:
##                      match a<=60:
##                         case True:
##                            print("adult")
##                         case False:
##                             match a>=61:
##                                case True:
##                                  print("senior")


                            
### clothes based on temperature
##a=int(input( "enter the temperature "))
##match a<10 :
##   case True:
##     print("wear a coat")
##   case False:
##     match a>=10 and a<=20:
##        case True:
##           print("wear a jacket")
##        case False:
##          match a>=21 and a<=30:
##             case True:
##               print("wear a t-shirt")
##             case False:
##               print("stay indoors ")



                 
##determining quadrant based on coordinates
##a=int(input( "enter  coordinates of x "))
##b=int(input ("enter  coordinates of y"))
##match a>0 and b>0:
##   case True:
##      print("the coordinates lie in quadrant 1")
##   case False:
##      match a<0 and b>0:
##         case True:
##           print("the coordinates lie in quadrant 4")
##         case False:
##           match a<0 and b<0:
##              case True:
##                 print("the coordinates lie in quadrant 3")
##              case False:
##                 match a>0 and b<0:
##                    case True:
##                       print("the coordinates lie in quadrant 2")
##                       
##                    
                 
                 
              
              
            
            
         
       
      
   

   
       

                   
             
           
           
      
      
      
     

      

      
                                  
                      
                 
                   
                  
                  
                  
               
               
               
               
            
         
      
  

 
     


    

     
 
     

     


                
        

        
   



                                     
                           
   
                        
                        
                        
                        
                       
                   





           
            
            
  




            

     
   
                    
                               
                           
                
              
