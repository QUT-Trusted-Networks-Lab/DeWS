const axios = require('axios'); 

const TENDERMINT_URL = process.env.TENDERMINT_URL ;

exports.sendTxData = async(requestMethod, apiInfo, requestURL, requestData, responseData) => {
    // 1. Prepare tx data to send  
    const SERVER_INFO = process.env.SERVER_INFO;
    const txBody = {
        serverInfo: SERVER_INFO,
        requestURL: requestURL,
        requestMethod: requestMethod,
        apiInfo: apiInfo,
        requestTime: new Date(),
        requestData: requestData,
        responseData: responseData
    }
    
    // 2. Call Consensus
    const tendermintResponse = await callConsensus(txBody);
    return tendermintResponse;
}

callConsensus = async(txBody) => {
    const objJsonStr = JSON.stringify(txBody);
    const buff = Buffer.from(objJsonStr, 'utf-8');
    const objJsonB64 = buff.toString('base64');
    const response = await axios({
                url: TENDERMINT_URL + '/broadcast_tx_commit',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                params: {
                    tx : `"${objJsonB64}"`,
                    id: 0011
                },
              })
    return response.data;
}

