from py2neo import Graph, Node, Relationship

url = 'http://localhost:7474'
username = "neo4j"
password = "password"

graph = Graph(url, auth = (username, password))

class Movie:

    def getMovieList():
        query = '''
        MATCH (m:Movie) 
        RETURN m.title AS title , m.tagline AS tagline, 
        m.released AS released
        '''
        return graph.run(query).data()
    
