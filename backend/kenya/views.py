from django.http import JsonResponse, Http404, HttpResponse
from django.conf import settings
import os
import json

def kenya_dashboard(request):
    return HttpResponse("Kenya Dashboard")


def get_view_json_data(request, filename):
    # Retrieve view and featureName from query parameters

    view = request.GET.get('view')
    feature_name = request.GET.get('featureName')
    print("view",view)
    print("feature_name",feature_name)

    if view in ["COUNTRY", "COUNTY"]:
        file_path = os.path.join(settings.BASE_DIR, 'kenya/static/data/COUNTY', f'{filename}.json')
    elif view in ["BASIN", "WATERSHED"]:
        file_path = os.path.join(settings.BASE_DIR, 'kenya/static/data/WATERSHED', f'{filename}.json')
    else:
        # Handle unexpected view values
        raise Http404("Invalid view parameter provided.")

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file and load the data
        with open(file_path, 'r') as file:
            data = json.load(file)

        # If a featureName is specified and not 'All', filter the data
        if feature_name and feature_name != 'All':
            filtered_data = [item for item in data if item.get(view) == feature_name]
            data = filtered_data

        return JsonResponse(data, safe=False)
    else:
        # If the file is not found, return a 404 error
        raise Http404("JSON file not found.")

def get_json_data(request, filename):
    file_path = os.path.join(settings.BASE_DIR, 'kenya/static/data', f'{filename}.json')
    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file and load the data
        with open(file_path, 'r') as file:
            data = json.load(file)

        return JsonResponse(data, safe=False)
    else:
        # If the file is not found, return a 404 error
        raise Http404("JSON file not found.")
