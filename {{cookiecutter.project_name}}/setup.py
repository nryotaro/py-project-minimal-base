from setuptools import setup, find_packages


setup(name='{{cookiecutter.project_name}}',
      version="0.0.1",
      packages=find_packages(exclude=["tests", "tests.*"]),
      install_requires=[
      ],
      entry_points={'console_scripts': ['{{cookiecutter.package_name}}={{cookiecutter.package_name}}:main']},
      extras_require={
          'test': [
              'pytest'
          ],
          'dev': [
              'ipython',
              'python-language-server[all]'
          ]})
