from read_words import *

class Processor:
    running = True
    randomise = False
    restart = False
    dictionary = {}
    def __init__(self, dictionary):
        self.dictionary  = dictionary

def print_help():
    print("type \"1\" to see it again")
    print("type \"2\" to look thought all the words in the selected section")
    print("type \"666\" to finish")
    print("type \"66\" to restart")
    print("type \"6\" to look through available sections")
    print("type \"00\" to restart with randomiser")
    print("type \"0\" to restart loop")

def main_cycle(processor):
    from random import randrange

    dictionary = processor.dictionary
    if len(dictionary) == 0:
        print(">> WARNING: dictionary is empty <<")
        processor.restart = True
        return processor
    print_help()
    user_input = ""
    processor.running = True
    processor.restart = False
    processor.randomise = False
    while processor.running:
        mistakes = 0
        keys_list = ["0"] * len(dictionary)
        keys = [key for key in dictionary.keys()]
        for i in range(len(keys)):
            if processor.randomise:
                rand_ind = randrange(0,len(keys))
                while keys_list[rand_ind] != "0":
                    rand_ind = randrange(0,len(keys))
                keys_list[rand_ind] = keys[i]
            else:
                keys_list[i] = keys[i]
        for i in range(len(keys_list)):
            key = keys_list[i]
            print(i + 1, "/", len(keys_list), "t: '" + key + "'")
            user_input = input(">>> ")
            if user_input == "1":
                print_help()
            elif user_input == "666":
                processor.running = False
                break
            elif user_input == "66":
                processor.restart = True
                processor.running = False
                break
            elif user_input == "6":
                print(get_sections())
            elif user_input == "00":
                processor.randomise = True
                break
            elif user_input == "0":
                processor.randomise = False
                break
            elif user_input == "2":
                for key in dictionary.keys():
                    print(">>", key)
                    wanted_data = ""
                    for data in dictionary[key]:
                        wanted_data += data + " "
                    wanted_data = wanted_data[0:len(wanted_data) - 2]
                    print("<<", wanted_data,"\n")
                break
            else:
                wanted_data = ""
                for data in dictionary[key]:
                    wanted_data += data + " "
                wanted_data = wanted_data[0:len(wanted_data) - 2]
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

        print("~~~~~~~~~~~~~~~~")
        print("mistakes:", mistakes)
        print("randomiser:", processor.randomise)
        print("~~~~~~~~~~~~~~~~")
    return processor

def main():
    print(get_sections())
    tags = input("enter tags or sections numbers: ").split()
    processor = Processor(get_dictionary(tags))
    processor = main_cycle(processor)
    while processor.restart:
        print(get_sections())
        tags = input("enter tags or sections numbers: ").split()
        processor.dictionary = get_dictionary(tags)
        processor = main_cycle(processor)
    check_for_repetitions()

