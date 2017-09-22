node {
    stage('Prepare') {
      deleteDir()
      git 'https://github.com/helgie/meetup_demo.git'
    }
    stage('Build') {
      sh 'docker build -t "xvfb-python" .'
    }
    stage('Run and archive') {
      sh 'docker run --rm -e "TEST=-s test_demo.py" -w /tests --volume "${PWD}:/tests" --volume "${PWD}:/tests/Screenshots" -t xvfb-python'
      archiveArtifacts allowEmptyArchive: true, artifacts: '*', caseSensitive: false
    }
}
