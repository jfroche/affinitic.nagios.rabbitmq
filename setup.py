from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='affinitic.nagios.rabbitmq',
      version=version,
      description="Data export for Direction Generale Agriculture",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='notyet',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['affinitic', 'affinitic.nagios'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'nagiosplugin'
      ],
      entry_points={
         'console_scripts': [
            'check_rabbit_channel_count = affinitic.nagios.rabbitmq.channel_count:main']})
