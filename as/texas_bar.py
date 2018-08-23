
# http://omz-software.com/pythonista/docs/ios/beautifulsoup.html
# http://omz-software.com/pythonista/docs/ios/beautifulsoup_guide.html

html_doc = """
<html><head><title>The Dormouse's story</title></head>


<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""






from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html5lib")
#print(soup.prettify())








#rows = soup.find_all('a')
#print(rows[0].text)
#headers = ["id", "Name", ]
#
#
#import csv
#with open('eggs.csv', 'w', newline='\n') as csvfile:
#       spamwriter = csv.writer(csvfile, lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
#
#       for row in rows:
#               spamwriter.writerow(["name"] + [row.text])



headers = ["id", "Name", "Firm", "Primary Practice Location", "Address", "Primary Practice Areas", "Full Profile URL", "Website URL", "Email URL", "vCard URL", "Telephone", "Image URL", "Badge Title", "Badge IMG", "Badge URL", "Duplicate Count"]



count = 1
duplicate_full_count = 0
duplicate_name_count = 0

#row_dict = dict()


csv_rows = list()
csv_rows.append(headers)
duplicate_name_check = list()
duplicate_full_check = list()

# encoding='utf-8'

import os,glob
folder_path = os.getcwd()
folder_path += "/texas_bar/"


for filename in os.listdir(folder_path):
    file_path = folder_path + filename
    html = open(file_path, 'r', encoding='utf-8')
    
    html_soup = BeautifulSoup(html, "html5lib")
    rows = html_soup.select("div.results")
    for row in rows:
    
        # Name csv_full_name
        html_name = row.find_all("h3")
        full_name = str()
        csv_full_name = str()
        for name in html_name[0].stripped_strings:
            full_name += " " + name
    
        csv_full_name = full_name.strip()
    
        # Firm csv_firm
        csv_firm = str()
        html_firm = row.find_all("h5")
        csv_firm = str(html_firm[0].text).strip()
    
        # Location csv_location
        html_location = row.select("p")
        location = list()
        for child in html_location[0].stripped_strings:
            location.append(child)
        csv_location = str()
        if len(location) > 0:
            if location[0] == "Primary Practice Location:":
                csv_location = location[1]
    
        # Address csv_address
    
        html_address = row.select("p.address")
        address = list()
        csv_address = str()
        if len(html_address) > 0:
            for child in html_address[0]:
                address.append(str(child).strip())
    
            for line in address:
                if line == '<br/>':
                    csv_address += ", "
                else:
                    csv_address += line
    
        # Practice Area csv_area
    
        csv_area = str()
        html_areas = row.select("p.areas")
        area = list()
        for child in html_areas[0].stripped_strings:
            area.append(child)
        csv_area = str(area[1]).strip()
    
    
        # Full Profile URL csv_profile_url
    
        csv_profile_url = str()
        html_profiles = row.select("a.read-more")
        csv_profile_url = html_profiles[0].get('href').strip()
    
    
        # Website URL, Email URL, vCard URL, Telephone
        # csv_website, csv_email, csv_vcard, csv_telephone
    
        html_contact = row.select("div.contact a")
    
        csv_website = str()
        csv_email = str()
        csv_vcard = str()
        csv_telephone = str()
        for item in html_contact:
            if item.text.strip() == 'VISIT WEBSITE':
                csv_website = item.get('href')
            elif item.text.strip() == 'EMAIL NOW':
                csv_email = item.get('href')
            elif item.text.strip() == 'Download vCard':
                csv_vcard = item.get('href')
            elif item.text.strip()[:4] == "Tel:":
                csv_telephone = item.text.strip()[5:]
    
        # Image URL csv_image
    
        csv_image = str()
        html_image = row.select_one("img.avatar")
        csv_image = str(html_image.attrs['style'][16:-2]).strip()
    
        # Badges csv_badges_title csv_badges_img csv_badges_url
    
        
        csv_badges_url = str()
        csv_badges_img = str()
        csv_badges_title = str()
        html_badges = row.select("div.badges")
        for possible_item in html_badges[0].contents:
#            try:
#                csv_badges += possible_item.replace('\n', '').replace('\t', '').strip()
#            except TypeError as e:
#print(e)
            try:
                csv_badges_title = str(possible_item.img.attrs['title']).strip()
                csv_badges_img = possible_item.img.attrs['src']
                csv_badges_url = possible_item.get('href')
            except AttributeError as e:
                try: 
                    csv_badges_url = possible_item.get('href')
                except AttributeError as e:
                    pass
                    

                
        csv_row = [csv_full_name,
            csv_firm,
            csv_location,
            csv_address,
            csv_area,
            csv_profile_url,
            csv_website,
            csv_email,
            csv_vcard,
            csv_telephone,
            csv_image,
            csv_badges_title,
            csv_badges_img,
            csv_badges_url ]
            
        #csv_rows.append(csv_row)
        
        if csv_row in duplicate_full_check:
            duplicate_full_check.append(csv_row)
            print(csv_row)
            duplicate_full_count += 1
        
        elif csv_full_name in duplicate_name_check:
            duplicate_name_check.append(csv_full_name)
            
#            dlist = row_dict[csv_full_name][1:]
#            for index in range(len(csv_row)):
#                if len(str(csv_row[index])) > 0 and len(str(dlist[index])) == 0:
#                    print("----------")
#                    print("new: ", csv_row[index])
#                    print()
#                    print("old: ", dlist)
#                    print("----------")
#                else:
#                    print(len(str(csv_row[index])), len(str(dlist[index])))

            
            duplicate_name_count += 1
            
        else:
            duplicate_full_check.append(csv_row)
            duplicate_name_check.append(csv_full_name)
            
#            row_dict[csv_full_name] = csv_row

            
            csv_row.insert(0, count)
            
            
            csv_rows.append(csv_row)
            count += 1


        
for row in csv_rows[1:]:
    #print(duplicate_full_check.count(inner_row))
    row.append(duplicate_name_check.count(row[1]))



print("count: ", count, " | len: ", len(csv_rows))
print("full duplicate count:", len(duplicate_full_check), " | name duplicate count: ", len(duplicate_name_check))


print(duplicate_name_count)
print(duplicate_full_count)
#print(duplicate_full_check)
#print(duplicate_name_check)

# 'a' is append mode, 'w' to rewrite the file
import csv
with open('texas_bar.csv', 'a', newline='\n', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile, lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)

    csv_writer.writerows(csv_rows)
    
    

#with open('dups.csv', 'a', newline='\n', encoding='utf-8') as csvfile:
#    csv_writer = csv.writer(csvfile, lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
#
#    csv_writer.writerows(duplicates)

    
