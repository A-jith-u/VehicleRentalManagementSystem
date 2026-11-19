from vehicle import Vehicle

class Bike(Vehicle):                 #Creating a subclass Bike which inherits the Vehicle class
    def calculate_rent(self,days):   #Calculating the rent of the bike by multiplying the rental price with the number of days and adding a service charge of 100
        rent=self.rental_price*days+100
        print(f" The rent of the bike for {days} days is {rent} (+ 100 for service charge)")  

