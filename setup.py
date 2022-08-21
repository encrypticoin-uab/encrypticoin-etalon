import os
import shutil
from collections import defaultdict

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = "0.1.1"

with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = defaultdict(list)
for name in os.listdir(os.path.join(HERE, "requirements")):
    if name not in ("base.in",):
        continue
    reqs = requirements[name.rpartition(".")[0]]
    with open(os.path.join(HERE, "requirements", name)) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line.startswith("-r"):
                continue
            reqs.append(line)
install_requirements = requirements.pop("base")


def _package_data_files(pkg: str):
    root = os.path.join(HERE, pkg)
    for parent, _, files in os.walk(root):
        for file in files:
            if file.endswith(".py") or file.endswith(".pyc"):
                continue
            yield os.path.relpath(os.path.join(parent, file), root)


package_data = {
    "encrypticoin_etalon": sorted(_package_data_files("encrypticoin_etalon")),
}
if package_data != {
    "encrypticoin_etalon": [
        "contract/BEP20EtalonToken.sol",
        "contract/BEP20EtalonToken.sol.abi",
        "contract/BEP20EtalonToken.sol.bin",
        "contract/BEP20EtalonToken.sol.sha256",
        "contract/common/1/IBEP20.sol",
        "contract/openzeppelin-contracts/4.5.0/access/Ownable.sol",
        "contract/openzeppelin-contracts/4.5.0/token/ERC20/ERC20.sol",
        "contract/openzeppelin-contracts/4.5.0/token/ERC20/IERC20.sol",
        "contract/openzeppelin-contracts/4.5.0/token/ERC20/extensions/IERC20Metadata.sol",
        "contract/openzeppelin-contracts/4.5.0/utils/Context.sol",
        "contract/openzeppelin-contracts/README.txt",
    ]
}:
    raise Exception(f"Package data has changed\n{str(package_data)}")


# Manually cleaning before build is required.
for p in [os.path.join(HERE, "build"), os.path.join(HERE, "dist"), os.path.join(HERE, "encrypticoin-etalon.egg-info")]:
    if os.path.exists(p):
        shutil.rmtree(p)

setup(
    name="encrypticoin-etalon",
    version=VERSION,
    description="Etalon token implementation by Encrypticoin UAB",
    long_description=long_description,
    url="etalon.cash",
    author="Nándor Mátravölgyi",
    author_email="dev@etalon.cash",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=find_packages(where=HERE, include=["encrypticoin_etalon"]),
    # package_data=package_data,
    install_requires=install_requirements,
    # entry_points={"console_scripts": console_scripts},
    extras_require=dict(requirements),
    python_requires=">=3.8",
)