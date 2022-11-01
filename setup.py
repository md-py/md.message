import setuptools

with open('readme.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='md.message',
    version='0.2.0',
    description='Set of contracts defines message processing lifecycle',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='License :: OSI Approved :: MIT License',
    package_dir={'': 'lib'},
    packages=['md.message'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
