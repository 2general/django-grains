from django.template import Library, Node, TemplateSyntaxError, Variable
from ..models import Grain

register = Library()


class GrainNode(Node):
    def __init__(self, nodelist, key, content_type):
        self.nodelist = nodelist
        self.key = Variable(key)
        self.content_type = Variable(content_type)

    def render(self, context):
        key = self.key.resolve(context)
        content_type = self.content_type.resolve(context)
        default_content = self.nodelist.render(context)
        grain_instance, created = Grain.objects.get_or_create(
            key=key, defaults={'content_type': content_type,
                               'value': default_content})
        if not created and grain_instance.content_type != content_type:
            grain_instance.content_type = content_type
            grain_instance.save()
        return grain_instance.value


@register.tag
def grain(parser, token):
    # pylint: disable=W0613
    #         Unused argument

    bits = token.split_contents()
    if len(bits) not in (2, 3):
        raise TemplateSyntaxError(
            "%r tag requires one or two arguments" % bits[0])
    nodelist = parser.parse(('endgrain',))
    parser.delete_first_token()
    key = bits[1]
    content_type = bits[2] if len(bits) >= 3 else '"text/plain"'
    return GrainNode(nodelist, key, content_type)
