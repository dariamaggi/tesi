import random
import time
import networkx


def intersect(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)


def arrange(listone):
    ter = len(listone) - 1
    while ter > 0:
        for i in range(ter):
            if listone[ter][1] > listone[i][1]:
                temp = listone[i]
                listone[i] = listone[ter]
                listone[ter] = temp
        ter -= 1
    return listone


def conta1(A, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1:
                count += 1
    return count


def anydup(thelist):
    seen = set()
    for x in thelist:
        if x in seen: return True
        seen.add(x)
    return False


def M0(A, A_star, n):
    onesA = 0
    corrisp = 0
    err = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] is 1:
                onesA += 1
                if A_star[i][j] is 1:
                    corrisp += 1  # ho azzeccato
            else:
                if A_star[i][j] is 1:  # colleg inaspettato
                    err += 1
    return [onesA, corrisp, err]


class Browser:
    def __init__(self, id, nav_type):
        self.limit = 3
        self.cat = []
        self.id = id
        self.reserve = []
        self.nav_type = nav_type
        if nav_type == "mobile":
            self.cache_len = 10
        else:
            if nav_type == "desktop":
                self.cache_len = 100
        self.cache = []
        self.full = False
        self.partners = []

    def findoccurrance(self, cat):
        occ = []
        for elem in cat:
            for it in self.reserve:
                if it[0] == elem and it[1] > 0:
                    occ.append([it[0], it[1]])
        return occ

    def updateUtility(self, news):
        for part in self.partners:
            for elem in news:
                if part.full is False and elem not in part.cache and intersection(part.cat, pages[elem][1]):
                    part.cache.append(elem)
                    if len(part.cache) == self.cache_len:
                        self.full = True
                if self.full:
                    break

    def countcats(self):
        lista = []
        for elem in self.cache:
            for iter in pages[elem][1]:
                lista.append(iter)
        return lista

    def uppity(self, page, rank):
        for part in self.partners:
            if part.reference[page - 1][0] > rank:
                return True
        return False

    def findrank(self, cat):
        pos=0
        for elem in self.reserve:
            if elem[0] == cat:
                pos=elem[1]
                break
        return pos

