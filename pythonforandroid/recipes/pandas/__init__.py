from pythonforandroid.toolchain import CythonRecipe


class PandasRecipe(CythonRecipe):
    version = 'v0.20.2'
    url = 'https://github.com/pandas-dev/pandas/archive/{version}.zip'
    name = 'pandas'

    depends = [
        ('python2', 'python3crystax'),
        'numpy', 'pytz', 'python-dateutil'
    ]


recipe = PandasRecipe()
