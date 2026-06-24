from fastapi import FastAPI

app = FastAPI()

text_posts = {
    1: {
        "title": "Introduction to Python",
        "content": "Python is a beginner-friendly programming language used in web development, AI, and automation."
    },
    2: {
        "title": "Learning FastAPI",
        "content": "FastAPI is a modern Python framework for building high-performance APIs."
    },
    3: {
        "title": "Benefits of Git",
        "content": "Git helps developers track changes, collaborate with others, and manage code versions."
    },
    4: {
        "title": "Understanding APIs",
        "content": "APIs allow different software applications to communicate with each other."
    },
    5: {
        "title": "Getting Started with Docker",
        "content": "Docker makes it easy to package and deploy applications in containers."
    },
    6: {
        "title": "Machine Learning Basics",
        "content": "Machine learning enables computers to learn patterns from data without explicit programming."
    },
    7: {
        "title": "Web Scraping with Python",
        "content": "Libraries like BeautifulSoup and Scrapy help extract data from websites."
    },
    8: {
        "title": "Database Fundamentals",
        "content": "Databases store and organize data efficiently for applications."
    },
    9: {
        "title": "Authentication in APIs",
        "content": "Authentication verifies the identity of users accessing an API."
    },
    10: {
        "title": "Building AI Agents",
        "content": "AI agents can automate tasks by combining LLMs, tools, and workflows."
    }
}

@app.get("/posts")
def get_posts(limit : int = None) :
    if limit is not None :
        return list(text_posts.values())[:limit]
    return list(text_posts.values())

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return text_posts.get(post_id)
