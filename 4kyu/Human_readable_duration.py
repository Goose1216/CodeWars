def format_duration(seconds):
    s = seconds % 60
    s_full = seconds
    m = (s_full // 60) % 60
    m_full = s_full // 60
    h = (m_full // 60) % 24
    h_full = m_full // 60
    d = (h_full // 24) % 365
    d_full = h_full // 24
    y = d_full // 365
    date = {"year": y,"day": d, "hour": h,"minute": m, "second": s}
    ans = ''
    for key,value in date.items():
        if value != 0:
            if value > 1: key += 's'
            if len(ans) == 0:
                ans += f"{value} { key}"
            else:
                ans += f", {value} {key}"
    ans = ans[::-1]
    ans =  ans.replace(',','dna ',1)
    ans = ans[::-1]
    if len(ans) == 0: return "now"
    return  ans