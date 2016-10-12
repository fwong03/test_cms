import colander
import deform.widget
import datetime

from persistent import Persistent

from substanced.content import content
from substanced.property import PropertySheet
from substanced.schema import (
    Schema,
    NameSchemaNode
    )
from substanced.util import renamer


def context_is_a_document(context, request):
    return request.registry.content.istype(context, 'Document')


class DocumentSchema(Schema):
    name = NameSchemaNode(
        editing=context_is_a_document,
        )
    title = colander.SchemaNode(
        colander.String(),
        )
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.RichTextWidget()
        )

class DocumentPropertySheet(PropertySheet):
    schema = DocumentSchema()

@content('Document', icon='glyphicon glyphicon-align-left', add_view='add_document',)
class Document(Persistent):

    name = renamer()

    def __init__(self, title='', body=''):
        self.title = title
        self.body = body


def context_is_a_blogentry(context, request):
    return request.registry.content.istype(context, 'BlogEntry')


class BlogEntrySchema(Schema):
    today = datetime.date.today()
    name = NameSchemaNode(
        editing=context_is_a_blogentry,
        )
    title = colander.SchemaNode(
        colander.String(),
        )
    # http://docs.pylonsproject.org/projects/deform/en/latest/api.html?highlight=date
    # class deform.widget.DateInputWidget(*args, **kwargs)
    # Renders a date picker widget...
    # Most useful when the schema node is a colander.Date object.
    date = colander.SchemaNode(
        colander.Date(),
        validator=colander.Range(today, None)
    )
    kind = colander.SchemaNode(colander.String(),
                               validator=colander.OneOf(['a', 'b']),
                               widget=deform.widget.SelectWidget(
                                   values=[('a', 'a'), ('b', 'b')]),
                               )
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.RichTextWidget()
        )

class BlogEntryPropertySheet(PropertySheet):
    schema = BlogEntrySchema()

@content('BlogEntry', name='Make a blog entry, peon', icon='glyphicon glyphicon-align-left', add_view='add_blog_entry')
class BlogEntry(Persistent):

    name = renamer()

    def __init__(self, title='', body='', date=''):
        self.title = title
        self.body = body
        self.date = date


def includeme(config): # pragma: no cover
    config.add_propertysheet('Basic', DocumentPropertySheet, Document)
    config.add_propertysheet('Basic', BlogEntryPropertySheet, BlogEntry)

