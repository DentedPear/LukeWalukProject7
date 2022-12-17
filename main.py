#Luke Waluk



class Triangle:
    def __init__(self):
        print("How Big In A Number Should The Triangle Be? ")
        Triangle_Size = int(input())
        print("What do you want your triangles to be made out of ")
        Triangle_Character = input()
        print("Your Triangle Is Below")

        # Create a line of increasing characters up to the number provided
        for x in range(Triangle_Size):
            # Print x number of characters the user specified
            for j in range(x + 1):
                print(Triangle_Character, end="")
            # Create A Newline
            print("")
        quit = input("Press Q To Quit To Menu / R To Retry :  ")
        quit = quit.lower()
        if quit == ("q"):
            return
        elif quit == ("r"):
            Triangle()

class Interest:

    # Base case of calculating and adding interest
    def calculate_interest(self, amt, rate):
        return amt + (amt * rate)

    def __init__(self):
        print("WELCOME TO THE INTEREST RATE CALCUALTOR!!")
        print("Enter Inital Ammount")
        while True:
            try:
                Amount = float(input())
                break
            except ValueError:
                print("That is not a valid entry. Please enter a valid currency amount.")


        print("Enter Interest Rate")
        while True:
            try:
                Interest_Rate = float(input())/100
                break
            except ValueError:
                print("That is not a valid entry for an interest rate. Please enter a valid percentage rate.")

        print("Enter Number Of Years Your Money Will Be In The Account")
        while True:
            try:
                Years_In_Account = int(input())
                break
            except ValueError:
                print("That is not a valid entry for years. Please enter a valid number of years.")

        # Recursive case: For each year in the account, calculate interest and add it to the amount
        for x in range(Years_In_Account):
            Amount = self.calculate_interest(Amount, Interest_Rate) #Amount + (Amount * Interest_Rate)
            Year = x + 1
            Formatted_Amount = "{:.2f}".format(round(Amount, 2))
            print(f"Year {Year} balance is ${Formatted_Amount}.")

        Formatted_Amount = "{:.2f}".format(round(Amount, 2))
        print(f"After {Years_In_Account} years, your balance would be ${Formatted_Amount}.")

        quit = input("Press Q To Quit To Menu / R To Retry :  ")
        quit = quit.lower()
        if quit == ("q"):
            return
        elif quit == ("r"):
            Interest()

class BackwardsList:
    def __init__(self):
        file = open("TextFile.txt","r")
        all_lines = file.readlines()
        # Loop backwards through the zero-based list items:
        for i in range(len(all_lines)-1, -1, -1):
            # Each line from the file already had a new-line character in it:
            print(all_lines[i], end="")

        quit = input("Press Q To Quit To Menu / R To Retry :  ")
        quit = quit.lower()
        if quit == ("q"):
            return
        elif quit == ("r"):
            BackwardsList()


# STARTUP MENU HERE
while True:
    print("---------------------------------------------------------------")
    print("Welcome To Luke Waluk's Menu Project, What Would You Like To Do?")
    print("")
    print("A) Calcuator Your Interest")
    print("")
    print("B) Create A Triangle")
    print("")
    print("C) Print List Backwards")
    print("")
    print("E) Exit Program")
    Choice = input()
    Choice = Choice.lower()
    if Choice == ("a"):
        #print("Starting Interest!")
        Interest()
    elif Choice == ("b"):
        print("Starting Triangle")
        Triangle()
    elif Choice == ("c"):
        print("Starting Backwards List!")
        BackwardsList()
    elif Choice == ("e"):
        print("exit")
        break
#Interest()
#BackwardsList()
#Triangle()