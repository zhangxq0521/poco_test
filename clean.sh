#!/usr/bin/env bash

for folder in "package" "build_x86" "test_package/build"; do
	if [ -e ${folder} ]; then rm -rf ${folder}; fi;
done




