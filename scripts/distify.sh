#! /bin/sh
#
# @example
# ./scripts/distify.sh
#
# @important
# ejecutar desde la raiz del proyecto

python3 ./setup.py sdist bdist_wheel
