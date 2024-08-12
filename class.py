class Restaurant:
    def __init__(self, name, cuisine_type):
        """Initializes the name and cuisine_type attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.login_attempts = 0
    
    def describe_restaurant(self):
        """Describes the restaurant"""
        print("Home away from home")

    def open_restaurant(self):
        """Tells the customers that the restaurant is now open"""
        print("Dear customers, we're now open!")
    
    def increment_login_attempts(self):
        """Increases the login attempts by 1 when called"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the login attempts to 0 when called"""
        self.login_attempts = 0

    def print_login_attempts(self):
        """Prints the login attempts before it was reset"""
        print(self.login_attempts)

restaurant = Restaurant("Continental", "Falafel")
print(restaurant.name, f"\nThe secrete lies in our {restaurant.cuisine_type} cuisine")
print("-------")
restaurant.describe_restaurant()
print("-------")
restaurant.open_restaurant()
print("-------")
restaurant.increment_login_attempts()
restaurant.increment_login_attempts()
restaurant.increment_login_attempts()
restaurant.increment_login_attempts()
print("-------")
restaurant.print_login_attempts()
print("-------")
restaurant.reset_login_attempts()
print(".........printing reset login attempts now........")
restaurant.print_login_attempts()
