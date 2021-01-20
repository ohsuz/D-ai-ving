#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


def normalize(input_string):
    normalized_string = " ".join(input_string.split()).lower()
    return normalized_string


def no_vowels(input_string):
    newString = ''
    for s in input_string:
        if s not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            newString += s
    no_vowel_string = newString
    return no_vowel_string
