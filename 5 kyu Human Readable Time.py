def make_readable(seconds):
    tab = []
    if seconds >= 3600:
        tab.append(seconds // 3600)
        seconds -= (seconds // 3600) * 3600
        tab.append(seconds // 60)
        seconds -= (seconds // 60) * 60
        tab.append(seconds)
    elif seconds >= 60:
        tab.append(00)
        tab.append(seconds // 60)
        seconds -= (seconds // 60) * 60
        tab.append(seconds)
    else:
        tab.append('00')
        tab.append('00')
        tab.append(seconds)
    tab = [str(i) for i in tab]
    for i in range(len(tab)):
        if len(tab[i]) < 2:
            tab[i] = '0' + tab[i]
    return ':'.join([str(i) for i in tab])

print(make_readable(359999), "U")
print(make_readable(5), "I")
print(make_readable(67), "O")

'''
Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
'''