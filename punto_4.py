generation = int(input('Enter the generation: '))

total_family_members = 0
#we add 1 to generation becaus we need to calculate until the current generation
# and the range ends on the previus number
for i in range(generation+1): 
    generation_family_members = 2**i # the member on each generations
    total_family_members += 2**i  # constantly add the number of each generation
    print(f'Generation {i} have {generation_family_members}')
    

print(f'Total number of members in the family: {total_family_members}')
