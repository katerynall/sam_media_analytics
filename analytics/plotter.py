import pandas as pd
import plotly.express as px
from analytics.models import User

class HistogramPlotter:
    def __init__(self, model, field):
        """
        Initialize the HistogramPlotter.
        :param model: Django model from which to retrieve data
        :param field: The field of the model to plot
        """
        self.model = model
        self.field = field
        self.dataframe = self.get_data()

    def get_data(self):
        """Retrieve data from the model and return it as a DataFrame"""
        query_set = self.model.objects.all().values(self.field)
        return pd.DataFrame(query_set)

    def create_plot(self, title):
        """Create a Plotly histogram plot from the DataFrame."""
        fig = px.histogram(self.dataframe, x=self.field)
        fig.update_layout(title=title)
        return fig.to_html(full_html=False)
