import sys
def count_words(text):    
    total_words = text.split()
    return(f"Found {len(total_words)} total words")

def character_count(text):
    characters = {}
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters



        

def sort(characters):
    dic_list = []
    for char in characters:
        if char.isalpha() == False:
            continue
        else:
            dict = {}
            dict["char"] = char
            dict["num"] = characters[char]
            dic_list.append(dict)
            dic_list = sorted(dic_list, key=lambda x: x["num"], reverse=True)
    return dic_list



def get_num(dic_list, char):
    for item in dic_list:
        if item["char"] == char:
            return item["num"]





