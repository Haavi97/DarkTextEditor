import sys
from cx_Freeze import setup, Executable

company_name = 'Haavi'
product_name = 'DarkTextEditor'

bdist_msi_options = {'upgrade_code': '{48B079F4-B598-438D-A62A-8A233A3F8901}',
                     'add_to_path': False,
                     'initial_target_dir': r'[ProgramFilesFolder]\% s\% s' % (company_name, product_name),
                     }

build_exe_options = {
    'includes': ['PyQt5', 'json'],
}

# GUI applications require a different base on Windows
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(script='main.py',
                 base=base,
                 )

setup(name=product_name,
      version='1.0.0',
      description='I was a bit tired of the Notepad aplication that Windows has for the simple texts since it cannot be configured to be in dark mode. I know I can use some IDE like VSC but for simple things it is handy to have an easy launch simple text editor.',
      author='Javier Ortin',
      author_email='fortin@taltech.ee',
      url='https://github.com/Haavi97/DarkTextEditor',
      data_files=[('', ['about.html']),
                  ('', ['style.css']),
                  ('', ['conf.json']),
                  ('', ['blackicon.ico']),
                  ('', ['blackicon.svg']),
                  ('', ['README.md'])],
      executables=[exe],
      options={'bdist_msi': bdist_msi_options,
               'build_exe': build_exe_options})
