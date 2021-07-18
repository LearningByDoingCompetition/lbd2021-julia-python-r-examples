from random import random
import subprocess
import sys
import time
import zmq


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['julia', 'python', 'r']:
        print('Call either of the following:')
        print('* python3 mockrun.py julia')
        print('* python3 mockrun.py python')
        print('* python3 mockrun.py r')
    else:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(f"ipc://submission-{sys.argv[1]}/socket")

        print(f'Starting controller ./submission-{sys.argv[1]}/start.sh')
        controller = subprocess.Popen([
            '/bin/bash', f'./submission-{sys.argv[1]}/start.sh'])

        print('Waiting for controller to start')
        time.sleep(2)

        code = controller.poll()
        if code is not None and code > 0:
            raise Exception(f'Controller error, exit code {code}')
        else:
            print('Controller started')

        for robot, d_control in [['robot-A', 3], ['robot-B', 5]]:
            for step in range(3):
                if step == 0:
                    print(f'Initialising {robot} on new trajectory')
                query = {
                    'system': robot,
                    'init': step == 0,
                    'd_control': d_control,
                    'state': [random() for _ in range(d_control - 1)],
                    'target': [random() for _ in range(2)],
                    'position': [random() for _ in range(2)],
                }
                print(f'Querying controller for next control input for {robot}')
                socket.send_json(query)
                time.sleep(1)
                while socket.poll(timeout=1000) == 0:
                    pass
                response = socket.recv_json()
                assert len(response) == d_control
                print(f'Received control input of correct length ({d_control})')

        print('Completed mockrun')

        controller.terminate()
        controller.kill()
