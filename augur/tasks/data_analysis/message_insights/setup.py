#SPDX-License-Identifier: MIT

import io
import os
import re

from setuptools import find_packages
from setuptools import setup

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())

setup(
    name="message_insights",
    version="0.3.1",
    url="https://github.com/chaoss/augur",
    license='MIT',
    author="Augur Team",
    author_email="akshblr555@gmail.com",
    description="Message Insights worker that detects novel messages & analyzes sentiment from issue, PR messages",
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.2',
        'Flask-Cors==4.0.1',
        'Flask-Login==0.5.0',
        'Flask-WTF==1.0.0',
        'requests==2.32.0',
        'psycopg2-binary==2.9.9',
        'click==8.0.3',
        'scipy>=1.10.0',
        'scikit-learn==1.5.0', #0.24.2',
        'numpy==1.26.0',
        'nltk==3.6.6',
        'pandas==1.5.3',
        'emoji==1.2.0',
        'keras>=2.15.0',
        'Keras-Preprocessing',
        'tensorflow==2.15.0',
        'h5py==3.10.0',
        'scikit-image==0.19.1',
        'joblib==1.2.0',
        'xgboost',
        'bs4==0.0.1',
        'xlrd==2.0.1',
        'gensim>=4.2.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ]
)
