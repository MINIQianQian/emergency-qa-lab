

# 1 判断 list 是否是回文


# 判断一个 list 正着读和反着读是否一样。


# 示例


# input:  [1,2,3,2,1]

# output: True

# input:  [1,2,3]

# output: False



def iahuiwen(num:list):


    return num == num[::-1]




# 2 找 list 中出现最多的数字


# 示例


# input:  [1,2,3,2,4,2,5]
# output: 2


def find_spec_num(num:list):


    count = {}


    for n in num:

        count[n] = count.get(n,0) + 1

    

    # result = max(count,key=count.get(n))


    for x,y in count.items():


        if y > maxnumber:


           maxkey = x


           maxnumber = y


    return maxkey

        


print(find_spec_num([1,2,3,2,4,2,5]))



# 3 找出 list 中重复的元素


# 示例


# input:  [1,2,3,2,4,5,3]

# output: [2,3]



def find_deplicate(num:list):


    seen = set()

    duplicate_list = []


    for n in num:


        if n not in seen:

            seen.add(n)
        else:

            duplicate_list.append(n)

    

    return duplicate_list



# 4 反转一个 list


# 示例


# input:  [1,2,3,4]

# output: [4,3,2,1]



def reserve_list(num:list):


    reservedlist = num[::-1]


    return reservedlist



# 5 判断字符串是否是回文


# 示例


# input: "level"

# output: True

# input: "hello"

# output: False


def is_huiwen(num:list):


    firstelement = 0


    last_element = len(num)-1


    while firstelement < last_element:


        if num[firstelement] != num[last_element]: 


            return False
        

        firstelement += 1

        last_element -= 1


    return True



print(is_huiwen("level"))



# 6 找两个数相加等于 target（Two Sum）


# 示例


# nums = [2,7,11,15]

# target = 9


# 输出


# [0,1]


# 因为


# 2 + 7 = 9


def find_target(num:list):


    new_list = []


    for x in len(num) -1:


        for y in len(num) - 1 - x:


            if num[x] + num[y] == 9:

                new_list.append(x)

                new_list.append(y)


    return  new_list           


print(find_target([2,7,11,15]))

        

# 7 合并两个排序 list


# 示例

# input:

# a = [1,3,5]

# b = [2,4,6]

# output:

# [1,2,3,4,5,6]


def conbin(x:list,y:list):


    result = x + y
    return result


print(conbin([1,3,5],[2,4,6]))



# 8 统计字符串中每个字符出现次数


# 示例


# input: "hello"


# 输出


# {

# h:1
# e:1
# l:2
# o:1

# }


def count_alf(name:str):


    name_list = list[name]


    counter = {}



    for n in name_list:


        counter[n] = counter.get(n,0) + 1
    

    return counter

print(count_alf("hello"))



# 9 找 list 中第二大的数字


# 示例


# input:  [3,7,2,9,5]


# output: 7


def fin_2ndmax(num:list):

    new_list = sorted(num)

    return new_list[len(num) -2 ]


print(fin_2ndmax([3,7,2,9,5]))


# 10 计算时钟时针和分针夹角（你刚做的题）


# 示例


# input: 3:30

# output: 75

# def find_clockangle(hours:int,mins:int):

#     # clock_angle = hours_angle - mins_angle + hoursmins

#     hours =  hours%12

#     hours_angle = 360/12*hours +360/12/60 * mins

#     mins_angle  = 360/60*mins


#     clock_angle = abs(hours_angle - mins_angle)

#     clock_angle = min(clock_angle,360-clock_angle)



#     return clock_angle


# print(find_clockangle(3,30))



# logs = [
#     "INFO: service started",
#     "ERROR: database failed",
#     "WARNING: high memory usage",
#     "ERROR: timeout",
#     "INFO: retrying"
# ]

# 输出：

# {"INFO": 2, "ERROR": 2, "WARNING": 1}

def report_inspect(lins:list):

    counts = {}

    for line in lins:

        if "INFO:" in line:
            counts["INFO"] = counts.get("INFO",0) + 1
        elif "ERROR:" in line:
            counts["ERROR"] = counts.get("ERROR",0) + 1
        elif "WARNING:" in line:
            counts["WARNING"] = counts.get("WARNING",0) + 1


    return counts


print(report_inspect([
    "INFO: service started",
    "ERROR: database failed",
    "WARNING: high memory usage",
    "ERROR: timeout",
    "INFO: retrying"
]))

# intervals = [(1,3), (2,6), (8,10), (9,12)]

# 如果区间 重叠，就合并。

# 输出：

# [(1,6), (8,12)]
    
def mergeintervel(intervel:list):

    
    intervel.sort()
    # intervals = [(1,3), (2,6), (8,10), (9,12)]
    ordered_list = []


    for x,y in intervel:

        if not ordered_list:
            # [(1,3)]
            ordered_list.append(x,y)
        elif x <= ordered_list[-1][1]:

            last_start,last_end = ordered_list[-1]

            ordered_list[-1]= last_start,max(last_end,y)
        else:
            ordered_list.append(x,y)

    return ordered_list





            





