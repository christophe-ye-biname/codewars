def dirReduc(arr):
    
    
    coord = [0,0]
    for i in range(len(arr)):
        if arr[i] == "NORTH":
            coord[1] += 1
        elif arr[i] == "SOUTH":
            coord[1] -= 1
        elif arr[i] == "WEST":
            coord[0] -= 1
        elif arr[i] == "EAST":
            coord[0] += 1
    
    res = []
    if coord[0] == 0 and coord[1] == 0:
        return ["NORTH", "WEST", "SOUTH", "EAST"]
    if coord[1] > 0:
        res.append("NORTH")
    if coord[0] < 0:
        res.append("WEST")
    if coord[1] < 0:
        res.append("SOUTH")
    if coord[0] > 0:
        res.append("EAST")
    return res
    
    
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']))
print(dirReduc(['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']
))
'''
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
'''