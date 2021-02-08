#!/usr/bin/env bash

conan install . --install-folder build_x86 --build=OpenSSL --build=Poco --build=zlib

conan build . --build-folder build_x86
