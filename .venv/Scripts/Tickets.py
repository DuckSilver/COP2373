# Alex Lewis / Assignment 1A
# Allows up to 20 transactions + lists number of buyers once all tickets are sold

def main():
    # Defining accumlating variables
    TicketCount = 20
    BuyerCount = 0

    # Loop until there are no more tickets
    while TicketCount > 0:
        print("")
        print("How many tickets would like to purchase?")
        salecount = input("Buy: ")
        RemainCheck = int(TicketCount) - int(salecount)

        # sets maximum tickets a buyer can purchase to 4
        if int(salecount) >= 5:
            print("Sorry! The maximum tickets a buyer can purchase is 4")

        # Stops the buyer from purchasing more tickets than are left
        elif RemainCheck > -1:
            print("Transaction complete!")
            TicketCount = RemainCheck
            # adds 1 buyer to statistics
            BuyerCount += 1

        # ends transaction if the buyer tries to purchase more tickets than are left
        else:
            print("Error: limited tickets")
            print("Uh oh... we don't have enough tickets left!")

    # provides statistics of the ticket sale
    def end():
        print(" ")
        print(" ")
        print("All 20 tickets sold!")
        print("Cinema sale statistics:")
        print(f"{BuyerCount} buyers")

    end()

main()