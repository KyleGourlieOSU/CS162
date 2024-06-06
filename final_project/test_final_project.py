import pytest, os, openpyxl, time
from PySide6 import QtCore, QtWidgets, QtGui, QtWidgets
from PySide6.QtWidgets import QTextBrowser
from final_project import Timecard_Win

@pytest.fixture
def app(qtbot):
    """widget for running PyQt test"""
    win = Timecard_Win()
    qtbot.addWidget(win)
    return win

def test_total_time(app):
    """test for checking the correct computation of the total time in multiple correct formats"""
    app.total_time(tst_tm_srt='6am', tst_tm_end='9pm', tst_lnch_start='12pm', tst_lnch_end='1pm')
    actual = app.total.__str__()
    expected = '14:00:00'
    assert actual == expected
    app.total_time(tst_tm_srt='6:00am', tst_tm_end='9:00pm', tst_lnch_start='12:00pm', tst_lnch_end='1:00pm')
    actual = app.total.__str__()
    expected = '14:00:00'
    assert actual == expected
    app.total_time(tst_tm_srt='6:00:00am', tst_tm_end='9:00:00pm', tst_lnch_start='12:00:00pm', tst_lnch_end='1:00:00pm')
    actual = app.total.__str__()
    expected = '14:00:00'
    assert actual == expected

def test_download_pdf(app):
    """test to see if pdf is being downloaded"""
    path_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path =  path_dir + r"\NSP_Timecard.pdf"
    file_exist = os.path.isfile(pdf_path)
    #leftover pdf might exist so lets delete
    if file_exist:
        os.remove(pdf_path)
    
    app.download_pdf()
    assert(os.path.isfile(pdf_path)) 

def test_upload_excel(app):
    """test upload and and reading data of excel"""
    test_name = 'Jeffrey'
    test_num = '8675309'
    test_day = 'Sunday'
    test_date = '9/24/2014'
    test_lnch_srt = '12pm'
    test_lnch_end = '1pm'
    test_tm_srt = '6am'
    test_tm_end = '4pm'
    app._name = test_name
    app._num =test_num
    app._day = test_day
    app._date = test_date
    app.time_start_btn.setText(test_tm_srt)
    app.lunch_start_btn.setText(test_lnch_srt) 
    app.lunch_end_btn.setText(test_lnch_end) 
    app.time_end_btn.setText(test_tm_end)
    app.upload_excel()
    path_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = path_dir + r"\NSP Timecard.xlsx" 
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active
   
    assert ws['C5'].value == app._name
    assert ws['K2'].value == app._num
    assert ws['K3'].value == app._day
    assert ws['K4'].value == app._date 
    assert ws['H27'].value == app.time_start_btn.text() 
    assert ws['I27'].value == app.lunch_start_btn.text()
    assert ws['J27'].value == app.lunch_end_btn.text()
    assert ws['K27'].value == app.time_end_btn.text() 
    
    wb.save(excel_path)