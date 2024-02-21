import requests

urls = [
    'https://habr.com/ru/companies/otus/articles/795065/',
    'https://habr.com/ru/articles/795281/',
    'https://habr.com/ru/articles/795395/',
    'https://habr.com/ru/companies/otus/articles/795391/',
    'https://habr.com/ru/companies/karuna/articles/795139/',
    'https://habr.com/ru/articles/795387/',
    'https://habr.com/ru/articles/795383/',
    'https://habr.com/ru/articles/795379/',
    'https://habr.com/ru/companies/redmadrobot/articles/795375/',
    'https://habr.com/ru/companies/bothub/articles/795143/',
    'https://habr.com/ru/companies/selectel/articles/794396/',
    'https://habr.com/ru/companies/friflex/articles/795347/',
    'https://habr.com/ru/companies/megafon/articles/795261/',
    'https://habr.com/ru/articles/795361/',
    'https://habr.com/ru/companies/onlinepatent/articles/795343/',
    'https://habr.com/ru/companies/piter/articles/795335/',
    'https://habr.com/ru/companies/xeovo/articles/795337/',
    'https://habr.com/ru/articles/795339/',
    'https://habr.com/ru/companies/spaceweb/articles/794993/',
    'https://habr.com/ru/companies/cinimex/articles/795307/',
    'https://habr.com/ru/companies/softpoint/articles/795305/',
    'https://habr.com/ru/companies/glowbyte/articles/795303/',
    'https://habr.com/ru/articles/795297/',
    'https://habr.com/ru/companies/X5Tech/articles/795289/',
    'https://habr.com/ru/articles/792682/',
    'https://habr.com/ru/companies/itsumma/articles/795279/',
    'https://habr.com/ru/articles/795265/',
    'https://habr.com/ru/companies/ru_mts/articles/795257/',
    'https://habr.com/ru/companies/jetinfosystems/articles/795247/',
    'https://habr.com/ru/articles/795105/',
    'https://habr.com/ru/companies/StartX/articles/795245/',
    'https://habr.com/ru/articles/795201/',
    'https://habr.com/ru/articles/795191/',
    'https://habr.com/ru/companies/tinkoff/articles/795061/',
    'https://habr.com/ru/articles/795165/',
    'https://habr.com/ru/companies/timeweb/articles/794941/',
    'https://habr.com/ru/companies/yandex/articles/794883/',
    'https://habr.com/ru/articles/793540/',
    'https://habr.com/ru/articles/794925/',
    'https://habr.com/ru/companies/brave/articles/795125/',
    'https://habr.com/ru/articles/795169/',
    'https://habr.com/ru/companies/yandex_praktikum/articles/793384/',
    'https://habr.com/ru/articles/795027/',
    'https://habr.com/ru/articles/795149/',
    'https://habr.com/ru/articles/795069/',
    'https://habr.com/ru/articles/794769/',
    'https://habr.com/ru/articles/795047/',
    'https://habr.com/ru/companies/bothub/articles/795021/',
    'https://habr.com/ru/companies/piter/articles/795011/',
    'https://habr.com/ru/companies/otus/articles/795035/',
    'https://habr.com/ru/articles/795029/',
    'https://habr.com/ru/companies/amvera/articles/795025/',
    'https://habr.com/ru/companies/ruvds/articles/792058/',
    'https://habr.com/ru/articles/794999/',
    'https://habr.com/ru/companies/pvs-studio/articles/794997/',
    'https://habr.com/ru/companies/auriga/articles/794054/',
    'https://habr.com/ru/companies/slurm/articles/794965/',
    'https://habr.com/ru/companies/lamoda/articles/793716/',
    'https://habr.com/ru/articles/794873/',
    'https://habr.com/ru/articles/794879/',
    'https://habr.com/ru/articles/794805/',
    'https://habr.com/ru/articles/794895/',
    'https://habr.com/ru/articles/794899/',
    'https://habr.com/ru/articles/794903/',
    'https://habr.com/ru/companies/nanosoft/articles/794775/',
    'https://habr.com/ru/companies/simbirsoft/articles/794728/',
    'https://habr.com/ru/companies/sberdevices/articles/794773/',
    'https://habr.com/ru/articles/794388/',
    'https://habr.com/ru/companies/ascon/articles/792200/',
    'https://habr.com/ru/articles/794963/',
    'https://habr.com/ru/specials/792652/',
    'https://habr.com/ru/companies/contentai/articles/794937/',
    'https://habr.com/ru/companies/postgrespro/articles/793068/',
    'https://habr.com/ru/articles/794829/',
    'https://habr.com/ru/articles/794849/',
    'https://habr.com/ru/companies/vk/articles/794164/',
    'https://habr.com/ru/companies/first/articles/794664/',
    'https://habr.com/ru/companies/otus/articles/794360/',
    'https://habr.com/ru/articles/794921/',
    'https://habr.com/ru/articles/794971/',
    'https://habr.com/ru/companies/pt/articles/794632/',
    'https://habr.com/ru/companies/selectel/articles/794927/',
    'https://habr.com/ru/articles/794981/',
    'https://habr.com/ru/articles/794750/',
    'https://habr.com/ru/articles/795057/',
    'https://habr.com/ru/companies/beeline_cloud/articles/795067/',
    'https://habr.com/ru/articles/795091/',
    'https://habr.com/ru/articles/795083/',
    'https://habr.com/ru/articles/795109/',
    'https://habr.com/ru/articles/795127/',
    'https://habr.com/ru/companies/metalamp/articles/795227/',
    'https://habr.com/ru/companies/2gis/articles/794777/',
    'https://habr.com/ru/articles/795231/',
    'https://habr.com/ru/articles/795225/',
    'https://habr.com/ru/articles/795223/',
    'https://habr.com/ru/companies/sigma/articles/795043/',
    'https://habr.com/ru/companies/raft/articles/795085/',
    'https://habr.com/ru/companies/ruvds/articles/794042/',
    'https://habr.com/ru/companies/postgrespro/articles/793156/',
    'https://habr.com/ru/companies/ua-hosting/articles/795179/',
    'https://habr.com/ru/articles/795103/',
]

def download_page(url, filename):
    response = requests.get(url)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

def download_pages():
    for i, url in enumerate(urls):
        filename = f'page_{i + 1}.html'
        download_page(url, filename)

        with open('index.txt', 'a', encoding='utf-8') as index_file:
            index_file.write(f'pages/{filename}: {url}\n')