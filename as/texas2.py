from bs4 import BeautifulSoup
import sys
sys.path.append('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/util/hellpaz/')

from logg import LoggingPrinter,Loge


# headers are .typeof(list()) == True/first item in stack

headers = ["id", "Search term", 'Student name','First semester enrolled','Last semester enrolled','Degree']

degree_headers = ['degree_name','Major name','Date degree received','Honors received','Special honors received','Degree notes']



class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []
		
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
		
	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)
	
	def show(self):
		return self.items

zipper_rows = Stack()
zipper_rows.push(headers)
	
count = 1
table_header_count = 0

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
							major_name = student.select_one("td.major_name").text.split('major').strip()
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
						try:
							sp_honors = student.select_one("td.sp_honors").text.strip()
						except Exception as e:
							with Loge(e):
								pass
						try:
							degree_note = student.select_one("td.degree_note").text.strip()
						except Exception as e:
							with Loge(e):
								pass
	
						#print("tr", student.td)
					else:
						print("Following <td> in Student row returned 'None':\n\n\t)", student, "\n\nRow End.")
						print()
			else:
				table_header_count += 1
				if str(student).startswith("<tr>"):
					print("Skipped Table Header No. " + str(table_header_count))
					print()
				else:
					print("Following row had no attrs:\n\n\t", student, "\n\nRow End.")
					print()
					
			
			
			student_row = Stack()
			degree_stack = Stack()
			
			if len(student_name) > 1:
				degree_rows_stack = Stack()
				degree_rows_stack.push(degree_headers)
				student_row.push(count)
				count += 1
				for field in [student_name, last_sem, first_sem, degree_rows_stack]:
					student_row.push(field)
				
				
				
				for field in [degree_name, major_name, degree_date, honors, sp_honors, degree_note]:
					if len(field) > 1:
						for field in [degree_name, major_name, degree_date, honors, sp_honors, degree_note]:
							degree_stack.push(field)
						degree_rows_stack = student_row.pop()
						degree_rows_stack.push(degree_stack)
						student_row.push(degree_rows_stack)
						break
						


				zipper_rows.push(student_row)
			else:

				for field in [degree_name, major_name, degree_date, honors, sp_honors, degree_note]:
					if len(field) > 1:
						for field in [degree_name, major_name, degree_date, honors, sp_honors, degree_note]:
							degree_stack.push(field)
						
						previous_entry = zipper_rows.pop()
						degree_rows_stack = previous_entry.pop()
						degree_rows_stack.push(degree_stack)
						previous_entry.push(degree_rows_stack)
						zipper_rows.push(previous_entry)
						
					
						print("Success:\n\n", degree_stack.show(), " >>> ", previous_entry.show(), " : ", previous_entry.peek().show(), "\n\nEnd\n")
						
						break


						
				
			
			
					
#			else:
#				print("Failure\n\n", degree_row, "\n\nEnd\n")
#				pass
#			except IndexError as e:
#						print("Zipper Rows Empty")
#						pass



				
			
			
#	print()
#	print("final")
#	for row in zipper_rows.show():
#		try:
#			student = row.show()
#			degrees = row.peek()
#			print("student", student)
#			print()
#			for degree in degrees.show():
#				print("\t\tdegree", degree.show())
#				print()
#			print()
#			print()
#		except:
#			print(row)


		csv_rows = list()
		
		for row in zipper_rows.show():
			try:
				student_list = list()
				student_stack = row.show()
				for item in student_stack:
					student_list.append(item)
				
				degrees_list = list()
				degrees_stack = student_list.pop()
				
									
				for degree in degrees_stack.show():
					
					degree_list = list()
					try:
						print(degree.size())
						print(degrees_stack.size())
						print("degree show", degree.show())
						degrees_list.append(degree.show())
					except:
						print("degree", degree)
						degrees_list.append(degree)
					#degrees_list.append(degree_list)


						
				student_list.append(degrees_list)



	
	
				csv_rows.append(student_list)
			except:
				header_list = row
				csv_rows.append(header_list)
		

		
		print(csv_rows)

import csv
with open('utexas.csv', 'a', newline='\n', encoding='utf-8') as csvfile:
	csv_writer = csv.writer(csvfile, lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)

	
		#	csv_rows.append(student_list)
		

	csv_writer.writerows(csv_rows)

	
		
	
	
