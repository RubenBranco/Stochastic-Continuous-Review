from setuptools import setup, find_packages


setup(
    name='stochastic_review',
    version='0.1.0',
    description='A package to encompass stochastic methods of continuous stock review.',
    long_description='',
    url='https://github.com/RubenBranco/stochastic-continuous-review',
    author='Ruben Branco',
    author_email='ruben.branco@outlook.pt',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Mathematics'
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
    keywords='operations research stochastic continuous review',
    package_dir={'': 'src'},
    packages=[
        'stochastic_review',
        'stochastic_review.models',
    ],
    install_requires=[
        "bullet",
        "scipy",
    ],
    entry_points={
        'console_scripts': {
            'stochastic_review=stochastic_review.main:main',
        },
    },
)
