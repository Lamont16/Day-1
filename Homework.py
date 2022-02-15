# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
cubelist = []
start = 1
end = 10
for count in range(start, end+1):
    cubes.append (count**3)
print(cubes)


x = 2
y = 100

for num in range(x, y + 1):
    if num > 1:
        for z in range(2, num):
            if(num % z) == 0:
                break
        else:
            print(num)


age = input('How old are you')
user_age = int(age)
if user_age <= 18:
    print('kids')
if user_age <= 65:
    print('adults')
else:
    print('seniors')