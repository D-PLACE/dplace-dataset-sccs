from setuptools import setup


setup(
    name='cldfbench_dplace-dataset-sccs',
    py_modules=['cldfbench_dplace-dataset-sccs'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-sccs=cldfbench_sccs:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
