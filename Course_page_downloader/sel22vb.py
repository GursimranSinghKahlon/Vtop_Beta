from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

username = str(raw_input("Enter the register no. : "))
password = getpass.getpass('Password : ')

executable_path = 'chromedriver'
chrome_options = Options()
chrome_options.add_extension('ensuitego.crx')

print("Opening browser window")
driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
driver.get("https://vtopbeta.vit.ac.in/vtop/")
driver.find_element_by_css_selector('.btn-primary').click()
driver.switch_to_window(driver.window_handles[1])

# LOGIN
element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, "uname")))
elem = driver.find_element_by_xpath('//*[@id="uname"]')
elem.clear()
elem.send_keys(username)

elem = driver.find_element_by_name("passwd")
elem.clear()
elem.send_keys(password)

#COURSE PAGE#
driver.find_element_by_xpath('//*[@id="form-signin_v1"]/div[4]/div[2]/button').click()
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/header/nav/a')))
driver.find_element_by_xpath('//*[@id="page-content"]/header/nav/a').click()
driver.find_element_by_xpath('//*[@id="dbMenu"]/ul/li[2]/a/span[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="idOf6"]/span').click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='semesterSubId']/option[text()='Fall Semester 2018-19 - VLR']").click()
time.sleep(2)

#List of courses
courses = []
all_options = driver.find_element_by_xpath('//*[@id="courseCode"]')
for option in all_options.find_elements_by_tag_name('option'):
    course = option.text
    print("Courses are: %s" % course)
    courses.append(str(course))
courses = courses[1:]
courses_count = len(courses)

#Iterate through each course
for course_count in range(courses_count):
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='semesterSubId']/option[text()='Fall Semester 2018-19 - VLR']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='courseCode']/option[text()='{}']".format(str(courses[course_count]))).click()
    time.sleep(3)

    #Count of teachers/slots for each course
    teachers_count = -1
    all_rows = driver.find_element_by_xpath('//*[@id="StudentCoursePage"]/div/div[5]/div/table/tbody')
    for option in all_rows.find_elements_by_tag_name('tr'):
        teachers_count+=1

    #Iterate through each teacher/slot
    for i in range(teachers_count):
        driver.find_element_by_xpath("//*[@id='semesterSubId']/option[text()='Fall Semester 2018-19 - VLR']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='courseCode']/option[text()='{}']".format(str(courses[course_count]))).click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="StudentCoursePage"]/div/div[5]/div/table/tbody/tr[{}]/td[9]/button'.format(str(i+2))).click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CoursePageLectureDetail"]/div/div[2]/div[3]/div[3]/div/a[2]')))
        driver.find_element_by_xpath('//*[@id="CoursePageLectureDetail"]/div/div[2]/div[3]/div[3]/div/a[2]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="back"]').click()
        time.sleep(2)
        i+=1

#LOGOUT
driver.find_element_by_xpath('//*[@id="page-content"]/header/nav/div/ul/li/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="btnLogout"]').click()