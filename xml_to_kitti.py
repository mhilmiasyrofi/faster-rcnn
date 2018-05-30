import os
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    path = "images/fashion_wanita/anotasi"
    if os.path.isdir(path) :
        for idx, f in enumerate(sorted(os.listdir(path))) :
            tree = ET.parse(path + '/' + f)
            root = tree.getroot()
            if idx == 0 :
                # print(root.attrib)
                
