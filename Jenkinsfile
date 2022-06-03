pipeline{
    agent {label 'worker-cloud'}
    options{
        buildDiscarder(logRotator(daysToKeepStr: '7'))
        disableConcurrentBuilds()
        timeout(time: 10, unit: 'MINUTES')
    }
    
    stages{
        stage('git-checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/priyanka-ajay-c32/ec2startstop.git' 
            }
        }
        
        stage('run Python script'){
            steps{
                sh "pwd"
                sh "python3 stop.py"
            }
        }
    }
}
