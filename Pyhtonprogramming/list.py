players = ["Rashford", "Mainoo","Amad", "Pogba", "Dybala","Cherki"]

print(players [1:4])
print(players[4:])# this will print players from index 4 to the end
print(players[-2:])#this will print the last 2 players in the list
print(players[:-3]) #this will print all players except the last 3
print(players[::2]) #this will print every second player in the list
print(players[::-1]) #this will print the players in reverse order
if "Pogba" in players:
    print("Pogba is available for selection")

# This code snippet demonstrates how to manipulate and access elements in a list of players.


players.sort() # this will sort player names by alphabet
print(players)
players.reverse()   # this will reverse the order of players in the list
print(players) # this will print the players in reverse order
sorted_players = sorted(players) # this will create a new sorted list without modifying the original
print(players)
