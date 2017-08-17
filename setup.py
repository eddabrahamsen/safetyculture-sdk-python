from setuptools import setup

setup(name = 'safetyculture-sdk-python',
      version = '1.4.0',
      description = 'SafetyCulture Python SDK and export tools',
      url = 'https://github.com/SafetyCulture/safetyculture-sdk-python',
      author = 'SafetyCulture',
      author_email = 'integrations@safetyculture.io',
      packages = ['safetypy', 'tools', 'tools/exporter'],
      install_requires = [
            'python-dateutil>=2.5.0',
            'pytz>=2015.7',
            'tzlocal>=1.3',
            'unicodecsv>=0.14.1',
            'requests>=2.10.0',
            'pyyaml>=3.11'
      ],
      python_requires = "!=3.*"
      )
