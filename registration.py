from customer import Customer, UpgradedCustomer
from decorators import admin_only


class RegistrationForm:
    """
    Registration class starts a registration process for customers.
    """
    TOTAL_NUMBER_OF_REGISTRATIONS = 0

    def __init__(self):
        """
        Constructor for registration. Creates empty customer list. Starts registration method
        :rtype: object

        """
        RegistrationForm.TOTAL_NUMBER_OF_REGISTRATIONS += 1
        self.customer_list = []
        self.show_options()

    @classmethod
    def show_number_of_registrations(cls):  # choice 7
        """
        Shows total number of registrations finished
        :return: total number
        :rtype: int
        """
        return cls.TOTAL_NUMBER_OF_REGISTRATIONS

    @staticmethod
    def validate_customer():
        """
        Validates customer name and surname if it's not empty
        :return: customer name, surname and phone
        :rtype: tuple
        """
        while True:
            name = input("Enter customer name:\n").capitalize()
            surname = input("Enter customer surname:\n").capitalize()
            if name and surname:
                return name.strip(), surname.strip()
            else:
                print("No name or surname given. Please enter a valid name and surname.")

    @staticmethod
    def validate_phone():
        """
        Validates customer phone
        :return: prefix and phone
        :rtype: str
        """
        while True:
            phone = (input("Enter Your phone with prefix:\n"))
            if phone:
                if len(phone) < 9:
                    print("The number is too short. Please enter a valid phone number.")
                if len(phone) == 9:
                    prefix = input("Enter Your phone prefix:\n")
                    phone = prefix + phone
                    return phone.strip()
                elif len(phone) > 9:
                    return phone.strip()
            else:
                print("No number given. Please enter a valid phone number.")

    @staticmethod
    def validate_address(user_input):
        """
        Validates customer address inputs if it's not empty
        :param user_input: input from user
        :type user_input: str
        :return: stripped user input
        :rtype: str
        """
        while True:
            if user_input:
                return user_input.strip()
            else:
                user_input = input("No input given. Please enter a valid input.")

    @staticmethod
    def fill_in_address(customer: UpgradedCustomer):
        """
        Fills address for Upgraded Customers
        :return: Nothing
        :rtype: None
        """
        customer.address["city"] = RegistrationForm.validate_address(input("Enter the city:\n").capitalize())
        customer.address["street"] = RegistrationForm.validate_address(input("Enter the street:\n").capitalize())
        customer.address["street_no"] = RegistrationForm.validate_address(input("Enter the street number:\n"))
        customer.address["zip_code"] = RegistrationForm.validate_address(input("Enter the zip code:\n"))

    @staticmethod
    def choose_customer(to_do: list):
        """ Returns a position of a selected customer
        :param to_do: list of customers
        :return: position
        :type to_do: list
        """
        if len(to_do) > 1:
            position = int(input("Select a customer by a number:\n")) - 1
        elif len(to_do) == 1:
            position = 0
        else:
            position = None
        return position

    @staticmethod
    def display_customers(list_of_customers: list):  # for choice 3, 4
        """
        Prints all registered customers
        :param list_of_customers: list of customers
        :type list_of_customers: list
        :return: Nothing
        :rtype: None
        """
        if len(list_of_customers) == 0:
            print("No customers found")
        else:
            for number, customer in enumerate(list_of_customers, 1):
                print(f"Registered customer no.{number}, {customer}")

    def show_options(self):
        """
        Customer registration: add a new customer, display all, find, update, delete,
        display all registration forms and exit
        :return: Nothing
        :rtype: None
        """
        print("This is a registration form")
        while True:
            print("Choose an option:")
            print(""" 
            1. New customer (one time registration)
            2. New customer (full registration)
            3. Overview of all registered customers
            4. Find a customer
            5. Update existing customer
            6. Delete existing customer (requires admin privileges)
            7. Display total number of Registration Forms 
            8. End
            """)

            try:
                choice = int(input("Your choice?\n"))

                if choice == 1:  # add a new customer (one time registration)
                    print("One time registration customer")
                    self.add_new_customer(1)
                elif choice == 2:  # add a new customer (full registration)
                    print("Full registration customer")
                    self.add_new_customer(2)
                elif choice == 3:  # get overview of all registered customers
                    print("Overview of all registered customers")
                    self.display_customers(self.customer_list)
                elif choice == 4:  # find a customer
                    print("Find a customer:")
                    customer_to_find = self.validate_customer()
                    found_customers = self.find_customer(customer_to_find[0], customer_to_find[1])
                    self.display_customers(found_customers)
                elif choice == 5:  # update customer
                    print("Update existing customer:")
                    customer_to_update = self.validate_customer()
                    self.update_customer(customer_to_update[0], customer_to_update[1])
                elif choice == 6:  # delete customer
                    print("Delete existing customer:")
                    customer_to_delete = self.validate_customer()
                    self.delete_customer(customer_to_delete[0], customer_to_delete[1])
                elif choice == 7:  # show number of registration forms
                    print(f"Total number of Registration Forms created {self.show_number_of_registrations()}")
                elif choice == 8:  # exit program
                    print("Exiting the registration system")
                    return None

            except ValueError:
                print("A number has to be provided!")

    def add_new_customer(self, choice: int):  # choice 1 and 2
        """
        Adds a new customer to the list of customers
        :return: Nothing
        :rtype: None
        """
        customer_to_add = self.validate_customer()
        customer_phone = self.validate_phone()
        new_customer = None
        if choice == 1:
            new_customer = Customer(customer_to_add[0], customer_to_add[1], customer_phone)
        elif choice == 2:
            new_customer = UpgradedCustomer(customer_to_add[0], customer_to_add[1], customer_phone)
            self.fill_in_address(new_customer)
        self.customer_list.append(new_customer)
        print(f"Customer {customer_to_add[0]} {customer_to_add[1]} added to the system")

    def find_customer(self, name: str, surname: str):  # choice 3
        """
        Finds if a customer (by name and surname) has been registred.
        :param name: customer name
        :type name: str
        :param surname: customer surname
        :type surname: str
        :return: list of found customers
        :rtype: list
        """
        found_customers = []
        for customer in self.customer_list:
            if customer.name == name and customer.surname == surname:
                found_customers.append(customer)
        return found_customers

    def update_customer(self, name: str, surname: str):   # choice 5
        """
        Updates a customer = all entries
        :param name: customer name
        :type name: str
        :param surname: customer surname
        :type surname: str
        :return: Nothing
        :rtype: None
        """
        to_update = self.find_customer(name, surname)
        self.display_customers(to_update)
        if to_update:
            position = self.choose_customer(to_update)
            updated_customer = self.validate_customer()
            updated_phone = self.validate_phone()
            to_update[position].name = updated_customer[0]
            to_update[position].surname = updated_customer[1]
            to_update[position].phone = updated_phone

            if isinstance(to_update[position], UpgradedCustomer):
                self.fill_in_address(to_update[position])
                update_birth = input("""
                Do you want to update date of birth as well? 
                Requires admin password (y/n)\n""").lower()
                if update_birth == "y":
                    self.update_customer_birth(to_update[position])
                else:
                    pass

            print(f"Customer {to_update[position].name} {to_update[position].surname} updated in the system")

    @staticmethod
    @admin_only
    def update_customer_birth(upgraded_customer: UpgradedCustomer):
        upgraded_customer.birth = input("Enter Your date of birth (dd.mm.YYYY):\n")

    @admin_only
    def delete_customer(self, name: str, surname: str):  # choice 6
        """
        Deletes a customer from a list of customers
        :param name: customer name
        :type name: str
        :param surname: customer surname
        :type surname: str
        :return: Nothing
        :rtype: None
        """
        to_delete = self.find_customer(name, surname)
        self.display_customers(to_delete)
        if to_delete:
            position = self.choose_customer(to_delete)
            for customer in self.customer_list:
                if hash(customer) == hash(to_delete[position]):
                    self.customer_list.remove(customer)
                    print("Customer deleted from the system")
