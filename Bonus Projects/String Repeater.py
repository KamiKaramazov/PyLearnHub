def repeater_str(str, n):
    return str * n

string = input("Give me a string: ")
n = int(input("Repeat time: "))
repeated_string = repeater_str(string, n)
print(repeated_string)