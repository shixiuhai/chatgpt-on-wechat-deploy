def count_string(str_1:str)->tuple:
    count_a_number = str_1.count("a")
    count_going_number = str_1[0:41].count("going")
    return (count_a_number,count_going_number)
    
if __name__ == "__main__":
    print(count_string("abcda"))
