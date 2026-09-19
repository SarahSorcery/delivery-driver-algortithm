

## Right now I will have the "main" ui here for checking packages & statuses

# check status of package
# check truck route progress given a time
# display stats of trucks
# display total milage of all trucks

def RunSimulation():
    print("Please choose an option from below by entering the specific key value: ")
    print("Display Package Status: s ")
    print("Display Truck Route Progress: t ")
    print("Display Truck Mileage Totals: m ")
    option = input(" ")

    match option:
        case 's':
            print("PACKAGE STATUS")
        case 't':
            print("ROUTE PROGRESS")
        case 'm':
            print("TOTAL MILEAGE")

    option = input("Enter 'b' to go back: ")
    if option == 'b':
        RunSimulation()
    else:
        print("Ending Simulation")



start = input("Greetings, initiate Delivery Driver Simulation?  y/n:  ")

if start == 'y' or start =='Y':
    # run simulation
    print("start")
    RunSimulation()
else:
    print("Goodbye")