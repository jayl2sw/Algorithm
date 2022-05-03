import re
from collections import defaultdict
def solution(word, pages):
    meta_p = re.compile('<meta property=\"og:url\" content=\"(.+)\"')
    a_p = re.compile('<a href="(.+)">')
    page_names = []
    basic_score = defaultdict(int)
    link_score = defaultdict(int)
    for page in pages:
        page = page.lower()
        page_name = meta_p.findall(page)[0]
        page_names.append(page_name)

        body = re.sub('[^a-zA-Z]', '.', page.lower())
        score = body.split('.').count(word.lower())
        basic_score[page_name] = score



        links = a_p.findall(page)
        for link in links:
            link_score[link] += score/len(links)


    for page_name in basic_score:
        basic_score[page_name] += link_score[page_name]

    answer = [k for k,v in basic_score.items() if max(basic_score.values()) == v][0]
    return page_names.index(answer)









print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))