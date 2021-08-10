class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print(f'My name is: {self.name}')


class SuperHero(Person):
    def __init__(self, name, hero_name):
        # super(SuperHero, self).__init__(name)
        super(SuperHero, self).__init__(name)
        self.name = name
        self.hero_name = hero_name

    def reveal_identity(self):
        # super(SuperHero, self).reveal_identity()
        print(f'... And I am {self.hero_name}')


# abhi = Person('Abhi')
# abhi.reveal_identity()

# dead = SuperHero('Wade Wilson', 'DeadPool')
# dead.reveal_identity()


from collections import Counter, defaultdict


def anagram(words):
    anagrams = defaultdict(list)
    for word in words:
        histogram = tuple(Counter(word).items())
        print('---')
        print(histogram)  # build a hashable histogram
        anagrams[histogram].append(word)
    return list(anagrams.values())


keywords = ("hi", "hello", "bye", "helol", "abc", "cab",
            "bac", "silenced", "licensed", "declines")

# anagram(keywords)
# print(anagram(keywords))

# coun = Counter('silenced')
# print(type(coun))
# print(coun)
# print('---------------------')
# co = coun.items()
# print(type(co))
# print(co)
# print('---------------------')
# for c in co:
#     print(type(c))
#     print(c)
#     # print(c.keys())
#

anagrams = defaultdict(list)
a = 'dilences'
b = 'silenced'
a_list = list(a)
a_list.sort()
# print(a_list)

b_list = list(b)
b_list.sort()
# print(b_list)

# if a_list == b_list:
#     print('match!')

# hist1 = Counter('dilences')
# hist2 = Counter('silenced')
# if hist1 == hist2:
#     print('match!')

# hist1 = tuple(Counter('dilences').items())
# hist2 = tuple(Counter('silenced').items())
# print(type(hist1))
# intersect = []
# for c, d in hist2:
#     print('c', c)
#     print('d', d)
#     for a, b in hist1:
#         print('a', a)
#         print('b', b)
#         if a == c & b == d:
#             # match = [True for c, d in hist2 if a == c & b == d]
#             # if match:
#             print('its a match')
# print(type(a))
# print(a, b)
# anagrams[hist1].append('silenced')
# print(list(anagrams.values()))


# def solution(arr):
#     small_n = min(arr)
#     big_n = max(arr)
#
#     if small_n < 0 and big_n < 0:
#         return 1
#     elif small_n < 0 and big_n > 0:
#         for n in range(1, big_n):
#             if n in arr:
#                 continue
#             else:
#                 return n
#         return big_n+1
#     elif small_n > 0 and big_n > 0:
#         for n in range(small_n, big_n+1):
#             if n in arr:
#                 continue
#             else:
#                 return n
#         return big_n+1
#
#
# sol = solution([1,2,3])
# print(sol)
A = [1, 2, 3, 3, 1, 3, 1]


# count = [0] * (3 + 1)
# count = Counter(A).items()
# for i,v in count:
#     print(i)
# print(count.index(1))
# b = set(A)
# print(b)


def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    print(count)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if A.count(A[i]) > 0:
            tmp = A.count(A[i])  # count[A[i]]
            print(tmp)
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp
            print(count)
        else:
            count[A[i]] = 1
    return A[index]


A = [1, 2, 3, 3, 1, 3, 1]
B = [1, 2, 3, 3, 1, 3, 1, 3]


# sol = solution(3, A)
# print(sol)
# print(max(0, 1))
# sol = solution(3, B)
# print(sol)


def solution(A):
    sum_dict = {}
    for num in A:
        sum_dict[num] = sum_digits(num)

    values = set(sum_dict.values())
    key_arr = []
    for tmp in values:
        key_set = set()
        for k, v in sum_dict.items():
            if tmp == v:
                key_set.add(k)
        key_arr.append(key_set)

    best = 0
    summ = 0
    for k in key_arr:
        size = len(k)
        if size < 2:
            summ = -1
        elif size == 2:
            summ = sum(k)
        elif size > 2:
            tmp = []
            max_num = max(k)
            k.remove(max_num)
            tmp.append(max_num)
            tmp.append(max(k))
            summ = sum(tmp)

        if summ == -1:
            best = -1
        else:
            best = max(best, summ)

    return best


