from random import *

match_cnt = 0
matching_num = int(input("put the waitng number of people: "))
for i in range(1,matching_num+1):
    expected_time = randrange(5, 51)
    
    if(expected_time >= 5 and expected_time <=15):
        match = "O"
        match_cnt += 1
    else:
        match = " "

    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(match,i,expected_time))

print("총 탑승 승객 : {0}명".format(match_cnt))

