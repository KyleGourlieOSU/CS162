from project_7 import Car, Truck, Engine, Tranny

#While I could have added user input for the parameters of each vehicle, I decided not to, 
#and to focus on more of the testing aspect and class structure of the program. Some of this
#program has chunks that I already created from project 1, where I did have user input for 
#all of the parameters of the vehicles
if __name__ == "__main__":
    my_truck = Truck(bed_type='short', cab_type='crew', mass=4000,
                drag_coef=0.3, year=2005, brand='Chevy', 
                engine=Engine(type='diesel', config='V8', displ=6.7, hprs=600, torq=700),
                tranny=Tranny(type='automatic', gears=8))
    my_truck.run()

    my_car = Car(capacity=5, mass=2000,
                drag_coef=0.3, year=1994, brand='Toyota', 
                engine=Engine(type='petrol', config='I4', displ=2.4, hprs=105, torq=95),
                tranny=Tranny(type='manual', gears=5))
    my_car.run()