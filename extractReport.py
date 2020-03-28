import sys
import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    hasSeenFailure = False
    message = ""
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
    
    for elem in root:
        if (elem.tag == "testcase"):
            elem_attrib = elem.attrib
            try:
                failure_message = (elem.find('failure').attrib)['message']
                hasSeenFailure = True
                message += "\n"
                message += printFormatter("testcase", elem_attrib['name']) + "\n"
                message += printFormatter("message", failure_message) + "\n"
                message += printFormatter("time", elem_attrib['time']) + "\n" 
            except AttributeError:
                pass
    
    if (hasSeenFailure):
        print("")
        print("Failed Test Cases:")
        print("------------------")
        print(message)
        print("")

def printFormatter(key, msg):
    keyLen = len(key)
    space = 12-keyLen
    return(key.capitalize() + " "*space + msg)

def main():
    path = sys.argv[1]
    print(path + "\n")
    parseXML(path)

if __name__ == "__main__":
    main()