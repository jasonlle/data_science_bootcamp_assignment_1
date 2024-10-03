# Jason Le (jl14793)
# Data Science Bootcamp Take-Home Problem Set #1

#1
def count_vowels(word):
    total = 0
    for letter in word:
        if letter in ['A','E','I','O','U','a','e','i','o','u']:
            total += 1
    return total

#2
def auto_cap(lst):
    new_word = ''
    for word in lst:
        for letter in word:
            new_word += letter.capitalize()
        print(new_word)
        new_word = ''
        
#3
def odd_even_identifier():
    for num in range(1,21):
        if num % 2 == 0:
            print(f'{num} is even')
        else:
            print(f'{num} is odd')

#4
def sum_of_integers(a,b):
    total = a
    total += b
    return total

def main():
#1
    word = 'apple'
    print(count_vowels(word))
    
    print('\n')
    
#2
    animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
    auto_cap(animals)
    
    print('\n')
    
#3
    odd_even_identifier()
    
    print('\n')
#4
    
    num_1 = 7
    num_2 = 3
    num_3 = 2
    print(sum_of_integers(num_1,num_2))
    print(sum_of_integers(num_3,num_1))
    
main()
            
