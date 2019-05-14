def subtract_dictionary_frequency(dictionary_one, dictionary_two):
    result = dict()
    keys_two = dictionary_two.keys()
    for key_one in dictionary_one.keys():
        if key_one in keys_two:
            new_value = dictionary_one[key_one] - dictionary_two[key_one]
            if new_value>0:
                result[key_one] = new_value
        else:
            result[key_one] = dictionary_one[key_one]
    return result