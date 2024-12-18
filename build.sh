#!/bin/bash

SERVER="."
WEB="../gymapp-web"

#######################################
#
# COMPILAR WEB
#
#######################################
echo -e "\n\n---- Compilar react ----\n"
npm --prefix "./$WEB" run build

echo -e "\n\n---- Borrar anteriores ----\n"
rm -r "$SERVER/static"
rm "$SERVER/templates/index.html"

echo -e "\n\n---- Mover ficheros ----\n"
cp -r "$WEB/dist/static" "$SERVER/static"
cp "$WEB/dist/index.html" "$SERVER/templates"

#######################################
#
# COMPILAR DOCKER
#
#######################################

docker build -t gymapp-api-v1:latest .
