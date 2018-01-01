import sqlite3 as lite
import sys
def DoodleTest(newCandidate):
    print("testing if ", newCandidate, " is really new!")
    
    try:
        con = lite.connect('/home/felipe/Raspberry/Robirdwatching/mydb.db')
        cur = con.cursor()
        cur.execute("select count(*) from Metadata;")
        lID=cur.fetchone()
        #print(lID)
        if lID[0]==0:
            print("This is the first Doodle!")
        else:
            cur.execute("select Legend from Metadata where Id=?;", (lID[0],))
            lastDoodle = cur.fetchall()
            testResult = lastDoodle[0][0]==newCandidate
            if lastDoodle[0][0]==newCandidate:
                print("Nope.... No new Doodle today")
            else:
                print("Yeah! We have a new Doodle!")
            return testResult
    except lite.Error as e:
        if con:
            con.rollback()
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close() 