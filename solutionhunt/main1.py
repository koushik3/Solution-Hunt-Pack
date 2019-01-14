import argparse
import colorsys
import imghdr
import imp
import os
import random
import cv2
import csv
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from nltk import PorterStemmer
import tkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
# from keras import backend as K
# from keras.models import load_model
from PIL import Image, ImageDraw, ImageColor,ImageFont
from importlib import reload
import sys
import requests
from bs4 import BeautifulSoup
import math
import numpy as np
import re
import webbrowser
import time
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
import summarize
import time
from selenium import webdriver
from selenium.webdriver.common import keys
import requests
import re
import webbrowser
import sys
from importlib import reload
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import webbrowser
import search_keywords as sk
import gsearch.googlesearch as s

# r=s.search("dog")	

parser = argparse.ArgumentParser(
    description='Run a YOLO_v2 style detection model on test images..')
parser.add_argument(
    '-t',
    '--test_path',
    help='path to directory of test images, defaults to images/',
    default='images')
parser.add_argument(
    '-o',
    '--output_path',
    help='path to output test images, defaults to images/out',
    default='images/out')



# text = """
#     The tool should integrate seamlessly with www.tatainnoverse.com
#     It should extract the keywords from the challenge uploaded on Tata Innoverse.com without any supervision
#     The keyword extraction algorithm must be highly accurate, close to 95% accuracy expected.
#     It should allow the user to edit the keyword list and then take it again as an input for solution scouting
#     It should crawl the Internet and extract information from all available sources that are present on Internet
#     It should create a report after the search is over. The report should be properly formatted and the information searched should be tagged according to the keywords that were used for searching the information.
#     The end user should be able to define the duration for which the search is to be performed.
#     The end user should be able to also define the level of accuracy, in relation to the keyword list, with which the search is to be performed.
# """


def key_words(text):
	display = Display(visible = 0, size = (800,600))
	display.start()

	driver = webdriver.Firefox(executable_path=r'/home/rpg/Downloads/geckodriver')

	driver.set_window_size(0,0)
	url = 'http://keywordextraction.net/term-extractor'
	driver.get(url)

	max_key =50

	driver.find_element_by_xpath("//textarea[@ id='text']").clear()
	driver.find_element_by_xpath("//textarea[@ id='text']").send_keys(text)
	driver.find_element_by_xpath("//input[@ id='sentnum']").clear()
	driver.find_element_by_xpath("//input[@ id='sentnum']").send_keys(max_key)
	driver.find_element_by_xpath("//input[@ class='btn btn-primary btn-large']").click()
	time.sleep(1)
	source = driver.page_source.replace('<br>', '\n')
	display.stop()
	soup = BeautifulSoup(source,"html.parser")
	data = soup.find_all("div",{"class":"span5"})
	for i in range(1,len(data)):
		everyblock=data[i].find_all("p")
		for j in range(0,len(everyblock)):
			key_words=everyblock[j].text.replace(u'\xa0', u' ').split("\n")
			for k in range(0,len(key_words)):
				key_words[k]=key_words[k].strip()
	key_words=list(set(key_words))
	key_words.remove('');
	# print(key_words)
	return key_words



def tata_innoverse_extractor(url):
		print(url)
		
		source_code = requests.get(url) #DKS: verify=False
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,"html.parser")
		data = soup.find_all("div",{"id":"singlechallengedesc"})
		# print(data)
		tot=[] 
		tot_non_imp=[]
		tot_imp=[]
		for i in range(0,len(data)):            
			non_imp=[]
			imp=[]
			everyblock=data[i].find_all(["p","li"])
			for j in range(0,len(everyblock)):
				tot.append(everyblock[j].text.replace(u'\xa0', u' '))
			everyblock=data[i].find_all("li")
			for j in range(0,len(everyblock)):
					tot_imp.append(everyblock[j].text.replace(u'\xa0', u' ') )
			everyblock=data[i].find_all("p")
			for j in range(0,len(everyblock)):
				tot_non_imp.append(everyblock[j].text.replace(u'\xa0', u' '))
		return (tot,tot_imp,tot_non_imp)


def summariser(content):  
	line=""
	for i in content:
	    line=line+i
	return summarize.summarize_text(line)


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


