def solution(video_len, pos, op_start, op_end, commands):
    m, s = map(int, video_len.split(':'))
    c_m, c_s = map(int, pos.split(':'))
    s_m, s_s = map(int, op_start.split(':'))
    e_m, e_s = map(int, op_end.split(':'))

    s += m * 60
    c_s += c_m * 60
    s_s += s_m * 60
    e_s += e_m * 60
    
    if s_s <= c_s <= e_s:
        c_s = e_s
    for i in commands:
        if i == "prev":
            c_s = max(0, c_s - 10)
        elif i == "next":
            c_s = min(s, c_s + 10)
        if s_s <= c_s <= e_s:
            c_s = e_s
        
    print(c_s, c_m)

    c_m = c_s // 60
    c_s = c_s % 60
    print(c_s, c_m)

    return ':'.join([str(c_m).zfill(2), str(c_s).zfill(2)])