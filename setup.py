from distutils.core import setup
setup(
  name = 'tinymlgen',
  packages = ['tinymlgen'],
  version = '0.1',
  license='MIT',
  description = 'Generate C code for microcontrollers from Tensorflow models',
  author = 'Simone Salerno',
  author_email = 'eloquentarduino@gmail.com',
  url = 'https://github.com/eloquentarduino/tinymlgen',
  download_url = 'https://github.com/eloquentarduino/tinymlgen/archive/v_01.tar.gz',
  keywords = ['ML', 'microcontrollers', 'tensorflow', 'machine learning'],
  install_requires=[
    'tensorflow',
    'hexdump'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Code Generators',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)