class MainWindow2(QWidget):
	def __init__(self,selected,level):
		QWidget.__init__(self)

		self.setGeometry(300,300,300,220)
		self.selected=selected
		self.level=level
		layout = QVBoxLayout()
		layout1 = QHBoxLayout()
		self.e1 = QLineEdit()
		layout.addWidget(self.e1)
		layout1.addStretch()
		layout.addLayout(layout1)
		self.listWidget = QListWidget()
		self.listWidget.setVisible(True)
		layout.addWidget(self.listWidget)

		self.listWidget.itemClicked.connect(self.Clicked)
		
		j=0;
		str3=''
		str4=''
		self.collect=[]
		self.result=[]
		#####################
		self.result=sk.search_keywords(self.selected,self.level)
		#####################
		for k in self.result:
			# self.collect.append(k)				
			str4=str4+str(k[3])
			temp1 =QListWidgetItem(str(k[3]))
			temp1.setTextColor(QColor('#1a0dab'))
			temp1.setFont(QFont('SansSerif', 14))
			self.listWidget.addItem(temp1)
			temp1 =QListWidgetItem("keywords: "+str(k[0])+" "+str(k[1])+" "+str(k[2]))
			temp1.setTextColor(QColor('#006621'))
			temp1.setFont(QFont('SansSerif', 14))
			self.listWidget.addItem(temp1)




		# for i in self.selected:
		# 	j=(j+1)%3
		# 	str3=str3+str(i)
		# 	if(j==0):
		# 		r=s.search(str3,num_results=20)
		# 		for k in r:
		# 			if( "tata innoverse" in k[0]):
		# 				continue
		# 			self.collect.append(k)				
		# 			str4=str4+str(k[0])
		# 			temp1 =QListWidgetItem(str(k[0]))
		# 			temp1.setTextColor(QColor('#000000'))
		# 			temp1.setFont(QFont('SansSerif', 14))
		# 			self.listWidget.addItem(temp1)
				
		# 		temp1 =QListWidgetItem("keywords: "+str4)
		# 		temp1.setTextColor(QColor('#000000'))
		# 		temp1.setFont(QFont('SansSerif', 14))
		# 		self.listWidget.addItem(temp1)
					



		self.setLayout(layout)
		self.setWindowTitle("Surrogator")
		self.showMaximized()
		self.show()


	def Clicked(self,item):
		index=self.listWidget.currentRow()
		print(index)
		paper=self.listWidget.currentItem().text()

		for i in self.result:
			# print(i)
			if(paper in i[3]):
				try:
					url=i[4]
					print(url)
					webbrowser.open(url)
				except:
					pass			


class MainWindow3(QWidget):
	def __init__(self,selected):
		QWidget.__init__(self)
		self.flo = QFormLayout()

		self.setGeometry(300,300,300,220)
		
		vbox=QVBoxLayout();
		vbox1=QHBoxLayout();
		vbox2=QHBoxLayout();

		self.l1=QLabel();
		self.l2=QLabel();
		self.l3=QLabel();
		self.l4=QLabel();

		self.l0=QLabel()		
		self.l0.setText("Select Level")
		self.l0.setFont(QFont('SansSerif', 30))
		self.l0.setStyleSheet("QLabel { background-color : black; color : white; }");
		self.l0.setFixedHeight(100)
		self.l0.setAlignment(Qt.AlignCenter)
		self.l0.setFixedWidth(500)
		self.flo.addRow(self.l0)

		self.selected=selected
		self.checks=[]
		c = QCheckBox("Easy")
		c.setCheckable(True)
		self.flo.addRow(c)
		
		self.checks.append(c)
		c = QCheckBox("Medium")
		c.setCheckable(True)
		self.flo.addRow(c)
		
		self.checks.append(c)
		c = QCheckBox("Hard")
		c.setCheckable(True)
		self.flo.addRow(c)
		
		self.checks.append(c)
		
		self.b0 = QPushButton("GO")
		self.b0.setFixedWidth(650)
		self.b0.setCheckable(True)
		self.b0.clicked.connect(self.btnstate0)
		self.flo.addRow(self.b0)
		vbox1.addWidget(self.l3);
		vbox2.addWidget(self.l4);		
		vbox.addLayout(vbox1);
		vbox.addLayout(self.flo);
		vbox.addLayout(vbox2);
		hbox1=QHBoxLayout();
		hbox2=QHBoxLayout();
		hbox1.addWidget(self.l1);
		hbox2.addWidget(self.l2);
		oLayout=QHBoxLayout();
		oLayout.addLayout(hbox1);
		oLayout.addLayout(vbox);
		oLayout.addLayout(hbox2);
		vbox1.addStretch();		
		vbox2.addStretch();
		hbox1.addStretch();		
		hbox2.addStretch();
		self.setLayout(oLayout);
		self.showMaximized()
		self.show()

	def btnstate0(self):
		
		self.level=0
		j=1
		for i in self.checks:
			if(i.isChecked()):
				self.level=j
				j=j+1

		print(self.level)		

		self.dialog =  MainWindow2(self.selected,self.level)
		self.dialog.show()
		self.close()
		print ("Button 1 clicked")	



