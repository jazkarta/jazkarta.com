# -*- coding: utf-8 -*-
"""Installer for the jazkarta.policy package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='jazkarta.policy',
    version='0.1',
    description="Policy package for the jazkarta.com site",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0b1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='Carlos de la Guardia',
    author_email='carlos@jazkarta.com',
    url='http://pypi.python.org/pypi/jazkarta.policy',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['jazkarta'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'jazkarta.contenttypes',
        'jazkarta.plonetheme',
        'Products.RedirectionTool',
        'collective.relatedslider',
        'Products.PloneFormGen',
        'collective.isotope',
        'collective.googleanalytics',
        'plone.tiles',
        'plone.app.tiles',
        'plone.app.mosaic',
        'jazkarta.tesserae',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
