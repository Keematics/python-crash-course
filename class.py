from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """This class represents a specific type of Restaurant"""
    def __init__(self, name, cuisine_type):
        """Inherits from the base class - Restaurant"""
        super().__init__(name, cuisine_type)
        self.flavours = ["Chocolate", "Vanilla"]

    def display_flavours(self):
        """Simulate displaying flavours to users"""
        for flavour in self.flavours:
            print(f"We have {flavour} flavour\n")
        
    

restaurant = Restaurant("Continental", "Falafel")
myicecreamstand = IceCreamStand("Kim's stand", "Sweetened")
myicecreamstand.display_flavours()
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
