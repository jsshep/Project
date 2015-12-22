# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 12:06:30 2015

@author: jonathan.shepard
"""
import pandas as pd
#import html parser, grab script text from web
url = "http://www.imsdb.com/scripts/Imaginarium-of-Doctor-Parnassus,-The.html"
from bs4 import BeautifulSoup
from urllib import urlopen
html_soup = BeautifulSoup(urlopen(url).read()) #read in teh html and let Beautiful soup get it into a form we can use with line breaks in text
type(html_soup)  # to see the type
print (html_soup.text)  #to see that the text looks like

script = []  # create an empty list
for row in html_soup.text.splitlines():
       script.append(row)

#convert list to dataframe
df = pd.DataFrame(script)
df.columns = ['text']

#clean data to get list of characters
df['character_candidates'] = df.text.str.isupper()
df['ext_scene_heading'] = df.text.str.contains(("EXT."), na=False)
df['int_scene_heading'] = df.text.str.contains(("INT."), na=False)
character_candidates = df.drop(df[df.character_candidates == False].index)
character_candidates = character_candidates.drop(character_candidates[character_candidates.ext_scene_heading == True].index)
character_candidates = character_candidates.drop(character_candidates[character_candidates.int_scene_heading == True].index)
cc_list = []
for x in character_candidates.text:
    cc_list.append(x)
for row in range(0,len(cc_list)):
  cc_list[row] = cc_list[row].replace(" ", "")
char = pd.DataFrame(cc_list)
char.columns = ['text']
char = char.drop_duplicates()
char.to_csv('imaginarium.csv', encoding='utf-8')

#manually add sex data in Excel for each character
#then read in new data, clean it

movie_sex = 'imaginarium.csv'
movie_sex2 = pd.read_table(movie_sex, sep=',', header=0)
movier_sex2 = movie_sex2.drop(movie_sex2[movie_sex2.sex == 'X'].index)

#assign boolean identifier to all uppercase lines in script, remove spaces to facilitate DataFrame merge

listdud = []
for x in df.text:
    listdud.append(x)
for row in range(0,len(listdud)):
  listdud[row] = listdud[row].replace(" ", "")
nospace = pd.DataFrame(listdud)
nospace.columns = ['text']
nospace['upper'] = nospace.text.str.isupper()

# merge script lines with manually-added "sex assignment" data
merged = pd.merge(nospace, movie_sex2, how='left')
merged.sex.value_counts()

#now it's time to count the lines of dialogue for each sex!

# first we count blank lines
merged['blank_line'] = merged.text == ""

#then add an empty list for male line counts
male_line_counts = []

#then compile a list to give us the number of line 1s, line 2s, etc
merged['shift_Male_ID'] = merged.sex.shift(1)
merged['newline'] = merged.shift_Male_ID == 'M'
merged.loc[(merged['shift_Male_ID'] == 'M') & (merged['blank_line'] == False), 'ML1'] = 1
merged['shift_line1'] = merged.ML1.shift(1)
merged.loc[(merged['shift_line1'] == 1) & (merged['blank_line'] == False), 'ML2'] = 1
merged['shift_line2'] = merged.ML2.shift(1)
merged.loc[(merged['shift_line2'] == 1) & (merged['blank_line'] == False), 'ML3'] = 1
merged['shift_line3'] = merged.ML3.shift(1)
merged.loc[(merged['shift_line3'] == 1) & (merged['blank_line'] == False), 'ML4'] = 1
merged['shift_line4'] = merged.ML4.shift(1)
merged.loc[(merged['shift_line4'] == 1) & (merged['blank_line'] == False), 'ML5'] = 1
merged['shift_line5'] = merged.ML5.shift(1)
merged.loc[(merged['shift_line5'] == 1) & (merged['blank_line'] == False), 'ML6'] = 1
merged['shift_line6'] = merged.ML6.shift(1)
merged.loc[(merged['shift_line6'] == 1) & (merged['blank_line'] == False), 'ML7'] = 1
merged['shift_line7'] = merged.ML7.shift(1)
merged.loc[(merged['shift_line7'] == 1) & (merged['blank_line'] == False), 'ML8'] = 1
merged['shift_line8'] = merged.ML8.shift(1)
merged.loc[(merged['shift_line8'] == 1) & (merged['blank_line'] == False), 'ML9'] = 1
merged['shift_line9'] = merged.ML9.shift(1)
merged.loc[(merged['shift_line9'] == 1) & (merged['blank_line'] == False), 'ML10'] = 1
merged['shift_line10'] = merged.ML10.shift(1)
merged.loc[(merged['shift_line10'] == 1) & (merged['blank_line'] == False), 'ML11'] = 1

merged['shift_line11'] = merged.ML11.shift(1)
merged.loc[(merged['shift_line11'] == 1) & (merged['blank_line'] == False), 'ML12'] = 1
merged['shift_line12'] = merged.ML12.shift(1)
merged.loc[(merged['shift_line12'] == 1) & (merged['blank_line'] == False), 'ML13'] = 1
merged['shift_line13'] = merged.ML13.shift(1)
merged.loc[(merged['shift_line13'] == 1) & (merged['blank_line'] == False), 'ML14'] = 1
merged['shift_line14'] = merged.ML14.shift(1)
merged.loc[(merged['shift_line14'] == 1) & (merged['blank_line'] == False), 'ML15'] = 1
merged['shift_line15'] = merged.ML15.shift(1)
merged.loc[(merged['shift_line15'] == 1) & (merged['blank_line'] == False), 'ML16'] = 1
merged['shift_line16'] = merged.ML16.shift(1)
merged.loc[(merged['shift_line16'] == 1) & (merged['blank_line'] == False), 'ML17'] = 1
merged['shift_line17'] = merged.ML17.shift(1)
merged.loc[(merged['shift_line17'] == 1) & (merged['blank_line'] == False), 'ML18'] = 1
merged['shift_line18'] = merged.ML18.shift(1)
merged.loc[(merged['shift_line18'] == 1) & (merged['blank_line'] == False), 'ML19'] = 1
merged['shift_line19'] = merged.ML19.shift(1)
merged.loc[(merged['shift_line19'] == 1) & (merged['blank_line'] == False), 'ML20'] = 1
merged['shift_line20'] = merged.ML20.shift(1)
merged.loc[(merged['shift_line20'] == 1) & (merged['blank_line'] == False), 'ML21'] = 1
merged['shift_line21'] = merged.ML21.shift(1)
merged.loc[(merged['shift_line21'] == 1) & (merged['blank_line'] == False), 'ML22'] = 1
merged['shift_line22'] = merged.ML22.shift(1)
merged.loc[(merged['shift_line22'] == 1) & (merged['blank_line'] == False), 'ML23'] = 1
merged['shift_line23'] = merged.ML23.shift(1)
merged.loc[(merged['shift_line23'] == 1) & (merged['blank_line'] == False), 'ML24'] = 1
merged['shift_line24'] = merged.ML24.shift(1)
merged.loc[(merged['shift_line24'] == 1) & (merged['blank_line'] == False), 'ML25'] = 1
merged['shift_line25'] = merged.ML25.shift(1)
merged.loc[(merged['shift_line25'] == 1) & (merged['blank_line'] == False), 'ML26'] = 1
merged['shift_line26'] = merged.ML26.shift(1)
merged.loc[(merged['shift_line26'] == 1) & (merged['blank_line'] == False), 'ML27'] = 1
merged['shift_line27'] = merged.ML27.shift(1)
merged.loc[(merged['shift_line27'] == 1) & (merged['blank_line'] == False), 'ML28'] = 1
merged['shift_line28'] = merged.ML28.shift(1)
merged.loc[(merged['shift_line28'] == 1) & (merged['blank_line'] == False), 'ML29'] = 1
merged['shift_line29'] = merged.ML29.shift(1)
merged.loc[(merged['shift_line29'] == 1) & (merged['blank_line'] == False), 'ML30'] = 1
merged['shift_line30'] = merged.ML30.shift(1)
merged.loc[(merged['shift_line20'] == 1) & (merged['blank_line'] == False), 'ML31'] = 1




#then add an empty list for male line counts
male_line_counts = []

for index, row in merged.iterrows():
    if row['ML1'] == 1:
        male_line_counts.append(1)
for index, row in merged.iterrows():
    if row['ML2'] == 1:
        male_line_counts.append(2)
for index, row in merged.iterrows():
    if row['ML3'] == 1:
        male_line_counts.append(3)
for index, row in merged.iterrows():
    if row['ML4'] == 1:
        male_line_counts.append(4)        
for index, row in merged.iterrows():
    if row['ML5'] == 1:
        male_line_counts.append(5)
for index, row in merged.iterrows():
    if row['ML6'] == 1:
        male_line_counts.append(6)
for index, row in merged.iterrows():
    if row['ML7'] == 1:
        male_line_counts.append(7)
for index, row in merged.iterrows():
    if row['ML8'] == 1:
        male_line_counts.append(8)
for index, row in merged.iterrows():
    if row['ML9'] == 1:
        male_line_counts.append(9)        
for index, row in merged.iterrows():
    if row['ML10'] == 1:
        male_line_counts.append(10)       
for index, row in merged.iterrows():
    if row['ML11'] == 1:
        male_line_counts.append(11)        
for index, row in merged.iterrows():
    if row['ML12'] == 1:
        male_line_counts.append(12)        
for index, row in merged.iterrows():
    if row['ML13'] == 1:
        male_line_counts.append(13)        
for index, row in merged.iterrows():
    if row['ML14'] == 1:
        male_line_counts.append(14)
for index, row in merged.iterrows():
    if row['ML15'] == 1:
        male_line_counts.append(15)
for index, row in merged.iterrows():
    if row['ML16'] == 1:
        male_line_counts.append(16)
for index, row in merged.iterrows():
    if row['ML17'] == 1:
        male_line_counts.append(17)
for index, row in merged.iterrows():
    if row['ML18'] == 1:
        male_line_counts.append(18)
for index, row in merged.iterrows():
    if row['ML19'] == 1:
        male_line_counts.append(19)        
for index, row in merged.iterrows():
    if row['ML20'] == 1:
        male_line_counts.append(20)       
for index, row in merged.iterrows():
    if row['ML21'] == 1:
        male_line_counts.append(21)        
for index, row in merged.iterrows():
    if row['ML22'] == 1:
        male_line_counts.append(22)        
for index, row in merged.iterrows():
    if row['ML23'] == 1:
        male_line_counts.append(23)        
for index, row in merged.iterrows():
    if row['ML24'] == 1:
        male_line_counts.append(24)
for index, row in merged.iterrows():
    if row['ML25'] == 1:
        male_line_counts.append(25)
for index, row in merged.iterrows():
    if row['ML26'] == 1:
        male_line_counts.append(26)
for index, row in merged.iterrows():
    if row['ML27'] == 1:
        male_line_counts.append(27)
for index, row in merged.iterrows():
    if row['ML28'] == 1:
        male_line_counts.append(28)
for index, row in merged.iterrows():
    if row['ML29'] == 1:
        male_line_counts.append(29)        
for index, row in merged.iterrows():
    if row['ML30'] == 1:
        male_line_counts.append(30)       
for index, row in merged.iterrows():
    if row['ML31'] == 1:
        male_line_counts.append(31)


# now we create a list containing all the male dialogue.
male_dialogue_list = []
for index, row in merged.iterrows():
    if row['ML1'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML2'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML3'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML4'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML5'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML6'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML7'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML8'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML9'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML10'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML11'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML12'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML13'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML14'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML15'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML16'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML17'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML18'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML19'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML20'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML21'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML22'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML23'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML24'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML25'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML26'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML27'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML28'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML29'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML30'] == 1:
        male_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['ML31'] == 1:
        male_dialogue_list.append(row['text'])

#now let's try to cut out the "false positives", like parentheticals and camera directions.
#we won't catch them all, but we should get most of it.    

    

for r in male_dialogue_list:
    if r.isupper():
        male_dialogue_list.remove(r)
for r in male_dialogue_list:
    if r.isupper():
        male_dialogue_list.remove(r)

final_male_dialogue = (filter(lambda x: "("not in x, male_dialogue_list))
    
#then we do the same things for female characters
        
#add an empty list for female line counts
female_line_counts = []

#then compile a list to give us the number of line 1s, line 2s, etc
merged['shift_Female_ID'] = merged.sex.shift(1)
merged['newline'] = merged.shift_Female_ID == 'F'
merged.loc[(merged['shift_Female_ID'] == 'F') & (merged['blank_line'] == False), 'FL1'] = 1
merged['shift_Fline1'] = merged.FL1.shift(1)
merged.loc[(merged['shift_Fline1'] == 1) & (merged['blank_line'] == False), 'FL2'] = 1
merged['shift_Fline2'] = merged.FL2.shift(1)
merged.loc[(merged['shift_Fline2'] == 1) & (merged['blank_line'] == False), 'FL3'] = 1
merged['shift_Fline3'] = merged.FL3.shift(1)
merged.loc[(merged['shift_Fline3'] == 1) & (merged['blank_line'] == False), 'FL4'] = 1
merged['shift_Fline4'] = merged.FL4.shift(1)
merged.loc[(merged['shift_Fline4'] == 1) & (merged['blank_line'] == False), 'FL5'] = 1
merged['shift_Fline5'] = merged.FL5.shift(1)
merged.loc[(merged['shift_Fline5'] == 1) & (merged['blank_line'] == False), 'FL6'] = 1
merged['shift_Fline6'] = merged.FL6.shift(1)
merged.loc[(merged['shift_Fline6'] == 1) & (merged['blank_line'] == False), 'FL7'] = 1
merged['shift_Fline7'] = merged.FL7.shift(1)
merged.loc[(merged['shift_Fline7'] == 1) & (merged['blank_line'] == False), 'FL8'] = 1
merged['shift_Fline8'] = merged.FL8.shift(1)
merged.loc[(merged['shift_Fline8'] == 1) & (merged['blank_line'] == False), 'FL9'] = 1
merged['shift_Fline9'] = merged.FL9.shift(1)
merged.loc[(merged['shift_Fline9'] == 1) & (merged['blank_line'] == False), 'FL10'] = 1
merged['shift_Fline10'] = merged.FL10.shift(1)
merged.loc[(merged['shift_Fline10'] == 1) & (merged['blank_line'] == False), 'FL11'] = 1
merged['shift_Fline11'] = merged.FL11.shift(1)
merged.loc[(merged['shift_Fline11'] == 1) & (merged['blank_line'] == False), 'FL12'] = 1
merged['shift_Fline12'] = merged.FL12.shift(1)
merged.loc[(merged['shift_Fline12'] == 1) & (merged['blank_line'] == False), 'FL13'] = 1
merged['shift_Fline13'] = merged.FL13.shift(1)
merged.loc[(merged['shift_Fline13'] == 1) & (merged['blank_line'] == False), 'FL14'] = 1
merged['shift_Fline14'] = merged.FL14.shift(1)
merged.loc[(merged['shift_Fline14'] == 1) & (merged['blank_line'] == False), 'FL15'] = 1
merged['shift_Fline15'] = merged.FL15.shift(1)
merged.loc[(merged['shift_Fline15'] == 1) & (merged['blank_line'] == False), 'FL16'] = 1
merged['shift_Fline16'] = merged.FL16.shift(1)
merged.loc[(merged['shift_Fline16'] == 1) & (merged['blank_line'] == False), 'FL17'] = 1
merged['shift_Fline17'] = merged.FL17.shift(1)
merged.loc[(merged['shift_Fline17'] == 1) & (merged['blank_line'] == False), 'FL18'] = 1
merged['shift_Fline18'] = merged.FL18.shift(1)
merged.loc[(merged['shift_Fline18'] == 1) & (merged['blank_line'] == False), 'FL19'] = 1
merged['shift_Fline19'] = merged.FL19.shift(1)
merged.loc[(merged['shift_Fline19'] == 1) & (merged['blank_line'] == False), 'FL20'] = 1
merged['shift_Fline20'] = merged.FL20.shift(1)
merged.loc[(merged['shift_Fline20'] == 1) & (merged['blank_line'] == False), 'FL21'] = 1
merged['shift_Fline21'] = merged.FL21.shift(1)
merged.loc[(merged['shift_Fline21'] == 1) & (merged['blank_line'] == False), 'FL22'] = 1
merged['shift_Fline22'] = merged.FL22.shift(1)
merged.loc[(merged['shift_Fline22'] == 1) & (merged['blank_line'] == False), 'FL23'] = 1
merged['shift_Fline23'] = merged.FL23.shift(1)
merged.loc[(merged['shift_Fline23'] == 1) & (merged['blank_line'] == False), 'FL24'] = 1
merged['shift_Fline24'] = merged.FL24.shift(1)
merged.loc[(merged['shift_Fline24'] == 1) & (merged['blank_line'] == False), 'FL25'] = 1
merged['shift_Fline25'] = merged.FL25.shift(1)
merged.loc[(merged['shift_Fline25'] == 1) & (merged['blank_line'] == False), 'FL26'] = 1
merged['shift_Fline26'] = merged.FL26.shift(1)
merged.loc[(merged['shift_Fline26'] == 1) & (merged['blank_line'] == False), 'FL27'] = 1
merged['shift_Fline27'] = merged.FL27.shift(1)
merged.loc[(merged['shift_Fline27'] == 1) & (merged['blank_line'] == False), 'FL28'] = 1
merged['shift_Fline28'] = merged.FL28.shift(1)
merged.loc[(merged['shift_Fline28'] == 1) & (merged['blank_line'] == False), 'FL29'] = 1
merged['shift_Fline29'] = merged.FL29.shift(1)
merged.loc[(merged['shift_Fline29'] == 1) & (merged['blank_line'] == False), 'FL30'] = 1
merged['shift_Fline30'] = merged.FL30.shift(1)
merged.loc[(merged['shift_Fline30'] == 1) & (merged['blank_line'] == False), 'FL31'] = 1

female_line_counts = []

for index, row in merged.iterrows():
    if row['FL1'] == 1:
        female_line_counts.append(1)
for index, row in merged.iterrows():
    if row['FL2'] == 1:
        female_line_counts.append(2)
for index, row in merged.iterrows():
    if row['FL3'] == 1:
        female_line_counts.append(3)
for index, row in merged.iterrows():
    if row['FL4'] == 1:
        female_line_counts.append(4)        
for index, row in merged.iterrows():
    if row['FL5'] == 1:
        female_line_counts.append(5)
for index, row in merged.iterrows():
    if row['FL6'] == 1:
        female_line_counts.append(6)
for index, row in merged.iterrows():
    if row['FL7'] == 1:
        female_line_counts.append(7)
for index, row in merged.iterrows():
    if row['FL8'] == 1:
        female_line_counts.append(8)
for index, row in merged.iterrows():
    if row['FL9'] == 1:
        female_line_counts.append(9)        
for index, row in merged.iterrows():
    if row['FL10'] == 1:
        female_line_counts.append(10)       
for index, row in merged.iterrows():
    if row['FL11'] == 1:
        female_line_counts.append(11)        
for index, row in merged.iterrows():
    if row['FL12'] == 1:
        female_line_counts.append(12)        
for index, row in merged.iterrows():
    if row['FL13'] == 1:
        female_line_counts.append(13)        
for index, row in merged.iterrows():
    if row['FL14'] == 1:
        female_line_counts.append(14)
for index, row in merged.iterrows():
    if row['FL15'] == 1:
        female_line_counts.append(15)
for index, row in merged.iterrows():
    if row['FL16'] == 1:
        female_line_counts.append(16)
for index, row in merged.iterrows():
    if row['FL17'] == 1:
        female_line_counts.append(17)
for index, row in merged.iterrows():
    if row['FL18'] == 1:
        female_line_counts.append(18)
for index, row in merged.iterrows():
    if row['FL19'] == 1:
        female_line_counts.append(19)        
for index, row in merged.iterrows():
    if row['FL20'] == 1:
        female_line_counts.append(20)       
for index, row in merged.iterrows():
    if row['FL21'] == 1:
        female_line_counts.append(21)        
for index, row in merged.iterrows():
    if row['FL22'] == 1:
        female_line_counts.append(22)        
for index, row in merged.iterrows():
    if row['FL23'] == 1:
        female_line_counts.append(23)        
for index, row in merged.iterrows():
    if row['FL24'] == 1:
        female_line_counts.append(24)
for index, row in merged.iterrows():
    if row['FL25'] == 1:
        female_line_counts.append(25)
for index, row in merged.iterrows():
    if row['FL26'] == 1:
        female_line_counts.append(26)
for index, row in merged.iterrows():
    if row['FL27'] == 1:
        female_line_counts.append(27)
for index, row in merged.iterrows():
    if row['FL28'] == 1:
        female_line_counts.append(28)
for index, row in merged.iterrows():
    if row['FL29'] == 1:
        female_line_counts.append(29)        
for index, row in merged.iterrows():
    if row['FL30'] == 1:
        female_line_counts.append(30)       
for index, row in merged.iterrows():
    if row['FL31'] == 1:
        female_line_counts.append(31)

# now we create a list containing all the female dialogue.
female_dialogue_list = []
for index, row in merged.iterrows():
    if row['FL1'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL2'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL3'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL4'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL5'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL6'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL7'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL8'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL9'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL10'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL11'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL12'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL13'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL14'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL15'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL16'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL17'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL18'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL19'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL20'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL21'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL22'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL23'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL24'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL25'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL26'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL27'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL28'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL29'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL30'] == 1:
        female_dialogue_list.append(row['text'])
for index, row in merged.iterrows():
    if row['FL31'] == 1:
        female_dialogue_list.append(row['text'])

#now let's try to cut out the "false positives", like parentheticals and camera directions.
#we won't catch them all, but we should get most of it.        

for r in female_dialogue_list:
    if r.isupper():
        female_dialogue_list.remove(r)
for r in female_dialogue_list:
    if r.isupper():
        female_dialogue_list.remove(r)

final_female_dialogue = (filter(lambda x: "("not in x, female_dialogue_list))

#now we know (roughly) how many male and female lines of dialogue are in the script! 
