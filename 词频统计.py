#词频统计.py
a=input()
def words_list():
    chardigit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '
    all_lines = ''
    for line in a:
        one_line = ''
        for ch in line:
            if ch in chardigit:
                one_line = one_line + ch
        all_lines = all_lines + one_line

    return all_lines.split()
def total_num(s):
    return len(s)
def word_dic(t):
    fre_dic = dict()
    for i in range(len(t)):
        fre_dic[t[i]] = fre_dic.get(t[i], 0) + 1
    return fre_dic
def word_fre(w):
    for key in w:
        w[key] = w[key]
        return w
def word_sort(v):
    sort_dic = sorted(v.items(), key=lambda e: e[1])
    return sort_dic
total = total_num(words_list())
print(word_sort(word_fre(word_dic(words_list())))[:])

