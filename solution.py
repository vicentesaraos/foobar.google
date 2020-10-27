# last gear rotates at 2 * 1st
# if impossible return list [-1, -1]

from fractions import Fraction
import random
import math


def solution(i):
    print("peg list", i)
    # choose 2-20 distinct list, asc
    b = sorted(random.sample(range(1, 10001), random.choice(range(2, 21))))

    # checks consecutive values for difference of 1,2,
    # minimum r == 1
    a = 0
    for x in range(len(i) - 1):
        if i[a + 1] - i[a] == 1:
            return print([-1,-1])
        if i[a + 1] - i[a] == 2:
            return print([-1, -1])
        a += 1

    # compute whole number radii value of each distance between pegs
    a = 0
    radiuslist = []
    # iterate number of pegs
    # distance is even
    if (len(i)-1) % 2 == 0:
        pass
    # odd distance:

    for x in range(len(i) - 1):
        p0 = i[a]
        p1 = i[a + 1]
        rangeofradii = p1 - p0 - 1
        # if distance is 2, radius = 1
        if rangeofradii == 1:
            radiuslist.append([1, 1])
            a += 1
        # if distance > 2 then append to the radii list
        else:
            b = 1
            for x in range(rangeofradii):
                radiuslist.append([b, p1 - p0 - b])
                b += 1
            a += 1
    # hundreth fraction list
    #z = [Fraction(x, 100) for x in range(1, 100)]
    # z =[Fraction(10/100), Fraction(25/100), Fraction(33/100), Fraction(50/100), Fraction(67/100), Fraction(75/100), Fraction(80/100), Fraction(90/100) ]
    z = [1/10, 1/4, 1/3, 1/2, 2/3, 3/4, 4/5, 9/10]
    #.1, .25, .33.., .5, .67, .75, .8, .9


    print("radiuslist", radiuslist)

    radiuslistfrac = []
    # index for last radii between pegs
    indexlist = []
    h = 0
    y = 0
    count = 0
    # adding fractionlist and wholenumradius to new list
    print("len of radiuslist", len(radiuslist))
    for x in range(len(radiuslist)):
        m = radiuslist[x]
        # equidistant pegs
        if radiuslist[x] == [1, 1]:
            radiuslistfrac.append([1, 1])
            indexlist.append(y)
            y += 1
        else:
            # equal radii between pegs
            if m[0] == m[1]:
                radiuslistfrac.append(m)
                y+1
                # decreasing radius x, incr y (x,y)
                for q in range(8):
                    radiuslistfrac.append([radiuslist[h][1] - z[q], z[q] + radiuslist[h][0]])
                    y += 1
                h += 1
                continue
            # last radius between pegs
            if m[1] == 1:
                radiuslistfrac.append(m)
                y += 1
                indexlist.append(y)
                h += 1
                continue
            # increasing radius x, decr y (x,y)
            if m[0] < m[1]:
                radiuslistfrac.append(m)
                y += 1
                for p in range(8):
                    radiuslistfrac.append([z[p] + radiuslist[h][0], radiuslist[h][1] - z[p]])
                    y += 1
                h += 1
                continue
            if m[0] > m[1]:
                radiuslistfrac.append(m)
                y += 1
                # decreasing radius x, incr y (x,y)
                for q in range(8):
                    radiuslistfrac.append([radiuslist[h][0] + z[q], radiuslist[h][1] - z[q]])
                    y += 1
                h += 1


    # solution search
    a = len(indexlist)
    print("len of index list", len(indexlist))
    print("index list", indexlist)
    print("fractionlist len", len(radiuslistfrac))
    b = 0
    answer = []
    # if a == b
    # return [-1,-1]
    # print("fl 0,1", radiuslistfrac[0][1])
    # print("fl 1,0", radiuslistfrac[1][0])
    # print("indexlist", indexlist)
    print("radiuslistfrac", radiuslistfrac)

   # if (len(indexlist) == 1):

    a = indexlist[0]
    b = math.floor((indexlist[0]+1)/2)
       # print("b", b)

    for value in range(b+1):
        z = radiuslistfrac[value][1]
        x = radiuslistfrac[value][0]
        for value2 in range(b+1):
            y = radiuslistfrac[value][0]
            if (y*2 == z) or (z - (y*2+.0000000000000001) < .0000000000000005) or ((z - (y*2-.0000000000000001)) < .0000000000000005):
                if isinstance(x, Fraction):
                    answer.append(Fraction(z).numerator)
                    answer.append(Fraction(z).denominator)
                else:
                    answer.append(z)
                    answer.append(1)
                if (len(answer)-1) == (len(indexlist)):
                    return print("answer", answer)
                else:
                  for value3 in(range(a+1)):
                       v = radiuslistfrac[value3][0]

    return print(-1,-1)


solution([1, 5])

'''
        for value in range(b+1):  # 0 - 14
            z = radiuslistfrac[value][1]
            for value2 in range(b+1, a+1): # 14-28
                y = radiuslistfrac[value][0]
                if (y*2 == z) or ((y*2)+.01) == z:
                    answer.append(z)
                    answer.append(y)
                    return print("answer", answer)
        return print(-1,-1)
'''
'''
    for list1 in range(indexlist[0]+1):
        z = radiuslistfrac[list1][0]
        d = (radiuslistfrac[list1][1])
        e = -1
        for list2 in range(indexlist[0]+1,indexlist[1]+1):
            if d == e:
                answer.append(int(z))
                answer.append(int(radiuslistfrac[list2][0]))
                if len(answer) == a-1:
                    return (answer)

                else:
                    e = radiuslistfrac[list2][0]
                    if len(answer) == a-1:
                        return (answer)
                    if a > 3:
                        for list3 in range(indexlist[0] + 1, indexlist[1]):
                             f = radiuslistfrac[list3][0]
                             if e == f:
                                answer.append(radiuslistfrac[x][0])
                    else:
                         end = -1
'''