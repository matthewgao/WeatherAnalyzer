WeatherAnalyzer v0.1
===============
## Introduce
This tools is used to anaylsis the radar image which comes from NMC, we can report where is going to rain, and send a weibo and SMS to somebody who care about it.

## Dependence

* numpy：http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/
* matplotlab：http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.1.1/
* scipy：http://sourceforge.net/projects/scipy/files/scipy/0.12.0/
* PIL
* pyparsing http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyparsing
* datautil http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-dateutil
* six http://www.lfd.uci.edu/~gohlke/pythonlibs/#six

## Issue
if you meet this “No module named six”

site-packages\scipy\lib 目录下的三个文件
six.py
six.pyo
six.pyc
复制到site-packages目录下就可以了。