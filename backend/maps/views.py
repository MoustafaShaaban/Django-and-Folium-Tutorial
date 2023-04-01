# maps/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.contrib import messages

from .models import Feature
from .utils import basemap


def index(request):
    map = basemap(request)
    return render(request, 'map.html', map)


class CreateFeature(generic.CreateView):
    model = Feature
    fields = ['name', 'type', 'description', 'latitude', 'longitude']
    template_name = 'create_feature.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        map = folium.Map(
        tiles='cartodbdark_matter',
        attr= 'Django and Folium'
    )

        folium.TileLayer('cartodbpositron').add_to(map)

        folium.LayerControl(position='bottomright').add_to(map)
        Fullscreen().add_to(map)
        LocateControl().add_to(map)
        Geocoder().add_to(map)
        folium.LatLngPopup().add_to(map)

        map = map._repr_html_()
        context = super().get_context_data(**kwargs)
        context['map'] = map
        return context
