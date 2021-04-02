a=int(input())
c=int(0)
for x in range(a):
    b=str(input())
    if b=="Cube":
        c+=6
    if b=="Octahedron":
        c+=8
    if b=="Tetrahedron":
        c+=4
    if b=="Dodecahedron":
        c+=12
    if b=="Icosahedron":
        c+=20
print(c)