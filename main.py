# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tabulate import tabulate  # pip install tabulate

NHAND = [6, 6, 6, 6, 6, 6, 0]  # North Hand
SHAND = [6, 6, 6, 6, 6, 6, 0]  # South Hand


def printboard():
    print(tabulate([
        [" ", str(NHAND[5]), str(NHAND[4]), str(NHAND[3]), str(NHAND[2]), str(NHAND[1]), str(NHAND[0]), " "],
        [str(NHAND[6]), "", "", "", "", "", "", str(SHAND[6])],
        [" ", str(SHAND[0]), str(SHAND[1]), str(SHAND[2]), str(SHAND[3]), str(SHAND[4]), str(SHAND[5]), " "]]
    ))

def moveSeeds(hole):
    if hole.isdigit():
        holetomove = int(hole)
        if holetomove <= 1 or holetomove >= 6:
            print(str(SHAND[holetomove-1]))
        else:
            print("Hole not found.")
    else:
        print("Please input a valid number from 1-6!")



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    printboard()
    print("You are the south side of the board")
    holeToMoveFrom = input("Choose hole from 1-6:\n")
    moveSeeds(holeToMoveFrom)
