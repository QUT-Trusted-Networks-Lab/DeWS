# DeWS: A Decentralized and Byzantine Fault-tolerant Web Services

## Prerequisites: 
* Install Tendermint: https://docs.tendermint.com/v0.35/introduction/install.html

* Install Docker: https://docs.docker.com/engine/install/

* Install Docker Compose: https://docs.docker.com/compose/install/

## How to run the WebService integrated Tendermint with 15 nodes:

* Copy .env file and init-docker folder in tendermint home folder (e.g. $TMHOME/init-docker and $TMHOME/.env).

* Replace docker-compose.yml file in tendermint home folder (e.g. $TMHOME/docker-compose.yml). The given docker-compose.yml file contains 15-nodes setup with ABCI application and web servers.

* Change the number of nodes in the Makefile at localnet-start target (In this case, the number of nodes is 15): 
```bash
localnet-start: localnet-stop build-docker-localnode
	@if ! [ -f build/node0/config/genesis.json ]; then docker run --rm -v $(CURDIR)/build:/tendermint:Z tendermint/localnode testnet --config /etc/tendermint/config-template.toml --v 15 --o . --populate-persistent-peers --starting-ip-address 192.167.10.2; fi
	docker-compose up
```

* Go to tendermint home folder: 
    cd $TMHOME

* Create 15 nodes using command: 
```bash
    tendermint testnet --v 15
```
    
* Build the tendermint binary using command: 
```bash
    make build-linux
```

* To start a 15-nodes testnet run: 
```bash
    make localnet-start
```

* To test the GET API run: 
```bash    
    python test_Get_API.py
```

* To test the GET API run: 
```bash
    python test_Post_API.py
```

## The project contains folders and files as following:

### tendermint-abci: Tendermint ABCI application written by Java
This Tendermint ABCI application verifies and logs transactions from web service. 
* Compatible with Tendermint version 0.32.3
* To generate all protobuf-type classes run:
./gradlew generateProto

* How to start the Tendermint ABCI application on local:
./gradlew run

### webservice: APIs integrated Tendermint consensus, written by JavaScript
* Install dependencies : npm install

* To run web service: npm start or node server

### init-docker: contains files to build images.
- abci.Dockerfile: to build tendermint-abci application image.
- webservice.Dockerfile: to build web service image.
- init-script.sql: to initialize database for each web server.

### docker-compose.yml: 
* The default docker-compose.yml file is provided by Tendermint with a 4-nodes setup.

* This file has been modified to launch 15 nodes-testnet associated with the customized ABCI application.

* This also helps to set up multiple Docker containers for the web service. 

### testWS: 
* To test and evaluate the end-to-end delay for POST/GET APIs.
