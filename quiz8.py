#Quiz 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

class House:
    def __init__(self, location, house_type, deal_type, price, complition_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.complition_year = complition_year
        # self.house_count = 0
        # self.house_list = []

    def show_detail(self):
        # print("총 {0}대의 매물이 있습니다.".format(self.house_count))
        # for house in self.house_list:
        #     print("{0}, {1}, {2}, {3}, {4}".format(house))
        print(self.location, self.house_type, self.deal_type, self.price, self.complition_year)


    # def add_house(self):
    #     # self.location = location
    #     # self.house_type = house_type
    #     # self.deal_type = deal_type
    #     # self.price = price
    #     # self.complition_year = complition_year
    #     self.house_count += 1
    #     self.house_list.append([self.location, self.house_type, self.deal_type, \
    #         self.price, self.complition_year])
    #     print("매물이 추가되었습니다. {0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, \
    #         self.price, self.complition_year))


# house1 = House("강남","아파트","매매","10억","2010년")
# house1.add_house()

# house2 = House("마포","오피스텔","전세","5억","2007년")
# house2.add_house()

# house3 = House("송파","빌라","월세","500/50","2000년")
# house3.add_house()

houses = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))

for house in houses: 
    house.show_detail()

