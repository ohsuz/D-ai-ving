import re

def solution(new_id):
    regex = re.compile('^(?!\.)((?!\.\.)[a-z0-9._\-]){3,15}(?<!\.)$') 
    notAllowed = re.compile('[^a-z0-9._-]')
    if not regex.match(new_id):
        new_id = new_id.lower()
        for char in set(notAllowed.findall(new_id)):
            new_id = new_id.replace(char,'')
        while '..' in new_id:
            new_id = new_id.replace('..','.')        
        new_id = new_id.strip('.')
        if not new_id:
            new_id = 'a'
        if len(new_id) > 15:
            new_id = new_id[:15]
            new_id = new_id.rstrip('.')
        while(len(new_id) <= 2):
            new_id = new_id + new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution(" "))