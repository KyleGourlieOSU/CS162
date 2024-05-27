"""## project_7.py- This program models inheritance and exception handling through the creation of a vehicle


The creation of a vehicle required the creation of a chassis, and then a choice of either a car or a truck. To create the 
chassis of the vehicle, an engine and transmission need to be created. The engine and
transmission classes have required attributes to simulate possible engine and transmission options respectfully.
Once the transmission and engine are created, they are then added to the chassis as required attributes of the
chassis. Once the chassis has been created, the last step is choosing a car or truck layout. Whatever choice 
has been made, all attributes are inherited from the car or truck object. This would be the child class of the Chassis
class. A special method that the chassis has is run() and repair(). Their methods have the purpose of showing how
to handle exceptions in the program. The exception occurs when the engine or transmission is broken through the method
repair(). This essentially chooses to randomly either break the engine or the transmission by setting the entire chassis
attributes to None. The run() method undoes this and the vehicle is fixed.


### Design:
The design of the script was completed by a diagram included within the zip file that this script is located at.


### Testing:
The testing of this program can be found under test_project_7.py


### Author:
Kyle Gourlie
"""

#imports
import random
import copy



class Engine:
    """## _summary_:
    Defines an engine object to simulate the creation of an engine given its specifications

    ### Parameters:
    - `type(str)`: type of engine such as petrol, diesel, EV, hybrid, etc.
    - `config(str)`: configuration of the engine such as I4, V6, V8, Electric, etc.
    - `displ(float)`: the displacement, in liters, of the engine.
    - `hprs(float)`: the peak horsepower of the engine in units of hprs.
    - `torque(float)`: the peak torque of the engine in ft-lbs.
    """ 
    def __init__(self, type: str, config: str, displ: float,
                hprs: float, torq: float):
        self.type = str(type)
        self.config = str(config)
        self.displ = abs(float(displ))
        self.hprs = abs(float(hprs))
        self.torq = abs(float(torq))
   
    def repair(self)-> bool:
        """Checks to see if the engine needs to be repaired or not
        
        returns:
        - False (bool): if engine does not need to be repaired
        - True (bool): if the engine does need to be repaired
        """
        #randomly determines if repair is needed
        num = random.random()
        if num < 0.5:
            return False
        else:
            return True
        
    def __str__(self):
        return (f'Engine Type: {self.type}\n'
                f'Engine Configuration: {self.config}\n'
                f'Engine Displacement: {self.displ}\n' 
                f'Engine Horsepower: {self.hprs}\n'
                f'Engine Torque: {self.torq}\n')



class Tranny:
    """## _summary_:
    Defines a Transmission object to simulate the creation of one given its specification

    ### Parameters:
    - `type(str)`: type of transmission such as manual, automatic, belt, etc.
    - `gears(int)`: number of gears within the transmission. 
    """
    def __init__(self, type: str, gears: int):
        self.type = str(type)
        self.gears = abs(gears)
           
    def repair(self):
        """Checks to see if the transmission needs to be repaired or not
        
        returns:
        - False (bool): if transmission does not need to be repaired
        - True (bool): if the transmission does need to be repaired
        """
        num = random.random()
        if num < 0.5:
            return False
        else:
            return True
        
    def __str__(self):
        return (f'Transmission Type: {self.type}\n'
                f'Number of Gears: {self.gears}\n')



