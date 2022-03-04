call C:\Users\Admin\MyHome\Py\main-env\Scripts\activate.bat
python C:\Users\Admin\MyHome\PhysicsExp\setup.py sdist bdist_wheel
call C:\Users\Admin\MyHome\Py\test-env\Scripts\activate.bat
pip install --upgrade C:\Users\Admin\MyHome\PhysicsExp\dist\physicsexp-0.0.1-py3-none-any.whl