def sum_digits(A):
    return sum(int(digit) for digit in str(A))


# sol = solution([51,71,17,42])
# print(sol)
# sol2 = solution([42,33,60])
# print(sol2)
# sol3 = solution([51, 32, 43])
# print(sol3)

# def solution_3(A):
#     x = sum(int(digit) for digit in str(A))
#     return x
#
#
# def solution_2(A):
#     num_str = str(A)
#     sum = 0
#     for i in range(0, len(num_str)):
#         sum += int(num_str[i])
#     return sum
#
# sol = solution(20000000)
# print(sol)
#
# sol2 = solution_2(20000000)
# print(sol2)


def solution(A, K):
    n = len(A)
    best = 0
    count = 1
    result = 0
    for i in range(n - 1):
        if A[i] == A[i + 1]:
            count = count + 1
        else:
            count = 0
        # print(best, count)
        if count > best and count > K:
            result = A[i]
        best = max(best, count)
        # print(best)
        # print('------')

    return result


# sol1 = solution([1,1,3,3,3,4,4,4,4,5], 2)
# print(sol1)
# sol5 = solution([1,1,3,3,3,4,5,5,5,5], 2)
# print(sol5)
# sol3 = solution([1,1,3,3,3,4,4,4,4,4,4,5,5,5], 2)
# print(sol3)
# sol4 = solution([1,1,3,3,3,4,4,4,4,4,4], 2)
# print(sol4)
# sol2 = solution([1,1,3,4,4,4,5,5,5,5], 2)
# print(sol2)


# Binary-Gap
# def bar_solution(N):
#     gap = 0
#     zero_count = 0
#     one_count = 'Inactive'
#     binary = str(int(bin(N)[2:]))
#     bin_len = len(binary)
#     print(binary)
#     for i in range(bin_len - 1):
#         num = int(binary[i])
#         num_plus = int(binary[i + 1])
#         print(f'num: {num} at index: {i}')
#         if num == 1 and num_plus == 0:
#             zero_count += 1
#             one_count = 'Active'
#             print(f'count-1: {zero_count}')
#         elif num == 0 and num_plus == 1:
#             gap = max(gap, zero_count)
#             one_count = 'Inactive'
#             print(f'count-3: {zero_count}')
#         elif num == 0 and num_plus == 0 and zero_count >= 1:
#             if i == bin_len - 2 and one_count == 'Active':
#                 # gap = 0
#                 # zero_count = 0
#                 print(f'count-2: {zero_count} and gap-1: {gap}')
#             else:
#                 zero_count += 1
#                 print(f'count-2: {zero_count}')
#         else:
#             next
#         if one_count == 'Inactive':
#             gap = max(gap, zero_count)
#             zero_count = 0
#         print(f'count-4: {zero_count} and gap-2: {gap}')
#     return gap


def bar_solution(N):
    gap = 0
    zero_count = 0
    one_count = False
    binary = str(int(bin(N)[2:]))
    bin_len = len(binary)
    for i in range(bin_len - 1):
        num = int(binary[i])
        num_plus = int(binary[i + 1])
        if num == 1 and num_plus == 0:
            zero_count += 1
            one_count = True
        elif num == 0 and num_plus == 1:
            gap = max(gap, zero_count)
            one_count = False
        elif num == 0 and num_plus == 0 and zero_count >= 1:
            zero_count += 1
        else:
            next
        if one_count is False:
            gap = max(gap, zero_count)
            zero_count = 0
    return gap


