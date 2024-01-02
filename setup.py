from setuptools import setup, find_packages

long_description = 'Balance chemical reaction equations - read the docs at https://www.github.com/nayakrujul/balance-equation'

setup(
  name = 'balance-equation',
  version = '1.0',
  license='Apache',
  description = 'Balance chemical reaction equations',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/balance-equation',
  download_url = 'https://github.com/nayakrujul/balance-equation/archive/refs/tags/v_10.tar.gz',
  keywords = ['balance', 'equation', 'reaction', 'chemistry'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    # 'Programming Language :: Python :: 3.4',
    # 'Programming Language :: Python :: 3.5',
    # 'Programming Language :: Python :: 3.6',
    # 'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points = {
    'console_scripts': [
      'balance = balance.cmdline:interface'
    ]
  }
)
