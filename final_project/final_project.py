"""final_project.py --Python script that automates North Santiam Paving Timecard

Summary:
This program's goal is the fully digitalize a physical timecard that one of my family member's currently uses.
Instead of writing out a physical copy, and needed to submit it physically, this program will do it all. The program
will allow the user to input all data required for the timecard. The inputted data required includes name, employee 
number, day, date, clock in time, lunch in time, lunch out time, and clock out time. The total work time will be calculated
automatically by the user selecting the blank button located directly underneath. Once all the data that the user wanted to 
input is completed, they will click the green 'Upload' button. This will in turn take all the data stored in Python and place
it into the specifically formatted Excel Spreadsheet. The next step that the User will want to take is to download the Excel sheet.
This will convert the Excel sheet into a PDF. This is the yellow button labeled 'Download Timesheet'. The last step the user will 
select is 'Send Email'. This will send a copy of the PDF to the designated employer who needs it. To change the recipient, one will
need to locate the method 'send_email'. The variable 'receiver' chooses the email address. The variable 'sender' chooses where the
email is being sent to. NOTE: the sender email address must be a gmail account. The gmail account requires the gmail address and gmail
password. This gmail password is NOT the normal gmail password, but the 'app password'. To access this password, two-factor authentication
must be ON within the sender's gmail address. You will need to create an App Password, and use this password within the script. The
ability to send emails through Python using available packages use gmail and this route to have access to the gmail account through Python.
An inputted function of the sender's gmail, password, and reciever's gmail was not implemented due to security purposes. This program is just
for my father, who wants the process as automated as possible. Having him to type his gmail, password, and boss's gmail was undesired by him.

Testing:
There is a testing function called 'test_final_project.py'
"""

#imports
import sys, openpyxl, os, yagmail, smtplib
from PySide6 import QtCore, QtWidgets, QtGui, QtWidgets
from PySide6.QtWidgets import QTextBrowser
from win32com import client
from datetime import timedelta

#important fonts to be used
really_small_font = QtGui.QFont('Times',10)
small_font = QtGui.QFont('Times',12)
small_bold = QtGui.QFont('Times',12, QtGui.QFont.Bold)
large_font = QtGui.QFont('Times',20)
large_bold_font = QtGui.QFont('Times', 20, QtGui.QFont.Bold) 

def box_generator(self, _type: str)-> list:
    """## _summary_: Creates cells for each row of data

    ### Args:
        - `_type (str)`: the label that describes the row of data

    ### Returns:
        - `list`: list of cell objects that are each a PtQt.QPushButton
    """
    #dictionary of types of inputs that need multiple boxes/cells
    type_dict = {'Job #': self.num_job_label,
                    'Phase': self.phase_label,
                    'Job Location': self.job_loc_label,
                    'Job Description': self.job_des_label,
                    'Time Start': self.tm_start_label,
                    'Time Finish': self.tm_end_label,
                    'Hours': self.hrs_label,
                    'Equip. #': self.eqp_num_label} 

    #creates list of boxes for each type based on dimensions of their labels
    if _type in type_dict.keys():
        boxes = [QtWidgets.QPushButton(self) for i in range(8)]
        #initializes the first box for the locations of the rest can be bound to it
        boxes[0].setGeometry(type_dict[_type].x(),type_dict[_type].y()+type_dict[_type].height(),
                                    type_dict[_type].width(),type_dict[_type].height())
        #initializes text, font, style, and geometry
        for i in range(0,len(boxes)):
            #last set of boxes needs to be treated differently
            if i == 7:
                boxes[i].setText('')
                boxes[i].setFont(small_bold)
                boxes[i].setStyleSheet("background-color: white; border: 2px solid black;")
            #all the other boxes are sent here
            else:
                boxes[i].setText('')
                boxes[i].setFont(small_bold)
                boxes[i].setStyleSheet("background-color: white; border: 2px solid black;")
                boxes[i+1].setGeometry(boxes[i].x(),boxes[i].y()+50, boxes[i].width(), boxes[i].height()) 
        return boxes
    #It should NOT be possible to reach this else statement, but I added it to cover all my bases
    else:
        print('Error has occured')
        return None 
    
