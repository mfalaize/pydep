from distutils.core import setup

setup(
    name='pydepenv',
    version='1.0.0dev',
    py_modules=['pydepenv'],
    url='https://github.com/mfalaize/pydepenv',
    license='GPL v3',
    author='Maxime Falaize',
    author_email='maxime.falaize@gmail.com',
    description='Python dependencies environment installer',
    requires=['pip'],
    scripts=['pydepenv']
)
