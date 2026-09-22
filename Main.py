from UI import UI
import time

from Truck import Truck
from PackageReader import PackageReader

pkg_reader = PackageReader()


# Testing initializing a truck:
def initialize_Truck1():
    truck1.add_package(pkg_reader.get_package_by_id('1'))
    truck1.add_package(pkg_reader.get_package_by_id('29'))
    truck1.add_package(pkg_reader.get_package_by_id('7'))
    truck1.add_package(pkg_reader.get_package_by_id('30'))
    truck1.add_package(pkg_reader.get_package_by_id('8'))
    truck1.add_package(pkg_reader.get_package_by_id('34'))
    truck1.add_package(pkg_reader.get_package_by_id('40'))
    truck1.add_package(pkg_reader.get_package_by_id('13'))
    truck1.add_package(pkg_reader.get_package_by_id('39'))
    truck1.add_package(pkg_reader.get_package_by_id('14'))
    truck1.add_package(pkg_reader.get_package_by_id('15'))
    truck1.add_package(pkg_reader.get_package_by_id('16'))
    truck1.add_package(pkg_reader.get_package_by_id('19'))
    truck1.add_package(pkg_reader.get_package_by_id('20'))
    truck1.add_package(pkg_reader.get_package_by_id('37'))

def initialize_Truck2():
    truck2.add_package(pkg_reader.get_package_by_id('6'))
    truck2.add_package(pkg_reader.get_package_by_id('5'))
    truck2.add_package(pkg_reader.get_package_by_id('21'))
    truck2.add_package(pkg_reader.get_package_by_id('4'))
    truck2.add_package(pkg_reader.get_package_by_id('24'))
    truck2.add_package(pkg_reader.get_package_by_id('23'))
    truck2.add_package(pkg_reader.get_package_by_id('26'))
    truck2.add_package(pkg_reader.get_package_by_id('22'))
    truck2.add_package(pkg_reader.get_package_by_id('10'))
    truck2.add_package(pkg_reader.get_package_by_id('11'))
    truck2.add_package(pkg_reader.get_package_by_id('31'))


def initialize_Truck1_2():
    truck1_2.add_package(pkg_reader.get_package_by_id('17'))
    truck1_2.add_package(pkg_reader.get_package_by_id('12'))
    truck1_2.add_package(pkg_reader.get_package_by_id('25'))
    truck1_2.add_package(pkg_reader.get_package_by_id('28'))
    truck1_2.add_package(pkg_reader.get_package_by_id('32'))
    truck1_2.add_package(pkg_reader.get_package_by_id('3'))
    truck1_2.add_package(pkg_reader.get_package_by_id('18'))
    truck1_2.add_package(pkg_reader.get_package_by_id('36'))
    truck1_2.add_package(pkg_reader.get_package_by_id('38'))

    truck1_2.add_package(pkg_reader.get_package_by_id('27'))
    truck1_2.add_package(pkg_reader.get_package_by_id('35'))
    truck1_2.add_package(pkg_reader.get_package_by_id('2'))
    truck1_2.add_package(pkg_reader.get_package_by_id('33'))
    truck1_2.add_package(pkg_reader.get_package_by_id('9'))

truck1 = Truck("1")
truck2 = Truck("2")
truck1_2 = Truck("1_2")

initialize_Truck1() #
initialize_Truck2() #
initialize_Truck1_2() #






# Package Update
update_package_9 = False











## Right now I will have the "main" ui here for checking packages & statuses

# check status of package
# check truck route progress given a time
# display stats of trucks
# display total milage of all trucks

def RunSimulation():

    update = input(UI.red + "ALERT! : New information has come in for package #9, would you like to update? " 
          + UI.yellow + "y/n: ")
    if update == 'y':
        update_package_9 = True




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
            print(truck1)
            print(truck2)
            print(truck1_2)
        case 'm':
            print(UI.head + "TOTAL MILEAGE" + UI.reset)

    print(UI.blue + "Back to Menu: " + UI.yellow + "b ")
    print(UI.blue + "Quit Simulation: " + UI.yellow + "ANY ")

    option = input(UI.yellow)

    if option == 'b':
        RunSimulation()
    else:
        print(UI.red + "Ending Simulation")
        time.sleep(1)
        print("GOODBYE" + UI.reset)




start = input(UI.green + "Greetings, initiate Delivery Driver Simulation?  y/n:  " + UI.yellow)

if start == 'y' or start =='Y':
    # run simulation
    print(UI.green + "STARTING SIMULATION" + UI.reset)
    time.sleep(1)
    RunSimulation()
else:
    print(UI.red + "GOODBYE" + UI.reset)