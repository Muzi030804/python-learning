import requests
from lxml import html
import csv

# 常量
TMDB_BASE_URL = "http://www.themoviedb.org"
TMDB_TOP_URL = "http://www.themoviedb.org/movie/top-rated"

#保存电影数据
def save_all_movies(all_movies):
    pass

#获取电影详情
def get_movie_info(movie_info_url):
    # 1. 发送请求, 获取电影详情数据
    movie_response = requests.get(movie_info_url)

    # 2. 解析数据, 获取电影详情
    movie_document = html.fromstring(movie_response.text)
    # 电影名称
    movie_name = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    # 电影年份
    movie_years = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    movie_dates = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")
    movie_tags = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")
    movie_cost_times = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")
    movie_scores = movie_document.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_languages = movie_document.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_directors = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li/p[1]/a/text()")
    movie_slogans = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    movie_descriptions = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    # 3. 返回电影详情
    movie_info = {
        "movie_name": movie_name[0].strip() if movie_name else '',
        "movie_years": movie_years[0].strip() if movie_years else '',
        "movie_dates": movie_dates[0].strip() if movie_dates else '',
        "movie_tags": ",".join(movie_tags) if movie_tags else '',
        "movie_cost_times": movie_cost_times[0].strip() if movie_cost_times else '',
        "movie_scores": movie_scores[0].strip() if movie_scores else '',
        "movie_languages": movie_languages[0].strip() if movie_languages else '',
        "movie_directors": movie_directors[0].strip() if movie_directors else '',
        "movie_slogans": movie_slogans[0].strip() if movie_slogans else '',
        "movie_descriptions": movie_descriptions[0].strip() if movie_descriptions else '',


    }


# 主函数, 定义核心逻辑

def main():
    # 1.发送请求, 获取高分电影榜单数据
    response = requests.get(TMDB_TOP_URL, timeout=10)

    # 2.解析数据, 获取电影列表
    document = html.fromstring(response.text)
    movie_list = document.xpath("//*[@class='media-card-list contents w-full']/div/*")

    # 3.遍历电影列表, 获取电影详情
    all_movies = []
    for movie in movie_list:
        movie_urls = movie.xpath("./div/div/a/@href")
        if movie_urls:
            #电影详情的url
            movie_info_url = TMDB_BASE_URL + movie_urls[0]
            # 发送请求, 获取电影详情数据
            movie_info = get_movie_info(movie_info_url)
            all_movies.append(movie_info)
    # 4.保存数据, 保存为csv文件
    save_all_movies(all_movies)

if __name__ == '__main__':
    main()