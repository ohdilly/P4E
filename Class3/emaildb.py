import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (orgs TEXT, count INTEGER)''')

fname = 'mbox-short.txt'
##if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    orgs = email.split('@')
    cur.execute('SELECT count FROM Counts WHERE orgs = ? ', (orgs[1],))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (orgs, count)
                VALUES (?, 1)''', (orgs[1],))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE orgs = ?',
                    (orgs[1],))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT orgs, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
