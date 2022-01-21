# US9
import psycopg2
import sys

def print_rows(rows):
    for row in rows:
        print(row)

#creates organized format and heading for top_viewed_show()

def ranking(brand_id):
    print("US9: As a brand, I want to know the rankings of engagement rate (num_views) of my advertisements so that I can see which advertisements are the most successful and model future ones after them.")
    tmpl= '''
    SELECT a.ad_id, COUNT(v.date_viewed)
        FROM Brands as b
            JOIN Ads as a ON b.brand_id = a.brand_id
            JOIN Views_Ad as v on a.ad_id = v.ad_id
    WHERE (b.brand_id=15)
    GROUP BY a.ad_id
    ORDER BY COUNT(v.date_viewed) DESC
    LIMIT 3;
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: Brands wants to see their top 3 ads.")
    print("ad_id, num_views")
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

ranking(brand_id=72)

#TEST CASES

#62
#72
#82

#all other Content_Creators do not have views within our DB.