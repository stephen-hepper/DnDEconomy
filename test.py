import os
#path = 'C:/Users/shepp/PycharmProjects/DnDEconomy/markets/gottstand.csv'
path = 'markets'


#out = os.path.isfile(path)
out = os.path.exists(path)
print(out)

for file in os.listdir(path):
    with open(os.path.join(path, file)) as f:
        header = f.readline()
        for line in f.readlines():
            item = (line.strip('\n').split(","))
            print(item)



