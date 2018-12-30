#! /usr/bin/bash


echo "export PYTHONPATH=$PYTHONPATH:$PWD" >> ~/.bashrc

exec bash
