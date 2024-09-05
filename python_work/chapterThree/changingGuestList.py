guestList = ['sam harris', 'barack obama', 'friedrich nietzsche']

inviteOne = f'Congraduations! {guestList[0].title()}, you have been formely invited to dinner!'
inviteTwo = f'Congraduations! {guestList[1].title()}, you have been formely invited to dinner!'
inviteThree = f'Congraduations! {guestList[2].title()}, you have been formely invited to dinner!'

print(inviteOne)
print(inviteTwo)
print(inviteThree)

print(f'It appears as tho {guestList[2].title()} is unable to attened tonight. I will need to invite another person!')

guestList[2] = 'marcus aurelius'

inviteOne = f'Congraduations! {guestList[0].title()}, you have been formely invited to dinner!'
inviteTwo = f'Congraduations! {guestList[1].title()}, you have been formely invited to dinner!'
inviteThree = f'Congraduations! {guestList[2].title()}, you have been formely invited to dinner!'

print(inviteOne)
print(inviteTwo)
print(inviteThree)