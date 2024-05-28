# uxto-set-experiments

# Prerequisites

    - A C++20 compatible compiler (gcc, clang, MSVC)
    - cmake 3.15 or above
    - Python 3 and pip

# Optionally, use a Python Virtual Environment
You might want or need to use a virtual environment to isolate your Python
installation from your system's default.

`python -m venv /my-virtual-environment`

It's usually a good idea to keep your virtual environment inside of the project's
folder, excluded from version control so we don't commit it by mistake.

`echo "my-virtual-environment" >> .gitignore`

When using this, all commands from here on that use a Python binarie must be
run by prepending `./my-virtual-environment/bin/` and then the binary,
like `conan` or `pip`.

# Install Conan

We need python 3 and pip to install Conan

`pip install conan --user --upgrade`

* If using a Python virtual environment, `--user` is not needed.

Verify `conan` instalation

`conan --version`

# Build

## Prepare the dependencies

We install the Knuth related dependencies:
```
pip install kthbuild --user --upgrade

conan remote add kth https://packages.kth.cash/api

conan config install https://github.com/k-nuth/ci-utils/raw/master/conan/config2023.zip

```

And then those specified in the Conan recipe:
```
conan lock create conanfile.py --version "1.0" --lockfile=conan.lock --lockfile-out=build/conan.lock
conan install conanfile.py --lockfile=build/conan.lock -of build --build=missing
```

## Build the program

```
cmake --preset conan-release \
         -DCMAKE_VERBOSE_MAKEFILE=ON \
         -DGLOBAL_BUILD=ON \
         -DCMAKE_BUILD_TYPE=Release

cmake --build --preset conan-release -j4 \
         -DCMAKE_VERBOSE_MAKEFILE=ON \
         -DGLOBAL_BUILD=ON \
         -DCMAKE_BUILD_TYPE=Release
```

# Run

```
./build/build/Release/uxto-set-experiments
```

If all worked, you should see a "Hello, World!".
