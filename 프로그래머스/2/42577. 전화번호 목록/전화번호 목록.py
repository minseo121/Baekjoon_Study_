def solution(phone_book):
    phone_dict = {}
    for num in phone_book:
        phone_dict[num] = True
    for i in phone_book:
        for j in range(1,len(i)):
            if i[:j] in phone_dict:
                return False
    return True
        
                
            