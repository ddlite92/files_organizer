from setuptools import setup, find_packages

setup(
    name="files_organizer",
    version="0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[

    ],
    entry_points={
        'console_scripts': [
            'file-organizer=organizer.cli:main',
        ],
        'gui_scripts': [
        'file-organizer-gui=organizer.qt_gui:main',
        ]
    },
    author="Dianah",
    author_email="junki2497@yahoo.com",
    description="A tool for organizing files",
    license="MIT",
    keywords="file organizer",
    url="https://github.com/ddlite92/files_organizer",
    include_package_data=True,
)