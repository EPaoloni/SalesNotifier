import json
import urllib.request
from bs4 import BeautifulSoup


def createGamesTableHTML(gameList):
    tableHTML = """\
    <table>
        <thead>
            <tr>
                <th>Game Name</th>
                <th>Special Price</th>
            </tr>
        </thead>
        <tbody>
    """

    for game in gameList['games']:
        gameName = game['gameName']
        gamePrice = game['gamePrice']
        tableHTML += """
        <tr>
            <td>""" + gameName + """</td>
            <td>""" + gamePrice + """</td>
        </tr>
        """

    tableHTML += """
        </tbody>
    </table>"""

    return tableHTML


def searchAllGames():
    gamesPage = urllib.request.urlopen('https://store.nintendo.com.ar')
    soup = BeautifulSoup(gamesPage, 'html.parser')
    gameList = {}
    gameList['games'] = []
    for index, game in enumerate(soup.select('.category-product-item-title')):
        gameName = game.select(
            '.category-product-item-title-link')[0].text.strip()
        gamePrice = game.select('.price')[0].text.strip()
        gameList['games'].append({
            'gameName': gameName,
            'gamePrice': gamePrice
        })
    return gameList


def searchGamesOnSale():
    gamesPage = urllib.request.urlopen('https://store.nintendo.com.ar')
    soup = BeautifulSoup(gamesPage, 'html.parser')
    gameList = {}
    gameList['games'] = []
    for index, game in enumerate(soup.select('.special-price')):
        gameName = game.find_parent('div', {'class': 'category-product-item-title'}).find(
            'a', {'class': 'category-product-item-title-link'}).text.strip()
        gamePrice = game.select('.price')[0].text.strip()
        gameList['games'].append({
            'gameName': gameName,
            'gamePrice': gamePrice
        })
    return gameList


def saveGameList(gameList):
    with open('resources/ReferenceGameList.json', 'w') as outfile:
        json.dump(gameList, outfile)


def getReceiversAddressList():

    receiversAddress = []

    with open("resources/receiversAddress.json") as receiversFile:
        addressesJSON = receiversFile.read()
        receiversAddress = json.loads(addressesJSON)
    
    if receiversAddress == []:
        return ""
    else :
        return receiversAddress['Emails']


def buildEmailMessage():
    gameList = searchGamesOnSale()

    if gameList['games'] == []:
        return None

    htmlMessage = createGamesTableHTML(gameList)
    return htmlMessage
