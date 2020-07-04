from fabric.api import env, local, run, sudo
from fabric.contrib.files import append, exists, sed

import random


# TO RUN: ../app/env/bin/fab deploy
# Or use the ./redeploy.sh script
REPO_URL = 'https://github.com/tornikeo/nailbiter.git'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = site_folder + '/source'
    _clear_site_folder(site_folder)
    _create_directory_structure(site_folder)
    _download_source_from_repo(source_folder)
    _install_docker_and_compose(source_folder)
    _run_docker_compose(source_folder)

def _clear_site_folder(site_folder):
    if exists(site_folder):
        sudo(f'rm -rf {site_folder}/*')
    run(f'mkdir -p {site_folder}')

def _create_directory_structure(site_folder):
    run(f'mkdir -p {site_folder}/source')

def _download_source_from_repo(source_folder):
    run(f'cd {source_folder} '
     f'&& git clone --depth 1 {REPO_URL} {source_folder}')
    # current_commit = local('git log -n 1 --format=%H', capture=True)
    # run(f'cd {source_folder} && git reset --hard {current_commit}')

def _install_docker_and_compose(source_folder):
    sudo('sudo apt-get -y update && sudo apt-get upgrade')
    sudo('apt install -y docker docker-compose')
    sudo('apt install -y docker-compose')

def _run_docker_compose(source_folder):
    run(f'cd {source_folder} && ./rebuild.sh')





