#!/bin/bash
ALLURE_ENDPOINT='http://10.23.9.53:8080/'
ALLURE_PROJECT_ID=6
ALLURE_TOKEN='63ef9731-c6dc-4b35-8077-aa7c059e248d'
run(){
  if [[ $OSTYPE == linux* ]]; then
    echo 'linux'
    chmod +x allurectl_linux
    ./allurectl_linux upload --endpoint=$ALLURE_ENDPOINT \
      --token=$ALLURE_TOKEN --project-id=$ALLURE_PROJECT_ID ./allure-results
  elif [[ $OSTYPE == darwin* ]]; then
    echo 'mac'
    chmod +x allurectl_mac
    ./allurectl_mac upload --endpoint=$ALLURE_ENDPOINT \
      --token=$ALLURE_TOKEN --project-id=$ALLURE_PROJECT_ID ./allure-results
  else 
    echo $OSTYPE
  fi
}
run
