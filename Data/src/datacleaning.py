def remove_subtitle_time(filename, encoding, src = "./", dst="./"):
    try:
        print("faula", filename)
        raw_sub = open(src+"%s" %filename, "r", encoding=encoding)
        clean_sub = open(dst+"%s-clean.txt" %filename, "w", encoding=encoding)
        for sub_line in raw_sub:
            if is_time(sub_line):
                pass
            elif convertable_to_int(sub_line):
                pass
            elif is_feeling(sub_line):
                pass
            else:
                print("write")
                clean_sub.write(sub_line)
        clean_sub.close()
    except:
        pass


def is_feeling(line):
    if line[0] == "[" or line[-1] == "]":
        return True


def is_time(line):
    try:
        return (line[2] == ":") and (line[5] == ":") and (line[8] == ",")
    except:
        return False


def convertable_to_int(line):
    try:
        int(line[:len(line)-1])
        return True
    except:
        return False
