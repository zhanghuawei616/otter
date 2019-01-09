from distutils.core import setup, Extension
import platform

LONGDOC = 'Fast C Short Path chinese and english cut'


if platform.python_version().startswith('2'):
    otter_py2 = Extension('_otter',
        include_dirs=['src/'],
        sources=['python/2/otter_py2_wrap.c'],
        library_dirs=['python/']
    )
    setup(name='otter',
          version='0.10',
          description='Use C  Chinese Words Segementation Utilities',
          long_description=LONGDOC,
          author='xuen',
          author_email='nanhangxuen@163.com',
          url='https://github.com/xuenhappy/otter',
          license="Apache2",
          classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache2 License',
            'Operating System :: OS Independent',
            'Natural Language :: Chinese (Simplified)',
            'Natural Language :: Chinese (Traditional)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.7',
            'Topic :: Text Processing',
            'Topic :: Text Processing :: Indexing',
            'Topic :: Text Processing :: Linguistic',
        ],
        keywords='NLP,tokenizing,Chinese word segementation',
        packages=['otter'],
        package_dir={'otter':'otter'},
          package_data={'otter':['src/*.py','dict/*.*']},
        ext_modules = [otter_py2],
    )


if platform.python_version().startswith('3'):

    otter_py3 = Extension('_otter',
            sources=['python/3/otter_py3_wrap.c'],
    )
    setup(name='otter',
          version='0.10',
        description='Use C  Chinese Words Segementation Utilities',
        long_description=LONGDOC,
        author='xuen',
        author_email='nanhangxuen@163.com',
        url='https://github.com/xuenhappy/otter',
        license="Apache2",
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache2 License',
            'Operating System :: OS Independent',
            'Natural Language :: Chinese (Simplified)',
            'Natural Language :: Chinese (Traditional)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.7',
            'Topic :: Text Processing',
            'Topic :: Text Processing :: Indexing',
            'Topic :: Text Processing :: Linguistic',
        ],
        keywords='NLP,tokenizing,Chinese word segementation',
        packages=['otter'],
        package_dir={'otter':'otter'},
          package_data={'otter':['src/*.py','dict/*.*']},
        ext_modules = [otter_py3],
)
