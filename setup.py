# setup.py
from setuptools import setup, find_packages

requires = [
        'pyramid',
        'pastedeploy',
        'pyramid-ipython',
        'waitress',
        'sqlalchemy',
        'psycopg2-binary',
        'pyramid_tm',
        'transaction',
        'zope.sqlalchemy',
        ]

setup(
        name='pyramid-for-beginners',
        version='0.0',
        description='An introduction to start with Pyramid',
        author='B.J. Bentvelsen',
        author_email='barend.bentvelsen@vanoord.com',
        keywords='web pyramid pylons',
        packages=find_packages(),
        include_package_data=True,
        install_requires=requires,
        entry_points={
            'paste.app_factory': [
                'main = tutorial:main',
                ],
            'console_scripts': [
                'initdb = tutorial.scripts.initializedb:main',
                ]
            }
        )
