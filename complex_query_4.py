#US 8
import psycopg2
import sys
    
def print_rows(rows):
    for row in rows:
        print(row)


def seen_by(user_id):
    print("As a content creator, I want to know which posts users are seeing and when so that I can track the popularity of my content and keep updated on good times to post content.")
    tmpl= '''
        SELECT DISTINCT(p.post_id), v.date_viewed, v.u2_user_id
            FROM Post as p
                JOIN Views_Post AS v ON v.post_id = p.post_id
                Join "User" as u ON u.user_id = p.user_id
        WHERE (v.u1_user_id=82)
        ORDER BY p.post_id;
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: Posts and when they're seen")
    print("post_id, date_viewed, user_seen_by")
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

seen_by(user_id = 82)



