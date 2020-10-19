import pandas


df = pandas.read_excel("url.xlsx")

data = df.head(3)
print(type(data))
print("获取到所有的值:\n%s"%data)#格式化输出