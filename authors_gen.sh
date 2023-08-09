#!/bin/bash

set -e

SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOTDIR="$(git -C "$SCRIPTDIR" rev-parse --show-toplevel)"

set -x

cat > "${ROOTDIR}/AUTHORS" <<- EOF
	# File @generated from authors_gen.sh. DO NOT EDIT.
	# This file shows the contributors to this repository.
	# See authors_gen.sh to make modifications.
	$(git -C "$ROOTDIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
