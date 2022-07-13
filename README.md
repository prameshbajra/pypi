# pypi
Working prototype to publish python packages to PIP

1. Make sure you have setuptools installed. This is available by default in Python3.

2. If you prefer to work in a virtual environment, then make sure you activate it.

3. You will also need wheel to be installed. You can do that by : `pip install wheel`

4. To publish we would need `twine`. To install it you can run `pip install twine`


### Build

```
python setup.py bdist_wheel
```

The build process will generate dist folder along with other folders.

### Publish to PIP/PYPI

```
twine upload dist/*
```

You will be asked your username and password here. If you do not have it, you can get one by resistering at www.pypi.org

> Note: Everytime you try to publish a new version make sure you update the version in `setup.py` file else you will not be allowed to upload the new changes.
> Also, keep in mind that it might take a minute or two to sync up with pypi, i.e. after uploading the package do not install it immediately. It will most probably fetch the older version. Wait for a minite and then it will fetch the new one.
