from datetime import datetime, timezone
import pytz

PERIOD = 300

def page():
    
    with open("pingtest2.txt","r") as f:
        data = f.readlines()
    
    data = [d.split() for d in data]
    #print(data[:2])
    
    data0 = [  [ int(d[0]), d[1].split("=")[1] if "=" in d[1] else ""  ] for d in data if len(d)>1 ]
    #print(data0)
    
    data = []
    drops = []
    drop_days = []
    
    drops = list(set([  PERIOD*int(d[0]/PERIOD)  for d in data0 ]))
    drops = [ [ dd for dd in data0 if PERIOD*int(dd[0]/PERIOD)==d ]  for d in drops  ]
    #print(drops[:10])
    drops =sorted( [ [d[0][0],sum([ float(dd[1]) for dd in d if dd[1]!="" ])/len(d),   max( [ float(dd[1]) for dd in d if dd[1]!="" ] ) ]  for d in drops ])
    now = datetime.now()
    #print(drops[:5])
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
<th>day</th><th>time</th><th>ave. lat</th><th>max. lat</th>
</thead>
""".format(now.strftime("%d/%m/%Y %H:%M:%S"),''.join(["<input type=\"checkbox\" name=\"b\" value=\"{}\" onclick=\"filter(event)\" {}>{}</input>".format(d,"checked",d) for d in drop_days]))
    
    for d in drops:
        output += '<tr name="{}" style="display:display"><td>{}</td><td>{}</td><td class="c">{}</td><td class="c">{}</td></tr>\n'.format(
            datetime.utcfromtimestamp(d[0]).replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/London')).strftime('%d/%m/%Y'),
            datetime.utcfromtimestamp(d[0]).replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/London')).strftime('%d/%m/%Y'), 
            datetime.utcfromtimestamp(d[0]).replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/London')).strftime('%H:%M:%S'), 
            int(d[1]),
            int(d[2])
        )
    
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