class Column:
    """## _summary_: Column object that defines each column of data based on label.
    """
    def __init__(self, label: QtWidgets.QLabel, boxes: list):
        self.boxes = boxes
        self.label = label

    def _type_box(self):
        return self.label.text()
    
    #dont need __str__() for this class but kept it to show proper use of classes
    def __str__(self):
        return f"{self.label.text()}"
    
    
class Timecard_Win(QtWidgets.QWidget):
    """## _summary_: Timecard window GUI QWidget object that contains the canvas of the GUI

    ### Args:
        - `QtWidgets (_type_)`: Parent class of the canvas. 
        Timecard_Win is inheriting the properties and attributes of QtWidgets.QWidget
    """
    def __init__(self):
        #parent constructor that is making Timecard_Win inherit all properties and attributes of QtWidgets.QWidget
        #this is where all the main functions for the GUI are ran at.
        super(Timecard_Win,self).__init__()
        self.setWindowTitle("North Santiam Paving Timesheet")
        self.main_timecard()
        self.lunch()
        self.terminal()
        
    def entry(self, row: int, col: Column):
        """## _summary_: Method that allows the user to enter all column data

        ### Args:
            - `row (int)`: index of the row
            - `col (column)`: index of the column
        """
        #ties all labels to corresponding types, that way column method _type_box() can be used
        type_dict = {'Job #': self.num_job_label,
                    'Phase': self.phase_label,
                    'Job Location': self.job_loc_label,
                    'Job Description': self.job_des_label,
                    'Time Start': self.tm_start_label,
                    'Time Finish': self.tm_end_label,
                    'Hours': self.hrs_label,
                    'Equip. #': self.eqp_num_label} 
        _type = col._type_box()
        if _type in type_dict.keys():
            entrance, done = QtWidgets.QInputDialog.getText(self, _type, f"Enter {_type}: ")
            col.boxes[row].setText(f'{entrance}')
        #This else statement should not be able to be accessed, but included to cover all my bases
        else:
            print(f'NOT recognizing {_type}')

    def main_timecard(self):
        """This method contains all the main visual pieces of the GUI"""
        
        #main title for the timesheet
        self.title_1 = QtWidgets.QLabel(self)
        self.title_1.setText("North Santiam Paving Company")
        self.title_1.setFont(small_bold)
        self.title_1.setGeometry(100,20,250,50)

        #Sub-title for the timesheet
        self.title_2 = QtWidgets.QLabel(self)
        self.title_2.setText("Daily Time Card")
        self.title_2.setFont(large_bold_font)
        self.title_2.setStyleSheet("font-style: italic;")
        self.title_2.setGeometry(110,60,250,30)

        #name of employee label
        self._name=''
        self.name_label = QtWidgets.QLabel(self)
        self.name_label.setText('Name:')
        self.name_label.setFont(small_font)
        self.name_label.move(1200,25)
        self.name_label.adjustSize()

        #name of employee button
        self.name = QtWidgets.QPushButton(self)
        self.name.setText(f"{self._name}")
        self.name.setFont(small_font)
        self.name.setStyleSheet("background-color: white;")
        self.name.setGeometry(self.name_label.x()+50,25,150,20)
        self.name.clicked.connect(self.name_update)

        #timecard employee number label
        self.num_label = QtWidgets.QLabel(self)
        self.num_label.setText("No:")
        self.num_label.setFont(small_font)
        self.num_label.move(self.name.x()+30,self.name_label.y()+25)
        self.num_label.adjustSize()

        #timecard employee number button
        self._num = ''
        self.num = QtWidgets.QPushButton(self)
        self.num.setText(f'{self._num}')
        self.num.setFont(small_font)
        self.num.setStyleSheet("background-color: white;")
        self.num.setGeometry(self.name_label.x()+120,self.num_label.y(),80,20)
        self.num.clicked.connect(self.num_update)

        #timecard  employee Day label
        self.day_label = QtWidgets.QLabel(self)
        self.day_label.setText('Day:')
        self.day_label.setFont(small_font)
        self.day_label.move(self.name_label.x()+80,self.num.y()+25)
        self.day_label.adjustSize()

        #timecard emplyee Day button
        self._day=''
        self.day = QtWidgets.QPushButton(self)
        self.day.setText(f"{self._day}")
        self.day.setFont(small_font)
        self.day.setStyleSheet("background-color: white;")
        self.day.setGeometry(self.name_label.x()+120,self.day_label.y(),80,20)
        self.day.clicked.connect(self.day_update)

        #timecard Employee Date label
        self.date_label = QtWidgets.QLabel(self)
        self.date_label.setText('Date:')
        self.date_label.setFont(small_font)
        self.date_label.move(self.day_label.x(),self.day_label.y()+25)
        self.date_label.adjustSize()

        #timecard Employee Date Button
        self._date=''
        self.date = QtWidgets.QPushButton(self)
        self.date.setText(f'{self._date}')
        self.date.setFont(small_font)
        self.date.setStyleSheet("background-color: white;")
        self.date.setGeometry(self.day.x(),self.date_label.y(),80,20)
        self.date.clicked.connect(self.date_update)

        #upload button
        self.upload = QtWidgets.QPushButton(self)
        self.upload.setText('Upload Timesheet')
        self.upload.setFont(large_bold_font)
        self.upload.setStyleSheet("background-color: lime;")
        self.upload.setGeometry(1180,140,300,75)
        self.upload.clicked.connect(self.upload_excel)

        #download button
        self.download = QtWidgets.QPushButton(self)
        self.download.setText('Download Timesheet')
        self.download.setFont(large_bold_font)
        self.download.setStyleSheet("background-color: yellow;")
        self.download.setGeometry(self.upload.x(),self.upload.y()+self.upload.height(),300,75)
        self.download.clicked.connect(self.download_pdf)

        #email send button
        self.send = QtWidgets.QPushButton(self)
        self.send.setText('Email Send')
        self.send.setFont(large_bold_font)
        self.send.setStyleSheet("background-color: red;")
        self.send.setGeometry(self.download.x(),self.download.y()+self.download.height(),300,75)
        self.send.clicked.connect(self.send_email)

        #Job # label
        self.num_job_label = QtWidgets.QLabel(self)
        self.num_job_label.setText('Job #')
        self.num_job_label.setFont(small_bold)
        self.num_job_label.setAlignment(QtCore.Qt.AlignCenter)
        self.num_job_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.num_job_label.setGeometry(100,100,75,50)

        #phase of job label
        self.phase_label = QtWidgets.QLabel(self)
        self.phase_label.setText('Phase')
        self.phase_label.setFont(small_bold)
        self.phase_label.setAlignment(QtCore.Qt.AlignCenter)
        self.phase_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.phase_label.setGeometry(self.num_job_label.x()+self.num_job_label.width(),self.num_job_label.y(),
                                     self.num_job_label.width(), self.num_job_label.height())
        
        #job location label
        self.job_loc_label = QtWidgets.QLabel(self)
        self.job_loc_label.setText('Job Location')
        self.job_loc_label.setFont(small_bold)
        self.job_loc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.job_loc_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.job_loc_label.setGeometry(self.phase_label.x()+self.phase_label.width(),self.num_job_label.y(),
                                 120,self.num_job_label.height())

        #job description label
        self.job_des_label = QtWidgets.QLabel(self)
        self.job_des_label.setText('Job Description')
        self.job_des_label.setFont(small_bold)
        self.job_des_label.setAlignment(QtCore.Qt.AlignCenter)
        self.job_des_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.job_des_label.setGeometry(self.job_loc_label.x()+self.job_loc_label.width(),self.num_job_label.y(),
                                 200,self.num_job_label.height())

        #blank spot to divide timesheet
        self.blank_spot_1 = QtWidgets.QLabel(self)
        self.blank_spot_1.setStyleSheet("background-color: black;")
        self.blank_spot_1.setGeometry(self.job_des_label.x()+self.job_des_label.width(),self.num_job_label.y(),
                                      60,9*50)

        #Time start label
        self.tm_start_label = QtWidgets.QLabel(self)
        self.tm_start_label.setText('Time Start')
        self.tm_start_label.setFont(small_bold)
        self.tm_start_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tm_start_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.tm_start_label.setGeometry(self.blank_spot_1.x()+self.blank_spot_1.width(),self.num_job_label.y(),
                                  120,50)

        #Time finish label
        self.tm_end_label = QtWidgets.QLabel(self)
        self.tm_end_label.setText('Time Finish')
        self.tm_end_label.setFont(small_bold)
        self.tm_end_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tm_end_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.tm_end_label.setGeometry(self.tm_start_label.x()+self.tm_start_label.width(),self.num_job_label.y(),
                                self.tm_start_label.width(),self.tm_start_label.height())

        #Hours label
        self.hrs_label = QtWidgets.QLabel(self)
        self.hrs_label.setText('Hours')
        self.hrs_label.setFont(small_bold)
        self.hrs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hrs_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.hrs_label.setGeometry(self.tm_end_label.x()+self.tm_end_label.width(),self.num_job_label.y(),
                             self.tm_start_label.width(),self.tm_start_label.height())

        #Equipment Number label
        self.eqp_num_label = QtWidgets.QLabel(self)
        self.eqp_num_label.setText('Equip. #')
        self.eqp_num_label.setFont(small_bold)
        self.eqp_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.eqp_num_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.eqp_num_label.setGeometry(self.hrs_label.x()+self.hrs_label.width(),self.num_job_label.y(),
                                 self.tm_start_label.width(),self.tm_start_label.height())
        
        #all boxes needed
        self.job_boxes = box_generator(self, _type='Job #')
        self.phase_boxes = box_generator(self, _type='Phase')
        self.job_loc_boxes = box_generator(self, _type='Job Location')
        self.job_descrpt_boxes = box_generator(self, _type='Job Description')
        self.time_start_boxes = box_generator(self, 'Time Start')
        self.time_end_boxes = box_generator(self, 'Time Finish')
        self.hrs_boxes = box_generator(self, 'Hours')
        self.equip_num_boxes = box_generator(self, 'Equip. #')

        #all columns needed
        self.job_num_col = Column(label=self.num_job_label, boxes=self.job_boxes)
        self.phase_col = Column(label=self.phase_label, boxes=self.phase_boxes)
        self.job_loc_col = Column(label=self.job_loc_label, boxes=self.job_loc_boxes)
        self.job_descpt_col = Column(label=self.job_des_label, boxes=self.job_descrpt_boxes)
        self.time_start_col = Column(label=self.tm_start_label, boxes=self.time_start_boxes)
        self.time_end_col = Column(label=self.tm_end_label, boxes=self.time_end_boxes)
        self.hrs_col = Column(label=self.hrs_label, boxes=self.hrs_boxes)
        self.equip_num_col = Column(label=self.eqp_num_label, boxes=self.equip_num_boxes)

        #setting functions for each button so if pressed, goes to correct function call
        for i in range(8):
            self.job_boxes[i].clicked.connect(lambda row=i, col=self.job_num_col: self.entry(row, col))
            self.phase_boxes[i].clicked.connect(lambda row=i, col=self.phase_col: self.entry(row, col))
            self.job_loc_boxes[i].clicked.connect(lambda row=i, col=self.job_loc_col: self.entry(row, col))
            self.job_descrpt_boxes[i].clicked.connect(lambda row=i, col=self.job_descpt_col: self.entry(row, col))
            self.time_start_boxes[i].clicked.connect(lambda row=i, col=self.time_start_col: self.entry(row, col))
            self.time_end_boxes[i].clicked.connect(lambda row=i, col=self.time_end_col: self.entry(row, col))
            self.hrs_boxes[i].clicked.connect(lambda row=i, col=self.hrs_col: self.entry(row, col))
            self.equip_num_boxes[i].clicked.connect(lambda row=i, col=self.equip_num_col: self.entry(row, col))

    def lunch(self):
        """This method handles all components underneath the lunch label on the timesheet"""
        #lunch label
        self.lunch_label = QtWidgets.QLabel(self)
        self.lunch_label.setText('Lunch')
        self.lunch_label.setFont(small_bold)
        self.lunch_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lunch_label.setGeometry(self.blank_spot_1.x(),self.blank_spot_1.y()+self.blank_spot_1.height()+50,50,25)

        #lunch end label
        #note the weird order of the labels due to all their positions tied to the lunch label for centering purposes
        self.lunch_end_label = QtWidgets.QLabel(self)
        self.lunch_end_label.setText('End')
        self.lunch_end_label.setFont(small_bold)
        self.lunch_end_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lunch_end_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.lunch_end_label.setGeometry(self.lunch_label.x()-50, self.lunch_label.y()+self.lunch_label.height(),
                                         self.tm_start_label.width(),self.tm_start_label.height())
        
        #lunch end button
        self.lunch_end_btn = QtWidgets.QPushButton(self)
        self.lunch_end_btn.setText('')
        self.lunch_end_btn.setFont(small_bold)
        self.lunch_end_btn.setStyleSheet("background-color: white; border: 2px solid black;")
        self.lunch_end_btn.setGeometry(self.lunch_end_label.x(), self.lunch_end_label.y()+
                                            self.lunch_end_label.height(), self.tm_start_label.width(),
                                            self.tm_start_label.height())
        self.lunch_end_btn.clicked.connect(self.lunch_end_update)
        
        #lunch start label
        self.lunch_start_label = QtWidgets.QLabel(self)
        self.lunch_start_label.setText('Start')
        self.lunch_start_label.setFont(small_bold)
        self.lunch_start_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lunch_start_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.lunch_start_label.setGeometry(self.lunch_end_label.x()-self.tm_start_label.width(),
                                           self.lunch_label.y()+self.lunch_label.height(),
                                           self.tm_start_label.width(),self.tm_start_label.height())
        
        #lunch start button
        self.lunch_start_btn = QtWidgets.QPushButton(self)
        self.lunch_start_btn.setText('')
        self.lunch_start_btn.setFont(small_bold)
        self.lunch_start_btn.setStyleSheet("background-color: white; border: 2px solid black;")
        self.lunch_start_btn.setGeometry(self.lunch_start_label.x(), self.lunch_start_label.y()+
                                            self.lunch_start_label.height(), self.tm_start_label.width(),
                                            self.tm_start_label.height())
        self.lunch_start_btn.clicked.connect(self.lunch_start_update)
        
        #lunch time start label
        self.lunch_tm_start_label = QtWidgets.QLabel(self)
        self.lunch_tm_start_label.setText('Time Start')
        self.lunch_tm_start_label.setFont(small_bold)
        self.lunch_tm_start_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lunch_tm_start_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.lunch_tm_start_label.setGeometry(self.lunch_start_label.x()-self.lunch_start_label.width(),
                                              self.lunch_start_label.y(),
                                              self.tm_start_label.width(),self.tm_start_label.height())
        
        #lunch time start button
        self.time_start_btn = QtWidgets.QPushButton(self)
        self.time_start_btn.setText('')
        self.time_start_btn.setFont(small_bold)
        self.time_start_btn.setStyleSheet("background-color: white; border: 2px solid black;")
        self.time_start_btn.setGeometry(self.lunch_tm_start_label.x(), self.lunch_tm_start_label.y()+
                                            self.lunch_tm_start_label.height(), self.tm_start_label.width(),
                                            self.tm_start_label.height())
        self.time_start_btn.clicked.connect(self.lunch_tm_start_update)
        
        #lunch finish label
        self.lunch_tm_end_label = QtWidgets.QLabel(self)
        self.lunch_tm_end_label.setText('Time Finish')
        self.lunch_tm_end_label.setFont(small_bold)
        self.lunch_tm_end_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lunch_tm_end_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.lunch_tm_end_label.setGeometry(self.lunch_end_label.x()+self.lunch_end_label.width(), self.lunch_end_label.y(),
                                            self.tm_start_label.width(),self.tm_start_label.height())
        
        #lunch finish button
        self.time_end_btn = QtWidgets.QPushButton(self)
        self.time_end_btn.setText('')
        self.time_end_btn.setFont(small_bold)
        self.time_end_btn.setStyleSheet("background-color: white; border: 2px solid black;")
        self.time_end_btn.setGeometry(self.lunch_tm_end_label.x(), self.lunch_tm_end_label.y()+
                                            self.lunch_tm_end_label.height(), self.tm_end_label.width(),
                                            self.tm_end_label.height())
        self.time_end_btn.clicked.connect(self.lunch_tm_end_update)
        
        #total time label
        self.lunch_tt_label = QtWidgets.QLabel(self)
        self.lunch_tt_label.setText('Total Time')
        self.lunch_tt_label.setFont(small_bold)
        self.lunch_tt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lunch_tt_label.setStyleSheet("background-color: yellow; border: 2px solid black;")
        self.lunch_tt_label.setGeometry(self.lunch_tm_end_label.x()+self.lunch_tm_end_label.width(), self.lunch_end_label.y(),
                                        self.tm_start_label.width(),self.tm_start_label.height())
        
        #total time button
        self.tt_label_btn = QtWidgets.QPushButton(self)
        self.tt_label_btn.setText('')
        self.tt_label_btn.setFont(small_bold)
        self.tt_label_btn.setStyleSheet("background-color: white; border: 2px solid black;")
        self.tt_label_btn.setGeometry(self.lunch_tt_label.x(), self.lunch_tt_label.y()+
                                            self.lunch_tt_label.height(), self.lunch_tt_label.width(),
                                            self.lunch_tt_label.height())
        self.tt_label_btn.clicked.connect(self.total_time)

    def terminal(self):
        """Method creates a GUI for the terminal so user can see direct text response to ensure correct running"""
        self.text_browser = QTextBrowser(self)  #creates text browser
        self.text_browser.setGeometry(QtCore.QRect(self.send.x(),self.send.y()+self.send.height(),
                                                   self.send.width(),400))
        self.text_browser.setStyleSheet("border: 5px solid black;""background-color : pink")
        self.text_browser.setFont(really_small_font)  #did 12 pt font so you can see the text, but doesn't take up all the space
        sys.stdout = self  #ties python script output terminal to textbrowser
        sys.stderr = self  #ties python script exception outputs to the textbrowser
    def write(self, text):
        """writes text to terminal QTextBrowser"""
        self.text_browser.insertPlainText(text)  

    def name_update(self):
        """Mini-GUI that takes User Input for Name of employee"""
        self._name, done1 = QtWidgets.QInputDialog.getText(self, "Name", 
        "Enter Name: ")
        self.name.setText(f"{self._name}")

    def name_update(self):
        """Mini-GUI that takes User Input for Name of employee"""
        self._name, done1 = QtWidgets.QInputDialog.getText(self, "Name", 
        "Enter Name: ")
        self.name.setText(f"{self._name}")

    def num_update(self):
        """Mini-GUI that taker User Input for Employee number"""
        self._num, done1 = QtWidgets.QInputDialog.getText(self, "No", 
        "Enter Employee Number: ")
        self.num.setText(f"{self._num}")

    def day_update(self):
        """Mini-GUI that takes User Input for entry of day"""
        self._day, done1 = QtWidgets.QInputDialog.getText(self, "Day", 
        "Enter Day: ")
        self.day.setText(f"{self._day}")

    def date_update(self):
        """Mini-GUI that takes User Input for entry of data"""
        self._date, done1 = QtWidgets.QInputDialog.getText(self, "Date", 
        "Enter Date: ")
        self.date.setText(f"{self._date}")

    def lunch_tm_start_update(self):
        """Mini-GUI that takes User Input for Time Start"""
        self.tm_srt, done1 = QtWidgets.QInputDialog.getText(self, "Time Start", 
        "Enter Time Start: ")
        self.time_start_btn.setText(f"{self.tm_srt}")

    def lunch_end_update(self):
        """Mini-GUI that takes User Input for Lunch End"""
        self._lnch_end, done1 = QtWidgets.QInputDialog.getText(self, "Lunch End", 
        "Enter End: ")
        self.lunch_end_btn.setText(f"{self._lnch_end}")

    def lunch_start_update(self):
        """Mini-GUI that takes User Input for Lunch Start"""
        self._lnch_start, done1 = QtWidgets.QInputDialog.getText(self, "Lunch Start", 
        "Enter Start: ")
        self.lunch_start_btn.setText(f"{self._lnch_start}")

    def lunch_tm_end_update(self):
        """Mini-GUI that takes User Input for Time Finish"""
        self.tm_end, done1 = QtWidgets.QInputDialog.getText(self, "Time Finish", 
            "Enter Time Finish: ")
        self.time_end_btn.setText(f"{self.tm_end}")

    def total_time(self, tst_tm_srt=None, tst_tm_end=None, tst_lnch_start=None, tst_lnch_end=None):
        """Computes the total time spent at work based on user inputs and correctly formatted times"""
        try:
            if tst_tm_srt == None and tst_tm_end == None and tst_lnch_start == None and tst_lnch_end == None:
                times = [self.tm_srt.lower(), self.tm_end.lower(), self._lnch_start.lower(), self._lnch_end.lower()]
            else:
                #for testing purposes
                times = [tst_tm_srt, tst_tm_end, tst_lnch_start, tst_lnch_end]
            #corrected times
            new_times = []   
            """will use the length of list to determine where it is getting stuck at
            len==1-> self.tm_srt
            len==2-> self.tm_end
            len==3-> self._lnch_start
            len==4-> self._lnch_end"""
            #list used to determine which time is being formatted
            test_times= []

            for time_ in times:
                #basically behaves as counter
                test_times.append('X')
                #removes whitespace
                time_cleaned = time_.replace(" ", "")
                #splits time into hr, min, and sec
                time_parts = time_cleaned.split(':')

                if 'am' in time_cleaned or 'pm' in time_cleaned:
                    #grabbing am_pm part
                    am_pm = time_cleaned[-2:]
                    #grabbing actual numerical values
                    time_cleaned = time_cleaned[:-2]
                    time_parts = time_cleaned.split(':')
                    
                    hr = int(time_parts[0])
                    #if len greater than 1, second part is min. If user only entered hr, then set to 0
                    min_ = int(time_parts[1]) if len(time_parts) > 1 else 0
                    #if len not 3, third part if sec. If user only entered hr, or hr and min, then set to 0
                    sec = int(time_parts[2]) if len(time_parts) == 3 else 0
                    #conversion to military time
                    if am_pm == 'pm' and hr != 12:
                        hr += 12
                    elif am_pm == 'am' and hr == 12:
                        hr = 0
                else:
                    # Process military time
                    hr = int(time_parts[0])
                    min_ = int(time_parts[1]) if len(time_parts) > 1 else 0
                    sec = int(time_parts[2]) if len(time_parts) == 3 else 0
                #creates timedelta objec to compute time difference
                time_obj = timedelta(hours=hr, minutes=min_, seconds=sec)
                new_times.append(time_obj)
            #takes differences
            delta_dy = new_times[1] - new_times[0]
            delta_lnc = new_times[3] - new_times[2]
            self.total = delta_dy - delta_lnc
            self.tt_label_btn.setText(f'{self.total}')

        except AttributeError as ae:
            self.check_time_attributes(ae)

        except ValueError as ve:
            self.check_time_types(ve,test_times)
     
    def check_time_attributes(self, ae):
        """Method to check which attributes have been entered for time calculating"""
        bools = [hasattr(self, 'tm_srt'),hasattr(self, 'tm_end'),hasattr(self, '_lnch_start'),hasattr(self, '_lnch_end')]
        vals = ['time start', 'time end', 'lunch time start', 'lunch time end']
        #basically a mask
        no_attris = [val for val, flag in zip(vals, bools) if not flag]
        print('The following attributes are missing:\n')
        for sentence in no_attris:
            print(f'--{sentence}')
        print(f'\nError:\n{ae}')

    def check_time_types(self, ve:str, test_times:list):
        """Method to check which time entries are not correctly formatted"""
        bad_list = [self.tm_srt,self.tm_end,self._lnch_start,self._lnch_end]
        #len==1-> self.tm_srt
        #len==2-> self.tm_end
        #len==3-> self._lnch_start
        #len==4-> self._lnch_end
        print('The following quantity is NOT in correct format:')
        print(f'\n--\'{bad_list[len(test_times)-1]}\'\n')
        print('Note that for time entries, only \'am\', \'pm\', or military time is allowed.')
        print('Please format entries as HH:MM:SS am/pm')
        print(f'\nError:\n{ve}')

    def upload_excel(self):
        """Method that uploads all data onto Excel"""
        print('Uploading to Excel...')   
        self.xlsx_path = 'NSP Timecard.xlsx'
        try:
            wb = openpyxl.load_workbook(self.xlsx_path)# Load excel file
            ws = wb.active #Declare the worksheet as active so it can be edited
            ws['C5'] = self._name #saving name
            ws['K2'] = self._num #saving employee number
            ws['K3'] = self._day #saving day
            ws['K4'] = self._date #saving date
            ws['H27'] = self.time_start_btn.text() #saving start time of work
            ws['I27'] = self.lunch_start_btn.text() #saving start lunch 
            ws['J27'] = self.lunch_end_btn.text() #saving lunch end 
            ws['K27'] = self.time_end_btn.text()  #saving end of work
            ws['L27'] = self.tt_label_btn.text()  #saving total time in HH:MM:SS format

            #Just for fun
            colA = chr(65)
            colB = chr(66)
            colC = chr(67)
            colD = chr(68)
            colI = chr(73)
            colJ = chr(74)
            colK = chr(75)
            colL = chr(76)

            #Loop that stores data in proper cells within Excel sheet.
            for i in range(1,9):
                row = 7 + 2*int(i)
                ws[colA + str(row)] = self.job_boxes[i-1].text() 
                ws[colB + str(row)] = self.phase_boxes[i-1].text() 
                ws[colC + str(row)] = self.job_loc_boxes[i-1].text()
                ws[colD + str(row)] = self.job_descrpt_boxes[i-1].text()
                ws[colI + str(row)] = self.time_start_boxes[i-1].text() 
                ws[colJ + str(row)] = self.time_end_boxes[i-1].text() 
                ws[colK + str(row)] = self.hrs_boxes[i-1].text() 
                ws[colL + str(row)] = self.equip_num_boxes[i-1].text()
            
            wb.save(self.xlsx_path)
            print("Upload and data saved!")
        
        except PermissionError as pe:
            print('Program can\'t open the Excel sheet due to file currently being opened.')
            print('Please close the Excel Sheet and try again.')
            print(f'\nError:\n{pe}')

        except FileNotFoundError:
            #error is no longer raised when terminal is changed into directory where Python script is located
            print('Program can\'t find the Excel Sheet')

    def download_pdf(self):
        """Method that downloads the timesheet as a PDF"""
        print("Downloading Excel Sheet to PDF...")
        try:
            path_dir = os.path.dirname(os.path.abspath(__file__))  #directory of the folder from Python script
            pdf_path =  path_dir + r"\NSP_Timecard.pdf"            #PDF path
            excel_path =  path_dir + r"\NSP Timecard.xlsx"         #Excel sheet path
            excel = client.Dispatch("Excel.Application")           #Opening the Excel application in order to edit Excel sheet through COM
            sheets = excel.Workbooks.Open(excel_path)              #Opens workbook
            work_sheets = sheets.Worksheets[0]                     #Takes the first sheet, since there is only 1 in the Excel sheet created
            work_sheets.ExportAsFixedFormat(0, pdf_path)           #exports the PDF
            sheets.Close(False)                                    #closes Excel File
            excel.Quit()                                           #closes the App
            print('Download complete!')
        except AttributeError as ee:
            #forcing it to close because after internet connection is made, must restart program
            print('The API connection between Microsoft Excel is not present.')
            print('Please check to make sure a proper internet connection has been made.')
            print(f'\nError:\n{ee}')
            exit()
    
    def send_email(self):
        try:
            receiver = "enter gmail here"   
            sender = 'j3441759@gmail.com'
            password = 'dgvf yhds rhcq ciri'
            body = "Attached to this email is a PDF version of my NSP Timecard"
            filename = "NSP_Timecard.pdf"
            print('Sending Email...')
            yagmail.register(sender, password)   #needs google app password
            yag = yagmail.SMTP(sender, password)
            yag.send(
                to=receiver,
                subject="Craig Gourlie --NSP Timecard PDF",
                contents=body, 
                attachments=filename)
            print('Email Sent Successfully!')
        except smtplib.SMTPAuthenticationError:
            print('\nsender gmail and/or password is not being processed correctly')
            print('Check the following:')
            print('1)   Gmail and Password is typed correctly')
            print('2)   Password entered is Google Apps Password\n')   

def main(): 
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0])) 
    os.chdir(script_dir)
    app = QtWidgets.QApplication([])        #creates the GUI object
    win =  Timecard_Win()                   #creates the GUI window object
    win.setStyleSheet("background-color: rgb(182, 182, 182); color: black") #background of window
    win.resize(800, 600)                 
    win.show()
    sys.exit(app.exec())                   #will exit the app when pressed X on GUI
        
