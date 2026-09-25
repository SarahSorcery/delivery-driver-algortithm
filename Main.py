# Sam Merrill ID: 012638734
from UI import UI
import time
import csv
from Package import Package
from Truck import Truck
from PackageReader import PackageReader

pkg_reader = PackageReader()


# Add packages to trucks
def initialize_Truck1():
    truck1.add_package(pkg_reader.get_package_by_id('6'))
    truck1.add_package(pkg_reader.get_package_by_id('28'))
    truck1.add_package(pkg_reader.get_package_by_id('25'))
    truck1.add_package(pkg_reader.get_package_by_id('32'))
    truck1.add_package(pkg_reader.get_package_by_id('22'))
    truck1.add_package(pkg_reader.get_package_by_id('23'))
    truck1.add_package(pkg_reader.get_package_by_id('24'))
    truck1.add_package(pkg_reader.get_package_by_id('26'))
    truck1.add_package(pkg_reader.get_package_by_id('1'))
    truck1.add_package(pkg_reader.get_package_by_id('6'))
    truck1.add_package(pkg_reader.get_package_by_id('31'))
    truck1.add_package(pkg_reader.get_package_by_id('40'))

def initialize_Truck2():
    truck2.add_package(pkg_reader.get_package_by_id('13'))
    truck2.add_package(pkg_reader.get_package_by_id('15'))
    truck2.add_package(pkg_reader.get_package_by_id('14'))
    truck2.add_package(pkg_reader.get_package_by_id('16'))
    truck2.add_package(pkg_reader.get_package_by_id('18'))
    truck2.add_package(pkg_reader.get_package_by_id('36'))
    truck2.add_package(pkg_reader.get_package_by_id('38'))
    truck2.add_package(pkg_reader.get_package_by_id('3'))
    truck2.add_package(pkg_reader.get_package_by_id('19'))
    truck2.add_package(pkg_reader.get_package_by_id('20'))

    truck2.add_package(pkg_reader.get_package_by_id('37'))
    truck2.add_package(pkg_reader.get_package_by_id('30'))
    truck2.add_package(pkg_reader.get_package_by_id('29'))

def initialize_Truck3():   
    truck3.add_package(pkg_reader.get_package_by_id('2'))
    truck3.add_package(pkg_reader.get_package_by_id('4'))
    truck3.add_package(pkg_reader.get_package_by_id('5'))
    truck3.add_package(pkg_reader.get_package_by_id('7'))
    truck3.add_package(pkg_reader.get_package_by_id('8'))
    truck3.add_package(pkg_reader.get_package_by_id('9'))
    truck3.add_package(pkg_reader.get_package_by_id('10'))
    truck3.add_package(pkg_reader.get_package_by_id('11'))
    truck3.add_package(pkg_reader.get_package_by_id('12'))
    truck3.add_package(pkg_reader.get_package_by_id('17'))
    truck3.add_package(pkg_reader.get_package_by_id('21'))
    truck3.add_package(pkg_reader.get_package_by_id('27'))
    truck3.add_package(pkg_reader.get_package_by_id('33'))
    truck3.add_package(pkg_reader.get_package_by_id('35'))
    truck3.add_package(pkg_reader.get_package_by_id('39'))

truck1 = Truck("1")
truck2 = Truck("2")
truck3 = Truck("3")

initialize_Truck1() #
initialize_Truck2() #
initialize_Truck3() #

