import random

def rank_posts(posts):
    """
    Ordena posts simulando viralidad.
    """

    if not posts:
        return []

    scored = []

    for post in posts:
        score = random.randint(1, 100)
        scored.append((score, post))

    scored.sort(reverse=True, key=lambda x: x[0])

    # top 3 posts
    top = [post for _, post in scored[:3]]

    return top
