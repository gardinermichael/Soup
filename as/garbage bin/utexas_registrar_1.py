from bs4 import BeautifulSoup



headers = ["id", "Search term", 'Student name','First semester enrolled','Last semester enrolled','Degree name','Major name','Date degree received','Honors received','Special honors received','Degree notes',]

#for child in soup.descendants:
#	if child.name == "h2":
#		try:
#			print("--------------")
#			print("------------------child: ", child.name)
#			
#			print("parent: ", child.parent.name)
#			print("parent class: ", child.parent.attrs)
#			print()
#			print("parents: ", [parents.name for parents in child.parents])
#			print("child class: ", child.attrs)
#		except AttributeError:
#			print()
#	
#print("--------------")
#
#table_parent = soup.find_all("form")
#
#for form in table_parent:
#	try:
#		for child in form.children:
#			if child.name == "h2":
#				print(child.name, child.attrs, child.text)
#	except AttributeError:
#			print()
#			
#			
#			
##results = soup.find_all(text='Search results beginning with B-NAGY, ANDREA:')
#print('@@@@@@@@@@@')
#
#
#th_parent = soup.find_all("th")


#for th in th_parent:
#	print(th.text)
zipper_rows = list()

zipper_rows.append(headers)
count = 1

import os,glob
folder_path = os.getcwd()
folder_path += "/utexas/"

for filename in os.listdir(folder_path):
	file_path = folder_path + filename
	html = open(file_path, 'r', encoding='utf-8')
	soup = BeautifulSoup(html, "html5lib")
	csv_rows = list()
		

	# Search Term
	table_form = soup.find_all("form")
	
	search_term = str()
	for form in table_form:
		try:
			search_term = form.h2.text[form.h2.text.find("with")+4:-1].strip()
		except AttributeError:
			pass


# student info
	students = soup.select("tbody tr")

#print(students)


#last_sem = str()
#first_sem = str()
#degree_name = str()
#major_name = str()
#degree_date = str()
#honors = str()
#student_name = str()

	#print(students.select('tr[class="student_main_info"]'))


	for student in students:
		student_row = list()
		last_sem = str()
		first_sem = str()
		degree_name = str()
		major_name = str()
		degree_date = str()
		student_name = str()
		honors
		sp_honors
		degree_note
		
		
		try:
			#print("atusbet", student)	#		if str(student.attrs['class'])[2:-2] == 'student_main_info':
	
			for child in student.children:
				try:
					result_class = str(child.attrs['class'])[2:-2]
					try: 
						if result_class == "filler":
							break
						result_text = str(child.text).strip()
						if result_class == "student_name":
							#student_row.append(result_text)
							student_name = result_text.strip()
						elif result_class == 'first_sem':
							#student_row.append(result_text[15:].strip())
							first_sem = result_text[15:].strip()
						elif result_class == 'last_sem':
							#student_row.append(result_text[15:].strip())
							last_sem = result_text[15:].strip()
					except:
						pass
					try:
						if result_class == 'degree_name':
							#student_row.append(result_text)
							degree_name = result_text
						elif result_class == 'major_name':
							major_name = result_text[5:].strip()
						elif result_class == 'degree_date':
							degree_date = result_text
					except:
							pass
				except (AttributeError, KeyError):
					pass
				
		except (AttributeError, KeyError):
			pass
		student_row = [count, search_term, student_name, first_sem, last_sem, degree_name, major_name, degree_date]
		#print(student_row)
		csv_rows.append(student_row)
	
	length = len(csv_rows)
	
	print(len(csv_rows), csv_rows[int(length)-1])

	
	
	for index in range(1,int(len(csv_rows)),1):
		try:
			#print("index", csv_rows[index])
			#print(csv_rows[index+1])
			#print(len(csv_rows)
#			print(index)
#			print(index+1, index+2)
			if len(csv_rows[index][2]) > 0 and len(csv_rows[index+1][5]) > 0:
				zipper_rows.append([count, search_term, csv_rows[index][2],
				csv_rows[index][3], csv_rows[index][4], csv_rows[index+1][5], csv_rows[index+1][6], csv_rows[index+1][7]])
				count += 1
			elif len(csv_rows[index][2]) > 0 and len(csv_rows[index+1][6]) > 0:
				zipper_rows.append([count, search_term, csv_rows[index][2],
				csv_rows[index][3], csv_rows[index][4], csv_rows[index+1][5], csv_rows[index+1][6], csv_rows[index+1][7]])
				count += 1
			elif len(csv_rows[index][2]) > 0 and len(csv_rows[index+1][7]) > 0:
				zipper_rows.append([count, search_term, csv_rows[index][2],
				csv_rows[index][3], csv_rows[index][4], csv_rows[index+1][5], csv_rows[index+1][6], csv_rows[index+1][7]])
				count += 1
			elif len(csv_rows[index][2]) > 0:
				zipper_rows.append([count, search_term, csv_rows[index][2],
				csv_rows[index][3], csv_rows[index][4], csv_rows[index+1][5], csv_rows[index+1][6], csv_rows[index+1][7]])
				count += 1
			
#			zipper_rows.append([count, search_term, csv_rows[index][2],
#			csv_rows[index][3], csv_rows[index][4], 
#			csv_rows[index+1][5], csv_rows[index+1][6], csv_rows[index+1][7]])
#			count += 1

			#print(csv_rows[index], csv_rows[index+1])
		except IndexError as e:
			print(e)


		
	
	
print(zipper_rows)



#tbody = soup.select("tbody")
#
#
#for tr in tbody:
#	print(tr.text.strip())
#	print("------")
#	break



	
	
#	for child in student.children:	
#		try:
#			result_class = str(child.attrs['class'])[2:-2]
#			result_text = str(child.text).strip()
#			if result_class in student_row:
#				pass
#			else:
#				student_row.append(result_class)
#			
#			
#			
#			
#			
#			
#			
#			
#			
#			
#			
##			if result_class == "student_name":
##				
##				student_name = result_text.strip()
##				#student_row[student_name] = [count, search_term]
##			for sibling in child.next_siblings.strip:	
##			#if len(student_row) > 0:
##				print(sibling)
##				if str(sibling.attrs['class'])[2:-2] == 'first_sem':
##					first_sem = result_text
##				elif result_class == 'last_sem':
##					last_sem = result_text
##				elif result_class == 'degree_name':
##					degree_name = result_text
##				elif result_class == 'major_name':
##					major_name = result_text
##				elif result_class == 'degree_date':
##					degree_date = result_text
##				else:
##					pass
##	#					print(child.name)
##	#					print(child.attrs['class'])
##	#					print(child.text)
##
##					
##				student_row = [count, search_term, student_name, first_sem, last_sem, degree_name, major_name, degree_date]
###				student_row.insert(0, search_term)
###				student_row.insert(0, count)
##
#
##				count += 1
##				student_row = list()	
##			
#
#		except (AttributeError, KeyError):
#			continue
#			
#		
#for header in student_row:
#	head = soup.select("td" +  "." + header)
#	print(head)
#	
#csv_rows.append(student_row)			

			
	




#print(csv_rows)



import csv
with open('utexas.csv', 'a', newline='\n', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile, lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)

    csv_writer.writerows(zipper_rows)


