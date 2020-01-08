
f = open('Test.html','w+')

Title = input ('Titel > ')

Introtext = input('Text > ')



Head = ("""
<html>
    <head> 
        <title>""" + (Title) + """ </title> 
    </head>
    <body>
        <h1>""" + (Title) + """ </h1>
        <p>""" + (Introtext) + """</p>
    </body>
</html>""") 

f.write(Head)
f.close()

x = open('Test.css','w+')

CSS = r'h1{color:whitesmoke; text-shadow: 5px 5px gray;}'

x.write(CSS)
