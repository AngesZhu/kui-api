#!/bin/bash

script_path=$(dirname "$(readlink -f "$0")")

export PYTHONPATH="$script_path:$script_path:$PYTHONPATH"

result=$(python $script_path/loading_config.py $script_path)

runweb -s waitress -a main:app --reload -b $result
