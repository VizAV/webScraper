from webScraper.webScraper import WebScraper
import os
from config import path,scrapFile
def main():
    scraper=WebScraper()

    scraper.setVars(os.curdir+scrapFile)

    for files in os.listdir(path):
        fileName = path+'/'+files

        inpFile = open(fileName, 'r').read()


        outputFile = scraper.convert(inpFile)
        outputFile['personID'] = files[:-5]
        print(outputFile)
if __name__ =='__main__':
    main()