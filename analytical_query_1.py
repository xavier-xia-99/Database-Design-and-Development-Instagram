# US2
import psycopg2
import sys

def print_rows(rows):
    for row in rows:
        print(row)

def top_viewed(user_id):
    print("US2: # As a content creator, I want to see my most viewed post so that I can see what type of content is most popular with my followers")
    tmpl= '''
    SELECT p.post_id, COUNT(v.post_id) as num_views
      FROM Views_post as v
            JOIN Post as p on p.post_id = v.post_id
     WHERE (user_id = 72)
     GROUP BY p.post_id
     ORDER BY COUNT(p.post_id) DESC
     LIMIT 1;
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: Creator wants to see the post with the most views.")
    print("post_id, num_views")
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

top_viewed(user_id=72)

#TEST CASES

#62
#72
#82

#all other Content_Creators do not have views within our DB.