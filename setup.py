from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(author='Chris Lamberson',
      author_email='clambers@jaguarlandrover.com',
      description='GitLab notification daemon',
      entry_points={
          'console_scripts': ['maitred=maitred.command_line:main'],
      },
      include_package_data=True,
      install_requires=['klein'],
      keywords='gitlab mattermost irc',
      license='GPLv3+',
      long_description=readme(),
      name='maitred',
      packages=['maitred'],
      test_suite='nose.collector',
      tests_require=['nose'],
      url='https://github.com/clambers/maitred',
      version='0.1',
      zip_safe=False)
