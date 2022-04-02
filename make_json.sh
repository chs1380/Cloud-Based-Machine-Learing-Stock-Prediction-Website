#!/bin/bash
REPOSITORY_URI=${REPO_ECR}
printf '[{"name": "WebContainer","imageUri": "'"$REPOSITORY_URI"'"}]' >imagedefinitions.json