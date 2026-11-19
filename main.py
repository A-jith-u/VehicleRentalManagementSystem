
#************************************************
#**************VEHICLE RENTAL MANAGEMENT*********
#************************************************

from Car import Car
from Bike import Bike

print("**********VEHICLE RENTAL MANAGEMENT**********")
print("\n")

car=Car("Maruti Suzuki","Daily use","KL01AB1234",6000)            #Creating an object of the Car class and passing the required arguments to the constructor
bike=Bike("Honda","Hourly","KL02CD5678",200)                      #Creating an object of the Bike class and passing the required arguments to the constructor

car.display_vehicle_details()                                     #Displaying the details of the car by calling the display_vehicle_details method of the Car class
car.calculate_rent(3)                                             #Calculating the rent of the car for 5 days by calling the calculate_rent method of the Car class

print("______________________________________________")

bike.display_vehicle_details()                                     #Displaying the details of the bike by calling the display_vehicle_details method of the Bike class
bike.calculate_rent(3)                                             #Calculating the rent of the bike for 3 days by calling the calculate_rent method of the Bike class
