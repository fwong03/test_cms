from pyramid.renderers import get_renderer
from pyramid.view import view_config
from ..resources import Document

#
#   Default "retail" view
#
@view_config(
    renderer='templates/splash.pt',
    )
def splash_view(request):
    manage_prefix = request.registry.settings.get('substanced.manage_prefix',
                                                  '/manage')
    return {'manage_prefix': manage_prefix}

#
#   "Retail" view for documents.
#
@view_config(
    context=Document,
    renderer='templates/document.pt',
    )
def document_view(context, request):
    return {'title': context.title,
            'body': context.body,
            'master': get_renderer('templates/master.pt').implementation(),
           }

@view_config(name='show_types', renderer='templates/show_types.pt')
def show_types(request):
    all_types = request.registry.content.all()
    return {'all_types': all_types}

