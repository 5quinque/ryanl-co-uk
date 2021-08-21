pipeline {
  agent {
    docker {
      image 'python:3.9'
    }

  }
  environment {
    DATABASE_HOST = "localhsot"
    DATABASE_NAME = "ryanl"
    DATABASE_USER = "root"
    DATABASE_PASS = "rootpass"
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
      agent {
          docker {
            image 'mariadb'
            args '-e MYSQL_ROOT_PASSWORD=rootpass'
          }
      }
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh '$HOME/.local/bin/pipenv run python manage.py test'
        }
      }
    }

  }
}