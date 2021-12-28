import json 
import os
from street import bbox, img_box
import sys

img_boxes = [] # 用來放所有圖片(包含旗下的bbox)


def read_rec(json_folder_path):
    '''
    /train_data/rec/train/
    '''

    counter_img = 0 # index of img

    for filename in os.listdir(json_folder_path):  #filename = ~~~~.txt

        img_boxes.append(img_box()) # 新增一個 img_box (一張圖片對應一個 img_box 物件)
        
        json_path = os.path.join(json_folder_path, filename)

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            bboxes = []  # 用來放屬於同一張圖片的bbox 
            counter_box = 0 # index of box  
            
            for item in data['shapes']:
                # if len(item['label']) > 1: #string length > 1
                bboxes.append(bbox()) #新增一個bbox
                filename = filename.replace('json', 'jpg')
                bboxes[counter_box].set_BBox(item['label'], item['points'], filename, counter_box) #設置bbox的屬性

                # print(item['label'], item['points'])
                img_boxes[counter_img].set_img_box(filename, bboxes) #設定img_box的屬性

                counter_box += 1

            if len(bboxes) == 0:
                print('empty box')
                img_boxes.pop(counter_img)
                counter_img -= 1

            
            # print('counter_box', counter_box)
            # print('boxes', len(bboxes))
            
        
        counter_img += 1 #下一張圖片
        f.close()
    print('counter img', counter_img)
    print('img_boxes', len(img_boxes))



def write_labels(base_dir, image_folder_path, save_folder_path):
    label_path = os.path.join(base_dir, 'train_list.txt')
    f = open(label_path, 'a', encoding="utf-8")
    for img in img_boxes:
        for box in img.boxes:
            img_path = os.path.join(save_folder_path, box.img_name)

            try:
                line = box.img_name + '\t' + str(box.label) + '\n'
                left, top, right, bottom = box.get_crop()
                crop_img(image_folder_path, img.filename, left, top, right, bottom, save_folder_path, box.img_name)
            except:
                print('Error', box.img_name)
                os.remove(img_path)

            
            if os.path.isfile(img_path):
                f.write(line) #crop成功才寫入
            else:
                print('skip', box.img_name)
    f.close()
        


# Improting Image class from PIL module 
from PIL import Image 

def crop_img(image_folder_path, name, left, top, right, bottom, save_folder_path, crop_name):
    
    img_path = os.path.join(image_folder_path, name)
    # Opens a image in RGB mode 
    img = Image.open(img_path) 
    
    # Cropped image of above dimension 
    # (It will not change orginal image) 

    img = img.crop((left, top, right, bottom)) 
    img.save(os.path.join(save_folder_path, crop_name))


    




def split_txt(base_dir):
    txt_list = base_dir + 'train_list.txt'
    train_path = base_dir + 'train.txt'
    valid_path = base_dir + 'valid.txt'

    with open(txt_list, 'r', encoding="utf-8") as f:
        data = f.readlines()
        print('len:', len(data))


    ratio = 0.99
    num = int(ratio*len(data))
    train = data[:num]
    valid = data[num:]

    print('valid', len(valid))
    print('train', len(train))

    with open(train_path, 'w+', encoding="utf-8") as f:
        f.writelines(train)

    with open(valid_path, 'w+', encoding="utf-8") as f:
        f.writelines(valid)






base_dir = '../train/' 
json_folder_path = base_dir + 'json/'
image_folder_path = base_dir + 'img/'
save_folder_path = base_dir + 'crop_img/'



# os.makedirs(save_folder_path, exist_ok=True)
# read_rec(json_folder_path)
# write_labels(base_dir, image_folder_path, save_folder_path)

split_txt(base_dir)
    

    

    
