"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Filip Hnilica
email: filip.hnilica@gmail.com
"""

texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

passwords = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}

def analyze_text(text):
    results = {
        'words': 0,
        'title_case': 0,
        'upper_case': 0,
        'lower_case': 0,
        'numeric_strings': 0,
        'sum_of_numbers': 0,
        'words_lengths': {}
    }
    words = text.split()
   
    for word in words:

        word_length = len(word.strip('.,;:!?()[]{}"\'-'))
        results['words_lengths'][word_length] = results['words_lengths'].get(word_length, 0) + 1
        if word.isdigit():
            results['numeric_strings'] += 1
            results['sum_of_numbers'] += int(word)
        elif word.isupper():
            results['upper_case'] += 1
        elif word.islower():
            results['lower_case'] += 1
        elif word.istitle():
            results['title_case'] += 1
        
        results['words'] += 1
    
    
    return results

def check_password(username, password):
    if username in passwords and passwords[username] == password:
        return True
    return False

def print_word_length_table(word_lengths):

    if not word_lengths:
        print("No words to display in table.")
        return
    
    # Print table header
    print("\nWord Length Table:")
    print(f"{'Len':<4} {'Occurences':<20} {'Nr.':<10}")
    print("-" * 40)
    
    #print each word length and its count
    for length, count in sorted(word_lengths.items()):
        asterisks = "*" * count
        print(f"{length:<2} | {asterisks:<20} | {count:<10}")

    print("-" * 40)
    print("Word length Table:")

input_username = str(input("Enter your username: "))
input_password = str(input("Enter your password: "))

print("-" * 40)

if check_password(input_username, input_password):

    print("Welcome to the app, " + input_username + "!")
    print("We have " + str(len(texts)) + " texts to be analyzed.")
    print("-" * 40)

    text_number = int(input("Enter a number between 1 and " + str(len(texts)) + ": "))
    print("-" * 40)

    if 1 <= text_number <= len(texts):
        selected_text = texts[text_number - 1]
        print("Analyzing text number " + str(text_number) + "...")
        analysis_results = analyze_text(selected_text)

        print("-" * 40)
        print(f"There are {analysis_results['words']} words in the selected text.")
        print(f"There are {analysis_results['title_case']} titlecase words.")
        print(f"There are {analysis_results['upper_case']} uppercase words.")
        print(f"There are {analysis_results['lower_case']} lowercase words.")
        print(f"There are {analysis_results['numeric_strings']} numeric strings.")
        print(f"The sum of all the numbers is: {analysis_results['sum_of_numbers']}.")
        print("-" * 40)
        print("Word length Table:")
        print_word_length_table(analysis_results['words_lengths'])
        print("-" * 40)
    else:
        print("Invalid number. Please enter a number between 1 and " + str(len(texts)) + ".")
        exit()
else:
    print("Invalid username or password. Please try again.")
    exit()