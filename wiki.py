#Program for wikipedia automation for tech for social good day
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SCROLL_PAUSE_TIME = 0.5



prisons = ['Maine State Prison',
'Northern State Correctional Facility',
'New Hampshire State Prison',
'Massachusetts Correctional Institution – Norfolk',
'Rhode Island Maximum Security Prison',
'MacDougall-Walker Correctional Institution',
'Rikers Island',
'East Jersey State Prison',
'State Correctional Institution – Fayette',
'Vaughn Correctional Center',
'Red Onion State Prison',
'West Virginia Penitentiary',
'Central Prison',
'Lieber Correctional Institution',
'Georgia State Prison',
'Limestone Correctional Facility',
'Riverbend Maximum Security Institution',
'Mississippi State Penitentiary',
'Louisiana State Penitentiary',
'Cummins Unit',
'Potosi Correctional Center',
'United States Penitentiary, Leavenworth',
'Oklahoma State Penitentiary',
'Huntsville Unit',
'The Penitentiary of New Mexico',
'Sterling Correctional Facility',
'Utah State Prison',
'Arizona State Prison Complex – Lewis',
'San Quentin State Prison',
'High Desert State Prison (Nevada)',
'Oregon State Penitentiary',
'Idaho Department of Correction',
'Nebraska State Penitentiary',
'Coyote Ridge Corrections Center',
'Wyoming State Penitentiary',
'Montana State Prison',
'North Dakota State Penitentiary',
'South Dakota State Penitentiary',
'Minnesota Correctional Facility – Faribault',
'Anamosa State Penitentiary',
'Dodge Correctional Institution',
'Menard Correctional Center',
'Chesapeake Detention Facility',
'Indiana State Prison',
'Michigan State Prison',
'Ohio State Penitentiary',
'Eastern Kentucky Correctional Complex',
'List of United States federal prisons']

while True:
    for prison in prisons:
        browser = webdriver.Chrome('/Users/morganmueller/Downloads/chromedriver')
        browser.get('https://www.wikipedia.org/')
        browser.maximize_window()
        #time.sleep(1)
        searchBar = browser.find_element_by_id('searchInput')
        searchBar.send_keys(prison)
        time.sleep(4)


        searchBar.send_keys(Keys.ENTER)
        time.sleep(5)
        scroll_range = browser.find_element_by_class_name('client-js')


        for down in range (0,400):
            scroll_range.send_keys(Keys.ARROW_DOWN)
            print(down)
            time.sleep(.01)

        for up in range(0, 400):
            scroll_range.send_keys(Keys.ARROW_UP)
            print(up)
            time.sleep(.05)

        time.sleep(3)
        browser.close();


# browser.execute_script("window.scrollTo(0, 200)")
# time.sleep(SCROLL_PAUSE_TIME)
# browser.execute_script("window.scrollTo(0, 400)")
# time.sleep(SCROLL_PAUSE_TIME)
# browser.execute_script("window.scrollTo(0, 1080)")
