def gitUrl = "https://github.com/rohitvit276/mysite_new.git"
def gitBranch = "master"

 stages {
        stage('GetCode') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "${gitBranch}"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
                    submoduleCfg: [],
                    userRemoteConfigs: [[credentialsId: 'GithubAccess', url: "${gitUrl}"]]])
            }
        }
   
   
stage('build') {
    steps {
        sh 'python aws-boto-creates3.py'
    }
}
