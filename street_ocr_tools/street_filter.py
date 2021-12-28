import os
import csv


def getFileNameWithoutExtension(path):
    '''
    (路徑)
    ------
    取得不帶有副檔名的檔案名字
    '''
    return path.split('\\').pop().split('/').pop().rsplit('.', 1)[0]


def not_small(row, size):
    p1x, p1y = int(row[1]), int(row[2])
    p2x, p2y = int(row[3]), int(row[4])
    p3x, p3y = int(row[5]), int(row[6])
    p4x, p4y = int(row[7]), int(row[8])

    left = p1x if p1x < p4x else p4x    # left:     p1x vs. p4x
    top = p1y if p1y < p2y else p2y     # top:      p1y vs. p2y
    right = p2x if p2x > p3x else p3x   # right:    p2x vs. p3x
    bottom = p3y if p3y > p4y else p4y  # bottom:   p3y vs. p4y

    width = right - left
    height = bottom - top
    # print(left, top, right, bottom)

    if width >= size and height >= size:
        return True
    else:
        return False




def check_seq(row):
    p1x, p1y = int(row[1]), int(row[2])
    p2x, p2y = int(row[3]), int(row[4])
    p3x, p3y = int(row[5]), int(row[6])
    p4x, p4y = int(row[7]), int(row[8])

    if p1x > p2x:
        return False
    elif p2y > p3y:
        return False
    elif p4x > p3x:
        return False
    elif p1y > p4y:
        return False
    else:
        return True
    

def csv_filter(csv_path, save_path, fname, size):

    csv_filename = fname + '_' + str(size)+'.csv'
    new_csv = []

    with open(csv_path, newline='', encoding="utf-8") as csvfile:

        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)

        seq_error = 0
        size_error = 0

        for row in rows:
            if check_seq(row) == False:
                # print('Seq False')
                seq_error += 1
            elif not_small(row, size) == False:
                # print('Size False')
                size_error += 1
            else:
                new_csv.append(row)

        Seq, Size = seq_error, size_error
        print('Seq, Size', Seq, Size)

    with open(save_path + csv_filename, 'w+', newline='', encoding='utf-8') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        
        # 寫入一列資料
        for item in new_csv:
            writer.writerow(item)


csv_path = '../output/private/test.csv'
save_path = '../output/private/'


csv_filter(csv_path, save_path, 'test', 10)






            
            
