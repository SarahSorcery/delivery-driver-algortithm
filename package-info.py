import csv
import packageObject as pkg


package_list = []


def get_package_info(package_file_path):
    #fill with actual fetching for hash table
    with open(package_file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        #create 1d array for now
        #target_list = []

        for line in reader:
            #target_list.append(line)

            #object testing
            package_id, address, city, state, zipcode, deadline, weight, status = line
            package_list.append(pkg.Package(package_id, address, city, state, zipcode, deadline, weight, status))

    #return target_list


def print_package_info(target_list):
    for item in target_list:
        print(item)

#test_list = get_package_info("WGUPS-package-file.csv")
#print_package_info(test_list)

#pkg.Package.print_info(package_list[22])

# populate list of packages from source CSV file
get_package_info("WGUPS-package-file.csv")

for item in package_list:
    pkg.Package.print_info(item)


###################################################################################################

# TESTING A HASH TABLE IMPLEMENTATION
hash_list = [
    [],[],[],[],[],[],[],[],[],[]
]



# we need to grab the ID, hash that value, and store the entire piece of data into the "bucket"
def add_hash(item):
    index = hash_function(item)
    hash_list[index].append(item)
    #return index

def hash_function(item):
    return item % 10