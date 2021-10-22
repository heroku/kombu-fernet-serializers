import kombu_fernet

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    "kombu_fernet",
    "kombu_fernet.serializers",
]

requires = [
    "kombu>=4.0.0",
    "cryptography>=2.0.2",
    "six>=1.10.0",
]

with open("README.rst") as f:
    readme = f.read()

setup(
    name="kombu-fernet-serializers",
    version=kombu_fernet.__version__,
    description="Symmetrically encrypted serializers for Kombu",
    long_description=readme,
    author="David Gouldin",
    author_email="dgouldin@heroku.com",
    url="https://github.com/heroku/kombu-fernet-serializers",
    packages=packages,
    package_data={"": ["LICENSE", "CHANGELOG"]},
    requires_python=">=3.6",
    include_package_data=True,
    install_requires=requires,
    license="MIT",
    zip_safe=False,
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ),
    entry_points={
        "kombu.serializers": [
            "fernet_json = kombu_fernet.serializers.json:register_args",
            "fernet_yaml = kombu_fernet.serializers.yaml:register_args",
            "fernet_pickle = kombu_fernet.serializers.pickle:register_args",
            "fernet_msgpack = kombu_fernet.serializers.msgpack:register_args",
        ]
    },
)
