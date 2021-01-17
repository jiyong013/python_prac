url = "http://naver.com"
# addr = "http://daum.net"
# addr = "http://google.com"

# url = input("enter the web address: ")

# step1 = url[7:]
step1 = url.replace("http://","")
# print(step1) #print for debug

dot_pos = step1.find(".")
# print(dot_pos) #print for dot pos index
# step2 = step1[:5]
step2 = step1[:step1.index(".")]
print(step2)

# word_len = len(step2)
# print(type(word_len))
# e_count = step2.count("e")
auto_pwd = step2[:3] + str(len(step2)) + str(step2.count("e")) + "!"

print(auto_pwd)

print("{0}의 비밀번호는 {1}입니다.".format(url, auto_pwd))
