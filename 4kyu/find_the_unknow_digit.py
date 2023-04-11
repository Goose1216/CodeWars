import operator
import re
Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Opers = {'+': operator.add, '*': operator.mul}
def solve_runes(Ans):
    for op in Opers.keys():
        if op in Ans or ('-' in Ans and op == '+'):
            for Digit in Digits:
                if str(Digit) not in Ans:
                    _Ans = Ans.replace('?', str(Digit))
                    if (re.search(r'\D0\d',_Ans)) != None: continue
                    _Ans = _Ans.replace('--','+')
                    _Ans = re.findall(r'-?\d+', _Ans)
                    _Ans = list(map(int,_Ans))
                    if Opers[op](_Ans[0], _Ans[1]) == _Ans[2]:
                        return Digit
    return -1