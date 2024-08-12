class Restaurant:
    def __init__(self, name, cuisine_type):
        """Initializes the name and cuisine_type attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describes the restaurant"""
        print("Home away from home")

    def open_restaurant(self):
        """Tells the customers that the restaurant is now open"""
        print("Dear customers, we're now open!")

restaurant = Restaurant("Continental", "Falafel")
print(restaurant.name, f"\nThe secrete lies in our {restaurant.cuisine_type} cuisine")
print("-------")
restaurant.describe_restaurant()
print("-------")
restaurant.open_restaurant()