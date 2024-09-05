guestList = ['sam harris', 'barack obama', 'friedrich nietzsche']

inviteOne = f'Congraduations! {guestList[0].title()}, you have been formely invited to dinner!'
inviteTwo = f'Congraduations! {guestList[1].title()}, you have been formely invited to dinner!'
inviteThree = f'Congraduations! {guestList[2].title()}, you have been formely invited to dinner!'

print(inviteOne)
print(inviteTwo)
print(inviteThree)

print(f'It appears as tho {guestList[2].title()} is unable to attened tonight. I will need to invite another person!')

guestList[2] = 'Marcus Aurelius'

inviteOne = f'Congraduations! {guestList[0].title()}, you have been formely invited to dinner!'
inviteTwo = f'Congraduations! {guestList[1].title()}, you have been formely invited to dinner!'
inviteThree = f'Congraduations! {guestList[2].title()}, you have been formely invited to dinner!'

print(inviteOne)
print(inviteTwo)
print(inviteThree)

print('Great news! I have found a bigger table and therefore can invite more guests!')

guestList.insert(0, 'lao tzu')
guestList.insert(1, 'kamala harris')
guestList.insert(2, 'maya angelou')

print('Well now I learned that the table will arrive late. So I can only invite two people.')

uninvitedOne = guestList.pop()
uninvitedTwo = guestList.pop()
uninvitedThree = guestList.pop()
uninvitedFour = guestList.pop()

