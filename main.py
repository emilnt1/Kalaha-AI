# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tabulate import tabulate #pip install tabulate

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
NHAND = [6, 6, 6, 6, 6, 6, 0]
SHAND = [6, 6, 6, 6, 6, 6, 0]





def printboard():
    print(tabulate([
        [" ", str(NHAND[5]), str(NHAND[4]), str(NHAND[3]), str(NHAND[2]), str(NHAND[1]), str(NHAND[0]), " "],
        [str(NHAND[6]), "", "", "", "", "", "", str(SHAND[6])],
        [" ", str(SHAND[0]), str(SHAND[1]), str(SHAND[2]), str(SHAND[3]), str(SHAND[4]), str(SHAND[5]), " "]]
    ))

printboard()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
