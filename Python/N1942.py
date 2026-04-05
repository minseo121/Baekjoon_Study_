import sys
input = sys.stdin.readline

num = 0
for _ in range(3):
    stime, ftime = input().split()
    st1,st2,st3 = map(int, stime.split(':'))
    ft1,ft2,ft3 = map(int,ftime.split(':'))
    result = 0

    while True:
        if st3 == 60:
            st2 += 1
            st3 = 0
        if st2 == 60:
            st1 += 1
            st2 = 0
        if st1 == 24:
            st1 = 0

        time = st1 * 10000 + st2 * 100 + st3
        if time % 3 == 0:
            result += 1
        
        if (st1 == ft1) and (st2 == ft2) and (st3 == ft3):
            break

        st3 += 1
    print(result)

