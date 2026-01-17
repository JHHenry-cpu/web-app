pipeline {

  agent any



  stages {

    stage('Checkout') {

      steps { checkout scm }

    }



    stage('Install & Test (APT)') {

      steps {

        sh '''

          set -e

          apt-get update

          apt-get install -y python3 python3-pip python3-pytest python3-flask

          python3 -m pytest -q

        '''

      }

    }



    stage('Build Docker Image') {

      steps {

        sh 'docker build -t web-app:latest .'

      }

    }

  }

}


