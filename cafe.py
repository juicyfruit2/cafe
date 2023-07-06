# Created a program that caluclates the total stock for my cafe

# placed 4 items in a list called menu 
Menu = ["Coffe", "Doughnuts", "muffins", "cappuccino"]

# created a dictionary line 7- 9 to assign each key to their value 
Stock_dict = {"Coffe": 100 , "Doughnuts": 50 , "muffins": 42 ,"cappuccino": 75}

Price_dict = {"Coffe": 20 , "Doughnuts": 12 , "muffins": 15, "cappuccino": 22 }

# iterating through all the items of the menu to get my total stock worth 
Total = 0
for items in Menu:
    Total = Total + Stock_dict[items] * Price_dict[items]

print("The total stock worth is R",Total)
