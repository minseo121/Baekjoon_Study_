def solution(bandage, health, attacks):
    t, x, y = bandage
    hp = health
    combo = 0
    current_time = 0
    
    for attack in attacks:
        attack_time, damage = attack
        gap = attack_time - current_time-1
        if gap > 0:
            hp += x*gap + y*(gap//t)
            hp = min(hp, health)
        
        hp -= damage
        if hp <= 0:
            return -1
        current_time = attack_time
        
    return hp
                