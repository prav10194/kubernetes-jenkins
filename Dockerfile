FROM python:3.6.12-alpine3.12

# Installing necessary packages and heroku
RUN apk --no-cache add curl bash nodejs npm git && \
    curl https://cli-assets.heroku.com/install.sh | sh

# To keep the container running
CMD tail -f /dev/null
