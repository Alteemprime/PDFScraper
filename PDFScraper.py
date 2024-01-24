import fitz #pymuPDF
import os
import pandas as pd

def parse_pdf(file_path):
    #fitz breaks down pdf file to list of page
    doc = fitz.open(file_path)
    text = ''
    for page_number in range(45,46) :
        page = doc[page_number]
        text += page.get_text()
    doc.close()
    return text

parsed_text = parse_pdf('.\\STATISTIK PERTANIAN 2022.pdf')
#make list from parsed text which every time \n is found in parsed_text, separate to each list element
texts_split = parsed_text.split('\n')
#remove hanging spaces in each found text in pdf page, also if text.strip True (it contains char, excluding null char a.k.a ''
texts_strip = [text.strip() for text in texts_split if text.strip()]

table_heading = ['No','Provinsi','Data2015','Data2016','Data2017','Data2018','Data2019']
#find table data from first find number 1 and extend it for 7 x 34 length (length of the table)
table_data = texts_strip[texts_strip.index('1') : (texts_strip.index('1')+(7*34))]
#reshape table_data so every 7 element become separate list
reshaped_table_data = [table_data[i:i+7] for i in range (0,len(table_data),7)]

#merge table heading and table data
df = pd.DataFrame(reshaped_table_data,columns=table_heading)

#texts_strip = [text  for text in texts_strip]    
#might be able to detect table contents using x, y, width, height, text, font to detect table contents
#parsed_block = fitz.open('.\\STATISTIK PERTANIAN 2022.pdf')[45].get_text('blocks')
print(df)
        
      