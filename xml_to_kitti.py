import os
import xml.etree.ElementTree as ET

filepath = ""
class_name = ""
x1 = ""
x2 = ""
y1 = ""
y2 = ""

if __name__ == '__main__':
    path = "images/fashion_wanita/anotasi"
    if os.path.isdir(path) :
        for idx, f in enumerate(sorted(os.listdir(path))) :
            tree = ET.parse(path + '/' + f)
            root = tree.getroot()
            filename = root.find("filename").text
            filepath = path + '/' + filename
            if idx == 0 :
                # print(root.attrib)
                for child in root :
                    if child.tag == "object" :
                        class_name = child.find("name").text
                        x1 = child.find("bndbox").find("xmin").text
                        y1 = child.find("bndbox").find("ymin").text
                        x2 = child.find("bndbox").find("xmax").text
                        y2 = child.find("bndbox").find("ymax").text
                        print(filepath + ',' +  x1  + ','  + y1 + ',' + x2 + ',' +  y2 + ','  + class_name)