# sol = bar_solution(529)
# print(sol)
# sol2 = bar_solution(1041)
# print(sol2)
# sol3 = bar_solution(15)
# print(sol3)
# sol4 = bar_solution(32)
# print(sol4)
# sol5 = bar_solution(20)
# print(sol5)


# Cyclic-Rotation
def cyc_solution(A, K):
    len_A = len(A)
    if len_A <= 1:
        return A
    elif len_A < K:
        K = K % len_A
        print(K)
        # K = int(str(tmp)[2:])

    target_index_arr = []
    for i in range(len_A):
        target_index_arr.append(get_index(i + 1, len_A, K))

    print(target_index_arr)
    new_arr = [0] * len_A
    for i in range(len_A):
        new_arr[target_index_arr[i]] = A[i]
    return new_arr


def get_index(position, length, move):
    target_pos = 0
    if position + move > length:
        target_pos = position + move - length
    else:
        target_pos = position + move
    return target_pos - 1


# sol = cyc_solution([3, 8, 9, 7, 6], 3)
# print(sol)
# sol2 = cyc_solution([3, 8, 9, 7, 6, 4, 6], 4)
# print(sol2)
# sol3 = cyc_solution([0, 0, 0], 1)
# print(sol3)
# sol4 = cyc_solution([1, 2, 3, 4], 4)
# print(sol4)
# sol5 = cyc_solution([1000], 5)
# print(sol5)
# sol6 = cyc_solution([1, 1, 2, 3, 5], 41)
# print(sol6)


def parse_accept_language(client_str, server_list):
    client_list = client_str.split(',')

    if len(server_list) <= 0 or not client_str:
        return 'This is not a valid request!'

    cl_set = set()
    for cl in client_list:
        cl_set.add(cl.strip())

    # print(cl_set)
    # accept = [ser for cl in cl_set for ser in server_list if cl == ser]
    accept = []
    for cl in cl_set:
        for ser in server_list:
            if cl == ser:
                accept.append(ser)

    # print(accept)
    return accept


# client = "en-US, fr-CA, fr-FR"
# server = ["fr-FR", "en-US"]
# par = parse_accept_language(client, server)
# print(par)
# par2 = parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])
# print(par2)
# par3 = parse_accept_language("en-US", ["en-US", "fr-CA"])
# print(par3)
# par4 = parse_accept_language("", [])
# print(par4)
# par5 = parse_accept_language("", ["en-US"])
# print(par5)
# par6 = parse_accept_language("atr", [])
# print(par6)
# par7 = parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])
# print(par7)
# par8 = parse_accept_language("en-US, en-US, fr-CA, fr-FR", ["en-US", "fr-FR"])
# print(par8)


def odd_occurrence_solution(N):
    length = len(N)
    if length % 2 == 0 or length == 1:
        return N

    odd = 0
    N.sort()
    print(f'N: {N}')

    for i in range(0, length - 2, 2):
        print(f'N: {N[i]} and {N[i + 1]} at {i}')
        if N[i] == N[i + 1]:
            next
        elif N[i + 1] == N[i + 2]:
            odd = N[i]
            break

        if odd == 0:
            odd = N[length - 1]
    return odd


# sol = odd_occurrence_solution([9,3,9,3,9,7,9])
# print(sol)
# sol2 = odd_occurrence_solution([9,3,9,3,9,7,9,7,5])
# print(sol2)
# sol3 = odd_occurrence_solution([3,9,3,9,9])
# print(sol3)
# sol4 = odd_occurrence_solution([3,9,3])
# print(sol4)
# sol5 = odd_occurrence_solution([1,1,1,3,4,5,4,3,1,2,2])
# print(sol5)
# sol6 = odd_occurrence_solution([3])
# print(sol6)


def reverse_str(S):
    string = ''
    str_list = S.split(' ')

    for s in str_list:
        N = len(s)
        word = ''
        for i in range(N - 1, -1, -1):
            word += (s[i])

        tmp = str(word).replace(', ', '')
        string = string + ' ' + tmp

    return string


