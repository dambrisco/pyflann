#!/usr/bin/python
from setuptools import setup, find_packages
setup(
	name = "pyflann",
	version = "1.6.11",
	packages = ['pyflann', 'pyflann.bindings', 'pyflann.io', 'pyflann.utils'],

	install_requires = [],
	include_package_data = True,
	package_data = {
		'': ['*.txt', '*.rst', '*.html', '*.frag'],
	},
)
