lst_player = ["ronaldo","messi","modric","neymar"]

# i = 1
# for items in lst_player:
#     if i%2 != 0 :
#         print(f"player name is {items}")
#     i = i+1

i = 1
for index,item in enumerate(lst_player) :
    if i%2 == 0 :
        print(f"{index}player name is {item}")
    i = i+1