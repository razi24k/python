sohp2 = 0
p2soh = 0
for i in range(1,101):
    x = i**2
    sohp2 += i
    p2soh += x
sohp2 = sohp2**2
print(abs(sohp2-p2soh))