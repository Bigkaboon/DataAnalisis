import nasdaqdatalink

def get_country_code():
    line = "-" * 30
    print("Country Codes:")
    print(line)

    country_codes = {
        'sweden': 'SWE',
        'united states': 'USA',
        'denmark': 'DNK',
        'norway': 'NOR',
        'brazil': 'BRA',
        'japan': 'JPN',
        'russia': 'RUS',
        'south africa': 'ZAF',
        'turkey': 'TUR',
        'mexico': 'MEX',
        'thailand': 'THA',
    }

    for country in country_codes:
        print(f"{country.capitalize()}")

    country_name = input("What Country Would You Like To See?").lower()

    if country_name in country_codes:
        return country_codes[country_name]
    else:
        print("Country Code not Found")


def get_series_id():

    series_ids = {
    'NY.GDP.MKTP.CD': 'GDP (current US$)',
    'NY.GDP.PCAP.CD': 'GDP per capita (current US$)',
    'SP.POP.TOTL': 'Population, total',
    'NY.GDP.MKTP.KD.ZG': 'GDP growth (annual %)',
    'EN.ATM.CO2E.KT': 'CO2 emissions (kt)',
    'IT.NET.USER.ZS': 'Internet users (% of population)',
    'SE.PRM.TENR': 'Primary completion rate, total (% of relevant age group)',
    'SP.POP.GROW': 'Population growth (annual %)',
    'EG.USE.PCAP.KG.OE': 'Energy use (kg of oil equivalent per capita)',
    'NY.GDP.DEFL.KD.ZG': 'Inflation, GDP deflator (annual %)'
    }

    for serie in series_ids:
        print(f"{serie}")
    
    serie_code = input("What Series Would You Like To See?")

    if serie_code in series_ids:
        return series_ids[serie_code]
    else:
        print("Series Id not Found")


def run_program():
    keepGoing = "y"

    while keepGoing == "y":

        
        series_code = get_series_id()
        country_code = get_country_code()
        

        if country_code:
            api = nasdaqdatalink.ApiConfig.api_key = "qtocsXQd_6id-x16U5Wq"

            table = nasdaqdatalink.get_table('WB/DATA',series_id=series_code, country_code=country_code)

            if table is not None:
                gdp_values = table['value']
                print(table)
            else:
                print("Failed to retrieve data.")

        keepGoing = input ("Do you want to keep looking? (y/n) ").lower()


run_program()