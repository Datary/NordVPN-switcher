#! /bin/sh
#
# @example
# ./scripts/upload.sh pekebuda myStrongPassword 0.0.1rc1
#
# @important
# ejecutar desde la raiz del proyecto

twine upload --repository-url http://pypi.registry.rtm.datary.io:8080 --skip-existing --username $1 --password $2 dist/datary-nordvpn-switcher-$3.tar.gz
