pipeline {
  agent {
    docker {
      image 'python:3.9'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'pip install pipenv'
        sh 'pipenv install --deploy --ignore-pipfile'
      }
    }

    stage('Test') {
      steps {
        sh 'python manage.py test'
      }
    }

  }
}