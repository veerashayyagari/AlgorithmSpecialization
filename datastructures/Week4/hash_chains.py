# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(self.bucket_count)]

    # interesting way of implementing
    # starts with s[|s| - 1]
    # then gets multiplied by x in each iteration
    # second iteration it becomes s[|s| - 1]*x + s[|s| - 2]
    # third iteration it becomes s[|s| - 1]*x^2 + s[|s| - 2]*x + s[|s| - 3]
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, chain):
        print('yes' if len(chain) > 0 else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(reversed(self.elems[query.ind]))
        else:            
            if query.type == 'find':                
                chainIdx = self._hash_func(query.s)
                chain = list(filter(lambda x : x == query.s,self.elems[chainIdx]))
                self.write_search_result(chain)
            elif query.type == 'add':
                chainIdx = self._hash_func(query.s)
                chain = list(filter(lambda x : x == query.s,self.elems[chainIdx]))
                if len(chain) == 0:
                    self.elems[chainIdx].append(query.s)                
            else:
                chainIdx = self._hash_func(query.s)
                try:
                    self.elems[chainIdx].remove(query.s)
                except ValueError:
                    pass

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
