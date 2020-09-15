from setuptools import setup

setup(
    name='scrapy-zenscrape',
    version='0.0.3',
    url='https://github.com/saasindustries/scrapy-zenscrape',
    description='Scrapy middleware for Zenscrape',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Clemens Ehrenreich',
    maintainer='Andreas Altheimer',
    maintainer_email='office@zenscrape.com',
    license='MIT',
    packages=['scrapy_zenscrape'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Scrapy',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.5',
    install_requires=['scrapy'],
)
