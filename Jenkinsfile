pipeline{
    agent {label 'worker-cloud'}
    options{
        buildDiscarder(logRotator(daysToKeepStr: '7'))
        disableConcurrentBuilds()
        timeout(time: 10, unit: 'MINUTES')
    }
    environment {
      
    }
    
    parameters {
        choice(name: 'OPEARTION', choices: ['STOP', 'START'])
    }
    stages{
        stage('Unit Testing'){
            steps{
                sh "echo hello C32"
            }
        }
        stage('Build '){
            steps{
                sh "echo hello C32"
                sh "sleep 8"
            }
        }
    }
    post{
        success{
            slackSend channel: 'jenkins', message: 'build success'
        }
    }
}
