from collections import OrderedDict

html_graph_header = '''<!DOCTYPE HTML>
<html>
<head>
<script>
window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
	exportEnabled: true,
	animationEnabled: true,
	title:{
		text: "Leela Chess Zero Self-Play BayesElo"
	},		
	axisY: {
	    includeZero: false,
		title: "Bayes Elo"
	},
	data: [{
		type: "rangeSplineArea",
		indexLabel: "{y[#index]}",
		toolTipContent: "id {x} </br> <strong>Error Margin: </strong> </br> [{y[0]}, {y[1]}]",'''
html_graph_footer = '''
	}]
});
chart.render();

}
</script>
</head>
<body>
<div id="chartContainer" style="height: 370px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>'''

with open('ratings.txt') as ratings_file:
    content = ratings_file.readlines()
    content = content[1:]  # skip header

content = [x.strip() for x in content]
content = [x.split() for x in content]

players = {}
for line in content:
    players[int(line[1])] = [int(line[2]), int(line[3]), int(line[4])]

ordered_players = OrderedDict(sorted(players.items()))

net_ids = [player for player in ordered_players]
error_ranges = [[ordered_players[player][0] + ordered_players[player][1],
                 ordered_players[player][0] - ordered_players[player][2]]
                for player in ordered_players]

html_graph_body = 'dataPoints:[\n'
for index, net_id in enumerate(net_ids):
    html_graph_body += '{{ x: {}, y: [{}, {}] }},\n'.format(net_id, error_ranges[index][0], error_ranges[index][1])
html_graph_body += ''']
},{
        type : "spline",
		toolTipContent: "id {x} : {y} Elo",
		dataPoints:['''

for index, net_id in enumerate(net_ids):
    html_graph_body += '{{ x: {}, y: {}}},'.format(net_id, ordered_players[net_id][0])
html_graph_body += ''']
                    '''

with open('graph.html', 'w') as graph_file:
    graph_file.write(html_graph_header)
    graph_file.write(html_graph_body)
    graph_file.write(html_graph_footer)
