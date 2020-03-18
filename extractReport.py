import sys
import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    attributes = root.attrib
    for k,v in attributes.items():
        cs = len(k)
        sp = 16-cs
        print(k.capitalize() + " "*sp + v)
        if ((k == "failures") and (int(v) > 0)) or ((k == "errors") and (int(v) > 0)):
            f = open("extractReport_status.log", "w")
            f.write("error")
            f.close()
    print("")

def main():
    path = sys.argv[1]
    print(path + "\n")
    parseXML(path)

if __name__ == "__main__":
    main()