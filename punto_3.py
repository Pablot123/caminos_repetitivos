building_heigh = int(input('Enter the heigh of the bilding: '))


not_touch_the_floor = True
seconds = 0
gravity_constant = 9.8
print('Distance | time')
while not_touch_the_floor:
    distance = (1/2)*gravity_constant*(seconds**2)

    if distance >= building_heigh:
        print('LLEGO AL SUELO')
        not_touch_the_floor = False
    else:  
        print(f' {distance}\t |  {seconds}')
        seconds +=1
