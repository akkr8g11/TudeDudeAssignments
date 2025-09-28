def countdown(start_num):
    while start_num >= 1:
        yield start_num
        start_num -= 1

generator_num = countdown(5)
"""
for num in generator_num:
    print(num)
"""
print 
print(next(generator_num))