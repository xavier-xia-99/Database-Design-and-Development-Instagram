#US 5
import psycopg2
import sys
    
def print_rows(rows):
    for row in rows:
        print(row)


def most_liked(user_id):
    print("As a content creator, I want to see which post of mine under a certain hashtag has the most likes. so that I can track interactions across content types.")
    tmpl= '''
        SELECT p.post_id, COUNT(l.post_id) as num_likes
        FROM Likes_post as l
            JOIN Post as p ON p.post_id = l.post_id
            JOIN Content_Creator as c on c.user_id = p.user_id
        WHERE (c.user_id=82) AND (p.hashtag='friendsandfam')
        GROUP BY p.post_id
        ORDER BY COUNT(l.post_id) DESC
        LIMIT 1;
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: This is the top of post of a content creator under hashtag 'friendsandfam'")
    print("postid, num_likes")
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

most_liked(user_id = 82)



