import xml.etree.ElementTree as ET
from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer

path_extracted_dir=r"C:\Users\Abhi\Downloads\cranfield\cran.all"
index_path=r"C:\Users\Abhi\Desktop\Index"
import os.path
from whoosh.fields import *


schema = Schema(title=TEXT(stored=True), docno=ID(stored=True), text_data=TEXT(stored=True), author_data=TEXT(stored=True),bibilo_text=TEXT(stored=True))
Text_data = []
Document_NO = []
AUTHOR = []
BIBLIO = []
Title = []

if not os.path.exists(index_path):
    os.mkdir(index_path)

ix = create_in(index_path, schema)




files=os.listdir(path_extracted_dir)
for sub_file in files:
    file_path=os.path.join(path_extracted_dir, sub_file)
    tree = ET.ElementTree(file=file_path)
    root = tree.getroot()
        #for child in root:
         #   print(child='text')
        #fal=tree.getiterator()
    Child_Text=root.find('TEXT')
    Child_Title=root.find('TITLE')
    Child_Donum=root.find('DOCNO')
    Child_Biblo=root.find('BIBLIO')
    Child_Author=root.find('AUTHOR')


    for Text_child,Title_Child,Donum_child, Biblo_child, Author_child in zip(Child_Text.itertext(),Child_Title.itertext(),Child_Donum.itertext(),Child_Biblo.itertext(),Child_Author.itertext()):
            Text_data.append(Text_child.replace('\n',""))
            #print(Title_Child)
            Title.append(Title_Child.replace('\n', ""))
            Document_NO.append(Donum_child.replace('\n', ""))
            BIBLIO.append(Biblo_child.replace('\n', ""))
            AUTHOR.append(Author_child.replace('\n', ""))
            #writer.add_document(title=str(Title_Child.replace('\n', "")), docno=str(Donum_child.replace('\n', "")), text_data=str(Text_child.replace('\n',"")),
                   #author_data=str(Author_child.replace('\n', "")), bibilo_text=str(Biblo_child.replace('\n', "")))

    #writer.commit()

print(len(Text_data))
print(len(Document_NO))
print(len(AUTHOR))
print(len(BIBLIO))
print(len(Title))
#w=ix.writer()
writer=ix.writer()
for x in range(len(Text_data)):
    writer.add_document(title=str(Title[x]), docno=str(Document_NO[x]), text_data=str(Text_data[x]), author_data=str(AUTHOR[x]),bibilo_text=str(BIBLIO[x]))
writer.commit()
'''
for t,d,a,b,ti in zip(Text_data,Document_NO, AUTHOR, BIBLIO, Title):
    print("title",t)
    print("Docu no",d)
    print("author",a)
    print("title", ti)
    print("BIBLIO",b)


    #w.add_document(title=ti, docno=d, text_data=t, author_data=a,bibilo_text=b)
#w.commit()
'''