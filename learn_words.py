from read_words import *

def print_help(dictionary = {}):
    print("type \"1\" to see it again")
    print("type \"2\" to look thought all the words in the selected section")
    print("type \"666\" to finish")
    print("type \"66\" to restart")
    print("type \"6\" to look through available sections")
    print("type \"000\" to restart with reversed order")
    print("type \"00\" to restart with randomiser")
    print("type \"0\" to restart loop")

def print_current_dictionary(dictionary):
    for key in dictionary.keys():
        print(">>", key)
        wanted_data = ""
        for data in dictionary[key]:
            wanted_data += data + " "
        wanted_data = wanted_data[0:len(wanted_data) - 1]
        print("<<", wanted_data,"\n")

funcs = {
    "1" : print_help,
    "2" : print_current_dictionary,
    "6" : get_sections,
}

class Processor:
    running = True
    randomise = False
    restart = False
    reverse = False
    dictionary = {}
    def __init__(self, dictionary):
        self.dictionary  = dictionary

def main_cycle(processor, tags):
    from random import randrange
    processor.running = True
    processor.randomise = False
    processor.restart = False
    processor.reverse = False
    dictionary = processor.dictionary
    if len(dictionary) == 0:
        print(">> WARNING: dictionary is empty <<")
        processor.restart = True
        return processor
    print_help()
    user_input = ""
    while processor.running:
        states = {
            "1"   : [processor.running, processor.randomise, processor.restart, processor.reverse, False],
            "2"   : [processor.running, processor.randomise, processor.restart, processor.reverse, True ],
            "666" : [False,             processor.randomise, processor.restart, processor.reverse, True ],
            "66"  : [False,             processor.randomise, True,              processor.reverse, True ],
            "6"   : [processor.running, processor.randomise, processor.restart, processor.reverse, False],
            "000" : [processor.running, processor.randomise, processor.restart, True,              True ],
            "00"  : [processor.running, True,                processor.restart, processor.reverse, True ],
            "0"   : [processor.running, False,               processor.restart, False,             True ],
        }
        print("~~~~~~~~~~~~~~~~")
        print("tags:", tags)
        mistakes = 0
        keys_list = ["0"] * len(dictionary)
        keys = [key for key in dictionary.keys()]
        for i in range(len(keys)):
            if processor.randomise:
                rand_ind = randrange(0,len(keys))
                while keys_list[rand_ind] != "0":
                    rand_ind = randrange(0,len(keys))
                keys_list[rand_ind] = keys[i]
            elif processor.reverse:
                keys_list[len(dictionary) - 1 - i] = keys[i]
            else:
                keys_list[i] = keys[i]
        i = 0
        while i < len(keys_list):
            key = keys_list[i]
            print(i + 1, "/", len(keys_list), "t: '" + key + "'")
            user_input = input(">>> ")
            if all([c.isdigit() for c in user_input]) and user_input in states:
                i -= 1
                processor.running, processor.randomise, processor.restart, processor.reverse, do_break = states[user_input]
                if user_input in funcs:
                    print(funcs[user_input])
                    funcs[user_input](dictionary)
                if do_break:
                    break
            else:
                wanted_data = ""
                for data in dictionary[key]:
                    wanted_data += data + " "
                wanted_data = wanted_data[0:len(wanted_data) - 1]
                if wanted_data == user_input:
                    print("CORRECT")
                else:
                    mistakes += 1
                    print("NO:'" + wanted_data + "'")
                    wrong = True
                    while wrong:
                        print("t: '" + key + "'")
                        user_input = input("### ")
                        if wanted_data == user_input:
                            print("CORRECT. going on...")
                            wrong = False
                        else:
                            print("NO:'" + wanted_data + "'")
            i += 1
        print("~~~~~~~~~~~~~~~~")
        print("mistakes:", mistakes)
        print("randomiser:", processor.randomise)
    return processor

def main():
    print(get_sections())
    tags = input("enter tags or sections numbers: ").split()
    processor = Processor(get_dictionary(tags))
    processor = main_cycle(processor, tags)
    while processor.restart:
        print(get_sections())
        tags = input("enter tags or sections numbers: ").split()
        processor.dictionary = get_dictionary(tags)
        processor = main_cycle(processor, tags)
    check_for_repetitions()

