def validate_battlefield(battlefield):
    cnt_good_ships = {4: 1, 3: 2, 2: 3, 1: 4}
    cnt_wrong_ships = {}
    battlefield_passed = [[0 for x in range(10)] for x in range(10)]
    switch = {
        'R': lambda m, n: (m, n + 1),
        'D': lambda m, n: (m + 1, n)
    }


    def cell(m, n):
        if m < 0 or n < 0 or m > 9 or n > 9 or battlefield_passed[m][n]: return 0
        return battlefield[m][n]


    def find(m, n, direction):
        m, n = switch[direction](m, n)
        if cell(m, n):
            return find(m, n, direction) + 1
        else:
            return 1


    def enum_ships():
        s1 = 0
        for x in cnt_wrong_ships.keys():
            s1 += x * cnt_wrong_ships[x]
            for s2 in (x for x in cnt_good_ships.keys() if cnt_good_ships[x] > 0):
                if x >= s2:
                    while s1 > 0 and cnt_good_ships[s2] > 0:
                        s1 -= s2
                        if s1 >= 0: cnt_good_ships[s2] -= 1
                    if s1 < 0:
                        s1 += s2
                        break
                else:
                    return False

        if s1 == 0 and all(x == 0 for x in cnt_good_ships.values()):
            return True
        return False


    def enum():
        for m in range(10):
            for n in range(10):
                #FIXME Intersections are considered and sometimes random tests fail
                if battlefield[m][n] == 1 and battlefield_passed[m][n] != 1:
                    len1 = find(m, n, 'R')
                    len2 = find(m, n, 'D')
                    if len2 > len1:
                        for x in range(len2): battlefield_passed[m + x][n] = 1
                        len_ = len2
                    else:
                        for x in range(len1): battlefield_passed[m][n + x] = 1
                        len_ = len1
                    if len_ in cnt_good_ships.keys() and cnt_good_ships[len_] > 0:
                        cnt_good_ships[len_] -= 1
                    else:
                        cnt_wrong_ships[len_] = cnt_wrong_ships[len_] + 1 if len_ in cnt_wrong_ships else 1


    def show(battlefield):
        for x in battlefield:
            print(' '.join(list(map(str, x))))

    if len([x[i] for x in battlefield for i in range(10) if x[i] > 0]) == 20:
        enum()
        show(battlefield)
        return enum_ships()
    print(len([x[i] for x in battlefield for i in range(10) if x[i] > 0]))
    return False