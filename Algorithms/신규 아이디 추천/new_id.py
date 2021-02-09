import re
def solution(new_id):
    answer = ""
    # phase1
    new_id = new_id.lower()
    # phase2
    new_id2 = ""
    for c in new_id:
        if c.isdigit() or c.isalpha() or c in ["-", "_", "."]:
            new_id2 += c
    new_id = new_id2
    # phase3
    new_id = re.sub("(\.\.+)", ".", new_id)
    # phase4
    if new_id:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    # phase5
    if not new_id:
        new_id = "a"
    # phase6
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    # phase4 again
    if new_id:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    # phase7
    if len(new_id) <= 2:
        last = new_id[-1]
        while len(new_id) < 3:
            new_id += last
    return new_id