# college={
# 1:"staff room",
# 2:"attendance",
# 'r':"students and teachers",
# 6.0:"course"
# }
# print(college[2])
# print(college['r'])
# print(college[6.1])     # KeyError

# a={1:"",2:"core",3:7,4:6.2,5:[1,4],6:(4,3),7:{1,2},8:{3:"world"}}
# print(a[1],type(a[1]))
# print(a[6],type(a[4]))
# print(a[8],type(a[8]))
# print(a,type(a))
# print(a.keys())
# print(a.values())
# print(a.items())

# a={1:"",2:"core",3:7,4:6.2,5:[1,4],6:(4,3),7:{1,2},8:{3:"world"}}
# a.clear()
# print(a)

# c=[101,244,345,456,786,964]
# print(dict.fromkeys(c,'pass'))
# print(dict.fromkeys(c,50))

h={1:"", 2: "python", 3: 7, 4: 6.2,
5: [1,4], 6: (4,3), 7: {1,2},8: {3: "world"}}
# print(h.get(4))
# print(h.get(10)) # None
# print(h[43])
# h.pop(7)
# print(h)
# h.popitem()
# print(h)

# h={1:"", 2: "python", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3), 7: {1,2},8: {3: "world"}}
# h.update({7: 'core python'})
# print(h)
# h.update({9: 'adv python'})
# print(h)

# h={1:"", 2: "python", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3), 7: {1,2},8: {3: "world"}}
# h.setdefault(8,'devops')
# print(h)
# h.setdefault(10, 'devops')
# print(h)

# print(dir(dict))