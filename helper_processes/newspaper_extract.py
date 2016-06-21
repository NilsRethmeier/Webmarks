from newspaper import Article


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def get_text(url):
    article = Article(url)
    download=article.download()
    parser= article.parse()
    authors=article.authors
    publish_date=article.publish_date # TODO: Slice publish date
    body_text=article.text
    body_text=body_text.replace('"','\"')
    body_text=body_text.replace('"','')
    #nlp=article.nlp()
    keywords=article.keywords
    summary=article.summary
    title=article.title
    tags=article.tags

    #print body_text

    title=strip_non_ascii(title)
    summary=strip_non_ascii(summary)
    body_text=strip_non_ascii(body_text)
    keywords=' '.join(keywords)
    keywords=strip_non_ascii(keywords)

    #print (title, summary, authors, publish_date, body_text, keywords)

    return (title, summary, authors, publish_date, body_text, keywords, tags)



#get_text("http://www.drstevesavage.com/speaking/")



