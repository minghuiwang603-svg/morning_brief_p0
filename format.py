def format_brief(articles: list) -> str:
    result = ""
    for article in articles:
        result += article["title"]
        result += "\n"
        result += article["link"]
        result += "\n\n"
    return result

