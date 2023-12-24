from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element("css selector",
                            '.main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(1) > a:nth-child(1)')
elem.click()

elems = browser.find_elements("css selector", 'p')
print(len(elems))
print(elems[1].text)

elem = browser.find_element('css selector', 'html')
print(elem.text)

# searchElem = browser.find_element("css selector", '.search-field')
# searchElem.send_keys('Zophie')
# searchElem.submit()

browser.back()
browser.forward()
browser.refresh()
browser.quit()
