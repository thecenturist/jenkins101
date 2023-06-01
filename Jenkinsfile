pipeline {
    agent {
        node {
            label 'built-in'
        }
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building"
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