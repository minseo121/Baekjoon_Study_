def solution(word):
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def make(current):
        if len(current) > 5:     
            return
        if current != "":         
            words.append(current)
        for v in vowels:          
            make(current + v)
    
    make("")
    
    return words.index(word) + 1