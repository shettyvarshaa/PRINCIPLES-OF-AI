import random
def takeSticks(curSticks, player):
    max_take = max(1, curSticks // 2)
    take = int(input("How many sticks would you like to take? ")) if player == 'user' else random.randint(1, max_take)
    return curSticks - take, 'computer' if player == 'user' else 'user', take
sticks, player = 12, 'user'
while sticks > 0:
    print(f"{sticks} sticks remaining in the pile.")
    sticks, next_player, taken = takeSticks(sticks, player)
    print(f"{player} has taken {taken} sticks.")
    player = next_player
print("Computer wins!" if player == 'user' else "User wins!")