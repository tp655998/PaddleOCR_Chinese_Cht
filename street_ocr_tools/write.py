import csv
import os
boxes =  [[[62.0,  571.0], [1218.0,  561.0], [1221.0, 905.0], [65.0, 916.0]]]

txts = ['國真熬早']

image_file = 'img_06'

def write_csv(image_file, boxes, txts, csv_path):
    '''
    answer
    '''
    rows = []
    # 開啟 CSV 檔案

    # 以迴圈輸出每一列
    for index in range(len(txts)):
        row = []
        row.append(image_file)

        for pos in boxes[index]:
            for cor in pos:
                row.append(cor)

        row.append(txts[index])
        rows.append(row)

    with open(csv_path, 'a', newline='', encoding='utf-8') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        
        # 寫入一列資料
        for item in rows:
            writer.writerow(item)
            print(item)
            
    print('finish')

csv_path = '../answer.csv'
write_csv(image_file, boxes, txts, csv_path)

