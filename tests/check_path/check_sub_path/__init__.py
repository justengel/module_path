import module_path

MY_DIR = module_path.my_dir()
DATA = module_path.join(MY_DIR, 'fakedata.txt')
EXISTS = module_path.exists(DATA)
