

def admin_only(func):
    """
    Checks if you have the right password (you are admin)
    :param func:
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        enter_password = int(input("Enter password: "))
        password = 753951
        if enter_password == password:
            print("Permission granted")
            return func(*args, **kwargs)
        else:
            print("Permission denied. You are not admin")
    return wrapper
