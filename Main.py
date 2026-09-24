from UI import UI
import time
import csv
from Package import Package
from Truck import Truck
from PackageReader import PackageReader

pkg_reader = PackageReader()


# Testing initializing a truck:
def initialize_Truck1():
    truck1.add_package(pkg_reader.get_package_by_id('13'))
    truck1.add_package(pkg_reader.get_package_by_id('15'))
    truck1.add_package(pkg_reader.get_package_by_id('14'))
    truck1.add_package(pkg_reader.get_package_by_id('16'))

    truck1.add_package(pkg_reader.get_package_by_id('19'))
    truck1.add_package(pkg_reader.get_package_by_id('20'))
    truck1.add_package(pkg_reader.get_package_by_id('1'))
    truck1.add_package(pkg_reader.get_package_by_id('29'))

    truck1.add_package(pkg_reader.get_package_by_id('7'))
    truck1.add_package(pkg_reader.get_package_by_id('25'))
    truck1.add_package(pkg_reader.get_package_by_id('24'))
    
        

def initialize_Truck2():
    truck2.add_package(pkg_reader.get_package_by_id('3'))
    truck2.add_package(pkg_reader.get_package_by_id('18'))
    truck2.add_package(pkg_reader.get_package_by_id('36'))
    truck2.add_package(pkg_reader.get_package_by_id('38'))

    truck2.add_package(pkg_reader.get_package_by_id('5'))
    truck2.add_package(pkg_reader.get_package_by_id('8'))
    truck2.add_package(pkg_reader.get_package_by_id('9'))
    truck2.add_package(pkg_reader.get_package_by_id('12'))

    
    truck2.add_package(pkg_reader.get_package_by_id('10'))
    truck2.add_package(pkg_reader.get_package_by_id('11'))
    truck2.add_package(pkg_reader.get_package_by_id('17'))
    truck2.add_package(pkg_reader.get_package_by_id('21'))

    truck2.add_package(pkg_reader.get_package_by_id('37'))
    truck2.add_package(pkg_reader.get_package_by_id('30'))
        

    


def initialize_Truck3():
    
    truck3.add_package(pkg_reader.get_package_by_id('6'))
    truck3.add_package(pkg_reader.get_package_by_id('28'))
    truck3.add_package(pkg_reader.get_package_by_id('34'))
    truck3.add_package(pkg_reader.get_package_by_id('40'))

    truck3.add_package(pkg_reader.get_package_by_id('39'))
    truck3.add_package(pkg_reader.get_package_by_id('32'))
    truck3.add_package(pkg_reader.get_package_by_id('27'))
    truck3.add_package(pkg_reader.get_package_by_id('35'))

    truck3.add_package(pkg_reader.get_package_by_id('2'))
    truck3.add_package(pkg_reader.get_package_by_id('33'))
    truck3.add_package(pkg_reader.get_package_by_id('4'))
    truck3.add_package(pkg_reader.get_package_by_id('23'))

    truck3.add_package(pkg_reader.get_package_by_id('26'))
    truck3.add_package(pkg_reader.get_package_by_id('22'))
    truck3.add_package(pkg_reader.get_package_by_id('31'))
    

truck1 = Truck("1")
truck2 = Truck("2")
truck3 = Truck("3")

initialize_Truck1() #
initialize_Truck2() #
initialize_Truck3() #



# Package Update
update_package_9 = False

# Correct address for #9 below
# AFTER 10:20 am
# 410 S State St., Salt Lake City, UT 84111




