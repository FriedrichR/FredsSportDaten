#!/bin/bash
conda create --name sportyspice
source activate sportyspice
conda env update --file ./environment.yml
conda install -n sportyspice -c conda-forge ds-lime