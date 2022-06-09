building_heigh = int(input('Enter the heigh of the bilding: '))


not_touch_the_floor = True #this is the flag to stop or continue the while loop
seconds = 0
gravity_constant = 9.8
print('Distance | time')
# i decide to do a while loop because we don't know the time when the ball hits the ground
# so i think a for loop didnt work for all the diferents heighs
while not_touch_the_floor:
    distance = (1/2)*gravity_constant*(seconds**2)

    #this conditional ends the loop when the results of the formula is grater that the heigh
    #of the building, that mean that the ball hits the groung 
    if distance >= building_heigh:  
        print('LLEGO AL SUELO')
        not_touch_the_floor = False
    else:  
        #here we print the distance traveled by the ball on each second and add 1 to the seconds
        print(f' {distance}\t |  {seconds}')
        seconds +=1
