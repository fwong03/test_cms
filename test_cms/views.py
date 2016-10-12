from pyramid.httpexceptions import HTTPFound

from pyramid.view import(
    view_config,
    view_defaults,
    )

from substanced.sdi import mgmt_view
from substanced.form import FormView
from substanced.interfaces import IFolder
from substanced.sdi import LEFT, RIGHT

from .resources import (
    DocumentSchema,
    BlogEntrySchema
)

#
#   SDI "add" view for documents
#
@mgmt_view(context=IFolder, name='add_document', tab_title='Add Document',
    permission='sdi.add-content', renderer='substanced.sdi:templates/form.pt',
    tab_condition=True, tab_near=RIGHT)
class AddDocumentView(FormView):
    title = 'Add Document'
    schema = DocumentSchema()
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        # import pdb; pdb.set_trace()
        name = appstruct.pop('name')
        document = registry.content.create('Document', **appstruct)
        self.context[name] = document
        return HTTPFound(
            self.request.sdiapi.mgmt_path(self.context, '@@contents')
            )

@mgmt_view(context=IFolder, name='add_blog_entry', tab_title='Add Blog Entry',
           permission='sdi.add-content', renderer='substanced.sdi:templates/form.pt',
           tab_condition=True, tab_near=RIGHT)
class AddBlogView(FormView):
    title = 'Add Blog Entry'
    schema = BlogEntrySchema()
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        # import pdb; pdb.set_trace()
        name = appstruct.pop('name')
        blog_entry = registry.content.create('BlogEntry', **appstruct)
        self.context[name] = blog_entry
        return HTTPFound(self.request.mgmt_path(self.context, '@@contents'))

