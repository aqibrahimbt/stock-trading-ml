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

    def get_source(self, fullname):
        """Provide source code object for a module in the models directory.

        :param fullname: str or pathlib.Path
        :returns: keras.model

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

        :param tree: TODO
        :returns: TODO

        """
        class ReplaceShapeNode(NodeTransformer):
            """Small implementation of a NodeTransformer class."""
            shape_string = str(self.input_shape)
            tuple_node = parse(shape_string).body[0].value

            def visit_Assign(self, node):
                """Define behaviour when visiting Assign-node."""
                if node.targets[0].id == 'shape':
                    node.value = self.tuple_node
                    print('Replaced!')
                return node

        tree = ReplaceShapeNode().visit(tree)
        fix_missing_locations(tree)
        return tree

    def get_code(self, fullname):
        """Return the code object for the specified module.

        :param fullname: TODO
        :returns: TODO

        """
        tree = self.get_ast(fullname)
        tree = self.transform_ast(tree)
        print(tree)
        print(ast.dump(tree))
        code = compile(tree, filename='<ast>', mode='exec')
        return code

    def import_model(self, fullname):
        """Return a model from the specified file as if it where imported.

        :param fullname: TODO
        :returns: TODO

        """
        code = self.get_code(fullname)
        exec(code, (nmspace := {}))
        return nmspace['model']

    def is_package(self, fullname):
        """TODO: Docstring for is_package.

        :param fullname: TODO
        :returns: TODO

        """
        pass
