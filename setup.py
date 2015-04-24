from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='python-gearbox',
    version=version,
    author='Eduardo M. Firvida Donestevez',
    packages=find_packages(),
    include_data_package=True,
    author_email='efirvida@gmail.com',
    description='Python library for gear transmission design',
    requires=['numpy', 'scipy'],
    url='https://github.com/efirvida/python-gearbox',
    download_url='https://github.com/efirvida/python-gearbox/archive/master.zip',
    keywords=['gearbox', 'gear', 'agma', 'iso', 'gear transmission', 'engineering'],
    platforms='any',
    license='MIT',
    zip_safe=False,
    classifiers=['Intended Audience :: Developers',
                 'Intended Audience :: Manufacturing',
                 'Intended Audience :: Science/Research',
                 'Natural Language :: English',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Software Development :: Libraries :: Application Frameworks'
                 ]
)

