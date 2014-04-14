Example/Base Buildout for Opsworks Plone Deployments
====================================================

This is a base buildout for Plone (currently 4.3-latest) for deploying
on AWS OpsWorks using the `opsworks-web-python` cookbooks.

For development start with:

    python2.7 ./bootstrap.py -c development.cfg
    bin/buildout -c development.cfg

If you want some Zope helpers in your ipython shell (`bin/ipzope`) then do the following:

    mkdir ~/.config/ipython/
    cp scripts/ipy_profile_zope.py ~/.config/ipython/

For production use the opsworks-web-python recipes to deploy to AWS Opsworks

## License && Authors
* Alec Mitchell <alecpm@gmail.com>

With thanks to Jazkarta, Inc. and KCRW Radio
```text
Copyright 2014, Alec Mitchell

Licensed under the BSD License.
```
