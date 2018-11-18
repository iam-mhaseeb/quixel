import  io
from setuptools import setup

with io.open('readme.md', encoding='utf_8') as fp:
    readme = fp.read()

setup(name='quixel',
      version='1.0',
      description='A happy light weight framework for text content analysis semantically.',
      long_description=readme,
      long_description_content_type='text/markdown',
      keywords='python, text analysis, nlp',
      url='https://github.com/iam-mhaseeb/quixel',
      author='Muhammad Haseeb',
      author_email='haseeb.emailbox@gmail.com',
      license='MIT',
      packages=['quixel'],
      zip_safe=False,
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
