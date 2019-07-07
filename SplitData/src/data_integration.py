import os

# #label 1:
# l1= open("label1.txt", "w")
# for item in os.walk("../semi_raw_data\\label1"):
#     files = item[2]
#     for file in files:
#         print(file)
#         t = open("../semi_raw_data\\label1\\"+file,"r").read()
#         l1.write(t.replace("-", ""))


def integrate(direcory, export_file):
    export = open(export_file, "w")
    for item in os.walk(direcory):
        files = item[2]
        for file in files:
            print(file)
            t = open(direcory + file, "r").read()
            export.write(t.replace("-", ""))
    export.close()


if __name__ == "__main__":
    integrate("../semi_raw_data\\label1\\", "label1.txt")
    integrate("../semi_raw_data\\label2\\", "label2.txt")