from analytics.models import User
from analytics.plotter import HistogramPlotter
from django.shortcuts import render

def plot_view(request):
    plotter = HistogramPlotter(User, 'service')  # 'service' is the field to plot
    graph = plotter.create_plot('Service Distribution')
    context = {'graph': graph}
    return render(request, 'plot.html', context)
