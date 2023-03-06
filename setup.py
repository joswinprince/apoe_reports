from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in apoe_reports/__init__.py
from apoe_reports import __version__ as version

setup(
	name="apoe_reports",
	version=version,
	description="APOE Report Import functionality addition in LIMS",
	author="Hephzibah Technologies Inc",
	author_email="david.alexander@hephzibahtech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
