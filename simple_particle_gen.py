import random

def to_string(my_list):
    retMe = str(my_list[0]) + ' ' + str(my_list[1]) + ' ' + str(my_list[2]) +'\n'
    return retMe

number = 0
user_input = input("Enter number of particles to generate: ")

print("Creating '" + str(user_input) + "' of particles...")

while number < int(user_input):
    select_plane = ['xy', 'yz', 'xz']
    selected_plane = random.choice(select_plane)
    
    sign = [1, -1]
    random_1 = (random.uniform(2, 3)) * (random.choice(sign))
    
    random_2 = (random.uniform(2, 3)) * (random.choice(sign))
    
    random_speed = (random.uniform(.5, 2)) * (random.choice(sign))
    
    position = []
    velocity = []
    
    if selected_plane == 'xy':
        position = [random_1, random_2, 0]
        velocity = [0, 0, random_speed]
    elif selected_plane =='yz':
        position = [0, random_1, random_2]
        velocity = [random_speed, 0, 0]
    elif selected_plane == 'xz':
        position = [random_1, 0, random_2]
        velocity = [0, random_speed, 0]
    
    firstline = to_string(position)
    secondline = to_string(velocity)
    
    with open ('particle' + str(number) + '.txt', "w") as particle_file:
        particle_file.write(firstline)
        particle_file.write(secondline)
    
    number = number + 1
        
        
        
        
        
        
        
        
        
        
        