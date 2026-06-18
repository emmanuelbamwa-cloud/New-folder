#Ask user for name with formatting
name = input("What's your name " ).strip().title()

#Split name into first and last
first, last =  name.split(" ")

#Say hello to user
print(f"hello, {name}")