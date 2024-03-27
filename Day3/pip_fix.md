python -m pip install SomePackage --use-feature=truststore

python -m pip install pip-system-certs --use-feature=truststore


C:\Users\<username>\AppData\Roaming\pip\pip.ini
[global]
trusted-host = pypi.python.org
               pypi.org
               files.pythonhosted.org

pip config set global.trusted-host \
    "pypi.org files.pythonhosted.org pypi.python.org" \
    --trusted-host=pypi.python.org \
    --trusted-host=pypi.org \
    --trusted-host=files.pythonhosted.org