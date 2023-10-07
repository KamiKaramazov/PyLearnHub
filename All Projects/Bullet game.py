def hero(bullets, dragons):
    bullets_needed = dragons * 2
    if bullets >= bullets_needed:
        return True
    else:
        return False

bullets = int(input("Please give me bullet: "))  
dragons = int(input("How many dragons you want: "))   

result = hero(bullets, dragons)

if result:
    print("The hero can survive!")
else:
    print("The hero cannot survive!")
