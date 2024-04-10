"""This scripts instantiates a Vehicle object with attributes, methods, and class methods defining the engine and transmission.

The class Vehicle requires attributes related to the general characteristics of the vehicle that are important for its physical
description such as its mass, and general manufactoring information. Three methods are present. The first is __str___(), which 
returns the name of the vehicle. The second is get_mpg(). This 'calculates' the estimated miles per gallon of the vehicle. Note
that this method is completely inaccurate. Its purpose is to show what possible parameters would be required for its estimation.
A 'master formula' for a vehicle's fuel mileage does not exist, but based on Physics knowledge, some important factors would be
overall fuel comsumption of the engine, air resistance, and mass. The formula for finding the fuel mileage is completely made up.
The last method is get_0_60(). This method 'calculates' the time the vehicle would take to go from 0 mph to 60 mph. Again, the
formula implemented is made up, and its purpose is to show multiple attribute calls within the method. Two class methods exist within
the Vehicle class: its engine and transmission. The engine class (Engine()) requires attributes related to the engine such as its type, 
piston configuration or motor configuration, horsepower, and torque. The transmission class (Tranny()) requires attributes of 
the transmission type, and number of gears. The rest of the script is organized by functions based on inputs required for the Vehicle class. 

Kyle Gourlie

Design:
The design of the script was completed by a diagram included within the zip file that this script is located at.

Testing:
To test this script, two vehicles were used. The first was a 1994 Toyota 4runner 2.4L 5-speed manual transmission with a drag coefficent
of 0.3 and cross sectional area of 20 m^2. Three pieces of information are printed out to see if the classes are working correctly. The
two ways to do this was to compute the miles per gallon and 0 to 60 value of the vehicle. These methods were important because they used all
three classes. Some other tests include entering strings for the parameters that need to be float values. When this happened, an exception 
occured and the user was forced to input all the parameters required for that portion again. 
"""


class Vehicle:
   """Creates vehicle object

   Parameters:
   - mass (float): The vehicle's mass in kilograms
   - drag_coef (float): The vehicle's drag coefficent
   - cross_sect (float): The vehicle's cross sectional area in square meters
   - yr (int): The model year of the vehicle
   - model (str): The model of the vehicle
   - make (str): The brand/make of the vehicle

   Examples:
   >>> car = Vehicle(2000,0.3,20,1994,'4Runner','Toyota')

   """
   def __init__(self, mass: float, drag_coef: float,
                 cross_sect: float, yr: int, model:str, make: str):
       self.mass = abs(float(mass))
       self.drag_coef = abs(float(drag_coef))
       self.cross_sect = abs(float(cross_sect))
       self.yr = abs(int(yr))
       self.model = str(model)
       self.make = str(make)


   def __str__(self):
       return f'{self.yr} {self.make} {self.model}'
      

   class Engine:
       """Creates Engine object for the vehicle class

       Parameters:
       - type (str): The vehicle's engine type such as diesel, petrol, EV, Hybrid, etc.
       - config (str): The vehicle's engine configuration such as V6, V8, V12, I4, VR6, etc.
       - displ (float): The vehicle's engine displacement volume in liters.
       - hprs (float): The vehicle's engine power in horsepower.
       - torq (float): The vehicle's torque in foot-pounds.
       """
       def __init__(self,type,config,displ,hprs,torq):
           self.type = str(type)
           self.config = str(config)
           self.displ = abs(float(displ))
           self.hprs = abs(float(hprs))
           self.torq = abs(float(torq))


   class Tranny:
       """Creates Transmission object for the vehicle class
       
       Parameters:
       - type (str): The vehicle's transmission type such as manual, automatic, belt, etc.
       - gears (int): The number of transmission gears.
       """
       def __init__(self,type,gears):
           self.type = str(type)
           self.gears = str(gears)


   def get_0_60(self):
       """This method 'calculates' the time it takes to go from 0 to 60 mph. Note that this
       equation is completely made up and not correct."""

       _0_60 = (self.Engine.displ + self.Engine.hprs - 
           self.mass/10 - (self.drag_coef*self.cross_sect))
       
       return _0_60


   def get_mpg(self):
       """This method 'calculates' the miles per gallon of the vehicle. Note that this 
       equation is completely made up and not correct.
       """
       mpg = 50 - self.Engine.displ*0.01 - (self.drag_coef*self.cross_sect)

       return mpg
       


