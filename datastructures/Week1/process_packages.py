# python3
from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time
        self.finish_time = None

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.finish_time = 0

    def Process(self, req):
        if len(self.queue) < self.size:
            if self.finish_time >= req.arrival_time:
                res = Response(False,self.finish_time)
                self.finish_time += req.process_time
            else:
                res = Response(False,req.arrival_time)
                self.finish_time = req.arrival_time + req.process_time
            req.finish_time = self.finish_time
            self.queue.append(req)
            return res

        if len(self.queue) == self.size and self.size > 0:
            if req.arrival_time >= self.queue[0].finish_time:
                self.queue.popleft()
                if self.finish_time >= req.arrival_time:
                    res = Response(False,self.finish_time)
                    self.finish_time += req.process_time
                else:
                    res = Response(False,req.arrival_time)
                    self.finish_time += req.arrival_time + req.process_time
                
                req.finish_time = self.finish_time
                self.queue.append(req)
                return res

        return Response(False, -1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
