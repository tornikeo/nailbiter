from fabric.api import env, local, run, sudo
from fabric.contrib.files import append, exists, sed

import random
import uuid


# TO RUN: ../app/env/bin/fab deploy:host=tornikeo@SERVER --sudo-password=PASSWORD
# Or use the ./redeploy.sh script
REPO_URL = 'https://github.com/tornikeo/nailbiter.git'
DEBUG=True

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _download_source_from_repo(source_folder)
    _install_docker_and_compose(source_folder)
    _add_user_to_docker_group()
    _create_env_file(source_folder)
    _run_docker_compose(source_folder)

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'source'):
        run(f'mkdir -p {site_folder}/{subfolder}')

def _download_source_from_repo(source_folder):
    if exists(source_folder + '/.git'):
        run(f'cd {source_folder} '
        f'&& git fetch')
    else:
        run(f'git clone {REPO_URL} {source_folder}')
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run(f'cd {source_folder} && git reset --hard {current_commit}')

def _install_docker_and_compose(source_folder):
    sudo('sudo apt-get -y --no-install-recommends update && sudo apt-get upgrade')
    sudo('apt install -y --no-install-recommends docker docker-compose')

def _add_user_to_docker_group():
    pass
    # sudo(f'usermod --append --groups docker {env.user}')
    # run(f'newgrp docker')
    # sudo('systemctl enable docker')

def _create_env_file(source_folder):
    secret_key = str(uuid.uuid4())
    sudo(f"sed 's/DEBUG_VALUE/{DEBUG}/g; " 
             f" s/SECRET_KEY_VALUE/{secret_key}/g; "
             f" s/DJANGO_ALLOWED_HOSTS_VALUE/{env.host}/g' "
             f" env.template | tee {source_folder}/.dev.env ")

def _run_docker_compose(source_folder):
    sudo(f'cd {source_folder} && ./rebuild.sh & disown')





