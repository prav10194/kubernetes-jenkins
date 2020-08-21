pipeline {
    agent {
        kubernetes {
      yaml """
apiVersion: v1
kind: Pod
metadata:
  name: heroku-example
  labels:
    some-label: heroku
spec:
  securityContext:
    runAsUser: 10000
    runAsGroup: 10000
  containers: 
    - name: jnlp
      image: 'odureg.azurecr.io/jnlp-slave:4.3-4-alpine'
      args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
    - name: heroku
      image: pranavbhatia/heroku:0.2
      volumeMounts:
      - name: var-run
        mountPath: /var/run
  volumes:
    - emptyDir: {}
      name: var-run
"""
    }
    }
    stages {
        stage ('Configuring authentication') {
            steps {
                container('heroku') {
                    sh 'echo "Container 1" && ls -la'
                }
            }
        }
        stage ('Create Heroku App') {
            steps {
                container('heroku') {
                    sh 'echo "Container 2" && ls -la'
                }
            }
        }
    }
}
