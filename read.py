data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))  # 因爲for loop是把清單中的東西一個一個拿出來，所以每拿一個他就會print一次
print(len(data))

print(data[0])
print('----------------------')
print(data[1])