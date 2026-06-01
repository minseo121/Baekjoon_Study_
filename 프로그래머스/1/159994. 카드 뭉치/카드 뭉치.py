def solution(cards1, cards2, goal):
    answer = True
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.pop(0)
            
        elif cards2 and i == cards2[0]:
            cards2.pop(0)
                
        else:
            answer = False
            break
    if answer:
        print("Yes")
        return "Yes"
    else:
        print("No")
        return "No"