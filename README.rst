===========
module_path
===========


Provided functions

  * files - importlib.resources files this function is the standard for retrieving resources for Python 3.9+
  * as_file - context manager for retrieving a true filepath for Python 3.9+.
  * my_dir - Return the directory this module is in. This should exist even in an executable.
  * my_path - Return the path to the module that called this method. This may not exist in an executable


Example
=======

.. code-block:: python

    # my_interface.py
    # sdl2 with sld2.dll in package
    # File Structure:
    #     my_sdl/
    #         sdl2_dll_path/
    #             SDL2.dll
    #         __init__.py
    #         my_interface.py
    import os
    from module_path import files, as_file

    with as_file(files('my_sdl').joinpath('sdl2_dll_path/SDL2.dll')) as sdl_path:
        os.environ.setdefault('PYSDL2_DLL_PATH', os.path.dirname(str(sdl_path)))
        import sdl2

    # Use sdl2
    assert sdl2 is not None


.. code-block::

    check_path/
        __init__.py
        main.py
        check_sub_path
             __init__.py
             fakedata.txt


.. code-block:: python

    # check_path/check_sub_path/__init__.py
    import os
    import module_path

    MY_DIR = module_path.my_dir()
    DATA = os.path.join(MY_DIR, 'fakedata.txt')
    EXISTS = os.path.exists(DATA)


.. code-block:: python

    # check_path/main.py
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

Build the executable with

.. code-block:: sh

    pyinstaller --name check_path -y --add-data "check_path/check_sub_path/fakedata.txt;check_path/check_sub_path/" check_path/main.py

After pyinstaller builds you will have a `dist` directory. The data for this example should be stored in `dist/check_path/check_path/check_sub_path/fakedata.txt`