#######
def get_distance_info():
    distance_dict = dict() # create a dictionary for references
    with open("WGUPS-distance-table.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            address = line.pop(0)  # remove address and assign for key
            street_address = " ".join(address.split()) # clean up address
            distance_dict[street_address] = line.copy() # add address & distance info to dictionary
    return distance_dict



#truck_time = 0


def nearest_neighbor(package_list, distance_dict, truck_time, distance_traveled):

    route_list = []
    shortest_path = 10.0
    # make a copy of the package list to remove from
    package_list_copy = package_list.copy()

    current_address = "HUB"

    while package_list_copy:
        # find package in list that has lowest distance in dictionary
        shortest_path, shortest_address = find_path(package_list_copy, distance_dict, current_address)
       # print(shortest_path) print(shortest_address)
        
        # remove package with shortest path and add it to route list
        for index, package in enumerate(package_list_copy):
            package_address = get_package_address(package)
                
            if (package_address == shortest_address):
                next_package = package_list_copy.pop(index)
                route_list.append(next_package) # add package to route list
                break
            #Package.set_status(next_package, "ENROUTE")
        
            travel_time = shortest_path * (60/18) # add time to truck
            truck_time += travel_time

            
            distance_traveled += shortest_path # Truck "travels"
            current_address = shortest_address # Truck moves to new address to start again
            #Package.set_status(next_package, "DELIVERED")

        #     print(
        #     f"{truck_time} - "
        #     f"Package {Package.get_id(next_package)} "
        #     f"delivered to {current_address}"
        # )

    #print(route_list)
    #print(distance_traveled)
    time.sleep(1)
    print(UI.red + "Truck heading back to HUB")
    time.sleep(1)


    return_travel =  get_distance(current_address, "HUB", distance_dict)
    distance_traveled += return_travel

    print(UI.yellow + f"Route Distance Traveled: {distance_traveled:.2f} miles" + UI.reset)
    print(UI.blue + f"Minutes On Road: {truck_time}" + UI.reset)

    

    return route_list, distance_traveled, truck_time
    # print(distance_traveled) print(route_list)
    
    pass


def find_path(package_list, distance_dict, current_address):
        shortest_path = float("inf")
        shortest_address = None
        for package in package_list:
                package_address = get_package_address(package)
                distance = get_distance(current_address, package_address, distance_dict)

                if distance < shortest_path: # and distance != 0.0:
                    shortest_path = distance
                    shortest_address = package_address

        return shortest_path, shortest_address

def get_distance(from_address, to_address, distance_dict):
    addresses = list(distance_dict.keys()) # put addresses into list for comparing
    if from_address not in addresses:
        print("FROM ADDRESS NOT FOUND:", repr(from_address))
        print("Available addresses:", addresses)
        raise ValueError(f"Address not found: {from_address!r}")

    if to_address not in addresses:
        print("TO ADDRESS NOT FOUND:", repr(to_address))
        print("Available addresses:", addresses)
        raise ValueError(f"Address not found: {to_address!r}")

    if from_address == to_address:
        return 0.0


    index1 = addresses.index(from_address)
    index2 = addresses.index(to_address)
    

    if index1 > index2:
        distance = distance_dict[from_address][index2]
    else:
        distance = distance_dict[to_address][index1]
    return float(distance)


def print_route_list(route_list, truck_num):
    print(UI.head + f"Truck {truck_num} Route:" + UI.green)
    for package in route_list:
        print(package)
    UI.reset

def format_address(address):

    address = address.strip()

    address = address.replace("South", "S")
    address = address.replace("North", "N")
    address = address.replace("East", "E")
    address = address.replace("West", "W")

    return address

def format_distance_dict(distance_dict):

    formatted_dict = {}

    for address, distances in distance_dict.items():
        fixed_address = format_address(address)
        formatted_dict[fixed_address] = distances

    return formatted_dict


def get_package_address(package):

    address = format_address(Package.get_address(package))
    zipcode = str(Package.get_zipcode(package)).strip()

    return f"{address} ({zipcode})"




###################################################################################################



## Right now I will have the "main" ui here for checking packages & statuses

# check status of package
# check truck route progress given a time
# display stats of trucks
# display total milage of all trucks

def RunSimulation():

    # Start
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
            print(truck3)
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

    update = input(UI.red + "ALERT! : New information has come in for package #9, would you like to update? " 
              + UI.yellow + "y/n: ")
    if update == 'y':
        update_package_9 = True
        package_9 = pkg_reader.get_package_by_id('9')
        # Package.set_address(package_9, "")
        # Package.set_zipcode(package_9, "")
        #Correct address for #9 below
        # AFTER 10:20 am
        # 410 S State St., Salt Lake City, UT 84111
        Package.update(package_9, "410 S State St", "Salt Lake City", "84111", "AFTER 10:20am", " ")


    RunSimulation()
else:
    print(UI.red + "GOODBYE" + UI.reset)


##########
# times
truck1_time = 0
truck2_time = 0
truck3_time = 0
start_time = 8 * 60

distance_traveled = 0.0

# take truck's package list and find it in distance dict
truck1_packages = truck1.get_package_list()  #hashmap
truck2_packages = truck2.get_package_list()
truck3_packages = truck3.get_package_list()

distance_data = get_distance_info() #dictionary
distance_data = format_distance_dict(distance_data)

#print(distance_data["1060 Dalton Ave S (84104)"][0]) Testing dictionary

truck1_route_list, truck1_distance_traveled, truck1_time = nearest_neighbor(truck1_packages, distance_data, truck1_time, distance_traveled)
truck2_route_list, truck2_distance_traveled, truck2_time = nearest_neighbor(truck2_packages, distance_data, truck2_time, distance_traveled)
truck3_route_list, truck3_distance_traveled, truck3_time = nearest_neighbor(truck3_packages, distance_data, truck3_time, distance_traveled)

total_distance = truck1_distance_traveled + truck2_distance_traveled + truck3_distance_traveled
truck1_time += start_time
truck2_time += start_time
truck3_time += start_time

print_route_list(truck1_route_list, 1)
print(f"Truck 1 time: {truck1_time / 60}")
print_route_list(truck2_route_list, 2)
print(f"Truck 2 time: {truck2_time / 60}")
print_route_list(truck3_route_list, 3)
print(f"Truck 3 time: {truck3_time / 60}")
print(UI.yellow + "*************************")
print(f"Total Distance Traveled: {total_distance}" + UI.reset)