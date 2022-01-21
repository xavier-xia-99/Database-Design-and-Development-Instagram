#US 10
import psycopg2
import sys
    
def print_rows(rows):
    for row in rows:
        print(row)


def give_donations(user_id):

    print("This is US10, where we follow me (user_id = 12) and give more donations to my favourite subscriber!")
    tmpl= '''
            SELECT u.display_name, s.donation_amt
            FROM Subscribes as s
            JOIN "User" as u on s.u2_user_id = u.user_id
            WHERE u1_user_id = 12
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("User Story summary: These are the initial donations to my favourite")
    print("Creator Name, Donated Amt")
    print_rows(rows)

    tmpl= '''
            UPDATE Subscribes
             SET donation_amt = donation_amt + 50
             WHERE u2_user_id = 42
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    print("")
    print('He decided to donate 50 more to Suarez!')
    print("")
    tmpl= '''

            SELECT u.display_name, s.donation_amt
            FROM Subscribes as s
            JOIN "User" as u on s.u2_user_id = u.user_id
            WHERE u1_user_id = 12 
    '''
    cmd = cur.mogrify(tmpl)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Creator Name, Donated Amt")
    print_rows(rows)
    print("")
    print("Now Suarez has $50 more from me!")

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

give_donations(user_id = 51)



