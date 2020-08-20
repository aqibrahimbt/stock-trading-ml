"""Module that provides a class to make import of models more abstract."""

from importlib.abc import InspectLoader
from ast import parse, fix_missing_locations, NodeTransformer
import ast


class ModelInspectLoader(InspectLoader):
    """Provides functionality for abstract model imports from standardized files."""
    def __init__(self, input_shape=None, output_mask=None):
        """"""
        self.input_shape = input_shape
        self.output_mask = output_mask

    def import_model(self, fullname):
        """Return a model from the specified file as if it where imported.

        :param fullname: TODO
        :returns: TODO

        """
        code = self.get_code(fullname)
        # python < 3.7
        nmspace = {}
        exec(code, nmspace)
        # python >= 3.7:
        # exec(code, (nmspace := {}))
        return nmspace['model']

    def get_source(self, fullname):
        """Provide source code object for a module in the models directory.

        :param fullname: str or pathlib.Path
        :returns: str

        """
        with open(fullname) as f:
            s = f.read()
        return s

    def get_ast(self, fullname):
        source = self.get_source(fullname)
        tree = parse(source)
        return tree

    def transform_ast(self, tree):
        """Transforms an ast to fit to the requested attributes.

        :param tree: ast - python abstract syntax tree
        :returns: ast

        """
        class ReplaceShapeNode(NodeTransformer):
            """Small implementation of a NodeTransformer class."""
            if self.input_shape:
                shape_string = str(self.input_shape)
                # parsing shape_string to an ast node defining a tuple
                tuple_node = parse(shape_string).body[0].value
            else:
                tuple_node = None

            def visit_Assign(self, node):
                """Define behaviour when visiting Assign-node."""
                if node.targets[0].id == 'shape' and self.tuple_node:
                    node.value = self.tuple_node
                    print('Replaced!')
                return node

        tree = ReplaceShapeNode().visit(tree)
        fix_missing_locations(tree)  # fixing node line numbers for compiler
        return tree

    def get_code(self, fullname):
        """Return the code object for the specified module.

        :param fullname: TODO
        :returns: TODO

        """
        tree = self.get_ast(fullname)
        transformed = self.transform_ast(tree)
        print(transformed)
        print(ast.dump(transformed))
        code = compile(transformed, filename='<ast>', mode='exec')
        return code

    def is_package(self, fullname):
        """TODO: Docstring for is_package.

        :param fullname: TODO
        :returns: TODO

        """
        pass
