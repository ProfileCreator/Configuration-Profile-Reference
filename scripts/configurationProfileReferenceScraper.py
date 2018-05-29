#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urlparse import urljoin
import bs4
import os
import sys
import requests
import datetime
import re

projectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

markdownPath = os.path.join(projectPath, 'markdown')
htmlPath = os.path.join(projectPath, 'html')

currentDate = datetime.date.today()
currentDateString = currentDate.strftime('%Y-%m-%d')

currentPath = os.path.join(htmlPath, 'current.html')

pageURL = 'https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html'

titlesIgnored = [ 'Payload-Specific Property Keys' ]

def downloadCurrentPage():
	currentPage = requests.get(pageURL)

	currentPageSoup = BeautifulSoup(currentPage.content, 'html.parser')

	documentVersionTag = currentPageSoup.find('meta', {"id": "document-version"})
	documentVersion = unicode(documentVersionTag['content'])

	documentDateTag = currentPageSoup.find('meta', {"id": "date"})
	documentDate = unicode(documentDateTag['content'])

	pagePath = os.path.join(htmlPath, 'page-' + documentVersion + '_' + documentDate + '_' + currentDateString + '.html')

	with open(pagePath, 'w+') as pageFile:
		pageFile.write(currentPage.content)

	if os.path.exists(currentPath):
		os.unlink(currentPath)
	os.symlink(pagePath, currentPath)

def sectionTable(tag):
	sectionTableString = ""
	table = tag.find('table', attrs={'class':'graybox'})
	rows = table.find_all('tr')
	for row in rows:
		sectionTableString += '|'

		# Header
		headers = row.find_all('th')
		headerSubrow=""
		for ele in headers:
			for content in ele.contents:
				sectionTableString += unicode(ele.text) + '|'
			headerSubrow += "-|"

		if headerSubrow:
			sectionTableString += '\n|' + headerSubrow

		# Row
		cols = row.find_all('td')
		for ele in cols:
			rowString = ""
			for idx, aTag in enumerate(ele.children):
				if aTag.name == "ul":
					rowString += '</br>' + sectionList(tag, True) + '</br>'

				elif aTag.name == "p":
					if idx == 0:
						rowString += sectionString(aTag)
					else:
						rowString += '</br>' + sectionString(aTag)

				# Ignore newlines
				elif unicode(aTag) == u"\n":
					continue

				else:
					tagName = ""
					if aTag.name:
						tagName = aTag.name
					print("FIXME - Unhandled td tag: " + tagName + " is type: " + str(type(aTag)))
			
			sectionTableString += rowString + '|'
		sectionTableString += '\n'
	return sectionTableString

def sectionSpanHref(tag):
	sectionSpanHrefString = ""
	for a in tag.find_all('a', href=True):
		link = a['href']
		text = unicode(a.text)
		if link.startswith("#"):
			sectionSpanHrefString += '[' + text + '](' + pageURL + link + ')'
		elif link.startswith("http"):
			sectionSpanHrefString += '[' + text + '](' + link + ')'
		elif link.startswith(".."):
			sectionSpanHrefString += '[' + text + '](' + urljoin(pageURL, link) + ')'
		else:
			print("FIXME - Unhandled href link: " + link)
	return sectionSpanHrefString

def sectionString(tag):
	cleanedString = ""
	for content in tag.contents:
		
		# Check if this string contains an emphazised link
		if content.name == "em" and content.children and any(isinstance(x, bs4.element.Tag) for x in list(content.children)):
			cleanedString += "*"
			for child in content.children:
				if child.name == "a":
					cleanedString += sectionSpanHref(content)
				else:
					cleanedString += unicode(child)
			cleanedString += "*"

		# Check if this string contains a span
		elif content.name == "span" or ( content.name == "a" and content['href'] ):
			cleanedString +=  sectionSpanHref(content)

		# Replace html tags with markdown
		else:
			cleanedString += unicode(content)
			cleanedString = re.sub(r"(<code>|</code>)", "`", cleanedString)
			cleanedString = re.sub(r"(<strong>|</strong>)", "**", cleanedString)
			cleanedString = re.sub(r"(<em>|</em>)", "*", cleanedString)
			cleanedString = re.sub(r"(<!--.*?-->)", "", cleanedString)
			if "<" in cleanedString:
				print("FIXME - Unhandled tag in string: " + cleanedString)

	return cleanedString

def sectionBox(tag):
	sectionBoxString = ""
	for pTag in tag.find_all("p"):
		string = sectionString(pTag)
		if unicode(string) != u"":
			sectionBoxString += '\n> ' + sectionString(pTag) + '  \n'
	return sectionBoxString

def sectionTitle(element):
	if element.name == "a":
		return element["title"]
	else:
		tag = element.find("a")
		if tag["title"]:
			return tag["title"]

def sectionLink(element):
	if element.name == "a":
		link = element["name"]
	else:
		tag = section.find("a")
		link = tag["name"]
	if link:
		return pageURL + '#' + link

def sectionList(tag, htmlNewlines=False, ordered=False):
	sectionListString = ""
	for idx, li in enumerate(tag.find_all("li")):
		for tag in li.children:
			indexCharacter="*"
			if ordered:
				indexCharacter = str(idx + 1)

			if htmlNewlines:
				sectionListString += '</br>' + indexCharacter + ' ' + sectionString(tag) + '  </br>'
				
			else:
				sectionListString += '\n' + indexCharacter + ' ' + sectionString(tag) + '  \n'
				
	return sectionListString

