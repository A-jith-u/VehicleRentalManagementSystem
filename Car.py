from vehicle import Vehicle

class Car(Vehicle):                   #Creating a subclass Car which inherits the Vehicle class
    def calculate_rent(self,days):     #Calculating the rent of the car by multiplying the rental price with the number of days and adding a service charge of 500
        rent=self.rental_price*days+500
        print(f" The rent of the car for {days} days is {rent} (+ 500 for service charge)")
