#!/bin/sh

../app/env/bin/fab \
    deploy:host=tornikeo@$REMOTE_ADDRESS \
    --sudo-password=$REMOTE_SUDO_PASSWORD
