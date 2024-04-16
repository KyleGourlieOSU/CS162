from project_1 import Vehicle
#year make model mass drag_coef cross_sect eng_type eng_config displ hrprs torque tran_type gears
#13 elements

cars=[]
with open('Assign_1/params.txt','r') as f:
    for line in f:
        lines= line.split(' ')
        
        try:
            car = Vehicle(mass=lines[3], drag_coef=lines[4],
                        cross_sect=lines[5], yr=lines[0], make=lines[1],
                        model=lines[2])
            
            #instantiates vehicle's engine object
            car.Engine = Vehicle.Engine(config=lines[7], type=lines[6], displ=lines[8], 
                                        hprs=lines[9], torq=lines[10])

            #instantiates vehicle's transmission object
            car.Tranny = Vehicle.Tranny(type=lines[11], gears=lines[12])    
            cars.append(car)
        except ValueError as mess:
            print(f'\nValueError Occuring for {car}')
            print(mess)
            continue


for i in range(len(cars)):
    try:
        mpg=cars[i].get_mpg()
        _0_60=cars[i].get_0_60()
        print(mpg)
        print(_0_60)
    except:
        print(f'Error has occured with {cars[i]}')
        continue
            


