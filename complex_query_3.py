#US 7
import psycopg2
import sys
    
def print_rows(rows):
    for row in rows:
        print(row)


def ad_views(user_id):
    print("This is US7, where we follow brand_id = 15 and find out how many users view my ad every month.")
    tmpl= '''
            SELECT v.ad_id, count(v.ad_id), EXTRACT(MONTH FROM v.date_viewed)::integer
            FROM Ads as a
            JOIN Views_Ad as v on a.ad_id = v.ad_id
            WHERE brand_id = 15
            GROUP BY EXTRACT(MONTH FROM v.date_viewed), v.ad_id
            ORDER BY count(v.user_id) ASC
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: very sad....")
    print("ad_id, view_count, month_viewed")
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

ad_views(user_id = 51)



