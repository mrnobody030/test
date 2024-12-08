#!/bin/bash

wget https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_118.0.2088.53-1_amd64.deb

# Confirm installation
microsoft-edge --version

python test.py
