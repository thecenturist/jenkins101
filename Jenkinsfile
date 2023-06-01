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
                echo "Building1"
                sh '''
                echo "doing test stuff.."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testin.."
                sh '''
                echo "doing test stuff.."
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