def check_for_repetitions():
    pass

def get_sections():
    lines = ""
    with open("dictionary.md", "r", encoding = "utf-8") as f:
        lines = f.readlines()
    output = ""
    count = 1
    for line in lines:
        if line[0:2] == "##":
            output += str(count) + ": " + line[2:len(line)]
            count += 1
    return output

def check_tags_for_numbers(tags):
    res = []
    try:
        res = [int(i) for i in tags]
    except:
        pass
    return res

def get_dictionary(tags = ""):
    lines = ""
    with open("dictionary.md", "r", encoding = "utf-8") as f:
        lines = f.readlines()
    dictionary = {}
    read_this_section = False
    access_by_number = False
    nums = check_tags_for_numbers(tags)
    if len(tags) == 0:
        read_this_section = True
    else:
        if len(nums) > 0:
            access_by_number = True
    counter = 0
    for i in range(len(lines)):
        line = lines[i]
        if len(tags) > 0 and line[0:2] == "//":
            counter += 1
            read_this_section = False
            if access_by_number:
                if counter in nums:
                    read_this_section = True
            else:
                for tag in tags:
                    if tag in line.split():
                        read_this_section = True
                        break
        elif line.count(" ") == len(line) - 1:
            continue
        elif line[0:2] != "##" and read_this_section:
            list_form = line.split(";")
            key = list_form[0]
            data = list_form[1:len(list_form)]
            for i in range(len(data)):
                tmp = data[i].split()
                data[i]= ""
                for j in range(len(tmp)):
                    if j < len(tmp) - 1:
                        data[i] += tmp[j] + " "
                    else:
                        data[i] += tmp[j]
            dictionary[key] = data
    return dictionary

def save_dictionary(dictionary):
    pass
