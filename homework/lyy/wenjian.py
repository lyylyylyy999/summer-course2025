# with open("homework/lyy/jingyesi.txt","r",encoding = "utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)


with open("homework/lyy/poem.txt","w",encoding = "utf-8") as f:
    f.write("我欲乘风归去，\n")
    f.write("有孔琼楼玉宇，\n")
    f.write("高处不胜寒。")

with open("homework/lyy/poem.txt","r+",encoding = "utf-8") as f:
    f.read()
    f.write("\n起舞弄清影，\n")
    f.write("何似在人间。")