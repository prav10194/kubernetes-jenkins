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
  containers: 
    - name: jnlp
      image: 'odureg.azurecr.io/jnlp-slave:4.3-4-alpine'
      args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
    - name: heroku
      image: pranavbhatia/heroku:0.3
      volumeMounts:
      - name: var-run
        mountPath: /var/run
  volumes:
    - emptyDir: {}
      name: var-run
"""
    }
    }
    environment {
        EMAIL_ID = credentials('HEROKU_ID')
        API_KEY = credentials ('HEROKU_API_KEY')
    }
    stages {
        stage ('Configuring authentication') {
            steps {
                container('heroku') {
                    sh ''' 
                    cat > ~/.netrc << EOF
machine api.heroku.com
  login $EMAIL_ID
  password $API_KEY
machine git.heroku.com
  login $EMAIL_ID
  password $API_KEY
EOF
                    '''
                }
            }
        }
        stage ('Create Heroku App') {
            steps {
                container('heroku') {
                    sh '''git clone https://github.com/prav10194/kubernetes-jenkins && \
                    cd heroku-flask && \
                    git init && git add . && git commit -m "Adding files" && \
                    heroku create && \
                    git push heroku master && heroku ps:scale web=1'''
                }
            }
        }
    }
}
