from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.1',
      description='Waste sorting',
      url='https://github.com/PIRomanCod',
      author='PIRomanCod',
      author_email='PIRomanCod@example.com',
      license='MIT',
      long_description=open('README.md').read(),
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder.clean:main']},)

# [metadata]
# name = clean_folder
# version = 1.0.0
# description = Waste sorting
# url = https: // github.com/PIRomanCod
# author = PIRomanCod
# author_email = PIRomanCod@example.com
# license = MIT
# long_description = open("README.md").read()

# [options]
# packages = find:
#     python_reqiures = >= 3.9


# [options.entry_points]
# console_scripts = clean_folder.clean: main
