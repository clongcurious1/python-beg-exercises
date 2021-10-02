#text-based interactive fiction
print('Welcome to the Santa Cruz Mountain Adventure Game')
print ('*************************************************')
print('You are visiting Santa Cruz, California.')
print('You go on an evening hike ALONE in the mountains.')
print('Select one item to take with you:')
print('map(m)', 'flashlight(f)', 'chocolate(c)', 'rope(r)', "or sticks(s):")
item = input('Make your choice: ')
print('You hear a humming sound.')
choice1 = input('Do you follow the sound? Enter yes(y) or no(n): ')
#path of user who CHOOSES to follow the sound
if choice1 == 'y':
    print('You keep moving closer to the sound.')
    print('The sound suddenly stops.')
    print('You realize you are LOST! Alone in the mountains!!!')
    print('You try to call on your phone, but there is NO signal.')
    direction = input('Which direction do you choose? north, south, east, or west?:')
    if direction == 'north':
        print('You reach an abandoned cabin.')
        if item == 'm':
            print('Use the map to find your way home.')
            print('Congratulations!!! You arrived home safely and won the game.')
        else:
            print('If you had a map, you could find your way home from here.')
            print("You are LOST alone in the mountains, and you LOST the game.")
    elif direction == 'south':
        print('You reach a river with a broken bridge.')
        if item == 'r' or item == 's':
            print('You chose an item you can now use to repair the bridge.')
            print('Congratulations!!! You arrived home safely and won the game.')
        else:
            print('If you had a rope or a stick, you could repair the bridge.')
            print("You are LOST alone in the mountains, and you LOST the game.")
    elif direction == 'west':
        print('You are walking and trip over a fallen log.')
        print('You have hurt your foot. You sit down and wait for help.')
        print('You realize you may be waiting a LONG time...and you are still LOST.')
        print("You are LOST alone in the mountains, and you LOST the game.")
    else:
        print('You reach the side of the highway. It is dark.')
        if item == 'f':
            print('Use your flashlight to signal oncoming cars.')
            print('A car stops and gives you a ride home.')
            print('Congratulations!!! You arrived home safely and won the game.')
            print('...but hitchhiking is still a risky choice, be more careful from now on.')
        else:
            print('If you had a flashlight, you could signal for help.')
            print("You are LOST alone in the mountains, and you LOST the game.")
    #this is the user who chooses NOT to follow the sound    
else:
    print('Good idea! You are not taking any risks.')
    print('Better play it safe, time to head back to the cabin.')
    print('You start walking back to your starting point.')
    print('You realize you are LOST! Alone in the mountains!!!')
    print('The humming sound is getting louder and louder.')
    print('You PANIC!!!')
    action = input('Do you start running? (r), or stop to make a call (c)?:')
    while action == 'c':
        print("The call does not go through. There's no signal.")
        action = input('Do you want to run (r), or try calling again (c)?: ')
        print('You are running fast. The sound gets really loud.')
        print('A woman on an electric scooter comes up behind you.')
        answer = input('She says, "Name my favorite computer programming language: ')
        if answer == 'python' or answer == 'Python':
            print('She says, "Yes, Python is my favorite programming language.')
            print('If you have any chocolate, I will help you get home.')
            if answer == 'c':
                print('You are in luck! You chose to bring CHOCOLATE along on your hike.')
                print('You give her the chocolate and hop on the scooter.')
                print('Congratulations!!! You arrived home safely and won the game.')
            else:
                print('What were you thinking? You should have chosen CHOCOLATE when you had the chance.')
                print("She rides away. You start to cry.")
                print("You are LOST alone in the mountains, and you LOST the game.")
        else:
            print('She did NOT like your answer.')
            print("She rides away. You start to cry.")
            print("You are LOST alone in the mountains, and you LOST the game.")