#!/usr/bin/env bash

DIR=$(
	cd "$(dirname "${BASH_SOURCE[0]}")" \
		>/dev/null 2>&1 && pwd
)

ROOT_DIR="${DIR}/.."

t-rec \
	--natural \
	--quiet \
	--decor none \
	--bg white \
	-e2s \
	"${ROOT_DIR}/bin/animation.py"

WIDTH=$(
	gifsicle --size-info t-rec.gif |
		head -n2 |
		tail -n1 |
		awk '{ print $3 }' |
		tr -d ' ' |
		sed 's/x/,/'
)

gifsicle \
	--crop "0,30-${WIDTH}" \
	"${ROOT_DIR}/t-rec.gif" >"${ROOT_DIR}/animation.gif"
