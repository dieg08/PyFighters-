'''
A rough code outline of how I think packets should be handled for multiplayer
in pyfighters
'''
def thoughts():
    listen()
    while(!GameOver):
        recv(packet)
        queue.put(packet)
        send(queue2.pop)

