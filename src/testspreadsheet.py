from xml.dom.minidom import getDOMImplementation

import csv



# this program can be used for newpapers and posters too.
#csvFile = 'myData.csv'
#csvData = csv.reader(open(csvFile))
def main():
    with open(r'\\svm-netapp-dlib.in.library.ucla.edu\DLIngest\armenia_testbatch1\test batch 1 (002-050) - test batch 1.csv',
              encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


if __name__ == '__main__': main()