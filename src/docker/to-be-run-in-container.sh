#!/usr/bin/env sh

cat /etc/resolv.conf

echo Copying to /etc/letsencrypt

mkdir -p /etc/letsencrypt/archive/some.domain/
cp /etc/resolv.conf /etc/letsencrypt/archive/some.domain/
ls -laR /etc/letsencrypt
echo "All done inside the container, moving on!"
