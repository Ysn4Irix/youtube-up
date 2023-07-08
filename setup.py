import os
os.system('sudo apt-add-repository universe')
os.system('sudo apt-get install python2-minimal')
os.system('curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py')
os.system('sudo python2 get-pip.py')
os.system('pip2 install --upgrade google-api-python-client')
os.system('pip2 install --upgrade google-auth-oauthlib google-auth-httplib2')
