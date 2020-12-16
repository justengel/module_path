"""
Get a modules path.

Notes:
    * sys._MEIPASS - Created by pyinstaller executable. This is the directory of the executable
      * If regular python run this does not exist
      * If pyinstaller created a directory this is the directory that contains the executable
      * If pyinstaller onefile this is "C:\\Users\\username\\AppData\\Local\\Temp\\_MEI#####" which is some temp directory.
    * frame.f_code.co_filename
      * In regular python run this is the absolute path of the module. "C:\\...\\check_path.py"
      * If pyinstaller created a directory this is the module filename "check_path.py"
      * If pyinstaller onefile this is the module filename "check_path.py"
    * module.__file__ (matches frame.f_code.co_filename)
      * In regular python run this is the absolute path of the module. "C:\\...\\check_path.py"
      * If pyinstaller created a directory this is the module filename "check_path.py"
      * If pyinstaller onefile this is the module filename "check_path.py"
    * sys.executable
      * If regular python run this is the path to your python.exe
      * If pyinstaller created a directory this is the absolute path to the executable
      * If pyinstaller onefile this is the absolute path to the executable
"""
import os
import sys
import inspect

# filepath = vars().get('__file__', getattr(sys, '_MEIPASS', os.path.dirname(sys.executable)))
# print(filepath)

# try:
#     THIS_DIR = os.path.dirname(os.path.abspath(__file__))
#     HELP_DIR = os.path.join(THIS_DIR, 'help')
#     if not os.path.exists(HELP_DIR):
#         raise EnvironmentError('Frozen executable does not have help dir')
# except (EnvironmentError, NameError, Exception):
#     THIS_DIR = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
#     HELP_DIR = os.path.join(THIS_DIR, 'help')


__all__ = ['my_path', 'my_dir',
           'isfile', 'isdir', 'isabs', 'dirname', 'basename', 'join', 'exists', 'abspath', 'relpath', 'realpath',
           ]


isfile = os.path.isfile
isdir = os.path.isdir
isabs = os.path.isabs
dirname = os.path.dirname
basename = os.path.basename
join = os.path.join
exists = os.path.exists
abspath = os.path.abspath
relpath = os.path.relpath
realpath = os.path.realpath


def my_path(*args, back=1, **kwargs):
    """Return the path of the module that called this function."""
    # Find the correct frame
    frame = inspect.currentframe()
    for _ in range(back):
        frame = frame.f_back

    # Get the frame filename
    filename = frame.f_code.co_filename  # Will be abspath with regular python run

    # Check if exists (in pyinstaller executables this will not exist
    if isabs(filename) and os.path.exists(filename):
        return filename
    else:
        # Note pyinstaller onefile will create a temp directory and create all pyd (C extension) files in that dir.
        exe_path = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))

        # Create the new filename
        filename = os.path.join(exe_path, filename)  # This may not exist, but the directory should
        return filename


    # print('===== OLD =====')
    # frame = inspect.currentframe().f_back
    # print('FRAME:', frame.f_code.co_filename, os.path.exists(frame.f_code.co_filename))
    # try:
    #     print('MODULE:', inspect.getmodule(frame).__file__, os.path.exists(inspect.getmodule(frame).__file__))
    # except (AttributeError, Exception):
    #     pass
    # try:
    #     print('MEIPASS:', getattr(sys, '_MEIPASS', 'NONE'), os.path.exists(getattr(sys, '_MEIPASS', 'NONE')))
    # except (AttributeError, Exception):
    #     pass
    # try:
    #     print('EXE:', sys.executable, os.path.exists(sys.executable))
    # except (AttributeError, Exception):
    #     pass
    # # try:
    # #     return inspect.getmodule(frame).__file__
    # # except (AttributeError, Exception):
    # #     directory = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
    # #     return os.path.join(directory, frame.f_code.co_filename)


def my_dir(*args, back=1, **kwargs):
    """Return the directory of the module that called this function.

    Args:
        back (int)[1]: Number of frames to step back.
            By default this is 1 so the module that calls this function is used.
    """
    return os.path.dirname(my_path(back=back+1))
