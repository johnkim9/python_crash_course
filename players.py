#Slicing a list
players=['charles','martina','michael','florence','eli']
print(players[0:3])
#[0:3] will give you the following elements: 0, 1, 2 because Python will stop one itme before the second index you specify. 
#In this case it's 3, so it will stop at 2
print(players[1:4])
#this will give you 1,2,3
print(players[:4])
#If you omit the first index in a slice, Python automatically starts your sliec at the beginning of the list
print(players[2:])
#all items from the third item through the last
#negative index returns an element a certain distance from the end of a list
print(players[-3:])
#output of the last three players on the roster

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

