pipeline {
  agent {
    docker {
      image 'python:3.9'
    }

  }
  environment {
    DB_CREDENTIALS = credentials('ryanl')

    DATABASE_HOST = "192.168.0.52"
    DATABASE_NAME = "ryanl"
    DATABASE_USER = "${DB_CREDENTIALS_USR}"
    DATABASE_PASS = "${DB_CREDENTIALS_PSW}"
  }
  stages {
    stage('Build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install pipenv'
          sh '$HOME/.local/bin/pipenv install --deploy --ignore-pipfile'
        }
      }
    }

    stage('Test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh '$HOME/.local/bin/pipenv run python manage.py test'
        }
      }
    }

  }
}