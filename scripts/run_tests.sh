#!/usr/bin/env bash

set -e

# shellcheck disable=SC2005
readonly SCRIPTSDIR="$(cd "$(dirname "${0}")"; echo "$(pwd)")"

cd_project_root() {
    echo '> cd to project root'
    pushd "${SCRIPTSDIR}" && pushd ..
}

restore_previous_working_dir() {
    echo '> Restore previous working directory'
    popd && popd
    echo
}

run_pytest() {
    echo
    echo '> Run pytest'
    py.test .
}

run_flake8() {
    echo
    echo '> Run flake8'
    echo -n 'Total errors: '
    flake8 . --count
}


main() {
    cd_project_root
    run_pytest
    run_flake8
    restore_previous_working_dir

    echo & echo 'Finished.'
}

main