if __name__ == '__main__':
    pages = []
    browsers = []
    temp = []
    cat_types = []
    nav_types = ["mobile", "desktop"]
    numCats = 15
    numPages = 1000
    numBrowsers = 500

    for i in range(1, numCats):
        cat_types.append(i)

    for j in range(numPages):
        pages.append([str(j), []])
        pages[j][1].append(random.sample(cat_types, 3))
        pages[j][1] = pages[j][1][0]

    static_graph = [[0 for x in range(numPages)] for y in range(numPages)]
    inferred_graph = [[0 for x in range(numPages)] for y in range(numPages)]

    for i in range(numPages):
        for j in range(numPages):
            if i == j or intersection(pages[i][1], pages[j][1]) < 2:
                static_graph[i][j] = random.choice([0,1,1])
            else:
                static_graph[i][j] = 1
    print(conta1(static_graph, numPages))
    for j in range(numBrowsers):
        browsers.append(Browser(j, "desktop"))

    successors = []

    for browser in browsers:
        seed = random.choice(range(numPages))
        res = True
        successors.append(seed)
        while res is True and len(browser.cache) < browser.cache_len:
            seed = random.choice(successors)
            successors = []
            browser.cache.append(seed)
            for j in range(numPages):
                if static_graph[seed][j] == 1:
                    successors.append(j)
            if successors == []:
                res = False
            if browser.cache_len==len(browser.cache):
                temp.append(browser.id)
                browser.full=True
                res=False
            else:
                res = random.choice(
                    [True, True, True,
                     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                     True, True,
                     True, True, False])
    avgd = 0
    avgm = 0
    numD = 0
    numM = 0
    arr_new = 0

    for browser in browsers:
        if browser.nav_type == "desktop":
            avgd += len(browser.cache)
            numD += 1
    print(avgd / numD)

    for browser in browsers:
        for j in range(len(browser.cache) - 1):
            inferred_graph[browser.cache[j]][browser.cache[j + 1]] = 1

    print(M0(static_graph, inferred_graph, numPages))

    for browser in browsers:
        caters = browser.countcats()
        ranged = numCats + 1
        ranks = []
        for j in range(1, ranged):
            ranks.append(caters.count(j))
        result = []

        lista1 = [[0, 0] for k in range(numCats)]
        for i in range(len(ranks)):
            lista1[i][0] = i + 1
            lista1[i][1] = ranks[i]
        lista1 = arrange(lista1)
        browser.reserve = lista1
        limite = min(browser.limit, len(lista1))
        for k in range(limite):
            browser.cat.append(lista1[k][0])

    numo = 0
    for i in range(100000):
        news = []
        partner1 = browsers[0]
        partner2 = browsers[0]
        while partner1 == partner2 or partner1.id in temp:
            couple = random.sample(range(numBrowsers), 2)
            partner1 = browsers[couple[0]]
            partner2 = browsers[couple[1]]
        carts = intersect(partner1.cat, partner2.cat)
        esito = len(carts) > 1
        if esito:
            for page in partner2.cache:
                if page not in partner1.cache and partner1.full == False and intersection(pages[page][1],
                                                                                          partner1.cat) > 0:
                    partner1.cache.append(page)
                    news.append(page)
                    j = len(partner1.cache) - 1
                    while j > 0:
                        if intersection(pages[partner1.cache[j]][1], pages[page][1]) > 0:
                            inferred_graph[partner1.cache[j]][page] = 1
                            break
                        j -= 1
                    if j == 0:
                        inferred_graph[page][page] = 1
                    for cats in pages[page][1]:
                        for elem in partner1.reserve:
                            if elem[0] == cats:
                                elem[1] += 1
                    partner1.reserve = arrange(partner1.reserve)
                    if partner1.reserve[0][0] not in partner1.cat:
                        partner1.cat.append(partner1.reserve[0][0])
                        print("escargot")

                    if len(partner1.cache) == partner1.cache_len:
                        partner1.full = True
                        temp.append(partner1.id)

            if news != []:
                for part in partner1.partners:
                    for page in news:
                        if page not in browsers[part].cache and intersection(pages[page][1], browsers[part].cat) > 0:
                            if browsers[part].full is False:
                                browsers[part].cache.append(page)
                                j = len(browsers[part].cache) - 1
                                while j >= 0:
                                    if intersection(pages[browsers[part].cache[j]][1], pages[page][1]) > 0:
                                        numo += 1
                                        inferred_graph[browsers[part].cache[j]][page] = 1
                                        break
                                    j -= 1
                                if j == 0:
                                    inferred_graph[page][page] = 1
                                    numo += 1
                                for cats in pages[page][1]:
                                    for elem in browsers[part].reserve:
                                        if elem[0] == cats:
                                            elem[1] += 1
                                listone = arrange(partner1.reserve)
                                if listone[0][0] not in partner1.cat:
                                    partner1.cat.append(listone[0][0])

                                if len(browsers[part].cache) == browsers[part].cache_len:
                                    browsers[part].full = True
                                    temp.append(part)

                if partner2.id not in partner1.partners:
                    # and len(news) >= len(partner1.cache) / 10
                    partner1.partners.append(partner2.id)
                    if partner1.id not in partner2.partners:
                        partner2.partners.append(partner1.id)


        else:
            lent = (int)(len(partner2.cache) / 2)
            news = random.sample(partner2.cache, lent)
            for page in partner2.cache:
                rks = []
                for cats in pages[page][1]:
                    rkp1 = partner1.findrank(cats)
                    rkp2 = partner2.findrank(cats)
                    found = False
                    if cats in partner1.cat or (rkp1 > 0 and rkp2 > 0):
                        for part in partner1.partners:
                            if page in browsers[part].cache or browsers[part].findrank(cats) > rkp2:
                                found = True
                                break
                        if found is False:
                            partner1.cache.append(page)
                            j = len(partner1.cache) - 1
                            while j>=0:
                                if intersection(pages[partner1.cache[j]][1], pages[page][1]) > 0:
                                    inferred_graph[partner1.cache[j]][page] = 1
                                    break
                                j -= 1
                            if j == 0:
                                inferred_graph[page][page] = 1
                            for elem in partner1.reserve:
                                if elem[0]==cats:
                                    elem[1]+=1
                            partner1.reserve=arrange(partner1.reserve)
                            if partner1.reserve[0][0] not in partner1.cat:
                                partner1.cat.append(partner1.reserve[0][0])
                            for part in partner1.partners:
                                if intersection(browsers[part].cat, pages[page][1])>1:
                                    browsers[part].cache.append(page)
                                    for cater in pages[page][1]:
                                        for elem in browsers[part].reserve:
                                            if elem[0]==cater:
                                                elem[1]+=1
                                                break
                                    browsers[part].reserve=arrange(browsers[part].reserve)
                                    if browsers[part].reserve[0][0] not in browsers[part].cat:
                                        browsers[part].cat.append(browsers[part].reserve[0][0])



                        if len(partner1.cache) == partner1.cache_len:
                            partner1.full = True
                            temp.append(partner1.id)
    for browser in browsers:
        print(browser.id, browser.partners)
    print(M0(static_graph, inferred_graph, numPages))
    print(len(temp))

    print("VAL ggiunro" + str(numo))
''' 
            esitA = False
            esitB = False
            for elem in partner2.cat:
                for iter in partner1.reserve:
                    if iter[0] == elem and iter[1] > 0:
                        esitA = True
                        break
            for elem in partner1.cat:
                for iter in partner2.reserve:
                    if iter[0] == elem and iter[1] > 0:
                        esitB = True
                        break

            exit = False
         
            if esitA and esitB:
                news = []
                for elem in partner2.cache:
                    if elem not in partner1.cache:
                        inter = partner1.findoccurrance(pages[elem][1])
                        found = False
                        pos = 0
                        for page in inter:
                            pos = 0
                            myvalue = page[1]
                            for partner in partner1.partners:
                                for elem in partner.reserve:
                                    if elem[0] == page and elem[1] > myvalue:
                                        pos = elem[1]
                                        found = True
                                        break
                                if found:
                                    break
                            if found is False:
                                news.append(page)
                                j = len(partner1.cache) - 1
                                while j >= 0:
                                    if page[1] in pages[partner1.cache[j]][1]:
                                        inferred_graph[partner1.cache[j]][page[0]] = 1
                                        break
                                    j -= 1

    print(conta1(inferred_graph, numPages))
    print(M0(static_graph, inferred_graph, numPages))
'''
