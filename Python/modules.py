import os
#dir(os)
import urllib

import commands

os.listdir(directory)
os.path.join(path1, path2)
os.path.exists()
os.path.abspath()
os.mkdir()

(status, commands) = commands.getstatusoutput('ls')


url = urllib.urlopen('www.google.com')
page = url.read()

download = urllib.urlretrieve('www.python.org', 'python3')
