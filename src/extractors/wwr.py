from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="

    res = get(f"{base_url}{keyword}")

    if res.status_code != 200:
        print("Can't request website.")
        return []
    else:
        results = []
        soup = BeautifulSoup(res.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for job_section in jobs:
            posts = job_section.find_all("li")
            posts.pop()
            for post in posts:
                anchors = post.find_all("a")
                anchor = anchors[1]
                link = anchor["href"]
                company, work_time, region = anchor.find_all(
                    "span", class_="company")
                title = anchor.find("span", class_="title")
                results.append({
                    "link": f"https://weworkremotely.com{link}".replace(",", " "),
                    "company": company.string.replace(",", " "),
                    "region": (region.string or "Unspecified").replace(",", " "),
                    "position": title.string.replace(",", " ")
                })
        return results
