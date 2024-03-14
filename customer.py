import datetime


class Customer:
    """ Customer class creates a new customers objects """
    def __init__(self, name: str, surname: str, phone: str):
        """ Constructor for customers. Creates customers with name, surname, phone and time of creation
        :param name: the name of the customer
        :type name: str
        :param surname: the surname of the customer
        :type surname: str
        :param phone: the phone number of the customer
        :type phone: str
        :rtype: object
        """
        self.name = name
        self.surname = surname
        self.email = f"{self.name}.{self.surname}@company_name.com"
        self.phone = phone
        self.registration_time = datetime.datetime.now()

    def __str__(self):
        """
        String representation of customer
        :return: A string
        :rtype: str
        """
        return f"""
        name: {self.name}, surname: {self.surname}, phone: {self.phone}, email: {self.email}
            registered: {self.show_date_time()}"""

    def show_date_time(self):
        """
        The date and time when the customer was created
        :return: A string
        :rtype: str
        """
        return datetime.datetime.strftime(self.registration_time, '%d.%m.%Y, %H:%M:%S')


class UpgradedCustomer(Customer):
    """
    Upgraded customer class. Inherits from Customer class. Adds address and date of birth.
    :rtype: object
    """
    def __init__(self, name: str, surname: str, phone: str):
        """
        Constructor for upgraded customers - inherits name, surname, phone and time of creation.
        Adds empty address and fills date of birth to customer
        :param name: the name of the customer
        :type name: str
        :param surname: the surname of the customer
        :type surname: str
        :param phone: the phone number of the customer
        :type phone: str
        :rtype: object
        """
        super().__init__(name, surname, phone)
        self.address = {}
        self.__birth = datetime.datetime.now()
        self.add_date_of_birth()

    def __str__(self):
        """
        String representation of customer
        :return: A string
        :rtype: str
        """
        return f"""
        name: {self.name}, surname: {self.surname}, phone: {self.phone}, email: {self.email}
            registered: {self.show_date_time()}, city {self.address["city"]}, age: {self.calculate_age(self.__birth)}"""

    @property
    def birth(self):
        """
        The date of birth of the customer
        :return: A string
        :rtype: str
        """
        return self.__birth

    @birth.setter
    def birth(self, new_birth_date: str):
        """Changes date of birth of the customer"""
        while True:
            try:
                self.__birth = datetime.datetime.strptime(new_birth_date, "%d.%m.%Y")
                print(f"Successfully changed date of birth to: {self.__birth}")
                break
            except ValueError:
                print("Invalid date format. Please enter date in the format dd.mm.YYYY.")
                new_birth_date = input("Enter Your date of birth (dd.mm.YYYY):\n")

    @staticmethod
    def calculate_age(date_of_birth: datetime.datetime):
        """
        Calculate the age (in years) based on the provided date of birth.
        :param date_of_birth: date of birth
        :rtype: int
        """
        now = datetime.datetime.now()
        age = now.year - date_of_birth.year
        if now.month < date_of_birth.month or (now.month == date_of_birth.month and now.day < date_of_birth.day):
            age -= 1
        return age

    def add_date_of_birth(self):
        """
        Sets bithday to Upgraded customer
        :return: Nothing
        :rtype: None
        """
        while True:
            user_input = input("Enter the date of birth (dd.mm.YYYY):\n")
            try:
                self.__birth = datetime.datetime.strptime(user_input, "%d.%m.%Y")
                break
            except ValueError:
                print("Invalid date format. Please enter date in the format dd.mm.YYYY.")
