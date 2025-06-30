from setuptools import setup, find_packages

setup(
    name="folder_organizer",
    version="0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'PySimpleGUI',
        'shutil',
    ],
    entry_points={
        'gui_scripts': [
            'folder-organizer=folder_organize.gui:run_gui',
        ],
    },
    author="Dianah",
    author_email="junki2497@yahoo.com",
    description="A tool for organizing files",
    license="MIT",
    keywords="file organizer",
    url="https://github.com/yourusername/ScreenOrganizer",
)