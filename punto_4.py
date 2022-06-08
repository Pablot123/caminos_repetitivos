generation = int(input('Enter the generation: '))

total_family_members = 0
for i in range(generation+1):
    generation_family_members = 2**i
    total_family_members += 2**i
    print(f'Generation {i} have {generation_family_members}')
    

print(f'Total number of people in the family are: {total_family_members}')
