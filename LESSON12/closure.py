def parent_func(man, coins):
    # coins = 5

    def play():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + man + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + man + " has " + str(coins) + " coin left.\n")
        else:
            print("\n" + man + " is out of coins.")

    return play


ram = parent_func("Ram", 4)
hari = parent_func("Hari", 7)

ram()
ram()

hari()
