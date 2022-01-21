#US 6
import psycopg2
import sys
    
def print_rows(rows):
    for row in rows:
        print(row)


def friend_follows(user_id):
    print("This is US6, where we follow user_id = 11 and find which content creator his friend follows")
    tmpl= '''
            SELECT u.display_name, u.user_id, c.contact_email
            FROM Follows as f 
            JOIN Subscribes as s on f.u2_user_id = s.u1_user_id
            JOIN Content_Creator as c on c.user_id = s.u2_user_id
            JOIN "User" as u on u.user_id = s.u2_user_id
            WHERE f.u1_user_id = 11
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: These are the influencers followed by friends of id: 11")
    print_rows(rows)
    print("user_id 11's friend in this case happen to be user_id : 12 and we verify this with analytic_query_3.py ")

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

friend_follows(user_id = 51)



