import freelex
import argparse
import sys
import os
import re
import xml.etree.ElementTree as ET
import shutil
import csv

def writeDictAsCSV(dictionary, filename):
    """saves a dictionary to a csv file"""
    #increment name no. if already exists
    csv_folder = os.path.join(os.getcwd(),"csv")
    if not os.path.exists(csv_folder):
        try:
            os.makedirs(csv_folder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    n=0
    while(os.path.isfile(os.path.join(csv_folder,filename + str(n) + ".csv"))==True):
        n = n+1
    f = open(os.path.join(csv_folder,filename + str(n) + ".csv"), 'w', encoding="utf-8", newline='')
    w = csv.writer(f)
    for key,value in dictionary.items():
        w.writerow([key, value[0], value[1]])
    f.close()
    print("Created and wrote to: "+ filename + str(n) + ".csv" + ".csv")

def appendDictAsCSV(dictionary, filename):
    """saves a dictionary to a csv file"""
    #increment name no. if already exists
    csv_folder = os.path.join(os.getcwd(),"csv")
    if not os.path.exists(csv_folder):
        try:
            os.makedirs(os.path.dirname(csv_folder))
        except IOError:
            pass
    f = open(os.path.join(csv_folder,filename+".csv"), 'w', encoding="utf-8", newline='')
    w = csv.writer(f)
    for key,value in dictionary.items():
        w.writerow([key, value[0], value[1]])
    f.close()
    print("Appended to: "+ filename + ".csv")

def singlish_csv(csv_filename, root):
    english_nzsl_dictionary = {}
    for entry in root.iter("entry"):
        print(entry.find("headword").text)
        id = entry.find("headwordid").text
        for videonum in range (1, 10):
            videoexample = "videoexample" + str(videonum)
            videotranslateexample = "videoexample" + str(videonum) + "translation"
            singlish_sentence = ""
            if(entry.find(videoexample)!=None and entry.find(videotranslateexample)!=None):
                for word in entry.find(videoexample):
                    singlish_sentence += word.text
                    singlish_sentence += " "
                singlish_sentence += ". "
                english_sentence = entry.find(videotranslateexample).text
                english_nzsl_dictionary[id] = [english_sentence, singlish_sentence]
    writeDictAsCSV(english_nzsl_dictionary, csv_filename)


def main(argv):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--fetchXML', action='store_true' ,help='whether to fetch xml from database')
    parser.add_argument('--fetchPics', action='store_true' ,help='whether to fetch pics from database')
    parser.add_argument('--writeDB', action='store_true' ,help='whether to write pics to a database')
    parser.add_argument('--singlishCSV', action='store_true' ,help='whether to extract english singlish data and write to csv')
    parser.add_argument('--filename', help='filename for xml dump', default='dnzsl-xmldump.xml')
    args = parser.parse_args()

    filename = args.filename

    if(args.fetchXML):
        print("Step 1: Fetching the latest signs from Freelex")
        freelex.fetch_database(filename)

    with open(filename, encoding="utf8") as f:
        data = f.read()
    data = data.replace("\x05", "")
    data = data.replace("<->", "")
    # Replace ampersands, which are XML control characters, with
    # the appropriate XML escape sequence
    data = re.sub(r"&(?=[^#])", "&#038;", data)
    parser = ET.XMLParser(encoding="UTF-8")
    root = ET.XML(data, parser=parser)

    if(args.fetchPics):
        print("Step 2: Fetching images from freelex")
        freelex.fetch_assets(root)

        print("Step 3: Rename all images to meet Android requirements")
        freelex.rename_assets(root)

    if(args.writeDB):
        print("Step 4: Write out nzsl.dat for Android")
        freelex.write_datfile(root)

        print("Step 5: Write out sqlite nzsl.db for iOS")
        freelex.write_sqlitefile()


    if(args.singlishCSV):
        print("Step 6: Singlish<->English")
        singlish_csv("english_nzsl_dictionary", root)

if __name__ == "__main__":
    main(sys.argv)
