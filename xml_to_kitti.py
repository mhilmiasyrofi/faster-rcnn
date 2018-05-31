import os
import xml.etree.ElementTree as ET

filepath = ""
class_name = ""
x1 = ""
x2 = ""
y1 = ""
y2 = ""

if __name__ == '__main__':
    pathxml = "images/topi/anotasi"
    path = "images/topi"
    if os.path.isdir(pathxml) :
        for idx, f in enumerate(sorted(os.listdir(pathxml))) :
            tree = ET.parse(pathxml + '/' + f)
            root = tree.getroot()
            filename = root.find("filename").text
            filepath = path + '/' + filename + ".JPEG"
            # print(root.attrib)
            for child in root :
                if child.tag == "object" :
                    # class_name = child.find("name").text
                    class_name = "topi"
                    x1 = child.find("bndbox").find("xmin").text
                    y1 = child.find("bndbox").find("ymin").text
                    x2 = child.find("bndbox").find("xmax").text
                    y2 = child.find("bndbox").find("ymax").text
                    print(filepath + ',' +  x1  + ','  + y1 + ',' + x2 + ',' +  y2 + ','  + class_name)

