## Notice：Project split!

分割之后本项目只包含数据处理工具程序，具体的实验数据和用到的数据处理脚本（原Experiment目录，git历史中可见）移动至项目中.

After splitting, this repository only contains data processing tools, while specific experiment data and my data processing scripts(the original `Experiment` directory, still visible in git history) were moved to 



## Build yourself

Assuming you are using Windows. 

**Change the command to make then work on your device! Don't just copy & paste!**

 **Prepare to build**

Set up environment to build and release python packages, detailed guide can be found on the [pypi website](https://packaging.python.org/tutorials/packaging-projects/). 

**Build**

```
python setup.py sdist bdist_wheel
```

Then the packaged wheel file can be found at `./dist/physicsexp-0.0.1-py3-none-any.whl`(Name may be different)

**Install**

**This package haven't been tested carefully, so using a virtualenv is recommended.**

Create a virtualenv(here named test-env)

```
python -m venv test-env
```

Activate it

```
./test-env/Scripts/activate.bat
```

Install the wheel (Use USTC mirror to accelerate, and it will download and install other required packages)

```
pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple path\to\physicsexp-0.0.1-py3-none-any.whl
```

Wait a moment for the installation to finish.