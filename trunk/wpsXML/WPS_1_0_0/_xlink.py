# ./_xlink.py
# PyXB bindings for NamespaceModule
# NSM:b43cd366527ddb6a0e58594876e07421e0148f30
# Generated 2010-10-21 16:22:53.558918 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:aaeb86ce-dd1e-11df-bb63-485b39ca0591')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a Python instance."""
    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=Namespace.fallbackNamespace(), location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)


# Atomic SimpleTypeDefinition
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.onLoad = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'onLoad')
STD_ANON.onRequest = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'onRequest')
STD_ANON.other = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'other')
STD_ANON.none = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'none')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic SimpleTypeDefinition
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.new = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'new')
STD_ANON_.replace = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'replace')
STD_ANON_.embed = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'embed')
STD_ANON_.other = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'other')
STD_ANON_.none = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'none')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
