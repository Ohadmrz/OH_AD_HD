# stocks_data = {
#     'TSLA': {
#         'ticker': 'TSLA',
#         'company_name': 'Tesla',
#         'employees_number': 5000,
#         'address': 'Claifornia',
#         'CEO_name': 'Elon Musk',
#         'stock_data':{
#             '14.11.2021': {
#                 'open': 1001.5,
#                 'close': 1020,
#                 'volume': 50000000
#             },
#             '15.11.2021':{
#                 'open': 1067.7,
#                 'close': 1045.5,
#                 'volume': 45000345
#             }
#         },
#     },
#
#     'AAPL': {
#         'ticker': 'AAPL',
#         'company_name': 'Apple',
#         'employees_number': 10000,
#         'address': 'New York',
#         'CEO_name': 'Tim Cook',
#         'stock_data': {
#             '14.11.2021': {
#                 'open': 320.7,
#                 'close': 322.8,
#                 'volume': 5_345_333
#             },
#             '15.11.2021': {
#                 'open': 300.7,
#                 'close': 320.5,
#                 'volume': 4_000_345
#             }
#         }
#     }
# }
# def get_stocks_stats(stocks_dict: dict) -> dict:
#     ret_dict = {}
#     for ticker, company_dict in stocks_dict.items():
#         ret_dict[ticker] = {}
#         open_sum = 0
#         close_sum = 0
#         volume_sum = 0
#         for date, stock_prices in company_dict['stock_data'].items():
#             open_sum += stock_prices['open']
#             close_sum += stock_prices['close']
#             volume_sum += stock_prices['volume']
#         ret_dict[ticker]['open_avg'] = open_sum / len(company_dict['stock_data'])
#         ret_dict[ticker]['close_avg'] = close_sum / len(company_dict['stock_data'])
#         ret_dict[ticker]['volume_avg'] = volume_sum / len(company_dict['stock_data'])
#     return ret_dict
#
# ret_val = get_stocks_stats(stocks_data)
# print(ret_val)

########################################################################################################################
# author_to_books_and_their_ids = {'amos oz': {
#                            'Amusim Ha avim': {'46596', '57389', '46035'},
#                            'fluk kurishima': {'46196', '57589', '46085'},
#                            'Amusim Mezavim': {'48596', '57489', '46005'}
#                                                                         },
#                 'sofi bukra': {
#                                'hamin taiiim': {'35354', '33346', '44221'},
#                                'hamin shabat': {'35854', '33946', '44291'},
#                                'hamin Ha-min': {'35374', '33326', '44421'}
#                                                                           }
#                                                                            }
#############################################################
#                                    #  replacing 2 lines:
# booksis = {'booki': {'131313'}}    #   |1|-  booksis = {}
# print(booksis)                     #   |2|-  booksis['booki'] = {'131313'}
# booksis['booker'] = '868686'
# print(booksis)
# booksis['booki'].add('232323')
# print(booksis)
#############################################################
# bo2au = {}
#
# bo = {'Fields Of Weedreams': {'03054', '66606'}, 'The Hitchhikers Guide To The Galaxy': {'03053'}}
# bo2au['Zohar Argov'] = bo
# print(bo2au)
#############################################################
# wow = {'Zohar Argov': {'Fields Of Weedreams': {'66606', '03054'}, 'The Hitchhikers Guide To The Galaxy': {'03053'}}}
#
# print('Zhar Argov' in wow)
# print(wow.get('Zohar Argov'))   ##  same
# print(wow['Zohar Argov'])       ##  same
########################################################################################################################
