# 1-usul

# def sayyora(lst):
#     ulcham = {
#         "Asteroid": 0, "Pluto": 1, "Mercury": 2, "Mars": 3,
#         "Venus": 4, "Earth": 5, "Neptune": 6, "Uranus": 7,
#         "Saturn": 8, "Jupiter": 9
#     }

#     if not lst:
#         return []
    
#     result = []
#     for i in range(1, len(lst)):
#         left = ulcham[lst[i - 1]]
#         current = ulcham[lst[i]]
#         if lst[i] == "Asteroid" and lst[i - 1] == "Asteroid":
#             result.append("=")
#         elif current > left:
#             result.append(">")
#         else:
#             result.append("<")
#     return result

# print(sayyora(["Mars", "Asteroid", "Venus", "Jupiter", "Asteroid", "Earth", "Pluto"]))
# print(sayyora(["Asteroid", "Asteroid", "Asteroid", "Earth", "Jupiter"]))
# print(sayyora(["Mercury", "Venus", "Earth", "Mars", "Asteroid", "Jupiter", "Saturn", "Uranus", "Neptune", "Asteroid", "Pluto"]))

# 2-usul
# def sayyora(a):
#     ord = ["Asteroid", "Pluto", "Mercury", "Mars", "Venus", "Earth", "Neptune", "Uranus", "Saturn", "Jupiter"]

#     if not a:
#         return []
    
#     result = []
#     for i in range(len(a)):
#         if a == "Asteroid":
#             result.append("=")
#         elif ord.index(a[i]) > ord.index(a[i - 1]):
#             result.append(">")
#         else:
#             result.append("<")
#     return result
# print(sayyora(["Mars", "Asteroid", "Venus", "Jupiter", "Asteroid", "Earth", "Pluto"]))
# print(sayyora(["Asteroid", "Asteroid", "Asteroid", "Earth", "Jupiter"]))
# print(sayyora(["Mercury", "Venus", "Earth", "Mars", "Asteroid", "Jupiter", "Saturn", "Uranus", "Neptune", "Asteroid", "Pluto"]))