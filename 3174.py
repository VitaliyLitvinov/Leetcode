s = 'cd34qwe'
list_s: list = list(s)
for idx in range(len(list_s)):
    if idx == 0 and list_s[idx].isdigit():
        list_s[idx] = '0'
    elif list_s[idx].isdigit():
        list_s[idx] = '0'
        cnt = 1
        while list_s[idx - cnt].isdigit():
            cnt += 1
        list_s[idx - cnt] = '0'
while '0' in list_s:
    list_s.remove('0')
print(''.join(list_s))
