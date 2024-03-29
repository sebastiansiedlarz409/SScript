from parser.nodes.nodes import *

class StructNode(Node):
    def __init__(self):
        self.name: str = None
        self.parent: str = None
        self.body: list[Node] = []

    def setBody(self, body: list[Node]):
        self.body = body

    def setName(self, name: str):
        self.name = name.upper()

    def setParent(self, parent: str):
        self.parent = parent.upper()

    def __repr__(self) -> str:
        ret = f"struct {self.name}({'' if self.parent == None else self.parent}):"
        for b in self.body:
            ret += f"\n{b}"
        return ret

class ImplNode(Node):
    def __init__(self):
        self.name: str = None
        self.parent: str = None
        self.body: list[Node] = []

    def setBody(self, body: list[Node]):
        self.body = body

    def setName(self, name: str):
        self.name = name.upper()

    def setParent(self, parent: str):
        self.parent = parent.upper()

    def __repr__(self) -> str:
        ret = f"impl {self.name}({'' if self.parent == None else self.parent}):"
        for b in self.body:
            ret += f"\n{b}"
        return ret

class DeclareFieldAssignNode(Node):
    def __init__(self):
        self.identifier: str = None
        self.child: Node = None
        self.const: bool = False

    def setIdentifier(self, identifier: str):
        self.identifier = identifier

    def setChild(self, child: Node):
        self.child = child

    def isConst(self):
        self.const = True

    def __repr__(self) -> str:
        if self.const:
            ret = f"(const) {self.identifier} <= {self.child}"
            return ret
        else:
            ret = f"{self.identifier} <= {self.child}"
            return ret
        
class MethodDeclarationNode(Node):
    def __init__(self):
        self.struct: str = None
        self.identifier: str = None
        self.params: list[Node] = [] #params
        self.child: list[Node] = [] #body

    def setStructName(self, name: str):
        self.struct = name

    def setIdentifier(self, identifier: str):
        self.identifier = identifier

    def setParams(self, param: list[Node]):
        self.params = param

    def setChild(self, child: list[Node]):
        self.child = child

    def __repr__(self) -> str:
        ret = f"{self.identifier}("
        for p in self.params:
            ret += f"[{p}]"
        ret+=f")\n"
        ret+=f"{{\n"
        for c in self.child:
            ret += f"{c}\n"
        ret+=f"}}"

        return ret
    
class StructAllocNode(Node):
    def __init__(self):
        self.struct: str = None
    
    def setStructName(self, name: str):
        self.struct = name

    def __repr__(self) -> str:
        ret = f"alloc {self.struct}"
        return ret
    
class StructMemberAccess(Node):
    def __init__(self):
        self.symbol: str = None
        self.member: str = None
        self.child: Node = None

    def setSymbol(self, symbol: str):
        self.symbol = symbol

    def setMember(self, member: str):
        self.member = member

    def setChild(self, child: Node):
        self.child = child

    def __repr__(self) -> str:
        ret = f"{self.symbol}.{self.member}"
        if type(self.child).__name__ == "StructMemberAccess":
            ret += f".{self.child}"
        return ret
    
class StructMemberWrite(Node):
    def __init__(self):
        self.symbol: str = None
        self.member: str = None
        self.child: Node = None

    def setSymbol(self, symbol: str):
        self.symbol = symbol

    def setMember(self, member: str):
        self.member = member

    def setChild(self, child: Node):
        self.child = child

    def __repr__(self) -> str:
        if self.child:
            ret = f"{self.symbol}.{self.member} = {self.child}"
        else:
            ret = f"{self.symbol}.{self.member}"
        return ret
    
class ImplMemberCall(Node):
    def __init__(self):
        self.symbol: str = None
        self.member: str = None
        self.params: list[Node] = []

    def setSymbol(self, symbol: str):
        self.symbol = symbol

    def setMember(self, member: str):
        self.member = member

    def setParams(self, params: list[Node]):
        self.params = params

    def __repr__(self) -> str:
        ret = f"{self.symbol}.{self.member}("
        if len(self.params) == 0:
            ret += ")"
        else:
            for p in self.params:
                ret += f"{p}"
                ret += ","
            ret = ret[:-1]
            ret += ")"
        return ret