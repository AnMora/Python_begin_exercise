def number_of_bottles(): 
    for i in range(4,0,-1):
        if i > 1:
            print(f"{i} bottles of milk on the wall, {i} bottles of milk. Take one down and pass it around, {i-1} bottles of milk on the wall.")
        if i < 1:
            print(f"{i} bottle of milk on the wall, {i} bottle of milk.  Take one down and pass it around, no more bottles of milk on the wall.")  
        else:
            print(f"No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, {i+98} bottles of milk on the wall.") 

number_of_bottles()