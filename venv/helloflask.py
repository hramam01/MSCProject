from flask import Flask, render_template
from graphviz import Digraph

from bokeh.client import pull_session
from bokeh.embed import server_session

import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/table")
def table():
    return render_template("Table.html")


@app.route("/svgtest")
def svgtest():
  process = pd.read_excel('/Users/hari/Desktop/Process.xlsx')
  steps = process['Process Step From']
  owner = process['Owner'].unique()

  dot1 = Digraph()
  dot1.graph_attr["splines"] = "line"
  dot1.graph_attr["newrank"] = "true"
  dot1.graph_attr['outputorder'] ='edgesfirst'
  dot1.graph_attr['rankdir'] = 'LR'
  dot1.graph_attr['shape'] = 'plaintext'
  dot1.graph_attr['size'] = "12.75,7.25"
  dot1.graph_attr['fontsize'] = "12"

  for i in enumerate(owner):
      processi = process[process['Owner'] == owner[i[0]]]
      owners = owner[i[0]]
      cname = 'cluster' + str(i[0])

      with dot1.subgraph(name=cname) as c:
          c.attr(style='filled', color='lightgrey',fontsize='20',label=str(owners))
          for index, row in processi.iterrows():
              c.node(row['Process Step From'], shape='box',width='3', height='.5',fixedsize='true',style='filled', color='white',fontsize='20')
              c.node_attr['href'] = '#'
  for i, val in enumerate(steps):
      if i == 0:
          prev = val
      else:
          dot1.edge(str(prev), str(val))
          dot1.edge_attr['arrowhead'] = 'normal'

          prev = val
  chart_output1 = dot1.pipe(format='svg').decode("utf-8")

  return render_template('svgtest.html', chart_output1=chart_output1)

@app.route("/VSM")
def vsm():
    pass



if __name__ == "__main__":
    app.run(debug=True)
