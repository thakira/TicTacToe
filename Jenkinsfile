pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile src/main/python/TicTacToe.py src/main/python/Settings.py src/main/python/Grid.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}