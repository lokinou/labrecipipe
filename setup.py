from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'vrnopain neurofeedback pipeline'
LONG_DESCRIPTION = 'Remote controller for labrecorder using pipe process. It takes care of sending the TCP messages'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="labrecipipe",
    version=VERSION,
    author="Loic Botrel",
    author_email="<loic.botrel@uni-wuerzburg.de>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
	#'meegkit @ git+https://github.com/nbara/python-meegkit.git#egg=meegkit[extra]'],
	#dependency_links=['git+https://github.com/nbara/python-meegkit.git#egg=meegkit'],
	python_requires='>=3.6.6',
    keywords=['labrecorder', 'labstreaminglayer'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
	license='Proprietary',
	url='https://github.com/lokinou/labrecipipe'
)