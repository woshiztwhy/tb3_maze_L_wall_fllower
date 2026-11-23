import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'maze_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zty',
    maintainer_email='zty@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "tb3_point2point = maze_control.tb3_point2point:main",
            "tb3_waypoints   = maze_control.tb3_waypoints:main",
            "tb3_pure_pursuit= maze_control.tb3_pure_pursuit:main",
            "tb3_avoid       = maze_control.tb3_avoid:main",
            "tb3_follow      = maze_control.tb3_follow:main",
            "tb3_wall_follower = maze_control.tb3_wall_follower:main",
            'scan_region = maze_control.scan_region_node:main',
            'lidar_simple_avoid = maze_control.tb3_avoid:main',
        ],
    },
)
