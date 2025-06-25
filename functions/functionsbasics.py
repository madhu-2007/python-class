# def my_function():
#     print("hello")
# my_function()

# def my_function(fname):
#     print(fname+"hello")
# my_function("emily")

# def my_function(fname,lname):
#     print(fname + " " + lname)

# my_function("Emil", "Refsnes")

def my_function(*kids):
    print( "the youngest is" +kids[2])
my_function("emil","daisy","ann")

def my_function(child1, child2 ):
    print(child2)
my_function(child1="emil",child2="lily")

def my_function(**kid):
    print("my friend is" +kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")  

def my_function(country="india"):
    print(country)
my_function("Sweden")
my_function("norway")
my_function()
my_function("Brazil")

def my_function(x):
    return(5*x)
print(my_function(3))
print(my_function(5))    
print(my_function(6))  

def myfunction():
  pass


def my_function(x, /):
  print(x)

my_function(3)

# def my_function(x, /):
#   print(x)

# my_function(x=3)

def my_function(a,b,/,*,c,d):
   print(a + b + c + d)
my_function(5, 6, c = 7, d = 8) 
