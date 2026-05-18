def solution(genres, plays):
    dict_genres = {} #장르에 속한 음악 고유 번호 저장 딕셔너리
    dict_plays = {} #각 고유 번호 노래들 플레이 횟수 저장
    dict_plays_genres = {} #장르 플레이 횟수 저장
    l = len(genres)
    answer = []
    for i in range(l):
        if not genres[i] in dict_genres:
            dict_genres[genres[i]] = []
        dict_genres[genres[i]].append(i)
        dict_plays[i] = plays[i]
        if not genres[i] in dict_plays_genres:
            dict_plays_genres[genres[i]] = plays[i]
        else:
            dict_plays_genres[genres[i]] += plays[i]
            
    print(dict_genres, dict_plays)
    
    result_genres = sorted(dict_plays_genres, key = lambda x:dict_plays_genres[x], reverse = True)
    dict_plays=sorted(dict_plays.items(), key=lambda x:x[1], reverse = True)
    
    for genre in result_genres:
        cnt = 0
        for j in dict_plays:
            if j[0] in dict_genres[genre]:
                answer.append(j[0])
                cnt += 1
                if cnt == 2:
                    break
    print(answer)
    return answer