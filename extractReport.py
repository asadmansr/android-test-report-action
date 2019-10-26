import sys
import os
import fnmatch
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
    print("\n")
    return exit_code

def find_test_reports():
    matches = []
    for root, dirnames, filenames in os.walk('.'):
        for filename in fnmatch.filter(filenames, 'TEST-*.xml'):
            matches.append(os.path.join(root, filename))
    return matches

def main():
    exit_code = 0
    reports = find_test_reports()
    for i in reports:
        print(i + "\n")
        result = parse_xml(i)
        print(result)
        if (result is not 0):
            print("non-zero")
            exit_code = 1
    sys.exit(1)

if __name__ == "__main__":
    main()