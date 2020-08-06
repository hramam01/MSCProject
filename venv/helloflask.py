from flask import Flask, render_template
from graphviz import Digraph
import matplotlib
import graphviz

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


import io
import base64

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

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


@app.route("/svgtest",methods=['GET'])
def svgtest():
  process = pd.read_excel('/Users/hari/Desktop/Process.xlsx')
  steps = process['Process Step From']
  owner = process['Owner'].unique()
  process['Takttime'] = process['Effort'].sum() / len(process)
  process['colors'] = np.where(process['Takttime'] >= process['Effort'], 'green', 'orange')

  dot1 = Digraph()
  dot1.graph_attr["splines"] = "line"
  dot1.graph_attr["newrank"] = "true"
  dot1.graph_attr['outputorder'] ='edgesfirst'
  dot1.graph_attr['rankdir'] = 'LR'
  dot1.graph_attr['shape'] = 'record'
  dot1.graph_attr['size'] = "12.75,7.25"
  dot1.graph_attr['fontsize'] = "12"

  for i in enumerate(owner):
      processi = process[process['Owner'] == owner[i[0]]]
      owners = owner[i[0]]
      cname = 'cluster' + str(i[0])

      with dot1.subgraph(name=cname) as c:
          c.attr(style='filled', color='lightgrey',fontsize='20',label=str(owners))
          for index, row in processi.iterrows():
              c.node(row['Process Step From'])
              c.node_attr['shape']='box'
              c.node_attr['width']='3'
              c.node_attr['height'] = '.5'
              c.node_attr['fixedsize'] = 'true'
              c.node_attr['style'] = 'filled'
              c.node_attr['fontsize'] = '20'
              c.node_attr['color'] = 'lightgrey'
              c.node_attr['color'] = row['colors']
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

@app.route("/VSM",methods=['GET'])
def vsm():
    process = pd.read_excel('/Users/hari/Desktop/Process.xlsx')
    process['Takttime'] = process['Effort'].sum() / len(process)
    process['colors'] = np.where(process['Takttime'] >= process['Effort'], 'green', 'orange')

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    for i, val in process.iterrows():
        axis.bar(val['Owner'], val['Effort'], color=val['colors'])

    axis.axhline(y=36.5, color='green', linestyle='-')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template("vsm.html", image=pngImageB64String)

if __name__ == "__main__":
    app.run(debug=True)
