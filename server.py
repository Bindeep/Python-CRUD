import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from src.table_crud import CRUDTable
from urllib.parse import urlparse
import re
from htmls.home import write_data
import os

ROOT_DIR = os.getcwd()
HTML_DIR = os.path.join(ROOT_DIR, 'htmls')

class FileRenderes:

    def file_downloader(self, file_name):
        file_path = os.path.join(HTML_DIR ,file_name)
        file_content = ''
        with open(file_path, 'rb') as f:
            file_content = f.read()
        return file_content

class Determiner:

    def method_determiner(self, url):
        methods = {'create': 'CREATE', 'read': 'READ', 'update': 'UPDATE', 'delete' :'DELETE',
        'static': 'STATIC'}
        home = re.compile(r'^/home/?$')
        view = re.compile(r'^/(home)/(\d+)/?$')
        update = re.compile(r'^/(\d+)/(update)/?$')
        delete = re.compile(r'^/(\d+)/(delete)/?$')
        create = re.compile(r'^/create/?$')
        static = re.compile(r'^/(\w+/)?(\w+\.css)$')

    
        if re.match(home, url):
            return methods.get('read'), None

        elif re.match(view ,url):
            return methods.get('read'), {'id': re.search(view, url).group(2)}

        elif re.search(update, url):
            return methods.get('update'), {'id': re.search(update, url).group(1)}
            
        elif re.search(delete, url):
            return methods.get('delete'), {'id': re.search(delete, url).group(1)}
        
        elif re.search(create, url):
            return methods.get('create'), None

        elif re.search(static, url):
            return methods.get('static') ,{'content': re.search(static, url).group(2)}

        else:
            return None, None


class Myhandler(BaseHTTPRequestHandler, Determiner, FileRenderes):

    def __init__(self, *args):
        self.userprofile_object = CRUDTable('postgres')
        super().__init__(*args)
    
    def set_headers(self, responses, status, content_type):
        self.send_response(int(responses), message=status)
        if int(responses) == 200:
            # self.send_response(int(responses), message=status)
            self.send_header('content-type', f'text/{content_type}')
        elif int(responses) == 301:
            self.send_header('Location', content_type)
        self.end_headers()

    def do_GET(self):
        method, id_dict = self.method_determiner(self.path)
        if method == 'READ':
            if id_dict is None:
                self.set_headers(200, 'OK', 'html')
                self.wfile.write(write_data(self.all_users()).encode())
            else:
                id = id_dict.get('id')
                self.set_headers(200, 'OK', 'html')
                self.wfile.write(write_data(self.specified_users(int(id))).encode())
        
        elif method == 'CREATE':
            form = ''
            with open('htmls/form.html') as f:
                for _ in f:
                    form += f.read()
            populated_html = re.sub(r'@@value@@', '', form)
            populated_html = re.sub(r'@@action@@', 'create', populated_html)
            self.set_headers(200, 'OK', 'html')
            self.wfile.write(populated_html.encode())
        
        elif method == 'DELETE':
            if id_dict is not None:
                id = id_dict.get('id')
                self.userprofile_object.delete_user('id', int(id))
            self.set_headers(301, 'DELETED', '/home')
        
        elif method == 'UPDATE':
            if id_dict is not None:
                id = id_dict.get('id')
                user_data = self.specified_users(int(id))
                form = ''
                with open('htmls/form.html', 'r') as f:
                    for _ in f:
                        form += f.read()
                data_list = user_data[0][:]
                populated_html = re.sub(r'@@value@@', '{}', form).format(*data_list)
                populated_html = re.sub(r'@@action@@', 'update', populated_html).format(id)
                self.set_headers(200, 'OK', 'html')
                self.wfile.write(populated_html.encode())
        
        elif method == 'STATIC':
            content = super().file_downloader(str(id_dict.get('content')))
            self.set_headers(200, 'OK', 'css')
            self.wfile.write(content)
    
    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        datas = data_string.decode()
        dictionary = {data.split('=')[0]: data.split('=')[1] for data in datas.split('&')}
        method = self.method_determiner(self.path)
        if method[0] == 'CREATE':
            self.userprofile_object.insert_into_table(**dictionary)
            self.set_headers(301, 'CREATE', '/home')
        elif method[0] == 'UPDATE':
            self.userprofile_object.update_into_table(**dictionary)
            self.set_headers(301, 'UPDATE', '/home')

    def do_write(self, obj):
        self.wfile.write(self.to_json(obj).encode())
    
    def to_json(self, obj):
        return json.dumps(obj)

    def all_users(self):
        return self.userprofile_object.get_all()

    def specified_users(self, value):
        return self.userprofile_object.retrieve_user('id', value)
    
    def insert_user(self, dictionary):
        return self.userprofile_object.insert_into_table(**dictionary)

    def delete_user(self, value):
        return self.userprofile_object.delete_user('id', value)
        

def run(server_class=HTTPServer, handler_class=Myhandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()




# class ContentWriter:

#     def write(self):
#         Myhandler.do_GET()
# class CRUDHandler(Myhandler):

#     def do_read():


# import http.server
# import socketserver
# import os

# PORT = 8000

# web_dir = os.path.join(os.path.dirname(__file__), 'static')
# os.chdir(web_dir)

# Handler = http.server.SimpleHTTPRequestHandler
# httpd = socketserver.TCPServer(("", PORT), Myhandler)
# print("serving at port", PORT)
# httpd.serve_forever()