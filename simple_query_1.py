import psycopg2
import sys
    
def print_rows(rows):
    for row in rows:
        print(row)


def friend_posts(user_id):
    print("This is US1, where we follow user_id = 51 and find his friends' post")
    tmpl= '''
            SELECT p.post_id, p.description, p.hashtag, p.location, f.u2_user_id
            FROM Follows as f 
            JOIN Post as p on p.user_id = f.u2_user_id
            WHERE f.u1_user_id = 51
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: .")
    for row in rows:
        p_id, desc, hashtag, loc, u2_id = row[0], row[1], row[2], row[3], row[4]
        print(f'post id: {p_id} of my friend, id:{u2_id} was posted at {loc} . It has content: {desc} #{hashtag} ')

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

friend_posts(user_id = 51)



