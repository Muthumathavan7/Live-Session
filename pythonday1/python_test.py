numbers = ["8778671966", "8778671955", "877786719444", "87786719999", "87786719888", "8778671977", "8778671911", "8778671922", "8778671933", "8778671910", "8778671912", "8778671966", "8778671955", "8778671644"]
numlen = len(numbers)
print(numlen)
valid_items = []
for num in numbers:
    # print(num)
    numlen1 = len(num)
    if numlen1 == 10:
        valid_items.append(num)
print("valid_items",valid_items, len(valid_items))
