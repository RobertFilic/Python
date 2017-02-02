#Write a function roman_to_int(string) that takes a roman number as a string and returns an integer representation of the number
#Your code needs to be able to handle numbers between 1 and 4999
'''
Number	        4	9	40	90	400	900
Notation	IV	IX	XL	XC	CD	CM
'''
dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# roman_to_int("MCMLIV")

def roman_to_int(roman_string):
    #define empty vector to save each character of the string
    char_length = [0 for x in range(len(str(roman_string)))]
    #define length of vector number which will have the final intiger
    number = [0 for x in range(len(str(roman_string))+1)]

   #go through the Roman string and write int number from dictionary to char_length
    for i in range(0, len(roman_string)):
        char_length[i] = dictionary[roman_string[i]]

    #read 2 consecutive positions in the vector and compare them
    for i in range(0, len(char_length)):
        n1 = char_length[i]
    #chec that n2 is not out of range. If it's out of range define it 0.
        if i < len(char_length)-1:
            n2 = char_length[i+1]
        else:
            n2 = 0

    # if n1 equal 0 skip this step (means we performed step 1 < 2 where we defined n1=0)
        if n1 == 0:
            pass
        
    # if n1 >= n2 copy 1 to number[i]
        elif n1 >= n2:
            number[i] = n1

    # if n1 < n2 write n2-n1
        elif n1 < n2:
            number[i] = n2 - n1
            char_length[i+1] = 0
    return(sum(number))
        

    
