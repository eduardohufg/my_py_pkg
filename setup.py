from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eduardohufg',
    maintainer_email='eduardochavezmartin10@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'add2ints_server = my_py_pkg.add2ints_server:main',
            'add2ints_client = my_py_pkg.add2ints_client:main',
            'computeRectangle_server = my_py_pkg.computeRectangle_server:main',
            'computeRectangle_client = my_py_pkg.computeRectangle_client:main',
        ],
    },
)
