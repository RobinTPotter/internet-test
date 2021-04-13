from datetime import datetime

def page():
    
    with open("pingtest.txt","r") as f:
        data = f.readlines()
    
    data = [d.split() for d in data]
    
    data0 = [[int(d[0]),d[5]] for d in data]
    
    data = []
    drops = []
    drop_days = []
    
    
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
                start_drop_day = datetime.utcfromtimestamp(start_drop).strftime('%d/%m/%Y')
                if not start_drop_day in drop_days: drop_days.append(start_drop_day)
    
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
<form>
{}
</form>
<table>
<thead>
<th>day</th><th>time</th><th>minutes</th><th>seconds</th>
</thead>
""".format(now.strftime("%d/%m/%Y %H:%M:%S"),''.join(["<input type=\"checkbox\" name=\"b\" value=\"{}\" onclick=\"filter(event)\">{}</input>".format(d,d) for d in drop_days]))
    
    for d in drops:
        output += '<tr name="{}" style="display:none"><td>{}</td><td>{}</td><td class="c">{}</td><td class="c">{}</td></tr>\n'.format(datetime.utcfromtimestamp(d[0]).strftime('%d/%m/%Y'),datetime.utcfromtimestamp(d[0]).strftime('%d/%m/%Y'), datetime.utcfromtimestamp(d[0]).strftime('%H:%M:%S'), int(d[1]/60), d[1]-(60*int(d[1]/60)))
    
    output += """</table>
<script>
function filter(x) {
console.log(x)
these = document.getElementsByName(x.srcElement.value)
console.log(these)
if (!x.srcElement.checked) {
these.forEach(function(v) {
v.style.display="none"
})}
else {
these.forEach(function(v) {
v.style.removeProperty("display")
})}
}
</script>
</body>
</html>
"""
    
    return output

if __name__ == "__main__":
    print(page())
