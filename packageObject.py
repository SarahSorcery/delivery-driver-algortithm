# Package Object

class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, status):
        self.package_id: int = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def get_id(self):
        return self.package_id

    def get_status(self):
        return self.status

    def print_info(self):
        print("ID: " +str(self.package_id))
        print("Address: " + self.address)
        print("City: " + self.city)
        print("State: " + self.state)
        print("Zipcode: " + self.zipcode)
        print("Deadline: " + str(self.deadline))
        print("Weight: " + self.weight)
        print("Status: " + self.status)
        print("********************************")


    def print_info_by_id(self, package_id):
        package = package_id
        if package is not None:
            package.print_info()

# delivery ID
# delivery address
# delivery deadline
# delivery city
# delivery state
# delivery zip code
# package weight
# delivery status