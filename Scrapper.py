import requests
from bs4 import BeautifulSoup
import pandas as pd

indeed_LIMIT = 50
indeed_URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={indeed_LIMIT}"

def extract_pages(URL):
    results = requests.get(URL)
    soup = BeautifulSoup(results.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = company_anchor.string
    else:
        company = company.string
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'SITE':'INDEED','Job': title, 'Company': company, "Location": location, "Link": f"https://kr.indeed.com/viewjob?jk={job_id}"}


def indeed_jobs(last_page):
    jobs = pd.DataFrame()
    print('Start Scrapping from "INDEED"')
    for page in range(last_page):
        print(f"Scrapping page {page+1}")
        result = requests.get(f"{indeed_URL}&start={page*indeed_LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_indeed(result)
            df = pd.DataFrame.from_dict([job])
            jobs = jobs.append(df)
            print(jobs)
    return jobs


def give_me_job(URL1, URL2):

    #INDEED
    last_page_1 = extract_pages(URL1)
    indeed = indeed_jobs(last_page_1)

    #return My_Job.to_excel('./Jobs(Python).xlsx')

#Trial
give_me_job(indeed_URL)