import MySQLdb

print "Content-Type: text/html\n"
print 
print "<html><head><meta http-equiv=\"Content-Type\" content>"
print "<body>"
print "<h1>Libros</h1>"
print "<ul>"
#base de datos query? y generacion
connection = MySQLdb.connect(user='yo', password='dejameentrar', db='books.db')
cursor = connection.cursor()
cursor.execute("SELECT nombre FROM libros ORDER BY fecha DESC
 LIMIT 10")
 
 for row in cursor.fetchall():
     print "<li>%s</li>"


print "</ul>"
print "</body></html>"
connection.close()
