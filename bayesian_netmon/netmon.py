import requests
import datetime

BAYESIAN_NETMON_URL = 'https://api.bayesian.io'

def get_country_stats(cnt = 10, end = datetime.datetime.utcnow(), start = (datetime.datetime.utcnow() + datetime.timedelta(days = -1)), key = ''):
	ENDPOINT = '/v1/stats/countries'
	req_data = {
		'cnt' : cnt,
		'end' : end.isoformat(),
		'start' : start.isoformat(),
		'key' : key,
	}
	r = requests.post('%s%s' % (BAYESIAN_NETMON_URL, ENDPOINT), json=req_data)
	if r.status_code != 200:
		raise Exception('get_country_stats Server error! %s' % r.text)
	return r.json()
	
def get_port_stats(cnt = 10, end = datetime.datetime.utcnow(), start = (datetime.datetime.utcnow() + datetime.timedelta(days = -1)), key = ''):
	ENDPOINT = '/v1/stats/ports'
	req_data = {
		'cnt' : cnt,
		'end' : end.isoformat(),
		'start' : start.isoformat(),
		'key' : key,
	}
	r = requests.post('%s%s' % (BAYESIAN_NETMON_URL, ENDPOINT), json=req_data)
	if r.status_code != 200:
		raise Exception('get_port_stats Server error! %s' % r.text)
	return r.json()
	
def get_ip_info(ip, end = datetime.datetime.utcnow(), start = (datetime.datetime.utcnow() + datetime.timedelta(days = -1)), key = ''):
	ENDPOINT = '/v1/query/ip'
	req_data = {
		'ip' : ip,
		'end' : end.isoformat(),
		'start' : start.isoformat(),
		'key' : key,
	}
	r = requests.post('%s%s' % (BAYESIAN_NETMON_URL, ENDPOINT), json=req_data)
	if r.status_code != 200:
		raise Exception('get_ip_info Server error! %s' % r.text)
	return r.json()
	
def get_country_ips(country_code, end = datetime.datetime.utcnow(), start = (datetime.datetime.utcnow() + datetime.timedelta(days = -1)), key = ''):
	ENDPOINT = '/v1/query/country'
	req_data = {
		'country' : country_code,
		'end' : end.isoformat(),
		'start' : start.isoformat(),
		'key' : key,
	}
	r = requests.post('%s%s' % (BAYESIAN_NETMON_URL, ENDPOINT), json=req_data)
	if r.status_code != 200:
		raise Exception('get_country_ips Server error! %s' % r.text)
	return r.json()
	
def get_ips_for_tag(tag, end = datetime.datetime.utcnow(), start = (datetime.datetime.utcnow() + datetime.timedelta(days = -1)), key = ''):
	ENDPOINT = '/v1/query/tag'
	req_data = {
		'tag' : tag,
		'end' : end.isoformat(),
		'start' : start.isoformat(),
		'key' : key,
	}
	r = requests.post('%s%s' % (BAYESIAN_NETMON_URL, ENDPOINT), json=req_data)
	if r.status_code != 200:
		raise Exception('get_ips_for_tag Server error! %s' % r.text)
	return r.json()
	
if __name__ == '__main__':
	print('Getting cuntry statistics!')
	stats = get_country_stats()
	for country, hits in stats['countries']:
		print('%s:%s' % (country, hits))
	
	print('Getting port statistics!')
	stats = get_port_stats()
	for country, hits in stats['ports']:
		print('%s:%s' % (country, hits))
	
	ip = '8.8.8.8'
	print('Looking up IP %s' % ip)
	query = get_ip_info(ip)
	if len(query['tags']) == 0:
		print('No info found for IP %s' % ip)
	else:
		for tag in query['tags']:
			print(tag)
		
	country = 'NL'
	print('Listing observed IPs for the country %s' % country)
	query = get_country_ips(country)
	if len(query['ips']) == 0:
		print('No info found for country %s' % country)
	else:
		for ip in query['ips']:
			print(ip)
		
	tag = 'VNC_BRUTEFORCER_HIGH'
	print('Looking up IPs for tag %s' % tag)
	query = get_ips_for_tag(tag)
	for ip in query['ips']:
		print(ip)