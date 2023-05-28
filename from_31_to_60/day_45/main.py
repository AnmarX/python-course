from bs4 import BeautifulSoup
import requests

######ANGELA#######
# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# # Write your code below this line 👇

# response = requests.get(URL)
# website_html = response.text

# soup = BeautifulSoup(website_html, "html.parser")

# all_movies = soup.find_all(name="h3", class_="title")

# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]

# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")


# '''
# FAQ: Empire's website has changed!

# When this lesson was created, I used this URL for the project: 
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
# You'll see that the h3 with the class "title" is no longer there. 
# To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

# '''
######ANGELA#######










# res=requests.get("https://news.ycombinator.com/")

# soup=BeautifulSoup(res.text,"html.parser")

# all_url=soup.find_all(name="span",class_="titleline")
# #print(all_url)
# anchor=[]
# for i in all_url:
#     #print(i.text)
#     anchor.append(i.a)
# print(anchor)

    

######ANGELA#######
# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://news.ycombinator.com/")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, 'html.parser')

# article_titles = []
# article_links = []
# for article_tag in soup.find_all(name="span", class_="titleline"):
#     article_titles.append(article_tag.getText())
#     article_links.append(article_tag.find("a")["href"])

# article_upvotes = []
# for article in soup.find_all(name="td", class_="subtext"):
#     if article.span.find(class_="score") is None:
#         article_upvotes.append(0)
#     else:
#         article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# max_points_index = article_upvotes.index(max(article_upvotes))
# print(
#     f"{article_titles[max_points_index]}, "
#     f"{article_upvotes[max_points_index]} points, "
#     f"available at: {article_links[max_points_index]}."
# )
######ANGELA#######







# with open("./31-60/day_45/website.html",encoding="utf-8") as file:
#     cont = file.read()

# soup = BeautifulSoup(cont, "html.parser")

# print(soup.prettify().encode("ascii", "ignore").decode("ascii"))

# print(soup.title)
# print(soup.title.name)
# print(soup.a)

# all=soup.find_all(name="a")
#print(all)

# for i in all:
#     pass
    #print(i.text)
    # print(i.get("href"))

# heading=soup.find(name="h1",id="name")
# print(heading.text)

# n=soup.select_one("#name")
# print(n)


# heading2=soup.find(name="h3",class_="heading")
# print(heading2.text)
# print(heading2.get("class"))
 

# url=soup.select_one(selector="p a")
# print(url)




