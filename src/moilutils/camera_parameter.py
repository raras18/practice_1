import json
import sys
from .resource_icon import *

try:
    from PyQt6 import QtWidgets, QtCore, QtGui
    from .ui_camera_parameter_form_pyqt6 import Ui_Dialog
    pyqt_version = "pyqt6"

except:
    from PyQt5 import QtWidgets, QtCore, QtGui
    from .ui_camera_parameter_form_pyqt5 import Ui_Dialog
    pyqt_version = "pyqt5"


class CameraParametersForm(Ui_Dialog):
    def __init__(self, recent_win, camera_parameter_path):
        super(CameraParametersForm, self).__init__()
        self.recent_win = recent_win
        self.file_parameter = camera_parameter_path
        self.setupUi(self.recent_win)

        self.main_controller = None
        self.camera_name = None
        self.camera_fov = None
        self.sensor_width = None
        self.sensor_height = None
        self.image_height = None
        self.image_width = None
        self.icy = None
        self.icx = None
        self.ratio = None
        self.calibration_ratio = None
        self.parameter_0 = None
        self.parameter_1 = None
        self.parameter_2 = None
        self.parameter_3 = None
        self.parameter_4 = None
        self.parameter_5 = None

        with open(self.file_parameter) as f:
            self.data = json.load(f)

        self.centralwidget.setStyleSheet(style_appearance)
        self.recent_win.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.recent_win.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.update_list_camera()

        self.frame.mouseMoveEvent = self.moveWindow
        self.frame.mousePressEvent = self.mousePressEvent
        self.btn_close.clicked.connect(self.recent_win.close)
        self.list_camera.currentIndexChanged.connect(self.handle_combo_box)
        self.btn_open_file.clicked.connect(self.add_new_parameter_from_file)
        self.btn_save.clicked.connect(self.save_parameter_from_ui)
        self.btn_clean_all.clicked.connect(self.clean_parameter_in_ui)
        self.btn_delete.clicked.connect(self.delete_camera_parameter)
        self.btn_synchronize.clicked.connect(self.delete_camera_parameter)

    def moveWindow(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.recent_win.move(self.recent_win.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def update_list_camera(self):
        self.list_camera.clear()
        parameter_list = []
        for key in self.data.keys():
            parameter_list.append(key)
        self.list_camera.addItems(parameter_list)
        self.handle_combo_box()

    def handle_combo_box(self):
        camera_index = self.list_camera.currentText()
        key = list(self.data[camera_index])
        if camera_index:
            self.camera_name = self.data[camera_index][key[0]]
            self.camera_fov = self.data[camera_index][key[1]]
            self.sensor_width = self.data[camera_index][key[2]]
            self.sensor_height = self.data[camera_index][key[3]]
            self.icx = self.data[camera_index][key[4]]
            self.icy = self.data[camera_index][key[5]]
            self.ratio = self.data[camera_index][key[6]]
            self.image_width = self.data[camera_index][key[7]]
            self.image_height = self.data[camera_index][key[8]]
            self.calibration_ratio = self.data[camera_index][key[9]]
            self.parameter_0 = self.data[camera_index][key[10]]
            self.parameter_1 = self.data[camera_index][key[11]]
            self.parameter_2 = self.data[camera_index][key[12]]
            self.parameter_3 = self.data[camera_index][key[13]]
            self.parameter_4 = self.data[camera_index][key[14]]
            self.parameter_5 = self.data[camera_index][key[15]]
            self.fill_the_properties_camera()

    def fill_the_properties_camera(self):
        self.label_camera_name.setText(self.camera_name)
        self.label_camera_fov.setText(str(self.camera_fov))
        self.label_cam_sensor_width.setText(str(self.sensor_width))
        self.label_cam_sensor_height.setText(str(self.sensor_height))
        self.label_image_center_X.setText(str(self.icx))
        self.label_image_center_Y.setText(str(self.icy))
        self.label_ratio.setText(str(self.ratio))
        self.label_image_width.setText(str(self.image_width))
        self.label_image_height.setText(str(self.image_height))
        self.label_calib_ratio.setText(str(self.calibration_ratio))
        self.label_parameter0.setText(str(self.parameter_0))
        self.label_parameter1.setText(str(self.parameter_1))
        self.label_parameter2.setText(str(self.parameter_2))
        self.label_parameter3.setText(str(self.parameter_3))
        self.label_parameter4.setText(str(self.parameter_4))
        self.label_parameter5.setText(str(self.parameter_5))

    def save_parameter_from_ui(self):
        camera_index = self.list_camera.currentText()
        self.data[camera_index][0] = self.label_camera_name.text()
        self.data[camera_index][1] = int(self.label_camera_fov.text()) if self.label_camera_fov.text() != "" else 220
        self.data[camera_index][2] = float(self.label_cam_sensor_width.text())
        self.data[camera_index][3] = float(self.label_cam_sensor_height.text())
        self.data[camera_index][4] = int(self.label_image_center_X.text())
        self.data[camera_index][5] = int(self.label_image_center_Y.text())
        self.data[camera_index][6] = float(self.label_ratio.text())
        self.data[camera_index][7] = int(self.label_image_width.text())
        self.data[camera_index][8] = int(self.label_image_height.text())
        self.data[camera_index][9] = float(self.label_calib_ratio.text())
        self.data[camera_index][10] = float(self.label_parameter0.text())
        self.data[camera_index][11] = float(self.label_parameter1.text())
        self.data[camera_index][12] = float(self.label_parameter2.text())
        self.data[camera_index][13] = float(self.label_parameter3.text())
        self.data[camera_index][14] = float(self.label_parameter4.text())
        self.data[camera_index][15] = float(self.label_parameter5.text())
        self.main_controller.camera_params.save_changes_data_parameter(self.data)

    def delete_camera_parameter(self):
        camera_index = self.list_camera.currentText()
        data = self.main_controller.camera_params.data_parameter
        data.pop(camera_index)
        self.clean_parameter_in_ui()
        self.update_list_camera()

    def clean_parameter_in_ui(self):
        self.label_camera_name.setText("")
        self.label_camera_fov.setText("")
        self.label_cam_sensor_width.setText("")
        self.label_cam_sensor_height.setText("")
        self.label_image_center_X.setText("")
        self.label_image_center_Y.setText("")
        self.label_ratio.setText("")
        self.label_image_width.setText("")
        self.label_image_height.setText("")
        self.label_calib_ratio.setText("")
        self.label_parameter0.setText("")
        self.label_parameter1.setText("")
        self.label_parameter2.setText("")
        self.label_parameter3.setText("")
        self.label_parameter4.setText("")
        self.label_parameter5.setText("")

    @classmethod
    def select_file(cls, parent=None, title="Open file", dir_path="/camera_parameter/", file_filter=""):
        """
        Find the file path from the directory computer.

        Args:
            parent (): The parent windows to show dialog always in front of user interface
            title: the title window of open dialog
            file_filter: determine the specific file want to search
            dir_path: Navigate to specific directory

        return:
            file_path: location
        """
        if pyqt_version == "pyqt6":
            option = QtWidgets.QFileDialog.Option.DontUseNativeDialog
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(parent, title, dir_path,
                                                                 file_filter, options=option)
        else:
            options = QtWidgets.QFileDialog.DontUseNativeDialog
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(parent, title, dir_path,
                                                                 file_filter,
                                                                 options=options)
        return file_path

    def add_new_parameter_from_file(self):
        parameter_path = self.select_file(None, "Select Parameter !", "../", "Parameter Files (*.json)")
        if parameter_path:
            with open(parameter_path) as f:
                camera = json.load(f)
            camera_name = str(camera["cameraName"])
            self.data[camera_name] = [None] * 16
            self.data[camera_name][0] = camera["cameraName"]
            self.data[camera_name][1] = ""
            self.data[camera_name][2] = camera["cameraSensorWidth"]
            self.data[camera_name][3] = camera["cameraSensorHeight"]
            self.data[camera_name][4] = camera["iCx"]
            self.data[camera_name][5] = camera["iCy"]
            self.data[camera_name][6] = camera["ratio"]
            self.data[camera_name][7] = camera["imageWidth"]
            self.data[camera_name][8] = camera["imageHeight"]
            self.data[camera_name][9] = camera["calibrationRatio"]
            self.data[camera_name][10] = camera["parameter0"]
            self.data[camera_name][11] = camera["parameter1"]
            self.data[camera_name][12] = camera["parameter2"]
            self.data[camera_name][13] = camera["parameter3"]
            self.data[camera_name][14] = camera["parameter4"]
            self.data[camera_name][15] = camera["parameter5"]
            self.update_list_camera()
            self.list_camera.setCurrentText(camera_name)
            self.handle_combo_box()

style_appearance = """
    QWidget {
        color: rgb(221, 221, 221);
        font: 10pt "Segoe UI";
        border: none;
    }

    #frame_main{
        background-color: rgb(37, 41, 48);
        border: 1px solid rgb(44, 49, 58);
        border-radius: 10px;
    }

    #label_title{

    color: rgb(238,238,238);
    font: 14pt "Segoe UI";
    }

    QLineEdit {
        font: 9pt "Segoe UI";
        background-color: rgb(33, 37, 43);
        border-radius: 5px;
        border: 2px solid rgb(33, 37, 43);
        padding-left: 10px;
        selection-color: rgb(255, 255, 255);
        selection-background-color: rgb(255, 121, 198);
    }
    QLineEdit:hover {
        border: 2px solid rgb(64, 71, 88);
    }
    QLineEdit:focus {
        border: 2px solid rgb(91, 101, 124);
    }

    QComboBox{
        background-color: rgb(27, 29, 35);
        border-radius: 5px;
        border: 2px solid rgb(52, 59, 72);
        padding: 5px;
        padding-left: 10px;
    }
    QComboBox:hover{
        border: 2px solid rgb(82, 94, 88);
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px;
        border-left-width: 3px;
        border-left-color: rgba(39, 44, 54, 150);
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;
        background-image: url(icons:light/cil-arrow-bottom.png);
        background-position: center;
        background-repeat: no-reperat;
     }
    QComboBox QAbstractItemView {
        color: rgb(255, 121, 198);
        background-color: rgb(33, 37, 43);
        padding: 10px;
        selection-background-color: rgb(39, 44, 54);
    }

    QPushButton {
        border: 2px solid rgb(52, 59, 72);
        border-radius: 5px;	
        background-color: rgb(52, 59, 72);
    }
    QPushButton:hover {
        background-color: rgb(57, 65, 80);
        border: 2px solid rgb(61, 70, 86);
    }
    QPushButton:pressed {	
        background-color: rgb(35, 40, 49);
        border: 2px solid rgb(43, 50, 61);
    }
"""
