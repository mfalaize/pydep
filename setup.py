from distutils.core import setup

setup(
    name='pydep',
    version='1.0.0dev',
    py_modules=['pydep'],
    url='https://',
    license='GPL v3',
    author='Maxime Falaize',
    author_email='maxime.falaize@gmail.com',
    description='Python dependencies tool',
    requires=['pip'],
    scripts=['pydep']
)
