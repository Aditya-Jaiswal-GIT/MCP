from fastmcp import FastMCP
mcp = FastMCP("Simple Calulator")
@mcp.tool()
def add(a:float,b:float):
    """ Return sum of 2 number """
    return a+b

@mcp.tool()
def sub(a:float,b:float):
    """ Return Difference of two number """
    return a-b

@mcp.tool()
def mul(a:float,b:float):
    """ Return Multiplication of two number """
    return a*b

@mcp.tool()
def div(a:float,b:float):
    """ Return the division of two number """
    return a/b


@mcp.resource("info://server")
def server():
    """ Return the information of server"""
    info = {
        'name' : "Simple Calculator",
        "version" : 1.0,
        "tool" : ['add','sub','mul','div'],
        'task' : "Perform simple calculation task",
        'Author': 'Aditya Jaiswal'
    }
    return info

if __name__ =="__main__":
    mcp.run(transport='http',host="0.0.0.0",port=8000)