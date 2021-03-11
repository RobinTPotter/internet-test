from datetime import datetime

def page():
    
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
    

    now = datetime.now()
    
    output = """<html>
<head>
<style>
td.c {{ text-align: center }}
th {{ text-align: center }}
table, th, td {{ border: 1px solid black }}
</style>
</head>
<body>
{}
<table>
<thead>
<th>time</th><th>minutes</th><th>seconds</th>
</thead>
""".format(now.strftime("%d/%m/%Y %H:%M:%S"))
    
    for d in drops:
        output += '<tr><td>{}</td><td class="c">{}</td><td class="c">{}</td></tr>\n'.format(datetime.utcfromtimestamp(d[0]).strftime('%d/%m/%Y %H:%M:%S'), int(d[1]/60), d[1]-(60*int(d[1]/60)))
    
    output += """</table>
</body>
</html>
"""
    
    return output

if __name__ == "__main__":
    print(page())
