from UI import UI

## Right now I will have the "main" ui here for checking packages & statuses

# check status of package
# check truck route progress given a time
# display stats of trucks
# display total milage of all trucks

def RunSimulation():
    print(UI.head + "Please choose an option from below by entering the specific key value: ")
    print(UI.blue + "Display Package Status: " + UI.yellow + "s ")
    print(UI.blue + "Display Truck Route Progress: " + UI.yellow + "t ")
    print(UI.blue + "Display Truck Mileage Totals: " + UI.yellow + "m ")
    option = input(UI.yellow)

    match option:
        case 's':
            print(UI.head + "PACKAGE STATUS" + UI.reset)
        case 't':
            print(UI.head + "ROUTE PROGRESS" + UI.reset)
        case 'm':
            print(UI.head + "TOTAL MILEAGE" + UI.reset)

    print(UI.blue + "Back to Menu: " + UI.yellow + "b ")
    print(UI.blue + "Quit Simulation: " + UI.yellow + "ANY ")
    option = input(UI.yellow)
    if option == 'b':
        RunSimulation()
    else:
        print(UI.red + "Ending Simulation")
        print("GOODBYE" + UI.reset)



start = input(UI.green + "Greetings, initiate Delivery Driver Simulation?  y/n:  " + UI.yellow)

if start == 'y' or start =='Y':
    # run simulation
    print(UI.green + "STARTING SIMULATION" + UI.reset)
    RunSimulation()
else:
    print(UI.red + "GOODBYE" + UI.reset)