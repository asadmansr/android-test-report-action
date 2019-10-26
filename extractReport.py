import sys
import xml.etree.ElementTree as ET

SPACE_THRESHOLD = 16

def parse_xml(xml_file):
    exit_code = 0
    tree = ET.parse(xml_file)
    root = tree.getroot()
    attributes = root.attrib
    for key,value in attributes.items():
        key_len = len(key)
        empty_space = SPACE_THRESHOLD - key_len
        print(key.capitalize() + " "*empty_space + value)
        if key == 'failures' and int(value) > 0:
            exit_code = 1
    print("")
    return exit_code

def output_result(code):
    file = open("android_test_report_action.txt", "w") 
    file.write(code) 
    file.close() 

def main():
    path = sys.argv[1]
    print(path + "\n")
    exit_code = parse_xml(path)
    output_result(str(exit_code))

if __name__ == "__main__":
    main()