class MainWindow1(QWidget):
	def __init__(self,tot,tot_imp,tot_non_imp):
		QWidget.__init__(self)

		self.setGeometry(300,300,300,220)
		self.tot=tot
		self.tot_imp=tot_imp
		self.tot_non_imp=tot_non_imp
		oLayout = QVBoxLayout()
		vbox1=QVBoxLayout()
		vbox2=QHBoxLayout()
		hbox1=QVBoxLayout()
		hbox2=QVBoxLayout()	
		hbox=QHBoxLayout()
		self.e0=QTextEdit()
		self.e0.setReadOnly(True)


		###############################		
		# self.e0.textCursor().insertHtml('<b>bold text</b>')
		# with open('a.txt', 'r') as myfile:
		# 	data=myfile.read().replace('\n', '')
		# 	self.e0.append(data);
		# self.e0.append("\n")
		###############################
		for i in self.tot:
			self.e0.append(i);
		###############################		


		self.e0.verticalScrollBar().minimum()
		self.e1=QTextEdit()
		self.e1.setReadOnly(True)


		###############################
		# self.e1.textCursor().insertHtml('<b>bold text</b>')
		# self.e1.append("apple");		
		###############################
		self.e1.append(str(summariser(self.tot)).replace('None - None\n',''))
		###############################
		self.e1.verticalScrollBar().minimum()		

		self.e2 = QLineEdit()
		hbox1.addWidget(self.e0)
		hbox1.addWidget(self.e1)
		
		self.b0 = QPushButton("GO")
		self.b0.setFixedWidth(650)
		self.b0.setCheckable(True)
		self.b0.clicked.connect(self.btnstate0)

		###############################
		self.imp=''
		self.checks = []
		for i in self.tot_imp:
			self.imp=self.imp+i
			# temp=key_words(i)
			# print(temp)
			# if not temp:
			# 	print("1")
			# else:	
			# 	print("2")
			# 	# self.checks=self.checks+temp
				# print(temp)
		
		print("@@@")
		print(self.imp)		
		temp=key_words(self.imp)
		print(temp)
		if not temp:
				print("1")
		else:
			self.checks=self.checks+temp
		print("##")
		print(self.checks)		


		self.checks=list(set(self.checks))

		# self.keys=[]
		# for i in self.checks:
		# 	c = QCheckBox(i)
		# 	c.setCheckable(True)
		# 	hbox2.addWidget(c)
		# 	self.keys.append(c)



		# self.non_imp=''
		# # self.checks = []
		# for i in self.tot_non_imp:
		# 	self.non_imp=self.non_imp+i
		# 	temp=key_words(i)
		# 	# print(temp)
		# 	if not temp:
		# 		print("1")
		# 	else:	
		# 		# self.checks.append(temp)
		# 		print("2")
		# 		self.checks=self.checks+temp
		# 		print(temp)
		
		# print("@@@")
		# print(self.non_imp)		
		# temp=key_words(self.non_imp)
		# print(temp)
		# if not temp:
		# 		print("1")
		# else:
		# 	self.checks=self.checks+temp
		# print("##")
		# print(self.checks)		


		self.checks=list(set(self.checks))

		# # self.keys=[]
		# for i in self.checks:
		# 	c = QCheckBox(i)
		# 	c.setCheckable(True)
		# 	hbox2.addWidget(c)
		# 	self.keys.append(c)	
		######################################################

		# self.checks=['tool/application','keyword list','relevance','web.the information','tata innoverse.com','challenge uploaded',
		# 'keyword extraction algorithm']
		# self.keys=[]
		####################################################
		# rlist=[]

		# for k in self.checks:
		# 	for j in self.checks:
		# 		if (k in j and k !=j):
		# 			rlist.append(k)

		# for k in rlist:
		# 	self.checks.remove(k)			

		self.keys=[]
		for i in self.checks:
			c = QCheckBox(i)
			c.setCheckable(True)
			hbox2.addWidget(c)
			self.keys.append(c)
		
		hbox2.addWidget(self.e2)
		hbox2.addWidget(self.b0)
		mygroupbox =QGroupBox('this is my groupbox')
		mygroupbox.setLayout(hbox2)
		scroll = QScrollArea()
		scroll.setWidget(mygroupbox)
		scroll.setWidgetResizable(True)
		scroll.setFixedHeight(700)
		lay = QVBoxLayout()
		lay.addWidget(scroll)
		vbox2.addLayout(hbox1)
		vbox2.addLayout(lay)
		self.setLayout(vbox2);
		self.showMaximized()
		self.show()


	def btnstate0(self):
		
		others= self.e2.text()
		oth=[]
		self.selected=[]
		if(others!=''):
			oth=others.split(":")	
			self.selected.append(oth)

		for i in self.keys:
			if(i.isChecked()==False):
				self.selected.append(i.text())
		print(self.selected)		
		self.dialog =  MainWindow3(self.selected)
		self.dialog.show()
		self.close()
		print ("Button 1 clicked") 


class MainWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.setGeometry(300,300,300,220)
		
		self.l0=QLabel()		
		self.l0.setText("Solution Hunt")
		self.l0.setFont(QFont('SansSerif', 30))
		self.l0.setStyleSheet("QLabel { background-color : black; color : white; }");
		self.l0.setFixedHeight(100)
		self.l0.setAlignment(Qt.AlignCenter)
		self.l0.setFixedWidth(500)
		
		self.e1 = QLineEdit()
		self.e1.setFont(QFont("Arial",20))
		self.e1.setFixedWidth(500)
		
		self.e2 = QLineEdit()
		self.e2.setFont(QFont("Arial",20))
		self.e2.setFixedWidth(250)
		
		self.b0 = QPushButton("GO")
		self.b0.setFixedWidth(250)
		self.b0.setCheckable(True)
		self.b0.clicked.connect(self.btnstate0)	
	

		self.flo = QFormLayout()
		self.flo.addRow(self.l0)
		self.flo.addRow(self.e1)
		self.flo.addRow(self.e2, self.b0)


		self.l1=QLabel();
		self.l2=QLabel();	


		self.l4=QLabel();
		self.l3=QLabel();	
		
		self.l1.setScaledContents(True)
		self.l3.setScaledContents(True)
		
		vbox=QVBoxLayout();
		vbox1=QHBoxLayout();
		vbox2=QHBoxLayout();

		vbox1.addWidget(self.l3);
		vbox2.addWidget(self.l4);
		
		vbox.addLayout(vbox1);
		vbox.addLayout(self.flo);
		vbox.addLayout(vbox2);

		hbox1=QHBoxLayout();
		hbox2=QHBoxLayout();
		hbox1.addWidget(self.l1);
		hbox2.addWidget(self.l2);

		oLayout=QHBoxLayout();
		oLayout.addLayout(hbox1);
		oLayout.addLayout(vbox);
		oLayout.addLayout(hbox2);
		vbox1.addStretch();		
		vbox2.addStretch();
		hbox1.addStretch();		
		hbox2.addStretch();
		self.setLayout(oLayout);
		self.showMaximized()		
		self.show()


	


	def btnstate0(self):
		
		test_link="http://www.tatainnoverse.com/tatacruciblehackathon/challenge.php?id="
		link=self.e1.text()
		num=self.e2.text()
		print(link)
		print(num)

		if(test_link in link or  RepresentsInt(num)):

			if(link!=''):
				print(link[int(link.find("=")+1):])
			else:
				link=test_link+num
			######################################################	
			self.tot=''
			self.tot_imp=''
			self.tot_non_imp=''
			######################################################	
			(self.tot,self.tot_imp,self.tot_non_imp)=tata_innoverse_extractor(link)	
			######################################################
			print(self.tot,self.tot_imp,self.tot_non_imp)
			self.dialog =  MainWindow1(self.tot,self.tot_imp,self.tot_non_imp)
			self.dialog.show()	
			self.close()			
		else:
			QMessageBox.question(self, 'Message - warning', "link not from TATA innoverse", QMessageBox.Ok, QMessageBox.Ok)
		
		print ("Button 0 clicked") 



def main():
	app = QApplication(sys.argv)
	oMainwindow = MainWindow()
	sys.exit(app.exec_())		

if __name__ == '__main__':
	if sys.version[0] == '2':
		reload(sys)
		sys.setdefaultencoding("utf-8")
	main()









# import sys
# from PyQt4.QtGui import *
# from PyQt4.QtCore import *

# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)

#         layout = QVBoxLayout()
#         self.checks = []
#         for i in xrange(5):
#             c = QCheckBox("Option %i" % i)
#             layout.addWidget(c)
#             self.checks.append(c)

#         self.setLayout(layout)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     w = Window()
#     w.show()

#     app.exec_()


