from bs4 import BeautifulSoup
from bs4 import re

doc=open("filepath\filename.html", 'rb')

soup = BeautifulSoup(doc, "html.parser")
doc.close()

#removes attributes other than class from table tag
for table in soup.find_all('table'):
    for attribute in ["style", "valign", "width", "border", "cellpadding",
                     "cellspacing"]:
        del table[attribute]
	
#removes attributes other than class from th	
for th in soup.find_all('th'):
    for attribute in ["style", "valign", "width"]:
        del th[attribute]
		
#remove p tags from within a th tag
for th in soup.find_all('th'):
    for p in th.find_all("p"):
        p.replaceWithChildren()
		
#removes span tags from within a th tag
for th in soup.find_all('th'):
    for span in th.find_all("span"):
        span.replaceWithChildren()
		
#removes attributes other than class from td		
for td in soup.find_all('td'):
    for attribute in ["style", "valign", "width"]:
        del td[attribute]
		
#removes span tags from within td tags
for td in soup.find_all('td'):
    for span in td.find_all("span"):
        span.replaceWithChildren()
		
#output html
out=soup.prettify('utf-8')
print(out)
docout=open(r"filepath\revised_filename.html",'wb')
docout.write(out)
docout.close()