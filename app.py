# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup

# 原始 HTML 程式碼
html_doc = """
<html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h2>Test Header</h2>
        <p>This is a test.</p>
        <a id="link1" href="/my_link1">Link 1</a>
        <a id="link2" href="/my_link2">Link 2</a>
        <p>Hello, <b class="boldtext">Bold Text</b></p>
    </body>
</html>
"""
# 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

# 網頁標題 HTML 標籤
title_tag = soup.title
print(title_tag.string)

# 所有超連結
a_tags = soup.find_all("a")
for tag in a_tags:
    print(tag.string)
    # 取出節點屬性
    print(tag.get("href"))

# 同時搜尋多種標籤，並限制數量
tags = soup.find_all(["a", "b"], limit=2)
print(tags)
