from random import randint
tc_no = randint(100000000, 1000000000)
list_tc = list(map(int, str(tc_no)))
tc10 = (sum(list_tc[0:10:2])*7 - sum(list_tc[1:9:2])) % 10
tc11 = (sum(list_tc[0:9]) + tc10) % 10
list_tc.append(tc10)
list_tc.append(tc11)
tckimlikno="".join(list(map(str, list_tc)))
print(tckimlikno)
