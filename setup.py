# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst'), encoding='UTF-8').read()

setup(name='dwdweather2',
      version='0.8.3',
      description='Python client to access weather data from Deutscher Wetterdienst (DWD), '
                  'the federal meteorological service in Germany.',
      long_description=README,
      license="MIT",
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Topic :: Communications",
        "Topic :: Database",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Archiving",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
      ],
      author='Marian Steinbach',
      author_email='marian@sendung.de',
      url='https://github.com/hiveeyes/dwdweather2',
      keywords='dwd cdc deutscher wetterdienst climate data center weather '
               'opendata data acquisition transformation export '
               'geospatial temporal timeseries '
               'sensor network observation '
               'http rest api '
               'json csv'
               'rdbms sql sqlite '
               'grafana',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'tqdm==4.32.1',
          'python-dateutil==2.8.0',
          'requests==2.22.0',
          'requests-cache==0.5.0',
          #'htmllistparse==0.5',     # Needs min. Python 3.3
          'beautifulsoup4==4.7.1',
      ],
      entry_points={
          'console_scripts': [
              'dwdweather = dwdweather.commands:run'
          ]
      }
)
