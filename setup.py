from setuptools import setup, find_packages

setup(
    name="math_quiz",  # The name of your package
    version="0.1",  # Initial version number
    packages=find_packages(),  # Automatically finds all packages in your project
    install_requires=[],  # List of dependencies; add packages here if needed
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',  # Command to run the main function in math_quiz.py
        ],
    },
    author="MuhammadJunaidkhizar",  # Replace with your name
    author_email="junaidkhizar5@gmail.com",  # Replace with your email
    description="A simple math quiz package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/MuhammadJunaidkhizar/dsss_homework_2",  # Replace with your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
 
