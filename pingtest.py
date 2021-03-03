from datetime import datetime


with open("pingtest.txt","r") as f:
    data = f.readlines()

data = [d.split() for d in data]

data0 = [[int(d[0]),d[-2]] for d in data]

data = []
drops = []


for d in data0:
    if d[1]=='is': data.append([d[0],'no wifi'])
    elif d[1]=='Net': data.append([d[0],'no internet'])
    else: data.append([d[0],'ok'])

# print(data[:10])

status = None
start_drop = 0

for d in data:
    if status is None: status = d[1]
    if d[1] != status:
        if status == 'ok' and d[1] == 'no internet':
            start_drop = d[0]
        if status == 'no internet' and d[1] == 'ok':
            drops.append([start_drop, d[0]-start_drop])

        status = d[1]

print ('<html>')
print ('<head>')
print ('<style>')
print ('td.c { text-align: center }')
print ('th { text-align: center }')
print ('table, th, td { border: 1px solid black }')

print ('</style>')
print ('</head>')
print ('<body>')
print ('<table>')

print ('<thead>')
print ('<th>time</th><th>minutes</th><th>seconds</th>')
print ('</thead>')

for d in drops:
    print('<tr><td>{}</td><td class="c">{}</td><td class="c">{}</td></tr>'.format(datetime.utcfromtimestamp(d[0]).strftime('%d/%m/%Y %H:%M:%S'), int(d[1]/60), d[1]-(60*int(d[1]/60))))

print ('</table>')
print ('</body>')
print ('</html>')

