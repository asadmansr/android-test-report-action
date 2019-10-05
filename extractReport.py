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
    print("")

def main():
    path = sys.argv[1]
    print(path + "\n")
    parseXML(path)

if __name__ == "__main__":
    main()