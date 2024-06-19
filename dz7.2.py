def correct_sentence(text):
    sentences_list = text.split('. ')
    fixed_sentences = []
    for s in sentences_list:
        if s:
            s = s.strip()
            s = s[0].upper() + s[1:]
            if not s.endswith('.'):
                s += '.'
            fixed_sentences.append(s)
    result_text = ' '.join(fixed_sentences)
    return result_text
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')