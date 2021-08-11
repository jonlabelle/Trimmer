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
}

install_pip_requirements() {
    echo '> Install pip requirements'
    pip3 install -r requirements.txt
}

main() {
    cd_project_root
    resolve_pip_cmd "$(python_major_version)"
    install_pip_requirements
    restore_previous_working_dir

    echo && echo 'Finished.'
}

main
