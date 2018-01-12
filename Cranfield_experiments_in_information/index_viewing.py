from whoosh.index import open_dir

index_path=r"C:\Users\Abhi\Desktop\Index"
ix = open_dir(index_path)
result=ix.searcher().documents()
count=0

for hit in result:
 print(hit['author_data'])
 count=count+1
#for hit in result:
    #print(len(hit))
print(count)