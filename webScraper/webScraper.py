import json
from bs4 import BeautifulSoup
class WebScraper():
    def __init__(self):
        pass

    def setVars(self,filePath):
        self.formatterTags = read(filePath)

    def convert(self,file):
        html = "".join(line.strip() for line in file.split("\n"))
        soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")

        personInfo = {}

        # for each division like basic Info, education, experience taken from the input json file
        for section in self.formatterTags['div']:
            sectionKey = list(section.keys())[0]
            sectionValue = list(section.values())[0]
            sectionInfo = []

            # We take the first set of nests like basicInfo, experience and schools
            # For each of the multiple tags the division may contain
            for itemSectionValueClass in sectionValue['class']:
                # for each class we look at the tag associated
                for itemSectionValueTag in sectionValue['tag']:
                    try:

                        # Get all the info under the class itemSectionValueClass with tag itemSectionValueTag in the form of
                        #  a dictionary from the html file
                        sectionDataHTML = soup.find_all(itemSectionValueTag, class_=itemSectionValueClass)

                        # for each element in the section in HTML. In some cases, it might be the like the education Array
                        for elemDataHTML in sectionDataHTML:

                            elemInfo = {}
                            # from the input json file, the various elements of each division we want to have
                            for elements in sectionValue['elements']:
                                elementKey = list(elements.keys())[0]
                                elementValue = list(elements.values())[0]

                                # for the various tags the input html may contain for each element
                                for itemElementValueClass in elementValue['class']:

                                    for itemElementValueTag in elementValue['tag']:
                                        uniqueTag = elementValue['tag'][0]
                                        try:

                                            if "span" in elementValue:
                                                if "class" in elementValue["span"]:
                                                    # Handle this using if conditions
                                                    data = elemDataHTML.find_all(itemElementValueTag,
                                                                                 class_=itemElementValueClass)[0]
                                                    elemInfo[elementKey] = \
                                                    data.find_all('span', class_=elementValue["span"]["class"])[
                                                        0].getText()
                                                elif type(elementValue["span"]) == str:
                                                    data = \
                                                        elemDataHTML.find_all(itemElementValueTag,
                                                                              class_=itemElementValueClass)[0]
                                                    elemInfo[elementKey] = \
                                                        data.find_all(elementValue["span"])[0].getText()

                                            else:
                                                elemInfo[elementKey] = elemDataHTML.find_all(itemElementValueTag,
                                                                                             class_=itemElementValueClass)[
                                                    0].getText()
                                        except:
                                            pass
                            sectionInfo.append(elemInfo)

                    except:
                        pass
            personInfo[sectionKey] = sectionInfo

        return personInfo


def read(filePath):
    try:  # Read the input file and the validator file
        formatterTags = json.load(open(filePath))

        return formatterTags
    except FileNotFoundError as e:
        print(e.__str__())
        exit()