#!/usr/bin/env bash

conan export . samuel/testing

conan install poco_test/0.1@samuel/testing --build=poco_test
