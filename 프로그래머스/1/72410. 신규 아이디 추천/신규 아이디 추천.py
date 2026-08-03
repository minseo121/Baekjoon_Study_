def solution(new_id):
    new = []
    for i in new_id:
        new.append(i)

    for i in range(7):
        if i == 0:
            for a in range(len(new)):
                if new[a].isalpha():
                    new[a] = new[a].lower()
        if i == 1:
            for a in range(len(new) - 1, -1, -1):          
                if new[a].isalpha() or new[a].isdigit() or new[a] in '-_.':
                    continue
                else:
                    del new[a]
        if i == 2:
            for a in range(len(new) - 1, 0, -1):           
                if new[a-1] == '.' and new[a] == '.':
                    del new[a]
        if i == 3:
            if new and new[0] == '.':
                del new[0]
            if new and new[-1] == '.':                    
                new.pop()
        if i == 4:
            if not new:
                new.append('a')
        if i == 5:
            if len(new) >= 16:
                for _ in range(len(new) - 15):
                    new.pop()
            if new[-1] == '.':
                new.pop()
        if i == 6:
            while len(new) < 3:
                new.append(new[-1])
    return ''.join(new)