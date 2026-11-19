from abc import ABC,abstractmethod

class Vehicle(ABC):                                #Creating an abstract class Vehicle which inherits the ABC class

    def __init__(self,vehicle_name,vehicle_type,vehicle_number,rental_price):
        self.vehicle_name=vehicle_name
        self.vehicle_type=vehicle_type
        self.vehicle_number=vehicle_number
        self.__rental_price=rental_price

    @abstractmethod                                  #Creating an abstract method calculate_rent which will be implemented in the subclasses
    def calculate_rent(self,days):
        pass

    def display_vehicle_details(self):               #Creating a method to display the details of the vehicle
        print(f" The vehicle name is:{self.vehicle_name}\n The vehicle type is:{self.vehicle_type}\n The vehicle number is:{self.vehicle_number}\n The rental price is:{self.__rental_price}")

    @property                                    
    def rental_price(self):                           #Creating a property decorator to access the private attribute __rental_price
        return self.__rental_price

    @rental_price.setter                               #Creating a setter method to set the value of the private attribute __rental_price
    def rental_price(self,value):
        self.__rental_price=value



    


