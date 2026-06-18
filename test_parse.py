from parse import parse
def test_parse():
    text = ("""<entry>
    <title>科技爱好者周刊（第 399 期）：中国 AI 大厂访问记</title>
    <link rel="alternate" type="text/html" href="http://www.ruanyifeng.com/blog/2026/06/weekly-issue-399.html" />
    <content type="html">测试正文</content>""")
    result = parse(text)
    assert result == [{"title":"科技爱好者周刊（第 399 期）：中国 AI 大厂访问记","link":"http://www.ruanyifeng.com/blog/2026/06/weekly-issue-399.html","body":"测试正文"}]
    