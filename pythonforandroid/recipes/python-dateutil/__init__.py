from pythonforandroid.toolchain import PythonRecipe


class DateutilRecipe(PythonRecipe):
    version = '2.6.0'
    url = 'https://github.com/dateutil/dateutil/archive/{version}.zip'
    name = 'python-dateutil'

    depends = [(
        'python2', 'python3crystax'
    )]


recipe = DateutilRecipe()
