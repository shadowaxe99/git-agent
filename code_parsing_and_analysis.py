```python
import os
import ast

repository_data = {}

def parse_and_analyze_code(repo_path):
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as source_code:
                    try:
                        tree = ast.parse(source_code.read())
                        analyze_ast(tree, file_path)
                    except Exception as e:
                        print(f"Error parsing file {file_path}: {str(e)}")

def analyze_ast(node, file_path):
    for child_node in ast.iter_child_nodes(node):
        if isinstance(child_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            function_name = child_node.name
            add_function_to_data(function_name, file_path)
        elif isinstance(child_node, ast.Import):
            for alias in child_node.names:
                add_import_to_data(alias.name, file_path)
        elif isinstance(child_node, ast.ImportFrom):
            module_name = child_node.module
            for alias in child_node.names:
                add_import_to_data(f"{module_name}.{alias.name}", file_path)
        analyze_ast(child_node, file_path)

def add_function_to_data(function_name, file_path):
    if file_path not in repository_data:
        repository_data[file_path] = {"functions": [], "imports": []}
    repository_data[file_path]["functions"].append(function_name)

def add_import_to_data(import_name, file_path):
    if file_path not in repository_data:
        repository_data[file_path] = {"functions": [], "imports": []}
    repository_data[file_path]["imports"].append(import_name)
```