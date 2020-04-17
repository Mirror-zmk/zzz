# 从成绩单文件 report.txt 中读取班级成绩，并完成统计分析

# 要求：
# 1.读取 report.txt 文件中的成绩；
# 2.统计每名学生总成绩、计算平均并从高到低重新排名；
# 3.汇总每一科目的平均分和总平均分（见下表第一行）；
# 4.添加名次，替换60分以下的成绩为“不及格”；
# 5.将处理后的成绩另存为一个新文件（result.txt）。

# 读取文件
with open('report.txt',encoding = 'utf8') as f:
    lines = f.readlines()
    lst = []
    for l in lines:   # 遍历每一行内容，将其作为一个个字符串传入列表lst
        l = l.split()
        lst.append(l)
    lst[0].append('总分')    # 在第一个字符串里添加这几项
    lst[0].append('平均分')
    lst[0].insert(0,'名次')
    # print(lst)

# 计算每一名同学的总分和平均分，将其传入列表中的每一个字符串末尾
for i in lst[1:]:
    scores = 0
    for j in i[1:]:
        scores += float(j)
        avg = scores / 9
    i.append(str('%d' % scores))
    i.append(str('%.1f' % avg))
    # print(i)

# 排序
lst.sort(key=lambda x:x[10],reverse=True)
# print(lst)

# 计算每一科目的平均分和总平均分，添加到lst
avg_lst = []      # 定义一个空列表接收所有计算出的科目平均分
for m in range(1,len(i)):
    sub_sum = 0
    sub_avg = 0
    for n in lst[1:]:
        sub_sum += float(n[m])
        sub_avg = sub_sum / len(lst[1:])
    avg_lst.append('%.1f' % sub_avg)
avg_lst.insert(0,'平均')
avg_lst.insert(0,'0')
# print(avg_lst)

# 插入到lst的第二项
lst.insert(1,avg_lst)
# print(lst)

# 添加排名
rank = 0
for x in lst[2:]:
    rank += 1
    x.insert(0,str(rank))
    # 顺便将成绩中低于60分的数据改成不及格，总分和平均分不需要改，所以到倒数第三位为止
    for y in range(2,len(x)-1):   # 前面加了0和平均，所以要从第三位开始看
        if float(x[y]) < 60:
            x[y] = '不及格'
# print(lst)

# 将数据写入result.txt文件
with open('result.txt','w',encoding='utf8') as f:
    for lines2 in lst:
        for l2 in lines2:
            f.write(l2+'  ')
        f.write('\n')



















