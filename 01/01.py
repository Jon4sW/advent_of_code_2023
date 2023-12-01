import re

with open("input", "r") as in_file:
    lines = in_file.readlines()


# First     
total_sum = 0

for line in lines:
    
    all_integers = re.findall("[0-9]", line)
    
    total_sum += int( all_integers[0] + all_integers[-1] )
    
print(total_sum)


# Second
word_to_int = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
    "zero":"0"
}

total_sum_2 = 0

for line in lines:
    
    all_integers = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine|zero))", line)
    
    fist_number = all_integers[0]
    if fist_number in word_to_int:
        fist_number = word_to_int[fist_number] 
    
    second_number = all_integers[-1]
    if second_number in word_to_int:
        second_number = word_to_int[second_number] 
        
    total_sum_2 += int( fist_number + second_number )
    
print(total_sum_2)


