from abc import ABC, abstractmethod

class ZPageHandler(ABC):

# Returns the URL path that should be used to register this page.
# @return the URL path that should be used to register this page.
    @abstractmethod
    def get_url_path(self):
        pass


# Emits the HTML generated page to the {@code outputStream}.
# @param queryMap the query components map.
# @param outputStream the output {@code OutputStream}.
    @abstractmethod
    def emit_html(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ZPageHandler:
            if any("get_url_path" in B.__dict__ for B in C.__mro__):
                if any("emit_html" in B.__dict__ for B in C.__mro__):
                    return True
        return NotImplemented
