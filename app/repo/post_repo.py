# from operator import itemgetter
# from app.db.database import driver
# from app.db.models import Location, Device, Interaction
# import toolz as t
#
#
# def insert_post(user_name: str, post: Post):
#     with driver.session() as session:
#         query = """
#         MATCH (u:User {name: $username})
#         WITH u LIMIT 1
#         MERGE (p:Post {content: $content, date: datetime($date)})
#         MERGE (u)-[:WROTE]->(p)
#         RETURN p
#         """
#         params = {"username": user_name, "content": post.content, "date": post.date.isoformat()}
#         result = session.run(query, params).single()
#         return result
#
#
# def get_all_posts():
#     with driver.session() as session:
#         query = "MATCH (p:Post) RETURN p"
#         res = session.run(query).data()
#         return t.pipe(res, t.partial(t.pluck, "p"), list)
#
#
# def update_post(old_content: str, mew_post: Post):
#     with driver.session() as session:
#         query = """
#         MATCH (p:Post {content: $old_content})
#         SET p.content = $new_content, p.date = datetime($new_date)
#         RETURN p
#         """
#         params = {"old_content": old_content, "new_content": mew_post.content, "new_date": mew_post.date}
#         result = session.run(query, params).single()
#         return (Maybe.from_optional(result)
#                 .map(itemgetter("p"))
#                 .map(lambda x: dict(x))
#                 .map(lambda d: {**d, 'date': str(d['date'])})
#                 .value_or(None))
#
#
# def delete_post(post_content: str):
#     with driver.session() as session:
#         query = """
#         MATCH (p:Post {content: $post_id})
#         DETACH DELETE p
#         """
#         params = {"post_content": post_content}
#         session.run(query, params)
#         return {"status": "deleted"}
