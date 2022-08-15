from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(driver, keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    driver.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    page_list = soup.find("ul", class_="pagination-list")
    if page_list == None:
        return 1
    else:
        pages = page_list.find_all("li", recursive=False)
        count = len(pages)
        if count >= 5:
            return 5
        else:
            return count


def extract_indeed_jobs(keyword):
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    results = []
    pages = get_page_count(driver, keyword)
    print("Found", pages, "pages")

    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        page_query = f"&start={page * 10}" if page > 0 else ""
        print(f"Requesting {base_url}?q={keyword}{page_query}")
        driver.get(f"{base_url}?q={keyword}{page_query}")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("a")
                title = anchor["aria-label"]
                link = anchor["href"]
                company = job.find("span", class_="companyName")
                region = job.find("div", class_="companyLocation")
                results.append({
                    "link": f"https://kr.indeed.com{link}".replace(",", " "),
                    "company": company.string.replace(",", " "),
                    "region": region.string.replace(",", " "),
                    "position": title.replace("의 전체 세부 정보", "").replace(",", " ")
                })
    driver.quit()
    return results
