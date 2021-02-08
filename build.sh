#!/usr/bin/env bash

conan install . --install-folder build_x86

conan build . --build-folder build_x86
