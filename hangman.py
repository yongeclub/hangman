def guess_next_letter(pattern, used_letters=[], word_list=[]):
    result = None
    letters = {}
    for word in word_list:
        for l in word:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1
    letters = sorted(letters.items(), key=lambda x:x[1], reverse=True)
    
    for x in letters:
        if x[0] not in used_letters:
            result = x[0]
            break
    return result

def test_function_should_return_something():
    pattern = '__i_e'
    used_letters = list('abcde')
    word_list = ['Get', 'like', 'in', 'plus', 'Sign', 'or', 'Online', 'free', 'Hotmail', 'your', 'apps', 'Outlook', 'Office', 'calendar', 'Word', 'PowerPoint', 'Excel', 'to', 'email', 'access', 'account', 'Live', 'and']
    print(guess_next_letter(pattern, used_letters, word_list))
    assert guess_next_letter(pattern, used_letters, word_list) is not None


test_function_should_return_something()