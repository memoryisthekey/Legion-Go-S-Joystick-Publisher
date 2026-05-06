from setuptools import find_packages, setup
import os 
from glob import glob

package_name = 'legion_joystick'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
            # Install launch files
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rno',
    maintainer_email='rno@mmmi.sdu.dk',
    description='TODO: Maps Legion Go S Joystick to cmd_vel for Husky',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'legion_joystick = legion_joystick.legion_joystick:main',
        ],
    },
)
