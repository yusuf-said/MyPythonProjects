deneme =""
deneme=deneme.replace(" ","")
print(deneme)

counted_letter = "k"
count=0
for i in deneme:
    if i == counted_letter:
        count+=1
    else:
        continue

print(count)

