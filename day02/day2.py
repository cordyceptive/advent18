def countLetterFreqs(word):
    freqs = {}
    for letter in word:
        if (letter in freqs):
            freqs[letter] += 1
        else:
            freqs[letter] = 1
    return freqs


def hasExactlyN(n, letter_freqs):
    for v in letter_freqs.values():
        if (v == n):
            return True


def offByOne(a, b):
    difference = False
    for i, ltr_a in enumerate(a):
        if (ltr_a != b[i]):
            if (difference):
                return False
            else:
                difference = True
    return True if difference else False


def common_letters(a, b):
    ltrs = []
    for i in range(len(a)):
        if (a[i] == b[i]):
            ltrs.append(a[i])
    return ''.join(ltrs)


with open('d2input.txt') as input:
    '''containsTwo = 0
    containsThree = 0
    for line in input:
        letter_freqs = countLetterFreqs(line)
        if (hasExactlyN(2, letter_freqs)):
            containsTwo += 1
        if (hasExactlyN(3, letter_freqs)):
            containsThree += 1
    print(f'checksum: {containsTwo * containsThree}')'''
    prev_words = []
    for line in input:
        for prev in prev_words:
            if (offByOne(prev, line)):
                print(f'common letters: {common_letters(prev, line)}')
                break
        prev_words.append(line)
