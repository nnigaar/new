import json


with open ('config.json','r',encoding="utf-8") as file:
    data = json.load(file)


data['vm']['ip'] = '192.168.42.1'
data['vm']['memory'] = '2048'


data['vm']["forwarded_ports"].append({
    "guest_port": 35729,
    "host_port": 35729
  })


data['vdd']["sites"]["drupal7"]["vhost"]["alias"].append(
    "www.admindrupal7.dev")
    
data['vdd']['sites']['drupal7']['account_name'] = 'my_account_name'
data['vdd']['sites']['drupal7']['account_mail'] = 'my_account_mail'
data['vdd']['sites']['drupal7']['account_pass'] = '12345'




with open("my_config.json", "w") as file:
    json.dump(data, file)