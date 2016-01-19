# -*- coding: utf-8 -*-
import codecs
import random

filelist = ['quotes_fr.txt', 'quotes_en.txt', 'quotes_de.txt']
filename = 'quotes_all.txt'
quotes = []
authors = []

for file in filelist:
    content = codecs.open(file, 'r', 'utf-8').readlines()
    for linenum in range(len(content) / 3):
        quoteline = content[linenum * 3]
        quoteline = quoteline[:-1]
        quotes.append(quoteline.strip(u"“”"))
        authors.append(content[linenum * 3 + 1].strip())
        #import pdb;pdb.set_trace()

# mix

numlist = range(len(quotes))
random.shuffle(numlist)

# write
with codecs.open(filename, 'w', 'utf-8') as fn:
    for n in numlist:
        fn.write(quotes[n] + u'\n')
        fn.write(authors[n] + u'\n')
        fn.write('\n')

        
    
        
