from setuptools import setup, find_packages

setup(
    name='math-quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Specify any dependencies your project needs
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',
        ],
    },
)
