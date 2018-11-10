import psycopg2

# !/usr/bin/env python3


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.DatabaseError as error:
        print(error)


def executeQuery(query):
    db, cursor = connect()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def printResult(rows, description):
    print()
    for row in rows:
        print('"' + str(row[0]) + '" - ' + str(row[1]) + description)
    print()
    print('--------------------------------------------------------')
    print()


if __name__ == '__main__':
    # First Query
    print('1. What are the most popular three articles of all time?')
    rows = executeQuery("""
    SELECT articles.title, articles_visits.visits
    FROM articles
    JOIN articles_visits ON articles.slug = articles_visits.slug
    ORDER BY visits DESC
    LIMIT 3;
    """)
    printResult(rows, ' views')

    # Second Query
    print('2. Who are the most popular article authors of all time?')
    rows = executeQuery("""
    SELECT sub.name, SUM(articles_visits.visits)
    FROM articles_visits
    JOIN
    (SELECT * FROM articles JOIN authors ON articles.author = authors.id) sub
    ON sub.slug = articles_visits.slug
    GROUP BY sub.name
    ORDER BY sum DESC;
    """)
    printResult(rows, ' views')

    # Third Query
    print('3. On which days did more than 1% of requests lead to errors?')
    rows = executeQuery("""
    SELECT TO_CHAR(date,'Mon dd, yyyy') AS date,
    ROUND(num_of_erros::decimal / num_of_requests::decimal * 100, 1)
    AS error_percentage
    FROM requests_status
    WHERE num_of_erros::decimal / num_of_requests::decimal > 0.01;
    """)
    printResult(rows, '% errors')
