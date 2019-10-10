from bs4 import BeautifulSoup
from bs4 import re

doc=open("filepath\filename.html", 'rb')

soup = BeautifulSoup(doc, "html.parser")
doc.close()

#removes style attributes of spans within spans
for span in soup.find_all('span'):
    for s in span.findAll('span'):
        for attribute in ["style"]:
            del s[attribute]
		
#output html
out=soup.prettify('utf-8')
print(out)
docout=open(r"filepath\revised_filename.html",'wb')
docout.write(out)
docout.close()