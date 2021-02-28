# BeautifulSoup module helps in web scrapping.
# requests module helps us to download a web page
from bs4 import BeautifulSoup
import request

#considering HTML
#%%html
#<!DOCTYPE html>
#<html>
#<head>
#<title>Page Title</title>
#</head>
#<body>
#<h3><b id='boldest'>Lebron James</b></h3>
#<p> Salary: $ 92,000,000 </p>
#<h3> Stephen Curry</h3>
#<p> Salary: $85,000, 000 </p>
#<h3> Kevin Durant </h3>
#<p> Salary: $73,200, 000</p>
#</body>
#</html>

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

print(soup.prettify())

#Tags
tag_object=soup.title
print("tag object:",tag_object)

print("tag object type:",type(tag_object))

tag_object=soup.h3
tag_object

#Childern Parents and Silblings
tag_child =tag_object.b
tag_child

#access the parent
parent_tag=tag_child.parent
parent_tag

#identical to 
tag_object

#tag_object parent is the body element.
tag_object.parent

#tag_object sibling is the paragraph element
sibling_1=tag_object.next_sibling
sibling_1
#sibling_2 is the header element which is also a sibling of both sibling_1 and tag_object
sibling_2=sibling_1.next_sibling
sibling_2
# Next sibling
sibling_2.next_sibling

#HTML Attributes

tag_child['id']

tag_child.attrs

tag_child.get('id')

#Navigable String
tag_string=tag_child.string
tag_string

#Verfiying the type
type(tag_string)

#Unicode
unicode_string = str(tag_string)
unicode_string