class Chassis:
    """## _summary_: 
    Defines a Chassis Object for the Construction of a Vehicle

    ### Parameters:
    - `mass(float)`: mass of chassis in kg.
    - `drag_coef(float)`: drag coefficent of the chassis
    - `year(int)`: year that the vehicle was made
    - `brand(str)`: the brand of the vehicle
    - `Engine(Engine Object)`: the engine placed on the chassis
    - `Transmission(Tranny Object)`: the transmission placed on the chassis
    """
    def __init__(self, mass: float, drag_coef: float, year: int,
                 brand: str, engine: Engine, tranny: Tranny):
        self.mass = abs(float(mass))
        self.drag_coef = abs(float(drag_coef))
        self.year = abs(int(year))
        self.brand = str(brand)
        self.Engine = engine
        self.Tranny = tranny

    def repair(self):
        """repair method for actually working on the chassis
        """
        #makes copies of the good parts
        self.good_eng = copy.deepcopy(self.Engine)
        self.good_tranny = copy.deepcopy(self.Tranny)
        #sees which parts needs to be repaired
        repair_eng = self.Engine.repair()
        repair_tranny = self.Tranny.repair()
        #sets the part that needs to be replaced as None
        if repair_eng:
            self.Engine = None
        elif repair_tranny:
            self.Tranny = None

    def fix_engine(self):
        """fixes the engine"""
        self.Engine =self.good_eng
    
    def fix_tranny(self):
        """fixes the transmission"""
        self.Tranny = self.good_tranny

    def run(self):
        """turns on the vehicle and takes it out for a drive"""
        self.repair()
        #if repair needed, exception of AttributeError will occur
        try:
            #Just grabbing a parameter from each class to see if they exist
            on_engine = self.Engine.torq
            on_tranny = self.Tranny.gears
            print('Your vehicle has been started correctly')

        except AttributeError:
            print('Your vehicle needs to be repaired')
            #going through each possibility of a broken part.
            #code structure would need to be re-evaluated for more than 2 broken parts
            if self.Engine == None:
                print("Engine needs to be fixed")
                input('Press ENTER to fix engine')
                self.fix_engine()
                print('Engine fixed')
                if self.Tranny == None:
                    print("Transmission needs to be fixed")
                    input('Press ENTER to fix Transmission')
                    print('Transmission fixed')
                    self.fix_tranny()
                
            elif self.Tranny == None:
                print("Transmission needs to be fixed")
                input('Press ENTER to fix Transmission')
                self.fix_tranny()
                print('Transmission fixed')
                if self.Engine == None:
                    print("Engine needs to be fixed")
                    input('Press ENTER to fix engine')
                    self.fix_engine()
                    print('Engine fixed')
            
            #Just grabbing a parameter from each class to see if they exist
            on_engine = self.Engine.torq
            on_tranny = self.Tranny.gears
            print('Your vehicle has been started correctly')
            print(self)



class Truck(Chassis):
    """## _summary_:
    Defines a Child Class of `Truck` from Parent `Chassis`

    ### Parameters:
        - `bed_type(str)`: type of bed on the truck such as short, mid, and long.
        - `cab_type(str)`: tyoe of cab on the truck such as regular, extended, and crew.
    """
    def __init__(self, bed_type: str, cab_type: str, mass,
                 drag_coef, year, brand, engine, tranny):
        super().__init__(mass, drag_coef, year, brand, engine, tranny)
        bed_types=['short','mid','long']
        cab_types=['regular','extended','crew']
        capacities = {
            'regular' : 3,
            'extended' : 5,
            'crew' : 6}
        self.bed_type = str(bed_type)
        self.cab_type = str(cab_type)
        #want to raise errors on purpose because of project specification of unhandled exception
        if self.bed_type not in bed_types:
            raise ValueError(f"'{self.bed_type}' is not a valid choice")
        elif self.cab_type not in cab_types:
            raise ValueError(f"'{self.cab_type}' is not a valid choice")
        #ensuring that the capacity size comes from cab size
        self.cap = capacities[cab_type]
    
    def __str__(self):
        return (f'\nYear: {self.year}\n'
                f'Brand: {self.brand}\n'
                f'Capacity: {self.cap}\n'
                f'Model: Truck\n'
                f'Cab size: {self.cab_type}\n'
                f'\nEngine Specifications:\n'
                f'{self.Engine}\n'
                f'Transmission Specifications:\n'
                f'{self.Tranny}\n'
                )
     


class Car(Chassis):
    """## _summary_:
    Defines a Child Class of `Car` from Parent `Chassis`

    ### Parameters:
        - `cap(int)`: seat capacity of the car.
    """
    def __init__(self, capacity: int, mass,
                 drag_coef, year, brand, engine, tranny):
        super().__init__(mass, drag_coef, year, brand, engine, tranny)
        self.cap = abs(int(capacity))

    def __str__(self):
        return (f'\nYear: {self.year}\n'
                f'Brand: {self.brand}\n'
                f'Capacity: {self.cap}\n'
                f'Model: Car\n'
                f'\nEngine Specifications:\n'
                f'{self.Engine}\n'
                f'Transmission Specifications:\n'
                f'{self.Tranny}\n')