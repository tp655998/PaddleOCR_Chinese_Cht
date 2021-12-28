import os 

def rename(id, image_folder_path, label_folder_path, old_img_path, old_label_path):
    new_img_path = image_folder_path + 'image_' + str(id).zfill(5) + '.jpg'
    os.rename(old_img_path, new_img_path)

    new_label_path = label_folder_path + 'image_' + str(id).zfill(5) + '.txt'
    os.rename(old_label_path, new_label_path)

def rename_(id, image_folder_path, label_folder_path, old_img_path, old_label_path, filename):
    suffix = '_' + filename.split('_', 1)[1]

    new_img_path = image_folder_path + str(id).zfill(5) + suffix
    os.rename(old_img_path, new_img_path)

    new_label_path = label_folder_path + str(id).zfill(5) + suffix.replace(".jpg",".txt")
    os.rename(old_label_path, new_label_path)


def read_file(image_folder_path, label_folder_path):
    # id = 4312     #train_augmentation
    id = 332       #train    
    counter = 0
    for filename in os.listdir(image_folder_path):
        old_img_path = os.path.join(image_folder_path, filename)
        old_label_path = os.path.join(label_folder_path, filename.replace(".jpg",".txt"))
        # rename(id, image_folder_path, label_folder_path, old_img_path, old_label_path)
        # id += 1

        rename_(id, image_folder_path, label_folder_path, old_img_path, old_label_path, filename)
        counter += 1
        if counter == 70:
            id += 1
            counter = 0
            
    print('rename finish')



image_folder_path = '../cultural_relics/sliced/images/'
label_folder_path = '../cultural_relics/sliced/labels/'
read_file(image_folder_path, label_folder_path)



