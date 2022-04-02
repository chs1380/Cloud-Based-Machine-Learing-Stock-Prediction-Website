#!/bin/bash
IMAGE_NAME=${Container_Name}
REPOSITORY_URI=${REPO_ECR}
printf '[{"name": "'"$IMAGE_NAME"'","imageUri": "'"$REPOSITORY_URI"'"}]' >imagedefinitions.json