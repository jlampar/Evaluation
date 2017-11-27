# -*- coding: utf-8 -*-
#####
#Lamparski Jakub, 11.11.2017
#v2.5
#Program takes 3 files as the input:
#- products.csv - products table (price,currency,quantity,corresponding_id
#- currency_ratio.csv - currencies and their ratio to PLN
#- correspondence.csv - limits of products count in cateogories
#Program reads all files and converts them to dictionaries. Then from products dictionary with particular corresponding ID it takes those with the highest total price (price * quantity), limiting data set by limit and aggregates prices.
#Results are saved to finest.csv with five columns: id, in_total, avgerage, currency,ignored. It summarizes the total and average price of products of each category and moreover how many products are ignored due to the limits.
#Output is placed into the same directory as input
#####

import csv

def csv_dict_loader(dict_file):

    csv_dict = {}

    for row in csv.DictReader(open(dict_file)):
        for col, value in row.iteritems():
            csv_dict.setdefault(col, []).append(value)

    return csv_dict

def compute_total_price(products,currence):

    total = []

    for elements_product in products['id']:
        nr = int(elements_product) - 1
        currency_index = currence['code'].index(products['currency'][nr])
        ratio = (float(currence['ratio'][currency_index]))
        total.append((int(products['price'][nr]) / ratio) * int(products['quantity'][nr]))

    return total

def sort_groups(products,total,match):

    zip_list = [list(x) for x in zip(products['currency'], products['quantity'], products['corresponding_id'], total)]

    match_list = []
    sorted_list = []

    for m_id in match['corresponding_id']:
        match_list.append([])

    for ele in zip_list:
        match_list[int(ele[2]) - 1].append(ele[3])

    for every_sub_list in match_list:
        sorted_list.append(sorted(every_sub_list, reverse=True))

    return sorted_list

def generate_output(sorted_group,match,test):

    output_list = []

    for every_element in sorted_group:
        index = sorted_group.index(every_element)
        count = int(match['limit'][index])
        ignored = len(every_element) - count
        total = 0
        for elements_element in every_element[0:count]:
            total += elements_element

        average = total / count

        t = '%.2f' % total
        av = '%.2f' % average

        output_list.append([index + 1, t, av, 'PLN', ignored])

    file_name = 'finest' + test + '.csv'

    with open(file_name, 'wb') as write_file:
        writer = csv.writer(write_file)
        writer.writerow(['id', 'in_total', 'average', 'currency', 'ignored'])
        writer.writerows(output_list)

data = csv_dict_loader('products.csv')
currencies = csv_dict_loader('currency_ratio.csv')
correspond = csv_dict_loader('correspondence.csv')

total_price = compute_total_price(data,currencies)

sorted_group = sort_groups(data,total_price,correspond)

generate_output(sorted_group,correspond,'')
