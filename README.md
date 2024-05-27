# uxto-set-experiments

# Prerequisites
    - A C++20 compatible compiler (gcc, clang, MSVC)
    - cmake 3.15 or above

# Install Conan

We need python 3 and pip to install Conan

`pip install conan --user --upgrade`


Verify `conan` instalation

`conan --version`

# Build

## Prepare the dependencies

```
conan lock create conanfile.py --version "1.0" --lockfile=conan.lock --lockfile-out=build/conan.lock
conan install conanfile.py --lockfile=build/conan.lock -of build --build=missing
```

## Build the program

cmake --preset conan-release \
         -DCMAKE_VERBOSE_MAKEFILE=ON \
         -DGLOBAL_BUILD=ON \
         -DCMAKE_BUILD_TYPE=Release

cmake --build --preset conan-release -j4 \
         -DCMAKE_VERBOSE_MAKEFILE=ON \
         -DGLOBAL_BUILD=ON \
         -DCMAKE_BUILD_TYPE=Release

# Run

```
./build/build/Release/uxto-set-experiments
```