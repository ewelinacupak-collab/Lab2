x = float(input("wprowadź pierwszą liczbę"))
y = float(input("wprowadź drugą liczbę"))
z = float(input("wprowadź trzecią liczbę"))

if x > y and x > z and y > z:
    print(x, y, z)
elif y > x and y > z and x > z:
    print(y, x, z)
elif z > x and z > y and y > x:
    print(z, y, x)
elif x > z and x > y and z > y:
    print(x, z, y)
elif y > x and y > z and z > x:
    print(y, z, x)
elif z > x and z > y and x > y:
    print(z, x, y)
