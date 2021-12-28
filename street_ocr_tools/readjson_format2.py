import json 
import os
from street import bbox, img_box

img_boxes = [] # 用來放所有圖片(包含旗下的bbox)

def read_file(image_folder_path, json_folder_path):
    counter_img = 0 # index of img

    with open(json_folder_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        for filename in os.listdir(image_folder_path): 
            file_id = filename.split('.')[0]

            
            bboxes = []  # 用來放屬於同一張圖片的bbox 
            counter_box = 0 # index of box  

            for item in data[file_id]:
                
                if len(item['transcription']) > 1 and len(item['points']) == 4:
                    bboxes.append(bbox()) #新增一個bbox
                    bboxes[counter_box].set_BBox(item['transcription'], item['points']) #設置bbox的屬性
                    print(item['transcription'], item['points'])

                    counter_box += 1

            if len(bboxes) != 0:
                img_boxes.append(img_box()) # 新增一個 img_box (一張圖片對應一個 img_box 物件)
                img_boxes[counter_img].set_img_box(filename, bboxes) #設定img_box的屬性
                # print('counter_box', counter_box)
                # print('boxes', len(bboxes))
                counter_img += 1 #下一張圖片

        f.close()
    print('counter img', counter_img)
    print('img_boxes', len(img_boxes))


def write_labels(save_folder_path):
    lines = []
    for img in img_boxes:
        label_path = os.path.join(save_folder_path, img.get_txt_name())
        f = open(label_path, 'w+', encoding="utf-8")
        for box in img.boxes:
            line = box.get_full_label() + '\n'
            lines.append(line)
            print(line)
        f.writelines(lines)
        lines = []
        f.close()
        


base_dir = '../ch/' 
img_folder_path = base_dir + 'img/'
json_folder_path = base_dir + 'train_full_labels.json'
save_folder_path = base_dir + 'labels'



os.makedirs(save_folder_path, exist_ok=True)
read_file(img_folder_path, json_folder_path)
write_labels(save_folder_path)
    
# img_boxes = read_file(json_path)
# write_labels(save_path, img_boxes)
# display_dataset_info(json_path)
# create_class_txt(save_path, 6)



    

    
