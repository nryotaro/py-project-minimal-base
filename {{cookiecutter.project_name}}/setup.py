from setuptools import setup, find_packages


setup(name='{{cookiecutter.project_name}}',
      version="0.0.1",
      packages=find_packages(),
      install_requires=[
      ],
      extras_require={
          'test': [
              'pytest'
          ],
          'dev': [
              'ipython',
              'python-language-server[all]'
          ]})
