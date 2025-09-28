raw_inputs = ["10", " ", "25", "abc", "", "30", " ", "xyz", "5"]
filterdValues = list(map(lambda value:int(value), \
                         list(filter(lambda input:input.strip() and \
                                     input.isdigit(), raw_inputs))))
print(filterdValues)
