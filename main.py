def sum(a, b, c):
    return a + b + c

def checkdraw(xState, ytState):
    for i in range(9):
        if xState[i] == 0 or ytState[i] == 0:
            return False
    return True

def checkwin(xState, ytSate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X wins")
            return 1

        if sum(ytSate[win[0]], ytSate[win[1]], ytSate[win[2]]) == 3:
            print("O wins")
            return 0
    return -1


def printboard(xState, ytState):
    zero = "X" if xState[0] == 1 else ("O" if ytState[0] == 1 else 0)
    one = "X" if xState[1] == 1 else ("O" if ytState[1] == 1 else 1)
    two = "X" if xState[2] == 1 else ("O" if ytState[2] == 1 else 2)
    three = "X" if xState[3] == 1 else ("O" if ytState[3] == 1 else 3)
    four = "X" if xState[4] == 1 else ("O" if ytState[4] == 1 else 4)
    five = "X" if xState[5] == 1 else ("O" if ytState[5] == 1 else 5)
    six = "X" if xState[6] == 1 else ("O" if ytState[6] == 1 else 6)
    seven = "X" if xState[7] == 1 else ("O" if ytState[7] == 1 else 7)
    eight = "X" if xState[8] == 1 else ("O" if ytState[8] == 1 else 8)

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ytState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to tik-tac-toe Game")
    while (True):
        printboard(xState, ytState)
        if turn == 1:
            print("X's Turn ")
            value = int(input("Please enter your SquareBox :"))
            xState[value] = 1
        else:
            print("O's Turn ")
            value = int(input("please enter your SquareBox :"))
            ytState[value] = 1
        cwin = checkwin(xState, ytState)
        if cwin != -1:
            print("Match Over")
            break
        if checkdraw(xState, ytState):
            print("Match Draw")
            break
        turn = 1 - turn
