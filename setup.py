# ----------------------------------------------------------------------------
# Copyright (c) 2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer


setup(
    name='q2-cutadapt',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='BSD-3-Clause',
    packages=find_packages(),
    author='Matthew Ryan Dillon',
    author_email="matthewrdillon@gmail.com",
    description='Find and remove adapters, primers, and other unwanted '
                'sequences from sequence data.',
    url='https://github.com/qiime2/q2-cutadapt',
    entry_points={
        'qiime2.plugins':
        ['q2-cutadapt=q2_cutadapt.plugin_setup:plugin']
    },
    package_data={
        'q2_cutadapt.tests': ['data/*'],
    },
    zip_safe=False,
)