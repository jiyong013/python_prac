from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# id = []
#id generation
# for i in range(1,21) :
#     id.append(i)
id = range(1,21)
# print(type(id))
id = list(id)
# print (id)

#shuffling
shuffle(id)
# print(id)

winners = sample(id,4)

# #sampling
# sampling1 = sample(id,1) # chicken, 1
# # print(sampling1)
# id_set =  set(id) - set(sampling1)
# # print(id_set)
# id_set = list(id_set)
# shuffle(id_set)
# sampling2 = sample(id_set,3) # coffee, 3

########## final print out ##############
print("-- Results --")
print("Chicken: {0}".format(winners[0]))
print("Coffee: {0}".format(winners[1:]))
print("-- Congratulation! --")
