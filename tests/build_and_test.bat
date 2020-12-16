pyinstaller --name check_path -y --add-data "check_path/check_sub_path/fakedata.txt;check_path/check_sub_path/" check_path/main.py

pyinstaller --name check_path -y --add-data "check_path/check_sub_path/fakedata.txt;check_path/check_sub_path/" check_path/main.py --onefile

.\dist\check_path.exe

.\dist\check_path\check_path.exe
