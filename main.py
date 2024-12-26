import csv
import time


# 生成文件初始化，写入表头
def get_init(infile, outfile):
    with open(infile, 'r', encoding="utf-8-sig") as file1:
        dataer = csv.reader(file1)
        ls = list(dataer)
    with open(outfile, 'w', encoding="utf-8-sig", newline="") as file2:
        writer_data = csv.writer(file2)
        writer_data.writerow(ls[0])
    return ls


# 读取文件数据
def get_data(file):
    ls = []
    with open(file, 'r', encoding="utf-8-sig") as file1:
        dataer = csv.reader(file1)
        next(dataer)
        for row in dataer:
            ls.append(row)
    return ls

# 版本信息
print("---------------欢迎使用TIMO---------------")
print("")
print("作者:阿巴阿巴家的迷你3pro      版本1.0.0")
print("")
print("-----------------------------------------")

# 提示用户输入
print("注意:使用前请先将文件转换为csv文件\n")
inputfi1 = input("请输入文件名1:") + ".csv"
inputfi2 = input("请输入文件名2:") + ".csv"
outputfi = input("请输入输出文件名:") + ".csv"
print("文件解析中....")

selcet_str = get_init(inputfi1, outputfi)
time.sleep(0.5)
print("文件解析完毕")
print(selcet_str[0])
compare_str = input("请输入比较字段:")
change_str = input("请输入更改字段:")
fill_str = input("请输入填充字段:")

print("目标文件生成中.....")
data1 = get_data(inputfi1)
data2 = get_data(inputfi2)

# 获取的第一列数据
ls1 = [data1[i][selcet_str[0].index(compare_str)] for i in range(len(data1))]
ls2 = [data2[j][selcet_str[0].index(compare_str)] for j in range(len(data2))]

updata = []

# 对比第一列数据，找出不同数据
for k in ls1:
    if k not in ls2:
        data1[ls1.index(k)][selcet_str[0].index(change_str)] = fill_str
        updata.append(data1[ls1.index(k)])
        print("已更改", data1[ls1.index(k)])

with open(outputfi, 'a', encoding="utf-8-sig", newline='') as file3:
    writer = csv.writer(file3)
    for l in data2:
        print("已写入", l)
        writer.writerow(l)
    for o in updata:
        print("已写入", o)
        writer.writerow(o)

print("写入完毕")
time.sleep(1)
print("目标文件已生成")
