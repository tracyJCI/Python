from lxml import etree
infile = open('hamlet-tei.xml','rb')
xml = infile.read()
infile.close()

tree = etree.fromstring(xml)

ns={'tei':'http://www.tei-c.org/ns/1.0'}

#print(tree.xpath('//tei:sp[@who="#F-ham-hor"]/tei:l/text()',namespaces=ns))
#print(tree.xpath('//tei:person[@xml:id="F-ham-ham"]/tei:persName[@type="standard"]/text()',namespaces=ns))
#name= tree.xpath('//tei:person[@xml:id="F-ham-ham"]/tei:persName[@type="standard"]/text()',namespaces=ns)
#print(" ".join(name[0].split()))
names= tree.xpath('//tei:person/tei:persName[@type="standard"]/text()',namespaces=ns)
print(len(names))

for name in names:
    print(name)
