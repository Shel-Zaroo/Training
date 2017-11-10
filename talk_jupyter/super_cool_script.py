import time


def run(answer):
    print(
        '\nPreparing to run the deep neural nets on the blockchain on %s'
        % answer)

    time.sleep(1)
    print('\n\nFitting the Deep Neural Net...')
    for i in range(50):
        print('.', end='')
        time.sleep(0.05)

    time.sleep(.5)
    print('\n\nFitting the even deeper neural network with RNNs...')
    for i in range(50):
        print('.', end='')
        time.sleep(0.05)

    time.sleep(.5)
    print('\n\nPrinting the Smart Contract on the Blockchain...')
    for i in range(10):
        print('.', end='')
        time.sleep(0.2)
    time.sleep(1)
    print('\n\nWaiting for the ink to dry...')
    time.sleep(2)
    print('\n\nComplete. Damn that was impressive.')
