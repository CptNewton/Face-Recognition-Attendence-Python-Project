import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Mitali Barman\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mitali Barman\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_Recognition_app.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Face Recognition Attendence",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'Images','data','Database','Attendence_Report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Nayan Jyoti Adhikary",
    executables = executables
    )
