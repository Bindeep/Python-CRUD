import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from Src.table_crud import CRUDTable
from urllib.parse import urlparse

class Myhandler(BaseHTTPRequestHandler):

    def __init__(self, *args):
        self.userprofile_object = CRUDTable('postgres')
        super().__init__(*args)

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/json')
        self.end_headers()
        url_path = urlparse(self.path).query
        query = str(url_path)
        # self.dictionary = dict(qc.split(r'=') for qc in query.split(r'&'))
        self.list = list(qc.split(r'=') for qc in query.split(r'&'))
        self.do_write()
    
    def do_write(self):
        self.wfile.write(self.to_json().encode())
    
    def to_json(self):
        if len(self.list[0]) <= 1:
            obj = self.all_users()
        else:
            key = self.list[0][0]
            value = self.list[0][1]
            obj = self.specified_users(key, value)
        return json.dumps(obj)

    def all_users(self):
        return self.userprofile_object.get_all()

    def specified_users(self, key, value):
        return self.userprofile_object.retrieve_user(key, value)

def run(server_class=HTTPServer, handler_class=Myhandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()