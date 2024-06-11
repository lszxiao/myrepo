import os,sys

# basePath=os.path.dirname(os.path.abspath(__file__))
# sys.path.append(basePath)

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        if self.check_file_exite():
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        else:
            return "file not exite"

    def write_file(self, content):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    def check_file_exite(self):
        if os.path.exists(self.file_path):
            return True
        else:
            return False

if __name__=="__main__":
    # file_handler = FileHandler('example.txt')
    
    # content = file_handler.read_file()
    # print(content)
    # file_handler.write_file('这是一段新的内容')
    # content = file_handler.read_file()
    # print(content)
    print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    print(os.path.dirname(os.path.abspath(__file__)))

    
