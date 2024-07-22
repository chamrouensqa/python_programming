print("Hello World!")

#commentCode
name = "Chamrouen"
print("my firstname is " +name)

#Nonlocal
def say_hello():
    firstName = "Chamrouensann"
    def say_hi():
        nonlocal firstName
        firstName = "omg Chamrouen"
        print(firstName)
    say_hi()
    print(firstName)
say_hello()
