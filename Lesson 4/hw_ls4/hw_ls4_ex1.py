inventory = {
    'gold' : [500],
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'breadloaf']
}

# add a key to inventory called 'pocket.'
# set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# remove 'dagger' from the list of items stored under the 'backpack' key.
remove = inventory['backpack']
remove.remove('dagger')

# add 50 to the number stored under the 'gold' key.
add = inventory['gold']
add.append(50)

print(inventory)
