import csv

def writer_in_csv(data):
    with open('Test_Work/EvoSoft/data.csv', mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Имя', 'Цена'])

        for i in data:
            name = i[0]
            final_price = i[1]
            writer.writerow([name, final_price])