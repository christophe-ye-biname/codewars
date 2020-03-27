def format_duration(seconds):
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
    str = ""
    for i in range(len(tab)):
        if tab[i] != '00' or tab[i] != 0 and i == 0 and tab[i] > 1:
            str += tab[i] + ''
    return tab

print(format_duration(3662))
print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
'''
Test.assertEquals(formatDuration(1), "1 second");
Test.assertEquals(formatDuration(62), "1 minute and 2 seconds");
Test.assertEquals(formatDuration(120), "2 minutes");
Test.assertEquals(formatDuration(3600), "1 hour");
Test.assertEquals(formatDuration(3662), "1 hour, 1 minute and 2 seconds");
'''