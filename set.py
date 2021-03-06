# p.97 집합자료형(set, 세트)
# v2.3부터 지원 / 집합에 관련된 자료를 쉽게 처리하기 위한 목적
# 파이썬 자료형 : 정수, 실수, 문자, 불, 리스트, 튜플, 딕셔러리, 셋
# dict_items, dict_keys, dict_values

set1 = set([1,2,3,4,5])
print(set1, type(set1))

# set는 중복을 허용하지 않는다.
# set는 순서를 보장하지 않는다.
set2 = set('hello python')
print(set2, type(set2))

#교집합 & , 합집합, 차집합
set3 = set([1,2,4,6,10])
set4 = set([1,2,3,7,10])

print('교집합 =>', set3 & set4) # set3.intersection(set4))
print('합집합 =>',set3 | set4) # set3.union(set4))
#print('차집합 =>',set3 | set4)

list1 = [1,2,3,5,3]
list2 = [2,1,10,9,4]
list3 = list1 + list2
# print(list3)