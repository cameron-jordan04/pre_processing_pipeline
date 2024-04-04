from setuptools import setup

setup(
   name='pre_processing',
   version='1.0',
   description='A useful module',
   author='Cameron Jordan',
   author_email='cameronjordan@berkeley.edu',
   packages=['pre_processing'],
   install_requires=['numpy', 'scipy', 'seaborn', 'matplotlib.pyplot', 'statsmodels.api', 'pywt', 'sklearn'],
)