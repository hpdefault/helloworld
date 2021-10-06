
a = [0,1,2,3,4,5,6,7,8,9,10]
b = [0,1,2,3,4,5,6,7,8,9,10]
c = [0,1,2,3,4,5,6,7,8,9,10]
n=[50,51,52,53,54,
   55,56,57,58,59,
   60,61,62,63,64,
   65]
print(n)

for veri in a:
    for veri2 in b:
        for veri3 in c:
            for eleman in n:
                eleman == ((6 * veri) + (9 * veri2) + (20 * veri3))
                veri == eleman - ((9 * veri2) + (20 * veri3))
                veri2 == eleman - ((6 * veri) + (20 * veri3))
                veri3 == eleman - ((6 * veri) + (9 * veri2))
                n.sort()
                if eleman == ((6 * veri) + (9 * veri2) + (20 * veri3)):
                    print("A =",veri,",",
                          "B =",veri2,",",
                          "C =",veri3," için",
                          "n = ",eleman)

