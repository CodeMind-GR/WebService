pipeline {
    agent any

    environments {
        DOCKER_IMAGE = 'your_docker_image_name' // 도커 이미지 이름을 지정하세요.
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Deploy on Develop Instance') {
            when {
                branch 'develop'
            }
            steps {
                script {
                    sshPublisher(
                        publishers: [
                            sshPublisherDesc(
                                configName: 'develop-instance-ssh', // Jenkins에 설정된 SSH connection 이름
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: '**/*',
                                        removePrefix: 'path/to/your/source', // 필요시 설정
                                        remoteDirectory: '/var/src/Service',
                                        execCommand: '''
                                            cd /var/src/Service &&
                                            docker build -t ${DOCKER_IMAGE}:develop . &&
                                            docker stop $(docker ps -q --filter ancestor=${DOCKER_IMAGE}:develop) || true &&
                                            docker rm $(docker ps -a -q --filter ancestor=${DOCKER_IMAGE}:develop) || true &&
                                            docker run -d --name my-app ${DOCKER_IMAGE}:develop
                                        '''
                                    )
                                ]
                            )
                        ]
                    )
                }
            }
        }

        stage('Build and Deploy on Service Instance') {
            when {
                branch 'main'
            }
            steps {
                script {
                    sshPublisher(
                        publishers: [
                            sshPublisherDesc(
                                configName: 'service-instance-ssh', // Jenkins에 설정된 SSH connection 이름
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: '**/*',
                                        removePrefix: 'path/to/your/source', // 필요시 설정
                                        remoteDirectory: '/var/src/Service',
                                        execCommand: '''
                                            cd /var/src/Service &&
                                            docker build -t ${DOCKER_IMAGE}:latest . &&
                                            docker stop $(docker ps -q --filter ancestor=${DOCKER_IMAGE}:latest) || true &&
                                            docker rm $(docker ps -a -q --filter ancestor=${DOCKER_IMAGE}:latest) || true &&
                                            docker run -d --name my-app ${DOCKER_IMAGE}:latest
                                        '''
                                    )
                                ]
                            )
                        ]
                    )
                }
            }
        }
    }
}

