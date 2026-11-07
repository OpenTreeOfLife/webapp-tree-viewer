from pyramid.view import notfound_view_config

from synthetic_tree_viewer.util import get_copy_of_view_dict


@notfound_view_config(renderer="synthetic_tree_viewer:templates/404.jinja2")
def notfound_view(request):
    request.response.status = 404
    view_dict = get_copy_of_view_dict(request)
    return {"body": "404 - Not Found"}
