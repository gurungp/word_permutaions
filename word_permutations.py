


def add_to_index(word_passed):
    final_list = []
    new_word = word_passed
    print(f"Word received is {word_passed}")
    for _ in range(len(word_passed) - 1):
        permutaion_lists = []
        for i in range(len(word_passed)):
            a=i+1
            if a==len(word_passed):
                a=0
            permutaion_lists.append(new_word[a])
        new_word = ''.join(permutaion_lists)
        final_list.append(''.join(new_word))

    print(f"Final list is {final_list}")
    return final_list

def find_all_permutations(word):
    # Step 1
    rest_of_word = {word[i:]:[] for i in range(0,len(word)-1)}
    print(rest_of_word)

    # Step 2
    temp=[]
    for word in reversed(rest_of_word):
        word_as_list = list(word)
        print(word_as_list)
        if(len(word)==2):
            flat_perm_list = ''.join(add_to_index(word))
            rest_of_word[word].append(word)
            rest_of_word[word].append(flat_perm_list)
            temp=rest_of_word[word]
            print(f"Temp : {temp}")
        else:
            for val in temp:
                new_word_to_add = word[0]+val
                rest_of_word[word].append(new_word_to_add)
                # print(f"New Word to Add : {new_word_to_add}")
                flat_perm_list = (add_to_index(new_word_to_add))
                for val in flat_perm_list:
                    rest_of_word[word].append(val)
                # print(f"New Word to Add : {flat_perm_list}")

            temp=rest_of_word[word]
    return rest_of_word

# word_for_test = 'abcde'
# result = find_all_permutations(word_for_test)
# print(f"Final Dictionary - {result}")
# print(f"Number of elements on abcd - {len(result[word_for_test])}")
# print(f"List of permutations - {result[word_for_test]}")
