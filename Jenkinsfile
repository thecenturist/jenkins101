pipeline {
    agent {
        node {
            label 'built-in'
        }
    }

    triggers {
        pollSCM '*/5 * * * *'
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testin.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Centurist
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}