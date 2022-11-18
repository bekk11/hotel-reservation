a = "fakaferry da adsad asd"

print(a[0])

for i in range(len(a)):
    if a[i] == ' ':
        a.replace(a[i], 'ay')
        a.replace(a[0], '')


print(a)
