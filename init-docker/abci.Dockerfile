FROM gradle:7.3.0-jdk11 AS builder

WORKDIR /app

ENV GIT_URL="https://github.com/QUT-Trusted-Networks-Lab/DeWS/archive/main.zip"

RUN wget "${GIT_URL}" -P /app

RUN unzip /app/main.zip

WORKDIR /app/DeWS-main/tendermint-abci 

USER root 
RUN chown -R gradle /app/DeWS-main/tendermint-abci
USER gradle              

RUN ./gradlew clean

RUN ./gradlew generateProto

RUN ./gradlew build --no-daemon

EXPOSE 26658

ENTRYPOINT ["./gradlew"]
CMD ["run", "--no-daemon"]
