"""
JSON file ===> dictionary
prompt key
compare value
if wrong - repeat
    else go further
count %of wrong
"""
import os
import json
import csv
import random
from speaker import Speaker

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
class Test:
    def __init__(self, dic):
        self.itms = list([(i, dic[i]) for i in dic])
        random.shuffle(self.itms)
        self.cur_idx = 0
        self.queque = [i for i in range(len(self.itms))]
        self.len = len(self.queque)
        self.hint = None
        self.speaker = Speaker()
    def get_quest(self, idx):
        return self.itms[idx][1]
    def get_ans(self, idx):
        return self.itms[idx][0]
    def sayAnswer(self):
        self.speaker.say(self.get_ans(self.cur_idx))
    def ask(self):
        if len(self.queque)>0:
            self.cur_idx = self.queque[0]
            del self.queque[0]
            return self.get_quest(self.cur_idx)
        else:
            return None
    def get_hint(self):
        if self.hint == None:
            idx = 0
        else:
            idx = None
        self.hint = hint(self.get_ans(self.cur_idx), self.hint, idx)
        return self.hint
    def is_right_ans(self, ans):
        if self.get_ans(self.cur_idx) == ans:
            self.hint  = False
            return True
        else:
            if len(self.queque)>0:
                if self.queque[-1]!=self.cur_idx:
                    self.queque.append(self.cur_idx)
            else:
                self.queque.append(self.cur_idx)
            return False

def import_quest(path = None):
    if path==None:
        path = os.path.dirname(os.path.realpath(__file__))
        path+="\\words.json"
    dic = dict([])
    try:
        print ("reading file : " + path)
        with open(path, mode="r") as f:
            txt = f.read()
            print ("OK\n")
    except Exception as err:
        print (err)
        return dic
    try:
        print ("decoding file : ")
        dic = json.loads(txt)
        print ("OK\n")
    except Exception as err:
        print (err)
        return dic
    return dic
def import_quest_csv(path = None):
    if path==None:
        path = os.path.dirname(os.path.realpath(__file__))
        path+="\\words.csv"
    dic = dict([])
    try:
        print ("reading file : " + path)
        with open(path, mode="r") as f:
            reader = csv.reader(f, quotechar = '"', delimiter = ",",
            quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in reader:
                dic[row[0]] = row[1]
    except:
        print(Exception)
    return dic
def runTest():
    test = Test(import_quest_csv())
    while True:
        que = test.ask()
        if que:
            is_right_ans = False
            while not is_right_ans:
                ans = input(que+"\n")
                is_right_ans = test.is_right_ans(ans)
                if not is_right_ans:
                    print(test.get_hint())
                else:
                    test.sayAnswer()
                if ans == "-exit":
                    return 0
        else:
            break
    return 0
runTest()
#print(import_quest())
#print(import_quest_csv())