# Day_04_02_csv.py
# csv : comma seperated values
import csv

def readCsv_1(filename):
    f = open(filename, 'r', encoding='utf-8')

    result =[]
    for line in f:
        # print(line.strip())
        row = line.strip().split(',')
        # print(row)
        result.append(row)

    f.close()

    return result

# kma = readCsv_1('Data/kms.txt')
# for items in kma:
#     # print('{}, {}'.format(items[0], items[1]))
#     print(*items, sep='')


def readUS500(filename):
    f = open(filename, 'r', encoding='utf-8')

    for row in f:
        print(row)

    f.close()

#
# kma = readUS500('Data/us-500.csv')


def readCsv_2(filename):
    f = open(filename, 'r', encoding='utf-8')

    rows = []
    for row in csv.reader(f):
        # print(row)
        rows.append(row)

    f.close()
    return rows



# print(readCsv_2('Data/us-500.csv'))


def writeCsv(filename, rows):
    f = open(filename, 'w', encoding='utf-8', newline='')

    # for row in rows:
    #     # f.write(str(row))
    #     f.write(','.join(row))
    #     f.write('\n')

    writer = csv.writer(f, quoting=csv.QUOTE_ALL,
                        delimiter=',')
    # for row in rows:
    #     writer.writerow(row)

    writer.writerows(rows)

    f.close()

if __name__ == '__main__':
    filename = 'Data/kms.txt'
    # readCsv_1(filename)

    # filename = 'Data/us-500.csv'
    # filename = 'Data/kma.csv'
    kma = readCsv_2(filename)

    writeCsv('Data/write.csv', kma)









