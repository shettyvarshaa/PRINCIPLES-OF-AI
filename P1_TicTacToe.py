board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
def displayBoard():
    print("-------------")
    for x in range (0, 3):
        print(f"| {board[x][0]} | {board[x][1]} | {board[x][2]} |")
        print("-------------")
def playerChance(chance):
    if chance == "X":
        return "O"
    return "X"
def boardCheck(chance):
    if board[0] == [chance, chance, chance] or board[1] == [chance, chance, chance] or board[2] == [chance, chance, chance]:
        return False
    for y in range(0, 3):
        if board[0][y] == chance and board[1][y] == chance and board[2][y] == chance:
            return False
    if board[0][0] == chance and board[1][1] == chance and board[2][2] == chance:
        return False
    if board[0][2] == chance and board[1][1] == chance and board[2][0] == chance:
        return False
    return True
def main():
    chance = "O"
    while(boardCheck(chance)):
        chance = playerChance(chance)
        x, y = input("Enter the location: ").split()
        x, y = int(x), int(y)
        board[x][y] = chance
        displayBoard()
    print(f"{chance} won !!!")
main()