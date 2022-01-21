import psycopg2
import sys
    
def print_rows(rows):
    for row in rows:
        print(row)

def post_likes(user_id):
    print("This is US3, where we follow content creator with user_id = 62 and find the number of likes of his 4th post")
    tmpl= '''
            SELECT count(l.post_id)
            FROM Likes_post as l
            WHERE l.u2_user_id = 62 and l.post_id = 4
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: How many likes does user_id 62 have for their 4th post? Ans: 1")
    print_rows(rows)

if __name__ == '__main__':
   try:
       db, user = 'instagram', 'isdb'
       if len(sys.argv) >= 2:
           db = sys.argv[1]
       if len(sys.argv) >= 3:
           user = sys.argv[2]
       conn = psycopg2.connect(database=db, user=user)
       conn.autocommit = True
       cur = conn.cursor()
   except psycopg2.Error as e:
       print("Unable to open connection: %s" % (e,))

post_likes(user_id = 42)



