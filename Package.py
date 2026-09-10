# Package Object

class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
        self.id: int = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def get_id(self):
        return self.id

    def get_status(self):
        return self.status

    def print_info(self):
        print("ID: " +str(self.id))
        print("Address: " + self.address)
        print("City: " + self.city)
        print("State: " + self.state)
        print("Zipcode: " + self.zipcode)
        print("Deadline: " + str(self.deadline))
        print("Weight: " + self.weight)
        print("Status: " + self.status)
        print("********************************")

## might need work?
    def print_info_by_id(self, id):
        if id is not None:
            self.print_info()

# delivery ID
# delivery address
# delivery deadline
# delivery city
# delivery state
# delivery zip code
# package weight
# delivery status