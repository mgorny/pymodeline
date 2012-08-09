#!/usr/bin/python
#	vim:fileencoding=utf-8
# (c) 2011 Michał Górny <mgorny@gentoo.org>
# Released under the terms of the 2-clause BSD license.

from distutils.core import setup

import os.path, sys

setup(
		name = 'pymodeline',
		version = '0',
		author = 'Michał Górny',
		author_email = 'mgorny@gentoo.org',
		url = 'http://bitbucket.org/mgorny/pymodeline',

		packages = ['pymodeline'],

		classifiers = [
			'Development Status :: 2 - Pre-Alpha',
			'Intended Audience :: Developers',
			'License :: OSI Approved :: BSD License',
			'Programming Language :: Python'
		]
)
