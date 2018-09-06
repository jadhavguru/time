import re

text = '''
5.15AM 
05:15 AM  
5.15am 
5.15 am
5.15 PM
555:15PM
5.15 PM 
 5.15pm
13:4
13:04:22 13:24:22.04 '''

date='''1-08-2018, 03/8/2018, 07.08.18 , 04-14-1994 '''

date1=''' October 22 , 2018 ,  October 24, 2018 ,  October 29,  2018 , 1 Nov,2018, 03 Nov ,2018  
32 Nov,2018 '''

mobile='''
7382293451,91738293451 or 91 7382293451 
	+917382293451 or +91 7382293451 or +  91 7382293451
	(+91)738229345 or ( +91 )7382293451 or (+91) 7382293451'''

landline='''
    22469
04322469 or 043 22469 	
	(043)22469 or ( 043 )22469 or (043) 22469
'''

currency='''
$500.12 , 500.12dollars, 500.1 dollars
               $ 1.24 , 1.25dollars,  $1,000.40 , $10,000.14
'''

email='''abcd.yz@iiith.ac.in  can be written like  
abcd.yz[AT]iiith.ac.in  or like 
 abcd.yz@iiith.ac[Dot]in , 
 abcd.yz@iiith.ac.In,
  abcd.nitt.edu  or  
  abcd@nitt.edu  etc'''

url='''
https://www.google.co.in
www.cricbuzz.in
 http://www.abcd.me
'''
names='''
Rama Viswanath called by her friends Rama V.  or  V.Rama
              Subash Chandra Bose called as  S. C. Bose  or sometimes  Subash C. Bose,     Mr. Subash Chandra Bose,    Mr. S. C. Bose
              
Sri  A. Sumanth,  Dr. S. Priya  , Dr.B.Kavitha, Prof. John Xavier are members of the committee.
'''
#pattern = re.compile(r'((\d\d)|(\d)):(\d\d)(am|AM|pm|PM)')



#text1 = pattern.finditer(text)

#for i in text1:
 #   print(i)
######################################33
data_pattern=re.compile(r'(([0-2]\d)|([0-9])|([0]\d))[\.|\/|-](([0][0-9])|([0-1][0-2])|[0-9])[\.|\/|-](([0-9][0-9][0-9][0-9])|[0-9][0-9])')

text2 = data_pattern.finditer(date)

for i in text2:
    print(i.group())
############################################
#data_pattern1=re.compile(r'((j|J)anuary|(F|f)ebruary|(M|m)arch|(A|a)pril|(m|M)(O|o)ctober|()')

#text3 = data_pattern1.finditer(date1)

#for i in text3:
  #  print(i.group())
  #################################
mobile_pattern=re.compile(r'(\(?\+?\s?(91)?\s?\))?\s?\d{10}')

text4 = mobile_pattern.finditer(mobile)

for i in text4:
    print(i.group())
########################
landline_pattern=re.compile(r'(\(?\s?\d{3}\s?\)?)?\s?\d{5}')

text5 = landline_pattern.finditer(landline)

for i in text5:
    print(i.group())
##########################
currency_pattern=re.compile(r'\$?\s?\d+(\,)?\d*\.\d+\s?(dollars)?')

text6 = currency_pattern.finditer(currency)

for i in text6:
    print(i.group())
###################################
email_pattern=re.compile(r'[a-zA-Z0-9.-]+\[?(at|@|At|AT)\]?[a-zA-Z]+(\[?(\.|Dot|dot|DOT)\]?[a-zA-Z]*)+')

text7 = email_pattern.finditer(email)

for i in text7:
    print(i.group())
###############################

url_pattern=re.compile(r'(https://)?www\.[a-zA-z0-9.-]+\.[a-zA-z0-9.-]*')

text8 = url_pattern.finditer(url)

for i in text8:
    print(i.group())
#########################
name_pattern=re.compile(r'((Mr|mr|Shr|shr|Dr|dr|prof|Prof)|(^[A-Z]+)\.?\s?([A-Za-z.]+(^[A-Z]+)?\s?[A-Za-z]+))')

text9 = name_pattern.finditer(names)

for i in text9:
    print(i.group())




