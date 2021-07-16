from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    #courses_html_tags = soup.find_all('div')
    #for course in courses_html_tags:
        #print(course.text)
    course_cards = soup.find_all('div', {"class": "card"})   #course_cards = soup.find_all('div', {"class": "card-text"})
    for course in course_cards:
        course_name = course.small.text
        course_price = course.a.text.split()[-1]
        print(course_name)
        print(f'{course_name} costs {course_price}')


