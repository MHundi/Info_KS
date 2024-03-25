from cone_area_lib import cone_area

radius = input("Gib Radius ein:")
height = input("Gib Höhe ein:")

print("Deine Eingabe für Radius war:",  radius )
print("Deine Eingabe für Höhe war: ", height)
print(" Die Mantelfäche beträgt", cone_area(radius, height))
#print(cone_area(12,3))1212