###################################################################################################
def get_distance_info():
    distance_dict = dict() # create a dictionary for references
    with open("WGUPS-distance-table.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            address = line.pop(0)  # remove address and assign for key
            street_address = " ".join(address.split()) # clean up address
            distance_dict[street_address] = line.copy() # add address & distance info to dictionary
    return distance_dict

def build_route(package_list, distance_dict, truck_time):

    route_list = []
    packages_remaining = package_list.copy() # make a copy of the package list to remove from
    current_address = "HUB"
    current_time = truck_time
    distance_traveled = 0.0

    while packages_remaining:
        # find package in list that has lowest distance in dictionary
        shortest_path, closest_package = nearest_neighbor(packages_remaining, distance_dict, current_address) # type: ignore

        travel_time = shortest_path * (60/18) # calculate travel minutes
        current_time += travel_time # add to current time

        distance_traveled += shortest_path # add distance to total
        current_address = get_package_address(closest_package)

        Package.set_delivery_time(closest_package, current_time)

        
        route_list.append(closest_package) # Add it to route list
        packages_remaining.remove(closest_package) # remove package with shortest path 

    return_travel =  get_distance(current_address, "HUB", distance_dict)
    distance_traveled += return_travel

    return route_list, distance_traveled, current_time
    #print(distance_traveled) print(route_list)

def nearest_neighbor(package_list, distance_dict, current_address):
        shortest_path = float("inf")
        closest_package = None
        for package in package_list:
                package_address = get_package_address(package)

                distance = get_distance(current_address, package_address, distance_dict)

                if distance < shortest_path:
                    shortest_path = distance
                    closest_package = package

        return shortest_path, closest_package

def get_distance(from_address, to_address, distance_dict):
    addresses = list(distance_dict.keys()) # put addresses into list for comparing

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

def get_package_status(package, time_entered, truck_time):
    delivery_time = Package.get_delivery_time(package)
    constraint = Package.get_status(package)

    if constraint == "Delayed on flight---will not arrive to depot until 9:05 am" and time_entered <= 545:
        return UI.red + "DELAYED" + UI.reset
    if time_entered <= truck_time:
        return UI.yellow + "AT HUB" + UI.reset
    if delivery_time <= time_entered:
        return UI.green + "DELIVERED" + UI.reset 
    return UI.head + "ENROUTE" + UI.reset

def format_time(minutes):
    hours = int(minutes // 60)
    mins = int(minutes % 60)

    if hours >= 12:
        tod = "PM"
    else:
        tod = "AM"

    display_hour = hours % 12
    if display_hour == 0:
        display_hour = 12

    return f"{display_hour}:{mins:02d} {tod}"

def print_package_statuses(package_list, time_entered, truck_time, truck_finish_time):
    print(UI.reset + f"Time Entered: {format_time(time_entered)}")
    print(f"Start Time: {format_time(truck_time)}    Finish Time: {format_time(truck_finish_time)}")
    print("#####################################################################################")
    print("ID   ADDRESS               STATUS               EST. DELIVERY TIME     CONSTRAINTS")
    print("#####################################################################################")
    for package in package_list:

        status = get_package_status(package, time_entered, truck_time)
        delivery_time = format_time(Package.get_delivery_time(package))
        #print(f"{package}  --| Est. Delivery: {delivery_time}")
        print(f"{Package.get_id(package)}:  {Package.get_address(package)},   -->  {status}      --| Est. Delivery: {delivery_time}  --| Deadline: {Package.get_deadline(package)}   {Package.get_status(package)}")

def print_all_statuses(time_entered):
    print(UI.head + "TRUCK #1" + UI.reset)
    print_package_statuses(truck1_route_list, time_entered, truck1_time, truck1_finish_time)
    print(UI.head + "TRUCK #2" + UI.reset)
    print_package_statuses(truck2_route_list, time_entered, truck2_time, truck2_finish_time)
    print(UI.head + "TRUCK #3" + UI.reset)
    print_package_statuses(truck3_route_list, time_entered, truck3_time, truck3_finish_time)

def status_options():
    print(UI.head + "PACKAGE STATUS" + UI.reset)

    time_entered = int(input(UI.green + "Enter a time:  "))

    truck_amt = input("Enter ALL or Truck #: ")
    if truck_amt == '1':
        print_package_statuses(truck1_route_list, time_entered, truck1_time)
    elif truck_amt == '2':
        print_package_statuses(truck2_route_list, time_entered, truck2_time)
    elif truck_amt == '3':
        print_package_statuses(truck3_route_list, time_entered, truck3_time)
    else:
        print_all_statuses(time_entered)
    
###################################################################################################
# times
truck1_time = 545 # (9:05 am)
truck2_time = 480 # (8:00 am)
truck3_time = 600 # (10:00 am)
distance_traveled = 0.0
    
# take truck's package list and find it in distance dict
truck1_packages = truck1.get_package_list()  #hashmap
truck2_packages = truck2.get_package_list()
truck3_packages = truck3.get_package_list()
    
distance_data = get_distance_info() #dictionary
distance_data = format_distance_dict(distance_data)
#print(distance_data["1060 Dalton Ave S (84104)"][0]) Testing dictionary
        
truck1_route_list, truck1_distance_traveled, truck1_finish_time = build_route(truck1_packages, distance_data, truck1_time)
truck2_route_list, truck2_distance_traveled, truck2_finish_time = build_route(truck2_packages, distance_data, truck2_time)
truck3_route_list, truck3_distance_traveled, truck3_finish_time = build_route(truck3_packages, distance_data, truck3_time)
    
total_distance = truck1_distance_traveled + truck2_distance_traveled + truck3_distance_traveled
###################################################################################################
def run_simulation():

    # MENU OPTIONS
    print(UI.head + "Please choose an option from below by entering the specific key value: ")
    print(UI.blue + "Display Package Status: " + UI.yellow + "s ")
    print(UI.blue + "Display Truck Mileage Totals: " + UI.yellow + "m ")
    print(UI.blue + "Display Package Information by ID: " + UI.yellow + "l")
    option = input(UI.yellow)

    match option:
        case 's': # STATUSES & TIME
            print(UI.head + "PACKAGE STATUS" + UI.reset)
            
            time_entered = int(input(UI.green + "Enter a time:  "))
            if time_entered >= 620: # 10:20 AM package #9 updates
                package_9 = pkg_reader.get_package_by_id('9')
                #Correct address for #9 below
                # AFTER 10:20 am # 410 S State St., Salt Lake City, UT 84111
                Package.update(package_9, "410 S State St", "Salt Lake City", "84111", "AFTER 10:20am", " ")

            truck_amt = input("Enter ALL or Truck #: ")
            if truck_amt == '1':
                print_package_statuses(truck1_route_list, time_entered,truck1_finish_time)
            elif truck_amt == '2':
                print_package_statuses(truck2_route_list, time_entered,truck2_finish_time)
            elif truck_amt == '3':
                print_package_statuses(truck3_route_list, time_entered,truck3_finish_time)
            else:
                print_all_statuses(time_entered)

        case 'm': # MILEAGE
            print(UI.reset + "**************************************************")
            print(UI.head + "TOTAL MILEAGE" + UI.reset)
            print(UI.green + f"{total_distance} mi")
            print(UI.head + "Truck #1: " + UI.green + f"{truck1_distance_traveled:.2f} mi")
            print(UI.blue + f"Start Time: {format_time(truck1_time)}")
            print(f"Finish Time: {format_time(truck1_finish_time)}")

            print(UI.head + "Truck #2: " + UI.green + f"{truck2_distance_traveled:.2f} mi")
            print(UI.blue + f"Start Time: {format_time(truck2_time)}")
            print(f"Finish Time: {format_time(truck2_finish_time)}")
            
            print(UI.head + "Truck #3: " + UI.green + f"{truck3_distance_traveled:.2f} mi")
            print(UI.blue + f"Start Time: {format_time(truck3_time)}")
            print(f"Finish Time: {format_time(truck3_finish_time)}")
            print(UI.reset + "**************************************************")

        case 'l': # PACKAGE LOOKUP
            entered_id = input("Enter a package ID to lookup data: ")
            data = pkg_reader.get_package_by_id(entered_id)
            print(data)

    print(UI.blue + "Back to Menu: " + UI.yellow + "b ")
    print(UI.blue + "Quit Simulation: " + UI.yellow + "ANY ")

    # MORE CHOICES OR END SIMULATION
    option = input(UI.yellow)
    if option == 'b':
        run_simulation()
    else:
        print(UI.red + "Ending Simulation")
        time.sleep(1)
        print("GOODBYE" + UI.reset)
###################################################################################################

start = input(UI.green + "Greetings, initiate Delivery Driver Simulation?  y/n:  " + UI.yellow)

if start == 'y' or start =='Y':
    # run simulation
    print(UI.green + "STARTING SIMULATION" + UI.reset)
    time.sleep(1)
    run_simulation()
else:
    print(UI.red + "GOODBYE" + UI.reset)