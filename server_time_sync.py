import SocketServer
import time


class UDPHandler(SocketServer.BaseRequestHandler):


    def process_request(self,action,data):
        actions_map = {"check_and_update":self.server.board.check_and_update,
                       "postions":self.server.board.player_postions,
                       "pickup": self.server.board.pickup}
        func = actions_map.get(action)
        return func(*data)

    def handle(self):
    	received_time =  time.time()
        data = self.request[0].strip().split(" ")
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        seq =  data[0]
        client_time_stamp = data[1]
        server_time = time.time() 
        pay_load = seq + " " + client_time_stamp + " " + str(received_time) + " " + str(server_time)
        socket.sendto( pay_load , self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.UDPServer((HOST, PORT), UDPHandler)
    #server.board = BoardGame() Monkey path to include the object
    server.serve_forever()