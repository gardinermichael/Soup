from bs4 import BeautifulSoup
import sys
sys.path.append('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/util/')

from logg import LoggingPrinter,Loge


headers = ["id", "Search term", 'Student name','First semester enrolled','Last semester enrolled','Degree']

degree_headers = ['degree_name','Major name','Date degree received','Honors received','Special honors received','Degree notes']


zipper_rows = list()

zipper_rows.append(headers)
count = 1

import os,glob
folder_path = os.getcwd()
folder_path += "/utexas/"

with LoggingPrinter():
	for filename in os.listdir(folder_path):
		file_path = folder_path + filename
		html = open(file_path, 'r', encoding='utf-8')
		soup = BeautifulSoup(html, "html5lib")
		
		
		students = soup.select('tr[class="student_main_info"]')
		
		students = soup.select('tr')
		
		#print(students[2].text.strip())
		#print("-----")
		
		for student in students:
			student_row = list()
			degree_row = list()
			
			student_name = str()
			last_sem = str()
			first_sem = str()
			
			degree_name = str()
			major_name = str()
			degree_date = str()
	
			honors = str()
			sp_honors = str()
			degree_note = str()
			
			
			if len(student.attrs) > 0:
				if str(student.attrs['class']) == "['student_main_info']":
					student_name = student.select_one("td.student_name").text.strip()
					first_sem = student.select_one("td.first_sem").text[15:].strip()
					last_sem = student.select_one("td.last_sem").text[15:].strip()
			elif student.th == None:
					if student.td != None:
						try:
							degree_name = student.select_one("td.degree_name").text.strip()
						except Exception as e:
							with Loge(e):
								pass
	
		
						try:
							major_name = student.select_one("td.major_name").text.strip()
						except Exception as e:
							with Loge(e):
								pass
						try:
							degree_date = student.select_one("td.degree_date").text.strip()
						except Exception as e:
							with Loge(e):
								pass
						
						try:
							honors = student.select_one("td.honors").text.strip()
						except Exception as e:
							with Loge(e):
								pass
	#					sp_honors = student.select_one("td.sp_honors").text.strip()
	#					degree_date = student.select_one("td.degree_date").text.strip()
	
						#print("tr", student.td)
						print('uuuuuuuuuuuuuuuh')
					else:
						print("elseelse", student)
						print("666666666")
			else:
				print("else", student)
				print("'mmmmmmmmmmm'")
				print()
					
			
			degree_row = [degree_name, major_name, degree_date, honors, sp_honors, degree_note]
			
			print(honors)
			print(degree_row)
			
							
			student_row = [student_name, first_sem, last_sem, degree_row]
			
			
			zipper_rows.append(student_row)
			
			
	print("final")
	print(zipper_rows)	
				#print(student)
				
				
#				print(student_name)
#				print(first_sem)
#				print(last_sem)
##				for descendant in student.descendants:
##					print("c", descendant)

#					if len(descendant.attrs) > 0:
#						print(child.attrs)
#						result_class = str(child.attrs['class'])[2:-2]
#						result_text = str(child.text).strip()
#						if result_class == "student_name":
#						#student_row.append(result_text)
#							student_name = result_text.strip()
#						elif result_class == 'first_sem':
#							#student_row.append(result_text[15:].strip())
#							first_sem = result_text[15:].strip()
#						elif result_class == 'last_sem':
#							#student_row.append(result_text[15:].strip())
#							last_sem = result_text[15:].strip()

		
		
		
	
		
	
	
