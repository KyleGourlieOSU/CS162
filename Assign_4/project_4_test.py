
from PySide6 import QtWidgets
from project_4 import Timecard_Win

app = QtWidgets.QApplication([])
win =  Timecard_Win()

def test_default_vals():
    """tests the default value types of all inputs"""

    assert type(win._num) == str
    assert type(win._name) == str
    assert type(win._day) == str
    assert type(win._date) == str

    assert type(win.job_1_num) == str
    assert type(win.job_2_num) == str
    assert type(win.job_3_num) == str
    assert type(win.job_4_num) == str
    assert type(win.job_5_num) == str

    assert type(win.job_1_phase) == str
    assert type(win.job_2_phase) == str
    assert type(win.job_3_phase) == str
    assert type(win.job_4_phase) == str
    assert type(win.job_5_phase) == str

    assert type(win.job_1_loc) == str
    assert type(win.job_2_loc) == str
    assert type(win.job_3_loc) == str
    assert type(win.job_4_loc) == str
    assert type(win.job_5_loc) == str

    assert type(win.job_1_descr) == str
    assert type(win.job_2_descr) == str
    assert type(win.job_3_descr) == str
    assert type(win.job_4_descr) == str
    assert type(win.job_5_descr) == str

def test_box_pos():
    """Tests the expected geometries of each job box"""
    exp_geo_intit = (100,350,72,50)
    val = exp_geo_intit[1]
    exp_geo = []
    for i in range(5):
        exp_geo.append((exp_geo_intit[0],val,exp_geo_intit[2],exp_geo_intit[3]))
        val = val + 50

    #gets actual geometry for the 5 job boxes and stores them as tuples
    act_geo_pyqt_1 = win.job_1_box.geometry()
    act_geo_1 = (act_geo_pyqt_1.x(), act_geo_pyqt_1.y(), act_geo_pyqt_1.width(), act_geo_pyqt_1.height())
    
    act_geo_pyqt_2 = win.job_2_box.geometry()
    act_geo_2 = (act_geo_pyqt_2.x(), act_geo_pyqt_2.y(), act_geo_pyqt_2.width(), act_geo_pyqt_2.height())

    act_geo_pyqt_3 = win.job_3_box.geometry()
    act_geo_3 = (act_geo_pyqt_3.x(), act_geo_pyqt_3.y(), act_geo_pyqt_3.width(), act_geo_pyqt_3.height())

    act_geo_pyqt_4 = win.job_4_box.geometry()
    act_geo_4 = (act_geo_pyqt_4.x(), act_geo_pyqt_4.y(), act_geo_pyqt_4.width(), act_geo_pyqt_4.height())

    act_geo_pyqt_5 = win.job_5_box.geometry()
    act_geo_5 = (act_geo_pyqt_5.x(), act_geo_pyqt_5.y(), act_geo_pyqt_5.width(), act_geo_pyqt_5.height())

    #stores each actual geometry in a list for easy iteration
    act_geo = [act_geo_1, act_geo_2, act_geo_3, act_geo_4, act_geo_5]

    for i in range(5):
        assert act_geo[i] == exp_geo[i]





    
   