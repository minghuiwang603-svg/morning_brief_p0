from format import format_brief
def test_format_brief():
    articles = [{"title":"a","link":"b"},{"title":"a1","link":"b1"}]
    result = format_brief(articles)
    assert result == "a\nb\n\na1\nb1\n\n"
