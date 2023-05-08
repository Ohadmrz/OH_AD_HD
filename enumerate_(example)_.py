# goods = [['apple', 'pear', 'peach', 'chery' ],
# ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
#     'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry' ]]
# for place, team in enumerate(goods):
#     for place_team, word in enumerate(team):
#     # print(place,place_team)
#      print(team,word)
#    #  print(len(word))

#
# goods = [['apple', 'pear', 'peach', 'chery' ],
# ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
#     'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry' ]]
# for place, team in goods.item():
#     for place_team, word in team.item():
#      print(place,place_team)
#      print(team,word)
#      print(len(word))
seq = {'a', 'b', 'c', 'd', 'e'}
lis1 = [2, 3]

res_dict = dict.fromkeys(seq, lis1)

print(str(res_dict))

lis1.append(4)

print(str(res_dict))
