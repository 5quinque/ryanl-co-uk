pipeline {
  agent {
    docker {
      image 'python:3.9'
    }
  }

  environment {
    SECRET_KEY = "jenkins-test-secret-key"
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