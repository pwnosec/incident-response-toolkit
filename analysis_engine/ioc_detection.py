def check_iocs(ioc_list, data):
    matches = [ioc for ioc in ioc_list if ioc in data]
    return matches
