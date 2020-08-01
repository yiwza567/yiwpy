start = int(input("ป้อนสูตรคูณเริ่มต้น = "))
stop = int(input("ป้อนสูตรคูณสุดท้าย = "))

for x in range(start, stop+1):
    print("แม่ = ", x)
    for y in range(1, 13):
        print(x, 'x', y, " = ", (x*y))

for x in range(-stop, -start+1):
    print("สูตรคูณแม่ = ", -x)
    for y in range(12, 1, -1):
        print(-x, 'x', y, " = ", (-x*y))
