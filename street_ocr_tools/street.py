class Relics:
    # 建構式
    def __init__(self, filename=None, cat=None, x=None, y=None, w=None, h=None, conf=None):
        self.__filename = filename
        self.__cat = cat
        self.__x = x  
        self.__y = y  
        self.__w = w  
        self.__h = h  
        self.__conf = conf  
        
    def set_info(self, filename, label, width, height):
        self.__filename = filename 
        
        label_info = label.split(' ')   
        
        self.__cat = label_info[0]
        
        self.__w = int(eval(label_info[3]) * width)   
        self.__h = int(eval(label_info[4]) * height)
        
        self.__x = int(eval(label_info[1]) * width - self.__w / 2) 
        self.__y = int(eval(label_info[2]) * height - self.__h / 2)
  
        self.__conf = label_info[5]  

    def get_info(self):
        filename = self.__filename
        cat = self.__cat
        x = self.__x
        y = self.__y
        w = self.__w
        h = self.__h
        conf = self.__conf
        line = [filename, cat, x, y, w, h, conf] 
        return line

    def get_conf(self, label):
        conf = label.split(' ')[5]  
        return eval(conf)
    
class data_obj:
    def __init__(self, file_id=None, image=None, label=None):
        self.__file_id = file_id
        self.__image = image
        self.__label = label
        
    def set_data(self, file_id, image, label):
        self.__file_id = file_id
        self.__image = image
        self.__label = label

class img_box:
    # 建構式
    def __init__(self, filename=None, boxes=None):
        self.filename = filename  
        self.boxes = boxes 
        
    # 方法(Method)
    def set_img_box(self, filename, boxes):
        self.filename = filename  
        self.boxes = boxes 

    def get_txt_name(self):
        return self.filename.split('.')[0]+'.txt'

    def get_img_name(self):
        return self.filename.split('.')[0]+'.jpg'

class bbox:
    # 建構式
    def __init__(self, label=None, p1x=None, p1y=None, p2x=None, p2y=None, p3x=None, p3y=None, p4x=None, p4y=None, img_name=None):
        '''
        label: 文字
        p1 ~ p4: 4個點座標
        img_name: crop_img_name
        '''
        self.label = label  

        self.p1x = p1x  
        self.p1y = p1y  

        self.p2x = p2x  
        self.p2y = p2y  

        self.p3x = p3x  
        self.p3y = p3y  

        self.p4x = p4x  
        self.p4y = p4y  

        img_name = img_name # crop img name

    def get_crop(self):
        '''
        output: left, top, right, bottom
        '''
        left = self.p1x if self.p1x < self.p4x else self.p4x    # left:     p1x vs. p4x
        top = self.p1y if self.p1y < self.p2y else self.p2y     # top:      p1y vs. p2y
        right = self.p2x if self.p2x > self.p3x else self.p3x   # right:    p2x vs. p3x
        bottom = self.p3y if self.p3y > self.p4y else self.p4y  # bottom:   p3y vs. p4y
        return left, top, right, bottom

        
    # 方法(Method)
    def set_BBox(self, label, points, filename=None, counter=None):
        self.label = label  

        p1, p2, p3, p4 = points

        self.p1x = p1[0]  
        self.p1y = p1[1] 

        self.p2x = p2[0]
        self.p2y = p2[1] 

        self.p3x = p3[0]  
        self.p3y = p3[1] 

        self.p4x = p4[0] 
        self.p4y = p4[1] 

        if filename != None:
            self.img_name = filename.split('.')[0] + '_' + str(counter).zfill(3) + '.jpg'

        
    def normalize(self, x, y, w, h, width, height): # 轉成 yolo format:  絕對位置 左上角(x, y) ==> 相對位置 中心點(x, y)
        x = (x+(w/2)) / width
        y = (y+(h/2)) / height
        w = w / width
        h = h / height
        return x, y, w, h
        
    def get_full_label(self): 
        label = self.label 

        p1x = str(self.p1x)  
        p1y = str(self.p1y)  

        p2x = str(self.p2x)  
        p2y = str(self.p2y)  

        p3x = str(self.p3x)  
        p3y = str(self.p3y)  

        p4x = str(self.p4x)  
        p4y = str(self.p4y)  


        return p1x + ',' + p1y + ',' + p2x + ',' + p2y + ',' + p3x + ',' + p3y + ',' + p4x + ',' + p4y + ',' + label
    
        
    
