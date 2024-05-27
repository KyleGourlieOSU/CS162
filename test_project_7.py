"""This test program checks for proper inheritance and proper handling of incorrect data input types.

To see if all attributes from the engine, transmission, and chassi were inherited and incorporated into
the car/truck, printing the object calls up all valuable parameters. If parameters were not inherited, 
exceptions would occur at this step. Successful implementation of this is shown in `test_car_creation()`
and `test_truck_creation()`. Seeing if incorrect data types for inputs within the classes are tested in
the rest of the tests. 
"""

from project_7 import Car, Truck, Engine, Tranny

def test_car_creation():
    my_car = Car(capacity=5, mass=2000,
                drag_coef=0.3, year=1994, brand='Toyota', 
                engine=Engine(type='petrol', config='I4', displ=2.4, hprs=105, torq=95),
                tranny=Tranny(type='manual', gears=5))
    my_car.run()
    print(my_car)

def test_truck_creation():
    my_truck = Truck(bed_type='short', cab_type='crew', mass=4000,
                drag_coef=0.3, year=2005, brand='Chevy', 
                engine=Engine(type='diesel', config='V8', displ=6.7, hprs=600, torq=700),
                tranny=Tranny(type='automatic', gears=8))
    my_truck.run()
    print(my_truck)

def test_car_wrong_param_creation():
    """Will fail due to 'five' not being an integer"""
    my_car = Car(capacity='five', mass=2000,
                drag_coef=0.3, year=1994, brand='Toyota', 
                engine=Engine(type='petrol', config='I4', displ=2.4, hprs=105, torq=95),
                tranny=Tranny(type='manual', gears=5))
    my_car.run()
    print(my_car)

def test_truck_wrong_param_1_creation():
    """Will fail due to 'shorts' not being a valid bed type"""
    my_truck = Truck(bed_type='shorts', cab_type='crew', mass=4000,
                drag_coef=0.3, year=2005, brand='Chevy', 
                engine=Engine(type='diesel', config='V8', displ=6.7, hprs=600, torq=700),
                tranny=Tranny(type='automatic', gears=8))
    my_truck.run()
    print(my_truck)

def test_truck_wrong_param_2_creation():
    """Will fail due to 'crews' not being a valid cab type"""
    my_truck = Truck(bed_type='short', cab_type='crews', mass=4000,
                drag_coef=0.3, year=2005, brand='Chevy', 
                engine=Engine(type='diesel', config='V8', displ=6.7, hprs=600, torq=700),
                tranny=Tranny(type='automatic', gears=8))
    my_truck.run()
    print(my_truck)


def test_truck_params():
    """test fails due to `repair()` should only be used in `run()` method, not by itself"""
    my_truck = Truck(bed_type='short', cab_type='crew', mass=4000,
            drag_coef=0.3, year=2005, brand='Chevy', 
            engine=Engine(type='diesel', config='V8', displ=6.7, hprs=600, torq=700),
            tranny=Tranny(type='automatic', gears=8))
    my_truck.repair()
    my_truck.run()
    print(my_truck)

def test_car_params():
    """test fails due to `repair()` should only be used in `run()` method, not by itself"""
    my_car = Car(capacity=5, mass=2000,
                drag_coef=0.3, year=1994, brand='Toyota', 
                engine=Engine(type='petrol', config='I4', displ=2.4, hprs=105, torq=95),
                tranny=Tranny(type='manual', gears=5))
    my_car.repair()
    my_car.run()
    print(my_car)


        


