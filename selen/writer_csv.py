import csv

def writer_in_csv(data):
    #Функция для записи данных в файл csv
    with open('Test_Work/EvoSoft/selen/data.csv', mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        #Шапка таблицы
        writer.writerow(['Имя', 'Цена'])

        #Шапка таблицы
        for i in data:
            name = i[0]
            final_price = i[1]
            #Запись строки в файл
            writer.writerow([name, final_price])