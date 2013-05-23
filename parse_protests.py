#!/usr/bin/env python2.7

import json
from corenlp import StanfordCoreNLP
import codecs
from lxml.html import parse
from lxml.html.clean import clean_html
from StringIO import StringIO
import pdb

# Get the corpus-file open
corpusjson = 'protest.json'
jsonobject = json.load(codecs.open(corpusjson))


# Get and clean the text: 
texts = (clean_html(parse(StringIO(obj[4].replace("\n", " ")))).getroot().text_content() for obj in jsonobject)
print "Story text generator object created."


# Turn it into a string object, then an html object, then back into string...
#texts = clean_html(parse(StringIO(text))).getroot().text_content()

print "Setting up parser: "
# Set up the parser
stanford_parser = StanfordCoreNLP()

print "Creating parser generator object: "
# Parse dat. 
parsed_texts = (stanford_parser.parse(unicode(text)) for text in texts)

# Save the result to a file
# Not sure how enumerate() works with generators; ostensibly a wrapper which 
# retains laziness, but I don't wanna risk it and introduce more variables. 
i = 0       # So, it's gross. Whatever. 
for story in parsed_texts: 
    i += 1
    with codecs.open(str(i)+".json", 'w') as fh: 
        json.dump(json.loads(story), fh, indent=2)

