"""
Build Steps:
 * Be in top level directory module_path. (should have module_path and tests folder inside).
 * pyinstaller -y --add-data "check_path/check_sub_path/fakedata.txt;check_path/check_sub_path/" check_path/main.py
   * --onefile is optional
"""
import module_path
try:
    from check_path.check_sub_path import MY_DIR, DATA, EXISTS
except (ImportError, Exception):
    from check_sub_path import MY_DIR, DATA, EXISTS


if __name__ == '__main__':
    path = module_path.my_path()
    directory = module_path.my_dir()
    print('path   \t', path, module_path.exists(path))  # Should be false with executable
    print('dir    \t', directory, module_path.exists(directory))

    print('sub_dir\t', MY_DIR, module_path.exists(MY_DIR))
    print('DATA   \t', DATA, EXISTS)

