pipeline {

  agent any



  stages {

    stage('Checkout') {

      steps { checkout scm }

    }



    stage('Install & Test') {

      steps {

        sh '''

          python3 -m venv venv

          . venv/bin/activate

          pip install -r requirements.txt

          python -m pytest -q

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


