#searcher
from whoosh.index import open_dir
from whoosh.query import *
index_path=r"C:\Users\Abhi\Desktop\Index"
ix = open_dir(index_path)
#from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser



qp = MultifieldParser(["title","docno","text_data","author_data","bibilo_text"],ix.schema)
q = qp.parse('what')
with ix.searcher() as s: #construct the query object directly#
    #print(list(s.lexicon("docno")))
    results = s.search(q)
    print(results)
    for hit in results:
        print(hit.rank)
        print(hit.values())
        print(hit.score)
        print(hit.docnum)


from whoosh.query import Every
#r_show = ix.searcher().search('title')
#print(r_show)