#!/usr/bin/env python3


import psycopg2
DBNAME = "news"


def get_top_articles():
    """function that select 3 top articles"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        record = c.execute("""
                               Select title,count(ip) AS top from articles,log
                               where log.path=concat
                               ('/article/', articles.slug)
                               GROUP BY title
                               order by top DESC LIMIT 3;""")
        for record in c:
            print(record)
        return c.fetchall()
        db.close()
    except:
        print "Error connection"


def get_top_three_authors():
    """function that select most authors"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        re = c.execute("""
                          SELECT name,COUNT
                          (ip) AS most FROM articles, log, authors
                          WHERE log.path = CONCAT('/article/', articles.slug)
                          AND articles.author = authors.id
                          GROUP BY name
                          ORDER BY most DESC; """)
        for re in c:
            print(re)
        return c.fetchall()
        db.close()
    except e:
        print "Error connection"


def get_errors_reports():
    """function that calculate error ber days"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        errors = c.execute("""
                             SELECT date(time),
                             round(100.0*sum(CASE log.status when '200 OK'
                             then 0 else 1 end)/count(log.status),2)
                             as "show error"
                             FROM log GROUP BY date(time)
                            ORDER BY "show error" DESC LIMIT 1; """)
        for errors in c:
            print(errors)
        return c.fetchall()
        db.close()
    except :
        print "Error connection"


if __name__ == "__main__":
    print("THE LIST OF POPULAR ARTICLES ARE:")
    get_top_articles()
    print("\n")
    print("Who are the most popular article authors of all time?")
    get_top_three_authors()
    print("\n")
    print("On which days did more than 1% of requests lead to errors?")
    get_errors_reports()
