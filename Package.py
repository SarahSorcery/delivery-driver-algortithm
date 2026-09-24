from UI import UI
# Package Object

class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
            return f"{self.id}, {self.address}, {self.deadline}, {self.status}"

    def get_id(self):
        return self.id

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_zipcode(self):
        return self.zipcode

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode


    def update(self, new_address, new_city, new_zipcode, new_deadline, new_status):
        self.address = new_address
        self.city = new_city
        self.zipcode = new_zipcode
        self.deadline = new_deadline
        self.status = new_status

#     def print_info(self):
#         print(UI.head + "ID: " +str(self.id))
#         print(UI.green + "Address: " + self.address)
#         print("City: " + self.city)
#         print("State: " + self.state)
#         print("Zipcode: " + self.zipcode)
#         print("Deadline: " + str(self.deadline))
#         print("Weight: " + self.weight)
#         print("Status: " + self.status + UI.reset)
#         print("********************************")

# ## might need work?
#     def print_info_by_id(self, id):
#         if id is not None:
#             self.print_info()
