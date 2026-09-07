def solution(today, terms, privacies):
    y, m, d = today.split('.')
    today_num = int(y) * 12 * 28 + int(m) * 28 + int(d)

    term_dict = {}
    for t in terms:
        name, month = t.split()
        term_dict[name] = int(month)

    answer = []
    for i in range(len(privacies)):
        date, name = privacies[i].split()
        y, m, d = date.split('.')

        expire = int(y) * 12 * 28 + int(m) * 28 + int(d)
        expire = expire + term_dict[name] * 28

        if today_num >= expire:
            answer.append(i + 1)

    return answer