from docutils.core import Publisher


class MarkdownPublisher(Publisher):
    def __init__(self, *args, **kwargs):
        Publisher.__init__(self, *args, **kwargs)

        # replace parser FORCELY
        from remarkdown.parser import MarkdownParser
        self.reader.parser = MarkdownParser()

    def publish(self):
        Publisher.publish(self)

        # set names and ids attribute to section node
        from docutils import nodes
        for section in self.document.traverse(nodes.section):
            titlenode = section[0]
            name = nodes.fully_normalize_name(titlenode.astext())
            section['names'].append(name)
            self.document.note_implicit_target(section, section)


def setup(_):
    # replace Publisher
    import sphinx.environment
    sphinx.environment.Publisher = MarkdownPublisher