# sol3 = reverse_str('This is Groupon')
# print(sol3)


import os
from datetime import date
import datetime


file_dict = {}
# fullFileLoc = '/datasink/%2Fsource%3Astring%2FmappingType%3Astring%2FfileType%3Astring%2Frelease%3Astring%2FspecVersion%3Astring/%2Fsource%3Af5d4c5d2-2951-4604-b9ad-0ef92177626e%2FmappingType%3AWIRRH_UK_EMIS_OBSERVATION%2FfileType%3AFILE_2%2Frelease%3A20160612120143%2FspecVersion%3A1/value.1471761801580'
# fullFileLoc = '/datasink/%2Fsource%3Astring%2FmappingType%3Astring%2FfileType%3Astring%2Frelease%3Astring%2FsubSource%3Astring%2FspecVersion%3Astring/%2Fsource%3A8c3b0171-47f9-4eae-b5a1-64f8112fc236%2FmappingType%3AXML_VALIDATION%2FfileType%3ASINGLE_FILE%2Frelease%3Av_1.20-CDH5%2FsubSource%3Ass1%2FspecVersion%3Asv2/value.1461345558748'
row = 'clk_1 C X WRITE 532 2016-04-22 12:06:34 /datasink/%2Fsource%3Astring%2FmappingType%3Astring%2FfileType%3Astring%2Frelease%3Astring/%2Fsource%3A8c3b0171-47f9-4eae-b5a1-64f8112fc236%2FmappingType%3ASINGLE_MULTILINE_FIXED_WIDTH_VALIDATION%2FfileType%3ASINGLE_FILE%2Frelease%3Av_1.20-CDH5/value.1461344794612'
components = row.split(' ')
# for i in range(len(components)):
# print(components[i] + ' at index ' + str(i))
file_size = components[4]
file_date = components[5]
file_time = components[6]
raw_file = components[7].split('%2F')
source_id = raw_file[5].split('%3A')[1]
map_type = raw_file[6].split('%3A')[1]
release, value = raw_file[8].split('%3A')[1].split('/')
if source_id in file_dict.keys():
    file_dict.get(source_id).append([file_size, file_date, file_time, raw_file])
else:
    file_dict[source_id] = [file_size, file_date, file_time, raw_file]


datasink = '/datasink/analytics'
des_file = '%2Fsource%3Astring%2FdataType%3Astring%2Frelease%3Astring'
now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S").replace('-', '')
direc = '%2Fsource%3A{}%2FdataType%3ACerner_DI_RAWENTITY%2Frelease%3A{}'.format('source_id', now)
full_path = datasink + '/' + des_file + '/' + direc
print(full_path)
create_dir = os.popen("hdfs dfs -mkdir {}".format(direc))



# for i in range(len(raw_file_loc)):
#     print(raw_file_loc[i] + ' at index ' + str(i))
#
# for comp in raw_file_loc:
#     # print(component)
#     # print('source%3Astring'.find('%3A'))
#     com_dict = {}
#     if comp.find('%3A') != -1:
#         com = comp.split('%3A')
#         if com[0] == 'source' and com[1] != 'string':
#             source_id = com[1]
#         if com[0] == 'mappingType' and com[1] != 'string':
#             map_type = com[1]
#         if com[0] == 'specVersion' and com[1] != 'string':
#             value = com[1].split('/')[1]
#         if com[0] == 'release' and com[1] != 'string':
#             release = com[1]

# print(raw_file)
# source_id = raw_file[5].split('%3A')[1]
# map_type = raw_file[6].split('%3A')[1]
# release, value = raw_file[8].split('%3A')[1].split('/')
# if source_id in file_dict.keys():
#     file_dict.get(source_id).append([file_size, file_date, file_time, raw_file])
# else:
#     file_dict[source_id] = [file_size, file_date, file_time, raw_file]

print('source_id: ', source_id)
print('map_type: ', map_type)
print('value: ', value)
print('release: ', release)