def sectionCodeSample(tag):
	sectionCodeSampleString = "```"

	table = tag.find('table')
	rows = table.find_all('tr')
	for row in rows:

		# Row
		cols = row.find_all('td')
		for ele in cols:
			rowString = ""
			for idx, aTag in enumerate(ele.children):
				if aTag.name == "pre":
					rowString += '\n' + unicode(aTag.text)
				else:
					try:
						print("FIXME - Unhandled codesample tag: " + aTag.name + " is type: " + str(type(aTag)))
						print(aTag)
					except:
						print("FIXME - Unhandled codesample tag: " + aTag.name)
						print(aTag)

			sectionCodeSampleString += rowString

	sectionCodeSampleString += "\n```"
	return sectionCodeSampleString

def exportSection(section, writeToFile=True):

	try:
		title = sectionTitle(section)
		if not title:
			print("ERROR: No title returned for section")
			return
		if title in titlesIgnored:
			print("Ignoring title: " + title)
			return
	except:
		print("ERROR: No title returned for section")
		return

	sectionPath = os.path.join(markdownPath, title + '.md')
	if writeToFile:
		sectionContent = "# " + title + '  \n'
	else:
		sectionContent = "### " + title + '  \n'

	link = sectionLink(section)
	if not link:
		print("ERROR: No link returned for section")
	else:
		sectionContent += '\n [' + 'Configuration Profile Reference - ' + title + '](' + link + ')  \n'

	# Loop through all child tags to the current section
	for tag in section.children:

		# Get tag name
		try:
			tagName = tag.name
		except:
			pass
		if tagName is None:
			tagName = '<unknown>'

		# Check if tag is an a tag, meaning title
		if tagName == "a" and tag["title"]:
			if title != tag["title"]:
				subtitle = sectionTitle(tag)
				if not subtitle:
					print("ERROR: No title returned for tag a")
					continue

				sublink = sectionLink(tag)
				if sublink:
					sectionContent += '### [' + subtitle + '](' + sublink + ')  \n'
				else:
					sectionContent += '### ' + subtitle + '  \n'

		# Check if tag is an p tag, meaning title
		elif tagName == "p":
			sectionContent += '\n' + sectionString(tag) + '  \n'

		# Check if tag is a div with a class 'tableholder', meaning table
		elif tagName == "div" and tag['class'] == ['tableholder']:
			sectionContent += '\n' + sectionTable(tag) + '  \n'

		# Check if tag is a div with a class 'notebox', meaning notebox
		elif tagName == "div" and tag['class'] == ['notebox']:
			sectionContent += '\n' + sectionBox(tag) + '  \n'

		# Check if tag is importantbox
		elif tagName == "div" and tag['class'] == [u'importantbox', u'clear']:
			sectionContent += '\n' + sectionBox(tag) + '  \n'

		# Check if tag is warningbox
		elif tagName == "div" and tag['class'] == [u'warningbox', u'clear']:
			sectionContent += '\n' + sectionBox(tag) + '  \n'

		# Check if tag is codesample
		elif tagName == "div" and tag['class'] == [u'codesample', u'clear']:
			sectionContent += '\n' + sectionCodeSample(tag) + '  \n'

		# Check if tag is an ul tag, meaning list
		elif tagName == "ul":
			sectionContent += '\n' + sectionList(tag, False, False) + '  \n'

		# Check if tag is an ol tag, meaning ordered list
		elif tagName == "ol":
			sectionContent += '\n' + sectionList(tag, False, True) + '  \n'

		# Check if tag is a subsection
		elif tagName == "section":
			sectionContent += '\n' + exportSection(tag, False) + '  \n'

		# Ignored tags below
		elif re.match('h[2-9]', tagName) and tag['class'] == ['jump']:
			continue

		# Ignore newlines
		elif unicode(tag) == u"\n":
			continue

		# If tagname is not handled, print it out so we can add support
		else:
			try:
				print("FIXME - Unhandled section tag: " + tagName + " is type: " + str(type(tag)))
				print(tag)
			except:
				print("FIXME - Unhandled section tag: " + tagName + " is type: <unknown>")
				print(tag)

	if writeToFile:
		with open(sectionPath, 'w+') as sectionFile:
			sectionFile.write(sectionContent.encode('utf-8'))

	return sectionContent

def deleteCurrentMarkdown():
	for file in os.listdir(markdownPath):
		path = os.path.join(markdownPath, file)
		try:
			if os.path.isfile(path):
				os.unlink(path)
		except Exception as e:
			print(e)

# Download the current page and check if it has changed
downloadCurrentPage()

# Open the current page html file
with open(currentPath, 'r') as f:
    file_content = f.read().decode('utf-8')

    # Read the html in the BeautifulSoup parser
    soup = BeautifulSoup(file_content, 'html.parser')

    # Get all <section> elements in a list
    article = soup.find('article')
    topSections = article.find_all('section', recursive=False)
    payloadSections = []

    # Prepare the allSections file
    allSections = ""
    allSectionsPath = os.path.join(markdownPath, '_All.md')

    # Delete all current markdown files
    deleteCurrentMarkdown()

    # Loop through all top level sections and export their contents to their respective markdown document
    for section in topSections:
    	sectionContent = exportSection(section)
    	if sectionContent:
    		allSections += '\n' + sectionContent
    	payloadSections += section.find_all('section', recursive=False)

    # Loop through all payload sections and export their contents to their respective markdown document
    for section in payloadSections:
    	sectionContent = exportSection(section)
    	if sectionContent:
    		allSections += '\n' + sectionContent


    # Write to allSections content to file
    with open(allSectionsPath, 'w+') as allSectionsFile:
		allSectionsFile.write(allSections.encode('utf-8'))
