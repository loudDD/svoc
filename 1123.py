from readExcel.readexcel import readExcel
read=readExcel()

for i in range(1,read.get_lines()):
    b=read.getvalue(i)
    print(b)
    print(type(b))