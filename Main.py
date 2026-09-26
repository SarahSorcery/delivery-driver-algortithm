# Sam Merrill ID: 012638734
from UI import UI
import time
import csv
from Package import Package
from Truck import Truck
from PackageReader import PackageReader

pkg_reader = PackageReader()


# Add packages to trucks

# Time Complexity: O(n)
# Space Complexity: O(n)
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

initialize_Truck1() # O(n)
initialize_Truck2() # O(n)
initialize_Truck3() # O(n)

###################################################################################################
# Time Complexity: O(n) n = rows in file
# Space Complexity: O(n)
def get_distance_info():
    distance_table = dict() # create for references
    with open("WGUPS-distance-table.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader: # O(n)
            address = line.pop(0)  # remove address and assign for key
            street_address = " ".join(address.split()) # clean up address
            distance_table[street_address] = line.copy() # add address & distance info to references
    return distance_table

# Time Complexity: O(p^2 * a) + O(p^2) --> o(p^2 * a)
# Space Complexity: O(p)
def build_route(package_list, distance_table, truck_time):

    route_list = []
    packages_remaining = package_list.copy() # copy pkg list to remove from --> [O(p)] time & space
    current_address = "HUB"
    current_time = truck_time
    distance_traveled = 0.0

    while packages_remaining: # O(n)
        # find package in list that has lowest distance O(n)
        shortest_path, closest_package = nearest_neighbor(packages_remaining, distance_table, current_address) # type: ignore

        travel_time = shortest_path * (60/18) # calculate travel minutes
        current_time += travel_time # add to current time

        distance_traveled += shortest_path # add distance to total
        current_address = get_package_address(closest_package) # O(a)

        Package.set_delivery_time(closest_package, current_time)

        route_list.append(closest_package) # Add it to route list
        packages_remaining.remove(closest_package) # remove package with shortest path --> O(p) avg

    # add return distance to total --> O(d)
    return_travel =  get_distance(current_address, "HUB", distance_table)
    distance_traveled += return_travel

    return route_list, distance_traveled, current_time
    #print(distance_traveled) print(route_list)

# Time Complexity: O(p * (a + n))
# Space Complexity: O(1)
def nearest_neighbor(package_list, distance_table, current_address):
        shortest_path = float("inf")
        closest_package = None
        for package in package_list: # O(p)
                package_address = get_package_address(package) # O(a)

                distance = get_distance(current_address, package_address, distance_table) # O(n)

                if distance < shortest_path:
                    shortest_path = distance
                    closest_package = package

        return shortest_path, closest_package

# Time Complexity: O(n)
# Space Complexity: O(n) (creating a list)
def get_distance(from_address, to_address, distance_table):
    # put addresses into list for comparing
    addresses = list(distance_table.keys()) # O(n)

    if from_address == to_address: # O(1)
        return 0.0

    index1 = addresses.index(from_address) # O(n)
    index2 = addresses.index(to_address) # O(n)
    # finds distance in bottom part of csv file based on which index is greater
    if index1 > index2:
        distance = distance_table[from_address][index2] # O(1)
    else:
        distance = distance_table[to_address][index1] # O(1)
    return float(distance) # O(1)
###################################################################################################
# Time Complexity: O(n)
# Space Complexity: O(1)
# loops through and prints packages in route of specified truck
def print_route_list(route_list, truck_num):
    print(UI.head + f"Truck {truck_num} Route:" + UI.green)
    for package in route_list:
        print(package)
    UI.reset

# Time Complexity: O(4n) --> O(n)
# Space Complexity: O(n) (replaces creates new instance)
# fixes address for later comparisons
def format_address(address):
    address = address.strip()
    address = address.replace("South", "S")
    address = address.replace("North", "N")
    address = address.replace("East", "E")
    address = address.replace("West", "W")
    return address

# Time Complexity: O(n x m) n = addresses, m = format_address
# Space Complexity: O(1)
# fixes all data
def format_distance_table(distance_table):
    formatted_table = {}

    for address, distances in distance_table.items(): # O(n)
        fixed_address = format_address(address) # O(n)
        formatted_table[fixed_address] = distances

    return formatted_table

# Time Complexity: O(n)
# Space Complexity: O(n) 
# returns package address & zipcode
def get_package_address(package):
    address = format_address(Package.get_address(package))
    zipcode = str(Package.get_zipcode(package)).strip()

    return f"{address} ({zipcode})"

# Time Complexity: O(1)
# Space Complexity: O(1)
# returns status depending on if the delivery time has passed in simulation
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

# Time Complexity: O(1)
# Space Complexity: O(1)
# formats inputted minutes to 12hr AM/PM format
def format_time(mins):
    hours = int(mins // 60)
    mins = int(mins % 60)

    if hours >= 12:
        tod = "PM"
    else:
        tod = "AM"

    display_hour = hours % 12
    if display_hour == 0:
        display_hour = 12

    return f"{display_hour}:{mins:02d} {tod}"

# Time Complexity: O(1)
# Space Complexity: O(1)
def format_minutes(time_entered):
    time_entered = time_entered.strip().upper()

    time = time_entered.split(":")
    hours = int(time[0])
    # seperate string for calculations
    minute_part = time[1].split()
    mins = int(minute_part[0])
    period = minute_part[1]
    # Add 12hrs depending on am or pm
    if period == "PM" and hours != 12:
        hours += 12
    elif period == "AM" and hours == 12:
        hours = 0

    return hours * 60 + mins


# Time Complexity: O(n), n = # of pkgs
# Space Complexity: O(1)
# prints info & status of packages by truck
def print_package_statuses(package_list, time_entered, truck_time, truck_finish_time, truck_distance):
    print(UI.reset + f"Time Entered: {format_time(time_entered)}")
    print(f"Start Time: {format_time(truck_time)}    Finish Time: {format_time(truck_finish_time)}")
    print(f"Miles Traveled: {truck_distance:.2f} mi")
    print("#####################################################################################")
    print("ID   ADDRESS               STATUS               EST. DELIVERY TIME     CONSTRAINTS")
    print("#####################################################################################")
    for package in package_list:

        status = get_package_status(package, time_entered, truck_time)
        delivery_time = format_time(Package.get_delivery_time(package))
        #print(f"{package}  --| Est. Delivery: {delivery_time}")
        print(f"{Package.get_id(package)}:  {Package.get_address(package)},   -->  {status}      --| Est. Delivery: {delivery_time}  --| Deadline: {Package.get_deadline(package)}   {Package.get_status(package)}")

# Time Complexity: O(n1 + n2 + n3) --> O(n), n = # of pkgs
# Space Complexity: O(1)
# prints info & status of packages of all trucks
def print_all_statuses(time_entered):
    print(UI.head + "TRUCK #1" + UI.reset)
    print_package_statuses(truck1_route_list, time_entered, truck1_time, truck1_finish_time, truck1_distance_traveled)
    print(UI.head + "TRUCK #2" + UI.reset)
    print_package_statuses(truck2_route_list, time_entered, truck2_time, truck2_finish_time, truck2_distance_traveled)
    print(UI.head + "TRUCK #3" + UI.reset)
    print_package_statuses(truck3_route_list, time_entered, truck3_time, truck3_finish_time, truck3_distance_traveled)

# Time Complexity: O(n), n = # of pkgs
# Space Complexity: O(1)
# asks user for options and prints status info accordingly
def status_options():
    print(UI.head + "PACKAGE STATUS" + UI.reset)

    time_entered = (input(UI.green + "Enter a time:  "))
    time_entered = format_minutes(time_entered)

    truck_amt = input("Enter ALL or Truck #: ")
    if truck_amt == '1':
        print_package_statuses(truck1_route_list, time_entered, truck1_time, truck1_distance_traveled)
    elif truck_amt == '2':
        print_package_statuses(truck2_route_list, time_entered, truck2_time, truck2_distance_traveled)
    elif truck_amt == '3':
        print_package_statuses(truck3_route_list, time_entered, truck3_time, truck3_distance_traveled)
    elif truck_amt == 'ALL':
        print_all_statuses(time_entered)
    else:
        print("Invalid Selection")
    
####################################################################################################
# times
truck1_time = 545 # (9:05 am)
truck2_time = 480 # (8:00 am)
truck3_time = 600 # (10:00 am)
distance_traveled = 0.0
    
# take truck's package list and find it in distance data
truck1_packages = truck1.get_package_list()  #hashmap
truck2_packages = truck2.get_package_list()
truck3_packages = truck3.get_package_list()
    
distance_data = get_distance_info() 
distance_data = format_distance_table(distance_data)
#print(distance_data["1060 Dalton Ave S (84104)"][0])
        
truck1_route_list, truck1_distance_traveled, truck1_finish_time = build_route(truck1_packages, distance_data, truck1_time)
truck2_route_list, truck2_distance_traveled, truck2_finish_time = build_route(truck2_packages, distance_data, truck2_time)
truck3_route_list, truck3_distance_traveled, truck3_finish_time = build_route(truck3_packages, distance_data, truck3_time)
    
total_distance = truck1_distance_traveled + truck2_distance_traveled + truck3_distance_traveled
###################################################################################################
def run_simulation():

    # MENU OPTIONS
    print(UI.head + "Please choose an option from below by entering the specific key value: ")
    print(UI.blue + "Display ALL Package Status: " + UI.yellow + 'a')
    print(UI.blue + "Display Package Status: " + UI.yellow + "s ")
    print(UI.blue + "Display Truck Mileage Totals: " + UI.yellow + "m ")
    print(UI.blue + "Lookup Package Information by ID: " + UI.yellow + "l")
    option = input(UI.yellow)

    match option:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        case 'a':
            print(UI.head + "ALL PACKAGE STATUSES")
            time_entered = input(UI.green + "Enter a time (ex 10:30 am): ")
            time_entered = format_minutes(time_entered)
            if time_entered >= 620: # 10:20 AM package #9 updates
                            package_9 = pkg_reader.get_package_by_id('9')
                            #Correct address for #9 below
                            # AFTER 10:20 am # 410 S State St., Salt Lake City, UT 84111
                            Package.update(package_9, "410 S State St", "Salt Lake City", "84111", "AFTER 10:20am", " ")
            print_all_statuses(time_entered)

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        case 's': # STATUSES & TIME
            print(UI.head + "PACKAGE STATUS" + UI.reset)
            
            time_entered = input(UI.green + "Enter a time (ex 10:30 am):  ")
            time_entered = format_minutes(time_entered)

            if time_entered >= 620: # 10:20 AM package #9 updates
                package_9 = pkg_reader.get_package_by_id('9')
                #Correct address for #9 below
                # AFTER 10:20 am # 410 S State St., Salt Lake City, UT 84111
                Package.update(package_9, "410 S State St", "Salt Lake City", "84111", "AFTER 10:20am", " ")

            truck_amt = input("Enter ALL or Truck #: ")
            if truck_amt == '1':
                print_package_statuses(truck1_route_list, time_entered, truck1_time, truck1_finish_time, truck3_distance_traveled)
            elif truck_amt == '2':
                print_package_statuses(truck2_route_list, time_entered, truck2_time, truck2_finish_time, truck3_distance_traveled)
            elif truck_amt == '3':
                print_package_statuses(truck3_route_list, time_entered, truck3_time, truck3_finish_time, truck3_distance_traveled)
            elif truck_amt =="ALL":
                print_all_statuses(time_entered)
            else:
                print("Invalid Selection")

        # Time Complexity: O(1)
        # Space Complexity: O(1)
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

        # Time Complexity: O(1)
        # Space Complexity: O(1)
        case 'l': # PACKAGE LOOKUP
            entered_id = input("Enter a package ID to lookup data: ")
            data = pkg_reader.get_package_by_id(entered_id) # O(1)
            print(data)

    print(UI.blue + "Back to Menu: " + UI.yellow + "b ")
    print(UI.blue + "Quit Simulation: " + UI.yellow + "ANY ")

    # MORE CHOICES OR END SIMULATION
    option = input(UI.yellow)
    if option == 'b':
        run_simulation() # O(n), runs n times --> recursive
    else:
        print(UI.red + "Ending Simulation")
        time.sleep(1)
        print("GOODBYE" + UI.reset)
###################################################################################################
# START OF PROGRAM
start = input(UI.green + "Greetings, initiate Delivery Driver Simulation?  y/n:  " + UI.yellow)

if start == 'y' or start =='Y':
    # run simulation
    print(UI.green + "STARTING SIMULATION" + UI.reset)
    time.sleep(1)
    run_simulation()
else:
    print(UI.red + "GOODBYE" + UI.reset)