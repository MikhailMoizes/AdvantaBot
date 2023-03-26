from bs4 import BeautifulSoup

# Парсинг данных из полученного xml файла в словарь
def getDataFromAdvantaXml(file, tags):
    result_dict = dict()
    with open(file, 'r', encoding='utf-8') as xmlData:
        xml_file = xmlData.read()
        soup = BeautifulSoup(xml_file, features='xml')
        for item in tags:
            for tag in soup.findAll(item):
                #print(f'{item}  {tag.text}')
                result_dict[item] = tag.text
    return result_dict



