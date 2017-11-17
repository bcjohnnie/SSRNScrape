import requests, re
from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://papers.ssrn.com/sol3/JelJour_Results.cfm?Network=no&form_name=journalBrowse&journal_id=157488')

sortElem = browser.find_element_by_css_selector('#sort-by')
sortElem.click()
clickElem = browser.find_element_by_css_selector('#sort-by > option:nth-child(6)')
clickElem.click()

bodyElem = browser.find_element_by_css_selector('.tbody')
body = bodyElem.get_attribute('innerHTML')

stopInd = body.find('11.')
html = body[:stopInd]

regex = re.compile(r"\s*(<[^<>]+>)\s*")
html2 = regex.sub("\g<1>", html)
html2 = html2[33:]


browser.close()

print(len(html2))

for i in range (10):
    print("Entry: " + str(i + 1))
    endRange = html2.find('<div class="trow')
    range = html2[:endRange]
    absLinkStart = range.find('href')
    absLinkEnd = range.find('>', absLinkStart)
    absLink = range[absLinkStart + 6: absLinkEnd - 1]
    print(absLink)
    titleStart = absLinkEnd + 1
    titleEnd = range.find('</a>')
    title = range[titleStart:titleEnd]
    print(title)
    if (range.find('<i>', titleEnd) != -1):
        citStart = range.find('<i>', titleEnd)
        citEnd = range.find('</i>', citStart)
        citation = range[citStart + 3: citEnd]
        print(citation)
    dateStart = range.find('Posted:', titleEnd)
    dateEnd = range.find('</span>', dateStart)
    date = range[dateStart:dateEnd]
    authEnd = dateEnd
    while(range.find('AbsByAuth', authEnd) != -1):
        authLinkStart = range.find('href', authEnd)
        authLinkEnd = range.find('target', authLinkStart)
        authLink = range[authLinkStart + 6: authLinkEnd - 1]
        authStart = range.find('>', authLinkEnd)
        authEnd = range.find('</a>', authLinkStart)
        author = range[authStart + 1: authEnd]
        print(authLink)
        print(author)
    affStart = range.find('afiliations', authEnd)
    affEnd = range.find('</div>', affStart)
    affiliations = range[affStart + 13: affEnd]
    print(affiliations)
    
    html2 = html2[endRange + 33:]
    
