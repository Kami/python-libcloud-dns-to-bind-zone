# Licensed to Tomaz Muraus under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# Tomaz muraus licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup


setup(
    name='libcloud_to_bind',
    version='0.1.0',
    long_description=open('README.rst').read(),
    packages=[
        'libcloud_to_bind'
    ],
    package_dir={
        'libcloud_to_bind': 'libcloud_to_bind'
    },
    install_requires=[
        'apache-libcloud>=0.13.1',
    ],
    url='https://github.com/Kami/python-libcloud-to-bind/',
    license='Apache License (2.0)',
    author='Tomaz Muraus',
    author_email='tomaz+pypi@tomaz.me',
    description='Python module which allows you to export Libcloud DNS ' +
                'zone to the BIND zone file format',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
