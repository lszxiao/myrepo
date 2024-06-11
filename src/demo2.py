from pycparser import c_parser, c_ast

def analyze_c_code(c_code):
    parser = c_parser.CParser()
    ast = parser.parse(c_code)
    return ast

def print_ast(node, indent=0):
    if isinstance(node, c_ast.Node):
        print(' ' * indent + node.__class__.__name__)
        for child in node.children():
            print_ast(child, indent + 2)
    elif isinstance(node, list):
        for item in node:
            print_ast(item, indent)
    else:
        print(' ' * indent + str(node))

if __name__ == '__main__':
    c_code = '''
    int main() {
        int a = 10;
        int b = 20;
        int c = a + b;
        return c;
    }
    '''
    ast = analyze_c_code(c_code)
    print_ast(ast)
