from distutils.core import setup

setup(name='python_plotting',
      description='Python Plotting Tutorial',
      author='Mike Hearne',
      author_email='mhearne@usgs.gov',
      url='',
      install_requires=[
          'jupyter',
          'matplotlib',
          'numpy',
          'cartopy',
          'pandas',
      ],
      entry_points={
          'console_scripts': [
              'load_quakeml = quakeml_db.bin.load_quakeml:main',
              'query_quakeml = quakeml_db.bin.query_quakeml:main',
              'delete_events = quakeml_db.bin.delete_events:main'
              'load_coordinates = quakeml_db.bin.load_coordinates:main'
          ]
      },

      )
