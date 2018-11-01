# mx = lambda x,y:x if x>y else y
# print(mx(8,5))
#
# list_1 = [1,2,3,4]
# print(list(map(lambda x:2*x,list_1)))
#
#
#
#
# students = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name,score])
# score_set = []
# for num in range(len(students)):
#     score_set.append(students[num][1])
# lowest_2nd_score = (sorted(list(set(score_set))))[1]
# lowest_2nd_students=list(map(lambda x:x[0] if x[1]==lowest_2nd_score else ' ', students))
# filtered=sorted(list(filter(lambda x:x!=' ',lowest_2nd_students)))
# for num in range(len(filtered)):
#     print(filtered[num])
#
#
# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])
#
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
#



string='ABCDCDC'
sub_string='CDC'
count=0
index_found=0
next_index=0
while index_found!=-1:
    index_found=string.find(sub_string,next_index)
    if index_found!=-1:
        count+=1
        next_index=index_found+1
    print(count, index_found, next_index)
print(count)


s = 'qA2'
print(s.isalnum())
print(not s.isdigit())
print( not s.isalpha())
print()