node {
  stage('prepare') {
    deleteDir()
    git 'https://github.com/helgie/meetup_demo.git'
  }
  stage('build') {
    sh 'docker build -t "qafest2017-xvfb" .'
  }
}
