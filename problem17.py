"""
Created on Thu Mar 22 12:31:10 2018

@author: patricio
"""

num_dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
               '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten',
               '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen',
               '15':'fifteen', '16':'sixteen', '17':'seventeen',
               '18':'eighteen', '19':'nineteen', '20':'twenty', 
               '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', 
               '70':'seventy', '80':'eighty', '90':'ninety'}

def return_num_in_letters(num_str):
    num_dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
                   '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten',
                   '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen',
                   '15':'fifteen', '16':'sixteen', '17':'seventeen',
                   '18':'eighteen', '19':'nineteen', '20':'twenty', 
                   '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', 
                   '70':'seventy', '80':'eighty', '90':'ninety'}
    if (len(str(int(num_str))) < 2):
        num_in_letters = num_dict[str(int(num_str))]
    else:
        if (num_str[0] == '1' or num_str[1] == '0'):
            num_in_letters = num_dict[num_str]
        else:
            num_in_letters = num_dict[num_str[0]+'0'] + num_dict[num_str[1]]
    return num_in_letters

def count_letters(string):
    str_count = len([letter for letter in string])
    return str_count
        

num_letter_list = []
for i in range(1,1000):
    num_str = str(i)
    if(len(num_str) < 3):
        num_letter_list.append(return_num_in_letters(num_str))
    else:
        if(num_str[1] == '0' and num_str[2] == '0'):
            num_letter = num_dict[num_str[0]] + 'hundred'
        else:
            num_letter = num_dict[num_str[0]] + 'hundredand' + return_num_in_letters(num_str[1:3])
        num_letter_list.append(num_letter)
num_letter_list.append('onethousand')

print(sum([count_letters(string) for string in num_letter_list]))
