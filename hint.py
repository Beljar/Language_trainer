import random
def hint(str_, prev_hint=None, idx=None):
    hint = []
    #str_without_spaces = str_.replace(" ", "")
    #prev_hint_without_spaces = prev_hint.replace(" ", "")
    if idx != None:
        if prev_hint:
            prev_hint[idx] = str_[idx]
            return prev_hint
        else:
            hint = list(map(lambda x: x if x == " " else "_", str_))
            hint[idx] = str_[idx]
            return "".join(hint)
    else:
        if prev_hint:
            hidden_chars_num = prev_hint.count("_")
            if hidden_chars_num > 1:
                hint_idx = random.randrange(0, hidden_chars_num)
            else:
                return str_
        else:
            str_without_spaces = str_.replace(" ", "")
            hint_idx = random.randrange(0, len(str_without_spaces))
            prev_hint = list(map(lambda x: x if x == " " else "_", str_))
        cur_idx = -1
        for i in range(len(str_)):
            if str_[i] != " ":
                if prev_hint[i] == "_":
                    cur_idx += 1
                    if hint_idx == cur_idx:
                        hint.append(str_[i])
                    else:
                        hint.append("_")
                    
                else:
                    hint.append(str_[i])
                
            else:
                hint.append(" ")
        return "".join(hint)

h = hint("test test", idx = 0)
print (h)
h = hint("test test", h)
print (h)
h = hint("test test", h)
print (h)
h = hint("test test", h)
print (h)
h = hint("test test", h)
print (h)
h = hint("test test", h)
print (h)