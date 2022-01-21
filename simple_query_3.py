# US4

import psycopg2
import sys
    
def print_rows(rows):
    for row in rows:
        print(row)

#generates all posts in a hashtag
def see_posts(hashtag):
    tmpl= '''
    SELECT post_id, user_id, date_posted, hashtag, location, description
      FROM Post
     WHERE hashtag = 'love';
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: User wants to see all posts with a single hashtag.")
    print("post_id, user_id, date_posted, hashtag, location, description")
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

see_posts('love')

# TEST CASES (more in CSV files)
# love
# vacation
# concert
# pride
# friendsandfam