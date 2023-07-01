alph_std = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "


def decode(s):
    i = 1  # number letter in s
    ans = ''
    for letter in s:
        if letter in ("!@#$%^&*()_+-=/\-"):
            ans += letter
            i += 1
            continue
        ind = alph_std.index(letter)
        for n in range(i):
            if ind & 1:
                ind -= 1
            else:
                ind += 66
            ind //= 2
        ans += alph_std[ind]
        i += 1
    print(ans)
    return ans
