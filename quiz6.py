#function

def std_weight (height, gender) :
    if(gender == '남자') :
        return (height * height * 22)
    elif(gender == '여자') :
        return (height * height * 21)
    else :
        return -1

height = int(input("키(cm)를 입력하세요(ex. 170): "))
gender = input("성별을 입력하세요(ex. 여자): ")

# height = 170
# gender = '남자'

#std_weight calculation
weight = round(std_weight(height/100, gender), 2)

print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다'.format(height,gender,weight))

