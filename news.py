import psycopg2


def executeQuery(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


if __name__ == '__main__':
    # First Query
    print()
    print('1. What are the most popular three articles of all time?')
    rows = executeQuery("""
    SELECT articles.title, articles_visits.visits
    FROM articles
    JOIN articles_visits ON articles.slug = articles_visits.slug
    ORDER BY visits DESC
    LIMIT 3;
    """)
    for row in rows:
        print('"' + row[0] + '" - ' + str(row[1]) + ' views')
    print()
    print('--------------------------------------------------------')

    # Second Query
    print()
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
    for row in rows:
        print(row[0] + ' - ' + str(row[1]) + ' views')
    print()
    print('--------------------------------------------------------')

    # Third Query
    print()
    print('3. On which days did more than 1% of requests lead to errors?')
    rows = executeQuery("""
    SELECT TO_CHAR(date,'Mon dd, yyyy') AS date,
    ROUND(num_of_erros::decimal / num_of_requests::decimal * 100, 1)
    AS error_percentage
    FROM requests_status
    WHERE num_of_erros::decimal / num_of_requests::decimal > 0.01;
    """)
    for row in rows:
        print(str(row[0]) + ' - ' + str(row[1]) + '% errors')
    print()
    print('--------------------------------------------------------')
