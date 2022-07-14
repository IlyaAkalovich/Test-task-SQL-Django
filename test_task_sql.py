import sqlite3

connection = sqlite3.connect('test_task')
print("MYSQL:", connection)

outcome_query = """SELECT client_number as client, 
                                SUM(outcome = "win") as win, 
                                SUM(outcome = "lose") AS lose 
                        FROM bid
                        INNER JOIN event_value
                        ON bid.play_id = event_value.play_id
                        GROUP BY client_number; """

games_query = """
                        SELECT MIN(home_team, away_team) AS A, 
                                MAX(home_team, away_team) AS B, 
                                COUNT(*) as games
                        FROM event_entity
                        GROUP BY A, B
                        HAVING games >= 1
                        ORDER BY games 
                            """


def get_sql_result(sql: str) -> list:
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


result = get_sql_result(outcome_query)
print('+-----------------------------------+')
print('| client_number |', 'Побед |', 'Поражений |')
print('+-----------------------------------+')

for n, win, lose in result:
    print('|', ' ' * 4, n, ' ' * 5,
          '|', ' ', win,
          ' |', ' ' * 3, lose, '    |'
          )
print('+-----------------------------------+')

result = get_sql_result(games_query)
ss = '-' * 59
print('+' + ss + '+')
print('|game                                               |games_count|')
print('+' + ss + '+')

for game1, game2, res in result:

    s = f"| {game1} {game2}"
    len_s = len(s)
    if len_s < 53:
        len_str = 53 - len_s
        print(f"| {game1} - {game2}" + " " * len_str + (f"| {res}  |" if res < 10 else f"| {res} |"))
print('+' + ss + '+')
connection.close
