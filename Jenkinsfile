node {
    stage('Prepare') {
      deleteDir()
      git 'https://github.com/helgie/meetup_demo.git'
    }
    stage('Build') {
      sh 'docker build -t "xvfb-python" .'
    }
}
