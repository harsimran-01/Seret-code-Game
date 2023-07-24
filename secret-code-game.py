import random

alphabtes_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


new_appended_word_1 = random.choice(alphabtes_list)
new_appended_word_2= random.choice(alphabtes_list)
new_appended_word_3 = random.choice(alphabtes_list)
new_appended_word_4 = random.choice(alphabtes_list)
new_appended_word_5 = random.choice(alphabtes_list)
new_appended_word_6 = random.choice(alphabtes_list)


def for_encode(string):

    splitted_string = list(string)         #coverts the input string into a list.
    
    count_string = len(splitted_string)      #counts the length of the list
    
    if count_string > 3:
        remove_first_alphabet = splitted_string.pop(0)                #removes the first string 
       
        append_alphabet = splitted_string.append(remove_first_alphabet)            #now append that removed string to the last
        
        final_string = "".join(splitted_string)              #converting list into a string.
        
        new_word = new_appended_word_1 + final_string          #adding random alphabets to the beginning and ending
        new_word_1 = new_appended_word_2 + new_word
        new_word_2 = new_appended_word_3 + new_word_1
        new_word_3 = new_word_2 + new_appended_word_4
        new_word_4 = new_word_3 + new_appended_word_5
        finallllly_code = new_word_4 + new_appended_word_6

        return f"\nYour ENCODED Code is *{finallllly_code}*\n ."
        
    else:
        new_string = " "
        for i in range(len(string)-1, -1, -1):                   #just reverse the string.
            new_string += string[i]
        return f"\nYour ENCODED Code is *{new_string}*\n ."    
        
def for_decode(string_2):

    splitted_string_2 = list(string_2)
    
    count_string_2 = len(splitted_string_2)
    
    if count_string_2 > 3:
        splitted_string_2 = splitted_string_2[:-3]      #removes last 3 string from the list
        
        splitted_string_2 = splitted_string_2[3:]       #removes first 3 string from the list
        
        final_string = splitted_string_2.pop()          #removes the last string from list no index is given as by default it is last.
        
        finallly_string = splitted_string_2.insert(0, final_string)    #inserted the last string which we removed above to the beginning.
        
        very_final = "".join(splitted_string_2)          #now again turn the list into a single string.
        return f"\nYour DECODED Code is *{very_final}*\n"
        
    else:
        new_string_2 = " "
        for i in range(len(string_2)-1, -1, -1):         #just reverse the string.
            new_string_2 += string_2[i]
        return f"\nYour DECODED Code is *{new_string_2}* \n"   
        
ask = input("\nDo you want to ENCODE or DECODE your CODE: ")
if ask == "ENCODE":                                                 #I have done this in another as want more specifications, we can put these into the below conditional statements also.
    print("\n*****WELCOME TO CODE ENCODER*****\n")        
else:
    print("\n*****WELCOME TO CODE DECODER*****\n")
        
input_new_string = input("Enter the Code: ").lower()

if ask == "ENCODE":
    a = for_encode(input_new_string)                        #calling functions acc the to the input   
    print(a)

else:
    b = for_decode(input_new_string)
    print(b)

