def format_duration(seconds):
    tab = []
    if seconds >= 3600:
        tab.append(seconds // 3600)
        seconds -= (seconds // 3600) * 3600
        tab.append(seconds // 60)
        seconds -= (seconds // 60) * 60
        tab.append(seconds)
    if seconds >= 60:
        tab.append(00)
        tab.append(seconds // 60)
        seconds -= (seconds // 60) * 60
        tab.append(seconds)
    if seconds < 60:
        tab.append(seconds)
    string = ""
    if len(tab) == 1:
        if tab[0] != 1:
            string += str(tab[0]) + ' seconds'
        else:
            string += str(tab[0]) + ' second'
    elif len(tab) == 4:
        for i in range(len(tab)):
            if i == 0 and tab[i] != 0:
                if tab[i] < 2:
                    string += str(tab[i]) + ' hour '
                else:
                    string += str(tab[i]) + ' hours '
            elif i == 1 and tab[i] != 0:
                if tab[i] < 2:
                    string += str(tab[i]) + ' minute '
                else:
                    string += str(tab[i]) + ' minutes '
            elif i == 2 and tab[i] != 0:
                if tab[i] < 2:
                    string += str(tab[i]) + ' second '
                else:
                    string += str(tab[i]) + ' seconds '
    return string

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