def menu():
   #This function is a text-based menu.
   while True:
       yes_no = input('Do you want to start the program? (y/n)')

       if yes_no.lower() == 'y':
           return True

       elif yes_no.lower() == 'n':
           return False
       else:
           print('INVALID RESPONSE. Try again')


def params():
   #This function controls all the parameters of the vehicle class
   print('\nVehicle Parameters:\n')
   valve = True
   while valve:
       valve = False

       try:
           yr = int(input('Enter the year of the vehicle:'))
           make = input('Enter the brand of the vehicle:')
           model = input('Enter the model of the vehicle:')
           mass = abs(float(input('Enter the mass (kg) of the vehicle:')))
           drag_coef = abs(float(input('Enter the drag coefficent of the vehicle:')))
           cross_sect = abs(float(input('Enter the cross sectional area (m^2) of the vehicle:')))
       
       except ValueError:
           valve = True
           print('\nTYPE ERROR. One of the entered vehicle parameters is invalid.\n Try again.\n')

   return yr,make,model,mass,drag_coef,cross_sect



def engine_params():
   #This function controls all the parameters of the vehicle's engine class
   print('\nEngine Parameters\n')
   valve = True
   while valve:
       valve = False

       try:
           type_ = input('Enter engine type (petrol, diesel, EV, etc):')
           config = input('Enter engine configuration (V6, V8, I4, motor, etc):')
           displ = abs(float(input('Enter engine displacement in liters:')))
           hrprs = abs(float(input('Enter the peak horsepower of the engine:')))
           torq = abs(float(input('Enter the peak torque of the engine:')))

       except ValueError:
           valve = True
           print('\nTYPE ERROR. One of the entered engine parameters is invalid.\n Try again.\n')
  
   return type_,config,displ, hrprs, torq



def tranny_params():
   #This function controls all the parameters of the vehicle's transmission class
   print('\nTransmission Parameters\n')
   valve = True
   while valve:
       valve = False

       try:
           type_ = input('Enter transmission type (manual, auto, belt):')
           gears = int(input('Enter the number of gears in the transmission excluding reverse:'))
       
       except ValueError:
           valve = True
           print('\nTYPE ERROR. One of the entered transmission parameters is invalid.\n Try again.\n')
  
   return type_,gears
  

       


if __name__ == "__main__":
   while True:
       val = menu()
       if val:
           input('\nThis program creates a vehicle object.\nPress ENTER to begin!')
           v_yr,v_make,v_model,v_mass,v_drag_coef,v_cross_sect = params()
           e_type,e_config,e_displ,hrprs, torq = engine_params()
           trn_type,trn_grs = tranny_params()

           #instantiates vehicle object
           car = Vehicle(mass=v_mass,drag_coef=v_drag_coef,
                       cross_sect=v_cross_sect,yr=v_yr,make=v_make,
                       model=v_model)
           
           #instantiates vehicle's engine object
           car.Engine = Vehicle.Engine(config=e_config, type=e_type, displ=e_displ, hprs=hrprs, torq=torq)

           #instantiates vehicle's transmission object
           car.Tranny = Vehicle.Tranny(type=trn_type,gears=trn_grs)
           
           #Testing the two vehicle's method
           mpg = car.get_mpg()
           _0_60_val = car.get_0_60()
           print()
           print(f'Name of car: {car}')
           print(f'Car miles per gallon: {mpg}')
           print(f'Car 0 to 60 mpg time in seconds: {_0_60_val}')
           print()
       
       else:
           print('exiting...')
           break
      

