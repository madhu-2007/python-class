##name = "Madhuvanthe"
##print(len(name))
##print(name[3])
##for i in name:
##  print(i)
##for i in "yuktha":
##    print(i)
##
##
##txt = "     The best things in life are free! "
##print("best" in txt)
##print("user" not in txt)
##
##print(name[0:5])
##print(name[:5])
##print(name[5:])
##print(txt.upper())
##print(txt.lower())
##print(txt.strip())
##print(txt.replace("b","w"))
##cartoon = "tom and jerry"
##print(cartoon.split("and"))
##
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##
##name="demo"
##print("name") 
##
##name="demo"
##print(name[3])
##
##for a in "telephone":
##    print(a)
##    
##name="demo"    
##print(len(name))
##
##a="happiness lies within"
##print( 'lies' in a )
##
##a="happiness lies within"
##if "lies" in a:
##    print("yes")
##
##a="happiness lies within"
##print( 'lies'  not in a )


####a="happiness lies within"
####if "lies" not in a:
####    print("no")

##Slicing Strings

##a="telephone"
##print(a[0:4])
##
##a="telephone"
##print(a[:4])
##
##a="telephone"
##print(a[4:])

##a="telephone"
##print(a[-5:-1])
##
##
##a="hardwork"
##print(a.upper())
##
##a="hardwork"
##print(a.lower())

##a="  hardwork "
##print(a.strip())

##a="car"
##print(a.replace("c","b"))

##a= "hello,world"
##print(a.strip(","))

##a = "Hello"
##b = "World"
##c = a + b
##print(c)

##a = "Hello"
##b = "World"
##print(a+" "+b)

##age=56
##txt=f"my name is demoname,my age is { age }"
##print(txt)

##price=78
##txt=f"the price is {price} dollars"
##print(txt)
##
##price=78
##txt=f"the price is {price:.3f} dollars"
##print(txt)
##
##txt=f"the price is{38*56} rupees"
##print(txt)

##escape characters

##txt = "We are the so-called \"Vikings\" from the north."
##print(txt)
##
##txt="it\'s a cat"
##print(txt)

##txt="thereby,I insert a \\(backslash)."
##print(txt)

##txt = "Hello\nWorld!"
##print(txt)
##
##txt = "Hello\rWorld!"
##print(txt)
##
##txt="hello\tWorld!"
##print(txt)


##txt = "Hello \bWorld!"
##print(txt) 

##txt = "Hello \fWorld!"
##print(txt)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

     ## capitalize

##txt="learning is GREAT"
##x=txt.capitalize()
##print(x)
##
##txt="33k is the price of this lap"
##x=txt.capitalize()
##print(x)
##

##txt="learning is GREAT"
##x=txt.casefold()
##print(x)

##txt="hi"
##x=txt.center(10)
##print(x)

##txt="hi"
##x=txt.center(10 ,"0")
##print(x)

##txt="apples are my favourite fruit,because apples are sweet"
##x=txt.count("apples")
##print(x)

######txt="apples are my favourite fruit,because apples are sweet"
######x=txt.count("apples" ,10,20)
######print(x)


##txt="my name is Madhu"
##x=txt.endswith("u")
##print(x)

##txt = "Hello, welcome to my world."
##
##x = txt.endswith("my world.", 17, 24)
##
##print(x)

##txt = "Hi, welcome to my castle."
##
##x = txt.endswith(("world.", "castle."))
##
##print(x)

##txt="H\te\tl\tl\to"
##print(txt.expandtabs())
##print(txt.expandtabs(4))
##print(txt.expandtabs(8))
##print(txt.expandtabs(15))


##txt = "Hello, welcome to my world."
##
##x = txt.find("welcome")
##
##print(x)


##txt = "Hello, welcome to my world."
##
##x = txt.find("l" )
##
##print(x)

##txt = "Hello, welcome to my world."
##
##x = txt.find("e", 5, 10)
##
##print(x)



##txt = "Hello, welcome to my world."
##
##print(txt.find("z"))
##print(txt.index("z"))

##formatting types

##txt ="this costs only about {price:.2f} dollors!"
##print(txt.format(price=49))

##txt="we have {:<10}pens."
##print(txt.format(38))
##
##txt="we have {:>10}pens."
##print(txt.format(38))

##txt="we have {:^10}pens."
##print(txt.format(38))

##txt="the temperature in iceland is {:=10} degrees celcius."
##print(txt.format(-18))

##txt = "The temperature is between {:+} and {:+} degrees celsius."
##
##print(txt.format(7, -3))

##txt = "The temperature is between {:-} and {:-} degrees celsius."
##
##print(txt.format(-3, 7))

##txt = "The temperature is between {:} and {:} degrees celsius."
##
##print(txt.format(-3, 7))
##txt ="the  fossils are about {:,}years old."
##print(txt.format(133000))

##txt ="the  fossils are about {:_}years old."
##print(txt.format(133000))

##
##txt1="My name is {fname}, I'm {age}".format(fname = "John", age = 36)
##print(txt1)
##
##txt2 = "My name is {0}, I'm {1}".format("John",36)
##print(txt2)
##
##txt3 = "My name is {}, I'm {}".format("John",36)
##print(txt3)

##txt = "Hello, welcome to my world."
##print(txt.index("m"))

##txt="SUV18"
##print(txt.isalnum())
##
##txt=" SUV 18 "
##print(txt.isalnum())

##txt="comY"
##print(txt.isalpha())
##
##txt=" com 17 "
##print(txt.isalpha())

##txt = "Company123"
##
##x = txt.isascii()
##
##print(x)

##txt="123"
##print(txt.isdecimal())

