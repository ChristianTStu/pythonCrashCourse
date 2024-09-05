placesToVisit = ['Spain', 'Japan', 'Thailand', 'Hungary', 'France']
# Original List
print(placesToVisit)

# Sorted List
print(sorted(placesToVisit))

# Sorted list, but in reverse aphabetical sort. 
print(sorted(placesToVisit, reverse=True))

# Proof of original list still intact.
print(placesToVisit)

# Reverse the original list
placesToVisit.reverse()
print(placesToVisit)

# Reverse the reversed-list back to normal
placesToVisit.reverse()
print(placesToVisit)

# Sort command for permant change to alphabet sort list.
placesToVisit.sort()
print(placesToVisit)

# Sort reverse command for permant change to alphabet sort list.
placesToVisit.sort(reverse=True)
print(placesToVisit)

