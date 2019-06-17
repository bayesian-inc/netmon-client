from setuptools import setup, find_packages

setup(
	# Application name:
	name="bayesian_netmon",

	# Version number (initial):
	version="0.1",

	# Application author details:
	author="Bayesian Inc",
	author_email="netmon@bayesian.io",

	# Packages
	packages=find_packages(),

	# Include additional files into the package
	include_package_data=True,


	# Details
	url="https://github.com/bayesian-inc/netmon-api",

	zip_safe = True,
	#
	# license="LICENSE.txt",
	description="Python client for Bayesian NetMon",

	# long_description=open("README.txt").read(),
	python_requires='>=3.6',
	
	install_requires=[
		'requests',
	],
	
	classifiers=(
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.6",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
)
