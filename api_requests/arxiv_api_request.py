### README
'''

GOAL OF THIS MODULE:

INPUT:

OUTPUT:

IMPORTANT NOTES:

TODOs DUMP (PLEASE ADD AS ISSUE, IF YOU CAN'T DO IT YOURSELF):

'''
####




import urllib
url = 'http://export.arxiv.org/api/query?search_query=deep+neural+networks:electron&start=0&max_results=10'
data = urllib.urlopen(url).read()
print data