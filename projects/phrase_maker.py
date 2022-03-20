user_phrases = []

def make_sentece(phrase):
    str_phrase = str(phrase)
    interrogatives = ('how', 'what', 'why')
    capitalized = str_phrase.capitalize()
    if  str_phrase.startswith(interrogatives): 
        return f'{capitalized}?'
    else: 
        return f'{capitalized}.'

def handle_user_inputs(): 
    while True: 
        phrase = input('Say something: ')
        if phrase == '\end': 
            break
        else: 
            user_phrases.append(make_sentece(phrase))

def print_phrases(user_phrases):
    for item in user_phrases: 
        print(item, end=' ')


handle_user_inputs()
print_phrases(user_phrases)