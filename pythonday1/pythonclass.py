numbers = ("8778671966", "8778671955", "877786719444", "87786719999", "87786719888", "8778671977", "8778671911", "8778671922", "8778671933", "8778671910", "8778671912", "8778671966", "8778671955", "8778671644")
a =  len(numbers)
print(a)
valid_items = []
invalid_items = []
for num in numbers:
    num1 = len(num)
    print(num1,"this num1")
    if num1 <= 10 and num not in valid_items:
        print(num1)
        valid_items.append(num)
    else:
        invalid_items.append(num)
print("valid_items", valid_items, len(valid_items))
print("invalid_items", invalid_items, len(invalid_items))