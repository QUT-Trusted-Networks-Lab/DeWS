import requests
import random, time
import json
# TEST 15 Nodes
base_url = "http://localhost:6881/customers"
headers =  {"Content-Type":"application/json"}

def get_customer_API(consensus_param):
    url = base_url + '/all?consensus=' + str(consensus_param)

    t0 = time.time()
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        t1 = time.time()
        time_taken = (t1 - t0) * 1000 #convert to milliseconds
        return time_taken, response.json()
    return -1, response.error

if __name__ == "__main__":
    print('================ Evaluate time difference calling get all customers GET API ================')
    average_time_without_consensus = 0;
    average_time_with_consensus = 0;
    result_file = '15_NODES_EVALUATE_POST.csv'
    with open(result_file, 'w') as file:
        file.write("No., Time without consensus(s), Time with consensus(s), End-to-end Delay, Response without consensus, Response with consensus\n")
    n_time = 1000
    for i in range(n_time):
        print("================================CALLING NO.{:d}: ================================".format(i+1))
        print('================================ WITHOUT CONSENSUS ================================')
        
        time_without_consensus, response_without_consensus = get_customer_API(0)
        if(time_without_consensus < 0):
            print('Error when calling API')
        average_time_without_consensus += time_without_consensus
        print("         Time taken: {:.5f} ".format(time_without_consensus))

        print('================================ WITH CONSENSUS ================================')
        time_with_consensus, response_with_consensus = get_customer_API(1)
        if(time_with_consensus < 0):
            print('Error when calling API')
        average_time_with_consensus += time_with_consensus
        print("         Time taken: {:.5f} ".format(time_with_consensus))
        time.sleep(30)
        with open(result_file, 'a') as file:
            file.write("{:d}, {:.5f}, {:.5f}, {:.5f}, {}, {}\n".format(i+1, time_without_consensus, time_with_consensus, time_with_consensus - time_without_consensus, response_without_consensus['consensusData'], response_with_consensus['consensusData']))
    average_time_without_consensus = average_time_without_consensus / n_time
    average_time_with_consensus = average_time_with_consensus / n_time
    print('\nAVERAGE TIME TAKEN without consensus {:.5f} (seconds)'.format(average_time_without_consensus))
    print('AVERAGE TIME TAKEN with consensus {:.5f} (seconds)'.format(average_time_with_consensus))
    print('FINISHED')
    with open(result_file, 'a') as file:
            file.write("\n{}, {:.5f}, {:.5f}, {:.5f}\n".format('AVERAGE', average_time_without_consensus, average_time_with_consensus, average_time_with_consensus - average_time_without_consensus))
    