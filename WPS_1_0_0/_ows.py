# ./WPS_1_0_0/_ows.py
# PyXB bindings for NamespaceModule
# NSM:30267ec97faf153699f3ab2e8f18d125f769245d
# Generated 2010-04-24 12:16:11.758399 by PyXB version 1.1.1
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6153a7ca-4f8a-11df-beaf-001fd0b3e7f9')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.binding.xml_
import WPS_1_0_0._xlink

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1', create_if_missing=True)
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
class VersionType (pyxb.binding.datatypes.string):

    """Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VersionType')
    _Documentation = u'Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. '
VersionType._CF_pattern = pyxb.binding.facets.CF_pattern()
VersionType._CF_pattern.addPattern(pattern=u'\\d+\\.\\d?\\d\\.\\d?\\d')
VersionType._InitializeFacetMap(VersionType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'VersionType', VersionType)

# Atomic SimpleTypeDefinition
class STD_ANON_1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_1._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_1._CF_pattern.addPattern(pattern=u'\\d+\\.\\d?\\d\\.\\d?\\d')
STD_ANON_1._InitializeFacetMap(STD_ANON_1._CF_pattern)

# Atomic SimpleTypeDefinition
class MimeType (pyxb.binding.datatypes.string):

    """XML encoded identifier of a standard MIME type, possibly a parameterized MIME type. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MimeType')
    _Documentation = u'XML encoded identifier of a standard MIME type, possibly a parameterized MIME type. '
MimeType._CF_pattern = pyxb.binding.facets.CF_pattern()
MimeType._CF_pattern.addPattern(pattern=u'(application|audio|image|text|video|message|multipart|model)/.+(;\\s*.+=.+)*')
MimeType._InitializeFacetMap(MimeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'MimeType', MimeType)

# Atomic SimpleTypeDefinition
class UpdateSequenceType (pyxb.binding.datatypes.string):

    """Service metadata document version, having values that are "increased" whenever any change is made in service metadata document. Values are selected by each server, and are always opaque to clients. See updateSequence parameter use subclause for more information. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UpdateSequenceType')
    _Documentation = u'Service metadata document version, having values that are "increased" whenever any change is made in service metadata document. Values are selected by each server, and are always opaque to clients. See updateSequence parameter use subclause for more information. '
UpdateSequenceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'UpdateSequenceType', UpdateSequenceType)

# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.NMTOKENS, pyxb.binding.basis.enumeration_mixin
class STD_ANON_2 (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = None
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'closed')
STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'open')
STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'open-closed')
STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'closed-open')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic SimpleTypeDefinition
class ServiceType (pyxb.binding.datatypes.string):

    """Service type identifier, where the string value is the OWS type abbreviation, such as "WMS" or "WFS". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ServiceType')
    _Documentation = u'Service type identifier, where the string value is the OWS type abbreviation, such as "WMS" or "WFS". '
ServiceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ServiceType', ServiceType)

# List SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class PositionType (pyxb.binding.basis.STD_list):

    """Position instances hold the coordinates of a position in a coordinate reference system (CRS) referenced by the related "crs" attribute or elsewhere. For an angular coordinate axis that is physically continuous for multiple revolutions, but whose recorded values can be discontinuous, special conditions apply when the bounding box is continuous across the value discontinuity:
a)  If the bounding box is continuous clear around this angular axis, then ordinate values of minus and plus infinity shall be used.
b)  If the bounding box is continuous across the value discontinuity but is not continuous clear around this angular axis, then some non-normal value can be used if specified for a specific OWS use of the BoundingBoxType. For more information, see Subclauses 10.2.5 and C.13. This type is adapted from DirectPositionType and doubleList of GML 3.1. The adaptations include omission of all the attributes, since the needed information is included in the BoundingBoxType. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PositionType')
    _Documentation = u'Position instances hold the coordinates of a position in a coordinate reference system (CRS) referenced by the related "crs" attribute or elsewhere. For an angular coordinate axis that is physically continuous for multiple revolutions, but whose recorded values can be discontinuous, special conditions apply when the bounding box is continuous across the value discontinuity:\na)  If the bounding box is continuous clear around this angular axis, then ordinate values of minus and plus infinity shall be used.\nb)  If the bounding box is continuous across the value discontinuity but is not continuous clear around this angular axis, then some non-normal value can be used if specified for a specific OWS use of the BoundingBoxType. For more information, see Subclauses 10.2.5 and C.13. This type is adapted from DirectPositionType and doubleList of GML 3.1. The adaptations include omission of all the attributes, since the needed information is included in the BoundingBoxType. '

    _ItemType = pyxb.binding.datatypes.double
PositionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'PositionType', PositionType)

# List SimpleTypeDefinition
# superclasses PositionType
class PositionType2D (pyxb.binding.basis.STD_list):

    """Two-dimensional position instances hold the longitude and latitude coordinates of a position in the 2D WGS 84 coordinate reference system. The longitude value shall be listed first, followed by the latitude value, both in decimal degrees. Latitude values shall range from -90 to +90 degrees, and longitude values shall normally range from -180 to +180 degrees. For the longitude axis, special conditions apply when the bounding box is continuous across the +/- 180 degrees meridian longitude value discontinuity:
a)  If the bounding box is continuous clear around the Earth, then longitude values of minus and plus infinity shall be used.
b)  If the bounding box is continuous across the value discontinuity but is not continuous clear around the Earth, then some non-normal value can be used if specified for a specific OWS use of the WGS84BoundingBoxType. For more information, see Subclauses 10.4.5 and C.13. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PositionType2D')
    _Documentation = u'Two-dimensional position instances hold the longitude and latitude coordinates of a position in the 2D WGS 84 coordinate reference system. The longitude value shall be listed first, followed by the latitude value, both in decimal degrees. Latitude values shall range from -90 to +90 degrees, and longitude values shall normally range from -180 to +180 degrees. For the longitude axis, special conditions apply when the bounding box is continuous across the +/- 180 degrees meridian longitude value discontinuity:\na)  If the bounding box is continuous clear around the Earth, then longitude values of minus and plus infinity shall be used.\nb)  If the bounding box is continuous across the value discontinuity but is not continuous clear around the Earth, then some non-normal value can be used if specified for a specific OWS use of the WGS84BoundingBoxType. For more information, see Subclauses 10.4.5 and C.13. '

    _ItemType = pyxb.binding.datatypes.double
PositionType2D._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
PositionType2D._InitializeFacetMap(PositionType2D._CF_length)
Namespace.addCategoryObject('typeBinding', u'PositionType2D', PositionType2D)

# Complex type DescriptionType with content type ELEMENT_ONLY
class DescriptionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DescriptionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Keywords uses Python identifier Keywords
    __Keywords = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Keywords'), 'Keywords', '__httpwww_opengis_netows1_1_DescriptionType_httpwww_opengis_netows1_1Keywords', True)

    
    Keywords = property(__Keywords.value, __Keywords.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Title'), 'Title', '__httpwww_opengis_netows1_1_DescriptionType_httpwww_opengis_netows1_1Title', True)

    
    Title = property(__Title.value, __Title.set, None, u'Title of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), 'Abstract', '__httpwww_opengis_netows1_1_DescriptionType_httpwww_opengis_netows1_1Abstract', True)

    
    Abstract = property(__Abstract.value, __Abstract.set, None, u'Brief narrative description of this resource, normally used for display to a human. ')


    _ElementMap = {
        __Keywords.name() : __Keywords,
        __Title.name() : __Title,
        __Abstract.name() : __Abstract
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DescriptionType', DescriptionType)


# Complex type DatasetDescriptionSummaryBaseType with content type ELEMENT_ONLY
class DatasetDescriptionSummaryBaseType (DescriptionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatasetDescriptionSummaryBaseType')
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}WGS84BoundingBox uses Python identifier WGS84BoundingBox
    __WGS84BoundingBox = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WGS84BoundingBox'), 'WGS84BoundingBox', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1WGS84BoundingBox', True)

    
    WGS84BoundingBox = property(__WGS84BoundingBox.value, __WGS84BoundingBox.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1Metadata', True)

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1BoundingBox', True)

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'Unambiguous identifier or name of this coverage, unique for this server. ')

    
    # Element {http://www.opengis.net/ows/1.1}DatasetDescriptionSummary uses Python identifier DatasetDescriptionSummary
    __DatasetDescriptionSummary = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatasetDescriptionSummary'), 'DatasetDescriptionSummary', '__httpwww_opengis_netows1_1_DatasetDescriptionSummaryBaseType_httpwww_opengis_netows1_1DatasetDescriptionSummary', True)

    
    DatasetDescriptionSummary = property(__DatasetDescriptionSummary.value, __DatasetDescriptionSummary.set, None, None)


    _ElementMap = DescriptionType._ElementMap.copy()
    _ElementMap.update({
        __WGS84BoundingBox.name() : __WGS84BoundingBox,
        __Metadata.name() : __Metadata,
        __BoundingBox.name() : __BoundingBox,
        __Identifier.name() : __Identifier,
        __DatasetDescriptionSummary.name() : __DatasetDescriptionSummary
    })
    _AttributeMap = DescriptionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DatasetDescriptionSummaryBaseType', DatasetDescriptionSummaryBaseType)


# Complex type ValueType with content type SIMPLE
class ValueType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueType')
    # Base type is pyxb.binding.datatypes.string

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ValueType', ValueType)


# Complex type BoundingBoxType with content type ELEMENT_ONLY
class BoundingBoxType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BoundingBoxType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}LowerCorner uses Python identifier LowerCorner
    __LowerCorner = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LowerCorner'), 'LowerCorner', '__httpwww_opengis_netows1_1_BoundingBoxType_httpwww_opengis_netows1_1LowerCorner', False)

    
    LowerCorner = property(__LowerCorner.value, __LowerCorner.set, None, u'Position of the bounding box corner at which the value of each coordinate normally is the algebraic minimum within this bounding box. In some cases, this position is normally displayed at the top, such as the top left for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ')

    
    # Element {http://www.opengis.net/ows/1.1}UpperCorner uses Python identifier UpperCorner
    __UpperCorner = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'UpperCorner'), 'UpperCorner', '__httpwww_opengis_netows1_1_BoundingBoxType_httpwww_opengis_netows1_1UpperCorner', False)

    
    UpperCorner = property(__UpperCorner.value, __UpperCorner.set, None, u'Position of the bounding box corner at which the value of each coordinate normally is the algebraic maximum within this bounding box. In some cases, this position is normally displayed at the bottom, such as the bottom right for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. ')

    
    # Attribute dimensions uses Python identifier dimensions
    __dimensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dimensions'), 'dimensions', '__httpwww_opengis_netows1_1_BoundingBoxType_dimensions', pyxb.binding.datatypes.positiveInteger)
    
    dimensions = property(__dimensions.value, __dimensions.set, None, u'The number of dimensions in this CRS (the length of a coordinate sequence in this use of the PositionType). This number is specified by the CRS definition, but can also be specified here. ')

    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'crs'), 'crs', '__httpwww_opengis_netows1_1_BoundingBoxType_crs', pyxb.binding.datatypes.anyURI)
    
    crs = property(__crs.value, __crs.set, None, u'Usually references the definition of a CRS, as specified in [OGC Topic 2]. Such a CRS definition can be XML encoded using the gml:CoordinateReferenceSystemType in [GML 3.1]. For well known references, it is not required that a CRS definition exist at the location the URI points to. If no anyURI value is included, the applicable CRS must be either:\na)\tSpecified outside the bounding box, but inside a data structure that includes this bounding box, as specified for a specific OWS use of this bounding box type.\nb)\tFixed and specified in the Implementation Specification for a specific OWS use of the bounding box type. ')


    _ElementMap = {
        __LowerCorner.name() : __LowerCorner,
        __UpperCorner.name() : __UpperCorner
    }
    _AttributeMap = {
        __dimensions.name() : __dimensions,
        __crs.name() : __crs
    }
Namespace.addCategoryObject('typeBinding', u'BoundingBoxType', BoundingBoxType)


# Complex type CTD_ANON_1 with content type ELEMENT_ONLY
class CTD_ANON_1 (DescriptionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Fees uses Python identifier Fees
    __Fees = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Fees'), 'Fees', '__httpwww_opengis_netows1_1_CTD_ANON_1_httpwww_opengis_netows1_1Fees', False)

    
    Fees = property(__Fees.value, __Fees.set, None, u'Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceTypeVersion uses Python identifier ServiceTypeVersion
    __ServiceTypeVersion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ServiceTypeVersion'), 'ServiceTypeVersion', '__httpwww_opengis_netows1_1_CTD_ANON_1_httpwww_opengis_netows1_1ServiceTypeVersion', True)

    
    ServiceTypeVersion = property(__ServiceTypeVersion.value, __ServiceTypeVersion.set, None, u'Unordered list of one or more versions of this service type implemented by this server. This information is not adequate for version negotiation, and shall not be used for that purpose. ')

    
    # Element {http://www.opengis.net/ows/1.1}AccessConstraints uses Python identifier AccessConstraints
    __AccessConstraints = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'), 'AccessConstraints', '__httpwww_opengis_netows1_1_CTD_ANON_1_httpwww_opengis_netows1_1AccessConstraints', True)

    
    AccessConstraints = property(__AccessConstraints.value, __AccessConstraints.set, None, u'Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. ')

    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Profile uses Python identifier Profile
    __Profile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Profile'), 'Profile', '__httpwww_opengis_netows1_1_CTD_ANON_1_httpwww_opengis_netows1_1Profile', True)

    
    Profile = property(__Profile.value, __Profile.set, None, u'Unordered list of identifiers of Application Profiles that are implemented by this server. This element should be included for each specified application profile implemented by this server. The identifier value should be specified by each Application Profile. If this element is omitted, no meaning is implied. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceType uses Python identifier ServiceType
    __ServiceType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ServiceType'), 'ServiceType', '__httpwww_opengis_netows1_1_CTD_ANON_1_httpwww_opengis_netows1_1ServiceType', False)

    
    ServiceType = property(__ServiceType.value, __ServiceType.set, None, u'A service type name from a registry of services. For example, the values of the codeSpace URI and name and code string may be "OGC" and "catalogue." This type name is normally used for machine-to-machine communication. ')


    _ElementMap = DescriptionType._ElementMap.copy()
    _ElementMap.update({
        __Fees.name() : __Fees,
        __ServiceTypeVersion.name() : __ServiceTypeVersion,
        __AccessConstraints.name() : __AccessConstraints,
        __Profile.name() : __Profile,
        __ServiceType.name() : __ServiceType
    })
    _AttributeMap = DescriptionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type CTD_ANON_2 with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }



# Complex type DomainMetadataType with content type SIMPLE
class DomainMetadataType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DomainMetadataType')
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.opengis.net/ows/1.1}reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'reference'), 'reference', '__httpwww_opengis_netows1_1_DomainMetadataType_httpwww_opengis_netows1_1reference', pyxb.binding.datatypes.anyURI)
    
    reference = property(__reference.value, __reference.set, None, u'Reference to data or metadata recorded elsewhere, either external to this XML document or within it. Whenever practical, this attribute should be a URL from which this metadata can be electronically retrieved. Alternately, this attribute can reference a URN for well-known metadata. For example, such a URN could be a URN defined in the "ogc" URN namespace. ')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __reference.name() : __reference
    }
Namespace.addCategoryObject('typeBinding', u'DomainMetadataType', DomainMetadataType)


# Complex type CTD_ANON_3 with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}DCP uses Python identifier DCP
    __DCP = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DCP'), 'DCP', '__httpwww_opengis_netows1_1_CTD_ANON_3_httpwww_opengis_netows1_1DCP', True)

    
    DCP = property(__DCP.value, __DCP.set, None, u'Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n')

    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_CTD_ANON_3_httpwww_opengis_netows1_1Metadata', True)

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Constraint'), 'Constraint', '__httpwww_opengis_netows1_1_CTD_ANON_3_httpwww_opengis_netows1_1Constraint', True)

    
    Constraint = property(__Constraint.value, __Constraint.set, None, u'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows/1.1}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Parameter'), 'Parameter', '__httpwww_opengis_netows1_1_CTD_ANON_3_httpwww_opengis_netows1_1Parameter', True)

    
    Parameter = property(__Parameter.value, __Parameter.set, None, u'Optional unordered list of parameter domains that each apply to this operation which this server implements. If one of these Parameter elements has the same "name" attribute as a Parameter element in the OperationsMetadata element, this Parameter element shall override the other one for this operation. The list of required and optional parameter domain limitations for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_opengis_netows1_1_CTD_ANON_3_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Name or identifier of this operation (request) (for example, GetCapabilities). The list of required and optional operations implemented shall be specified in the Implementation Specification for this service. ')


    _ElementMap = {
        __DCP.name() : __DCP,
        __Metadata.name() : __Metadata,
        __Constraint.name() : __Constraint,
        __Parameter.name() : __Parameter
    }
    _AttributeMap = {
        __name.name() : __name
    }



# Complex type CTD_ANON_4 with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Exception uses Python identifier Exception
    __Exception = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Exception'), 'Exception', '__httpwww_opengis_netows1_1_CTD_ANON_4_httpwww_opengis_netows1_1Exception', True)

    
    Exception = property(__Exception.value, __Exception.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netows1_1_CTD_ANON_4_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_opengis_netows1_1_CTD_ANON_4_version', STD_ANON_1, required=True)
    
    version = property(__version.value, __version.set, None, u'Specification version for OWS operation. The string value shall contain one x.y.z "version" value (e.g., "2.1.3"). A version number shall contain three non-negative integers separated by decimal points, in the form "x.y.z". The integers y and z shall not exceed 99. Each version shall be for the Implementation Specification (document) and the associated XML Schemas to which requested operations will conform. An Implementation Specification version normally specifies XML Schemas against which an XML encoded operation response must conform and should be validated. See Version negotiation subclause for more information. ')


    _ElementMap = {
        __Exception.name() : __Exception
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __version.name() : __version
    }



# Complex type KeywordsType with content type ELEMENT_ONLY
class KeywordsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'KeywordsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Keyword uses Python identifier Keyword
    __Keyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Keyword'), 'Keyword', '__httpwww_opengis_netows1_1_KeywordsType_httpwww_opengis_netows1_1Keyword', True)

    
    Keyword = property(__Keyword.value, __Keyword.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Type'), 'Type', '__httpwww_opengis_netows1_1_KeywordsType_httpwww_opengis_netows1_1Type', False)

    
    Type = property(__Type.value, __Type.set, None, None)


    _ElementMap = {
        __Keyword.name() : __Keyword,
        __Type.name() : __Type
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'KeywordsType', KeywordsType)


# Complex type MetadataType with content type ELEMENT_ONLY
class MetadataType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MetadataType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}AbstractMetaData uses Python identifier AbstractMetaData
    __AbstractMetaData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AbstractMetaData'), 'AbstractMetaData', '__httpwww_opengis_netows1_1_MetadataType_httpwww_opengis_netows1_1AbstractMetaData', False)

    
    AbstractMetaData = property(__AbstractMetaData.value, __AbstractMetaData.set, None, u'Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. ')

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'arcrole'), 'arcrole', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'href'), 'href', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'role'), 'role', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'show'), 'show', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkshow', WPS_1_0_0._xlink.STD_ANON_1)
    
    show = property(__show.value, __show.set, None, u"\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'about'), 'about', '__httpwww_opengis_netows1_1_MetadataType_about', pyxb.binding.datatypes.anyURI)
    
    about = property(__about.value, __about.set, None, u'Optional reference to the aspect of the element which includes this "metadata" element that this metadata provides more information about. ')

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'title'), 'title', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'actuate'), 'actuate', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinkactuate', WPS_1_0_0._xlink.STD_ANON_2)
    
    actuate = property(__actuate.value, __actuate.set, None, u"\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'type'), 'type', '__httpwww_opengis_netows1_1_MetadataType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default=u'simple')
    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        __AbstractMetaData.name() : __AbstractMetaData
    }
    _AttributeMap = {
        __arcrole.name() : __arcrole,
        __href.name() : __href,
        __role.name() : __role,
        __show.name() : __show,
        __about.name() : __about,
        __title.name() : __title,
        __actuate.name() : __actuate,
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'MetadataType', MetadataType)


# Complex type WGS84BoundingBoxType with content type ELEMENT_ONLY
class WGS84BoundingBoxType (BoundingBoxType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WGS84BoundingBoxType')
    # Base type is BoundingBoxType
    
    # Element LowerCorner ({http://www.opengis.net/ows/1.1}LowerCorner) inherited from {http://www.opengis.net/ows/1.1}BoundingBoxType
    
    # Element UpperCorner ({http://www.opengis.net/ows/1.1}UpperCorner) inherited from {http://www.opengis.net/ows/1.1}BoundingBoxType
    
    # Attribute dimensions is restricted from parent
    
    # Attribute dimensions uses Python identifier dimensions
    __dimensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dimensions'), 'dimensions', '__httpwww_opengis_netows1_1_BoundingBoxType_dimensions', pyxb.binding.datatypes.positiveInteger, fixed=True, unicode_default=u'2')
    
    dimensions = property(__dimensions.value, __dimensions.set, None, u'The number of dimensions in this CRS (the length of a coordinate sequence in this use of the PositionType). This number is specified by the CRS definition, but can also be specified here. ')

    
    # Attribute crs is restricted from parent
    
    # Attribute crs uses Python identifier crs
    __crs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'crs'), 'crs', '__httpwww_opengis_netows1_1_BoundingBoxType_crs', pyxb.binding.datatypes.anyURI, fixed=True, unicode_default=u'urn:ogc:def:crs:OGC:2:84')
    
    crs = property(__crs.value, __crs.set, None, u'This attribute can be included when considered useful. When included, this attribute shall reference the 2D WGS 84 coordinate reference system with longitude before latitude and decimal values of longitude and latitude. ')


    _ElementMap = BoundingBoxType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = BoundingBoxType._AttributeMap.copy()
    _AttributeMap.update({
        __dimensions.name() : __dimensions,
        __crs.name() : __crs
    })
Namespace.addCategoryObject('typeBinding', u'WGS84BoundingBoxType', WGS84BoundingBoxType)


# Complex type GetCapabilitiesType with content type ELEMENT_ONLY
class GetCapabilitiesType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GetCapabilitiesType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}AcceptFormats uses Python identifier AcceptFormats
    __AcceptFormats = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AcceptFormats'), 'AcceptFormats', '__httpwww_opengis_netows1_1_GetCapabilitiesType_httpwww_opengis_netows1_1AcceptFormats', False)

    
    AcceptFormats = property(__AcceptFormats.value, __AcceptFormats.set, None, u'When omitted or not supported by server, server shall return service metadata document using the MIME type "text/xml". ')

    
    # Element {http://www.opengis.net/ows/1.1}Sections uses Python identifier Sections
    __Sections = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sections'), 'Sections', '__httpwww_opengis_netows1_1_GetCapabilitiesType_httpwww_opengis_netows1_1Sections', False)

    
    Sections = property(__Sections.value, __Sections.set, None, u'When omitted or not supported by server, server shall return complete service metadata (Capabilities) document. ')

    
    # Element {http://www.opengis.net/ows/1.1}AcceptVersions uses Python identifier AcceptVersions
    __AcceptVersions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AcceptVersions'), 'AcceptVersions', '__httpwww_opengis_netows1_1_GetCapabilitiesType_httpwww_opengis_netows1_1AcceptVersions', False)

    
    AcceptVersions = property(__AcceptVersions.value, __AcceptVersions.set, None, u'When omitted, server shall return latest supported version. ')

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updateSequence'), 'updateSequence', '__httpwww_opengis_netows1_1_GetCapabilitiesType_updateSequence', UpdateSequenceType)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, u'When omitted or not supported by server, server shall return latest complete service metadata document. ')


    _ElementMap = {
        __AcceptFormats.name() : __AcceptFormats,
        __Sections.name() : __Sections,
        __AcceptVersions.name() : __AcceptVersions
    }
    _AttributeMap = {
        __updateSequence.name() : __updateSequence
    }
Namespace.addCategoryObject('typeBinding', u'GetCapabilitiesType', GetCapabilitiesType)


# Complex type LanguageStringType with content type SIMPLE
class LanguageStringType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LanguageStringType')
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netows1_1_LanguageStringType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang
    }
Namespace.addCategoryObject('typeBinding', u'LanguageStringType', LanguageStringType)


# Complex type RangeType with content type ELEMENT_ONLY
class RangeType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RangeType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Spacing uses Python identifier Spacing
    __Spacing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Spacing'), 'Spacing', '__httpwww_opengis_netows1_1_RangeType_httpwww_opengis_netows1_1Spacing', False)

    
    Spacing = property(__Spacing.value, __Spacing.set, None, u'The regular distance or spacing between the allowed values in a range. ')

    
    # Element {http://www.opengis.net/ows/1.1}MaximumValue uses Python identifier MaximumValue
    __MaximumValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaximumValue'), 'MaximumValue', '__httpwww_opengis_netows1_1_RangeType_httpwww_opengis_netows1_1MaximumValue', False)

    
    MaximumValue = property(__MaximumValue.value, __MaximumValue.set, None, u'Maximum value of this numeric parameter. ')

    
    # Element {http://www.opengis.net/ows/1.1}MinimumValue uses Python identifier MinimumValue
    __MinimumValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinimumValue'), 'MinimumValue', '__httpwww_opengis_netows1_1_RangeType_httpwww_opengis_netows1_1MinimumValue', False)

    
    MinimumValue = property(__MinimumValue.value, __MinimumValue.set, None, u'Minimum value of this numeric parameter. ')

    
    # Attribute {http://www.opengis.net/ows/1.1}rangeClosure uses Python identifier rangeClosure
    __rangeClosure = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'rangeClosure'), 'rangeClosure', '__httpwww_opengis_netows1_1_RangeType_httpwww_opengis_netows1_1rangeClosure', STD_ANON_2, unicode_default=u'closed')
    
    rangeClosure = property(__rangeClosure.value, __rangeClosure.set, None, u'Specifies which of the minimum and maximum values are included in the range. Note that plus and minus infinity are considered closed bounds. ')


    _ElementMap = {
        __Spacing.name() : __Spacing,
        __MaximumValue.name() : __MaximumValue,
        __MinimumValue.name() : __MinimumValue
    }
    _AttributeMap = {
        __rangeClosure.name() : __rangeClosure
    }
Namespace.addCategoryObject('typeBinding', u'RangeType', RangeType)


# Complex type SectionsType with content type ELEMENT_ONLY
class SectionsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SectionsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Section uses Python identifier Section
    __Section = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Section'), 'Section', '__httpwww_opengis_netows1_1_SectionsType_httpwww_opengis_netows1_1Section', True)

    
    Section = property(__Section.value, __Section.set, None, None)


    _ElementMap = {
        __Section.name() : __Section
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SectionsType', SectionsType)


# Complex type UnNamedDomainType with content type ELEMENT_ONLY
class UnNamedDomainType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UnNamedDomainType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Meaning uses Python identifier Meaning
    __Meaning = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Meaning'), 'Meaning', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1Meaning', False)

    
    Meaning = property(__Meaning.value, __Meaning.set, None, u'Definition of the meaning or semantics of this set of values. This Meaning can provide more specific, complete, precise, machine accessible, and machine understandable semantics about this quantity, relative to other available semantic information. For example, other semantic information is often provided in "documentation" elements in XML Schemas or "description" elements in GML objects. ')

    
    # Element {http://www.opengis.net/ows/1.1}DefaultValue uses Python identifier DefaultValue
    __DefaultValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DefaultValue'), 'DefaultValue', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1DefaultValue', False)

    
    DefaultValue = property(__DefaultValue.value, __DefaultValue.set, None, u'The default value for a quantity for which multiple values are allowed. ')

    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1Metadata', True)

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}AllowedValues uses Python identifier AllowedValues
    __AllowedValues = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AllowedValues'), 'AllowedValues', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1AllowedValues', False)

    
    AllowedValues = property(__AllowedValues.value, __AllowedValues.set, None, u'List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. ')

    
    # Element {http://www.opengis.net/ows/1.1}UOM uses Python identifier UOM
    __UOM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'UOM'), 'UOM', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1UOM', False)

    
    UOM = property(__UOM.value, __UOM.set, None, u'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ')

    
    # Element {http://www.opengis.net/ows/1.1}DataType uses Python identifier DataType
    __DataType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataType'), 'DataType', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1DataType', False)

    
    DataType = property(__DataType.value, __DataType.set, None, u'Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ')

    
    # Element {http://www.opengis.net/ows/1.1}NoValues uses Python identifier NoValues
    __NoValues = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NoValues'), 'NoValues', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1NoValues', False)

    
    NoValues = property(__NoValues.value, __NoValues.set, None, u'Specifies that no values are allowed for this parameter or quantity.')

    
    # Element {http://www.opengis.net/ows/1.1}ReferenceSystem uses Python identifier ReferenceSystem
    __ReferenceSystem = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'), 'ReferenceSystem', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1ReferenceSystem', False)

    
    ReferenceSystem = property(__ReferenceSystem.value, __ReferenceSystem.set, None, u'Definition of the reference system used by this set of values, including the unit of measure whenever applicable (as is normal). In this case, the xlink:href attribute can reference a URN for a well-known reference system, such as for a coordinate reference system (CRS). For example, such a URN could be a CRS identification URN defined in the "ogc" URN namespace. ')

    
    # Element {http://www.opengis.net/ows/1.1}ValuesReference uses Python identifier ValuesReference
    __ValuesReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ValuesReference'), 'ValuesReference', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1ValuesReference', False)

    
    ValuesReference = property(__ValuesReference.value, __ValuesReference.set, None, u'Reference to externally specified list of all the valid values and/or ranges of values for this quantity. (Informative: This element was simplified from the metaDataProperty element in GML 3.0.) ')

    
    # Element {http://www.opengis.net/ows/1.1}AnyValue uses Python identifier AnyValue
    __AnyValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AnyValue'), 'AnyValue', '__httpwww_opengis_netows1_1_UnNamedDomainType_httpwww_opengis_netows1_1AnyValue', False)

    
    AnyValue = property(__AnyValue.value, __AnyValue.set, None, u'Specifies that any value is allowed for this parameter.')


    _ElementMap = {
        __Meaning.name() : __Meaning,
        __DefaultValue.name() : __DefaultValue,
        __Metadata.name() : __Metadata,
        __AllowedValues.name() : __AllowedValues,
        __UOM.name() : __UOM,
        __DataType.name() : __DataType,
        __NoValues.name() : __NoValues,
        __ReferenceSystem.name() : __ReferenceSystem,
        __ValuesReference.name() : __ValuesReference,
        __AnyValue.name() : __AnyValue
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'UnNamedDomainType', UnNamedDomainType)


# Complex type DomainType with content type ELEMENT_ONLY
class DomainType (UnNamedDomainType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DomainType')
    # Base type is UnNamedDomainType
    
    # Element Meaning ({http://www.opengis.net/ows/1.1}Meaning) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element DefaultValue ({http://www.opengis.net/ows/1.1}DefaultValue) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element AllowedValues ({http://www.opengis.net/ows/1.1}AllowedValues) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element UOM ({http://www.opengis.net/ows/1.1}UOM) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element DataType ({http://www.opengis.net/ows/1.1}DataType) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element NoValues ({http://www.opengis.net/ows/1.1}NoValues) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element ReferenceSystem ({http://www.opengis.net/ows/1.1}ReferenceSystem) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element ValuesReference ({http://www.opengis.net/ows/1.1}ValuesReference) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Element AnyValue ({http://www.opengis.net/ows/1.1}AnyValue) inherited from {http://www.opengis.net/ows/1.1}UnNamedDomainType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_opengis_netows1_1_DomainType_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Name or identifier of this quantity. ')


    _ElementMap = UnNamedDomainType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = UnNamedDomainType._AttributeMap.copy()
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'DomainType', DomainType)


# Complex type CodeType with content type SIMPLE
class CodeType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodeType')
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute codeSpace uses Python identifier codeSpace
    __codeSpace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'codeSpace'), 'codeSpace', '__httpwww_opengis_netows1_1_CodeType_codeSpace', pyxb.binding.datatypes.anyURI)
    
    codeSpace = property(__codeSpace.value, __codeSpace.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __codeSpace.name() : __codeSpace
    }
Namespace.addCategoryObject('typeBinding', u'CodeType', CodeType)


# Complex type CTD_ANON_5 with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Operation uses Python identifier Operation
    __Operation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Operation'), 'Operation', '__httpwww_opengis_netows1_1_CTD_ANON_5_httpwww_opengis_netows1_1Operation', True)

    
    Operation = property(__Operation.value, __Operation.set, None, u'Metadata for one operation that this server implements. ')

    
    # Element {http://www.opengis.net/ows/1.1}ExtendedCapabilities uses Python identifier ExtendedCapabilities
    __ExtendedCapabilities = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtendedCapabilities'), 'ExtendedCapabilities', '__httpwww_opengis_netows1_1_CTD_ANON_5_httpwww_opengis_netows1_1ExtendedCapabilities', False)

    
    ExtendedCapabilities = property(__ExtendedCapabilities.value, __ExtendedCapabilities.set, None, u'Individual software vendors and servers can use this element to provide metadata about any additional server abilities. ')

    
    # Element {http://www.opengis.net/ows/1.1}Parameter uses Python identifier Parameter
    __Parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Parameter'), 'Parameter', '__httpwww_opengis_netows1_1_CTD_ANON_5_httpwww_opengis_netows1_1Parameter', True)

    
    Parameter = property(__Parameter.value, __Parameter.set, None, u'Optional unordered list of parameter valid domains that each apply to one or more operations which this server interface implements. The list of required and optional parameter domain limitations shall be specified in the Implementation Specification for this service. ')

    
    # Element {http://www.opengis.net/ows/1.1}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Constraint'), 'Constraint', '__httpwww_opengis_netows1_1_CTD_ANON_5_httpwww_opengis_netows1_1Constraint', True)

    
    Constraint = property(__Constraint.value, __Constraint.set, None, u'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this server. The list of required and optional constraints shall be specified in the Implementation Specification for this service. ')


    _ElementMap = {
        __Operation.name() : __Operation,
        __ExtendedCapabilities.name() : __ExtendedCapabilities,
        __Parameter.name() : __Parameter,
        __Constraint.name() : __Constraint
    }
    _AttributeMap = {
        
    }



# Complex type ContentsBaseType with content type ELEMENT_ONLY
class ContentsBaseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContentsBaseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}DatasetDescriptionSummary uses Python identifier DatasetDescriptionSummary
    __DatasetDescriptionSummary = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatasetDescriptionSummary'), 'DatasetDescriptionSummary', '__httpwww_opengis_netows1_1_ContentsBaseType_httpwww_opengis_netows1_1DatasetDescriptionSummary', True)

    
    DatasetDescriptionSummary = property(__DatasetDescriptionSummary.value, __DatasetDescriptionSummary.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}OtherSource uses Python identifier OtherSource
    __OtherSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OtherSource'), 'OtherSource', '__httpwww_opengis_netows1_1_ContentsBaseType_httpwww_opengis_netows1_1OtherSource', True)

    
    OtherSource = property(__OtherSource.value, __OtherSource.set, None, u'Reference to a source of metadata describing  coverage offerings available from this server. This  parameter can reference a catalogue server from which dataset metadata is available. This ability is expected to be used by servers with thousands or millions of datasets, for which searching a catalogue is more feasible than fetching a long Capabilities XML document. When no DatasetDescriptionSummaries are included, and one or more catalogue servers are referenced, this set of catalogues shall contain current metadata summaries for all the datasets currently available from this OWS server, with the metadata for each such dataset referencing this OWS server. ')


    _ElementMap = {
        __DatasetDescriptionSummary.name() : __DatasetDescriptionSummary,
        __OtherSource.name() : __OtherSource
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ContentsBaseType', ContentsBaseType)


# Complex type BasicIdentificationType with content type ELEMENT_ONLY
class BasicIdentificationType (DescriptionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BasicIdentificationType')
    # Base type is DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_BasicIdentificationType_httpwww_opengis_netows1_1Metadata', True)

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpwww_opengis_netows1_1_BasicIdentificationType_httpwww_opengis_netows1_1Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'Unique identifier or name of this dataset. ')


    _ElementMap = DescriptionType._ElementMap.copy()
    _ElementMap.update({
        __Metadata.name() : __Metadata,
        __Identifier.name() : __Identifier
    })
    _AttributeMap = DescriptionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BasicIdentificationType', BasicIdentificationType)


# Complex type ReferenceGroupType with content type ELEMENT_ONLY
class ReferenceGroupType (BasicIdentificationType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReferenceGroupType')
    # Base type is BasicIdentificationType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}AbstractReferenceBase uses Python identifier AbstractReferenceBase
    __AbstractReferenceBase = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AbstractReferenceBase'), 'AbstractReferenceBase', '__httpwww_opengis_netows1_1_ReferenceGroupType_httpwww_opengis_netows1_1AbstractReferenceBase', True)

    
    AbstractReferenceBase = property(__AbstractReferenceBase.value, __AbstractReferenceBase.set, None, None)


    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _ElementMap.update({
        __AbstractReferenceBase.name() : __AbstractReferenceBase
    })
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ReferenceGroupType', ReferenceGroupType)


# Complex type AddressType with content type ELEMENT_ONLY
class AddressType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AddressType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Country'), 'Country', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1Country', False)

    
    Country = property(__Country.value, __Country.set, None, u'Country of the physical address. ')

    
    # Element {http://www.opengis.net/ows/1.1}DeliveryPoint uses Python identifier DeliveryPoint
    __DeliveryPoint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DeliveryPoint'), 'DeliveryPoint', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1DeliveryPoint', True)

    
    DeliveryPoint = property(__DeliveryPoint.value, __DeliveryPoint.set, None, u'Address line for the location. ')

    
    # Element {http://www.opengis.net/ows/1.1}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PostalCode'), 'PostalCode', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1PostalCode', False)

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, u'ZIP or other postal code. ')

    
    # Element {http://www.opengis.net/ows/1.1}AdministrativeArea uses Python identifier AdministrativeArea
    __AdministrativeArea = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AdministrativeArea'), 'AdministrativeArea', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1AdministrativeArea', False)

    
    AdministrativeArea = property(__AdministrativeArea.value, __AdministrativeArea.set, None, u'State or province of the location. ')

    
    # Element {http://www.opengis.net/ows/1.1}ElectronicMailAddress uses Python identifier ElectronicMailAddress
    __ElectronicMailAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ElectronicMailAddress'), 'ElectronicMailAddress', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1ElectronicMailAddress', True)

    
    ElectronicMailAddress = property(__ElectronicMailAddress.value, __ElectronicMailAddress.set, None, u'Address of the electronic mailbox of the responsible organization or individual. ')

    
    # Element {http://www.opengis.net/ows/1.1}City uses Python identifier City
    __City = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'City'), 'City', '__httpwww_opengis_netows1_1_AddressType_httpwww_opengis_netows1_1City', False)

    
    City = property(__City.value, __City.set, None, u'City of the location. ')


    _ElementMap = {
        __Country.name() : __Country,
        __DeliveryPoint.name() : __DeliveryPoint,
        __PostalCode.name() : __PostalCode,
        __AdministrativeArea.name() : __AdministrativeArea,
        __ElectronicMailAddress.name() : __ElectronicMailAddress,
        __City.name() : __City
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'AddressType', AddressType)


# Complex type AbstractReferenceBaseType with content type EMPTY
class AbstractReferenceBaseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AbstractReferenceBaseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'arcrole'), 'arcrole', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'title'), 'title', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'href'), 'href', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI, required=True)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'show'), 'show', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkshow', WPS_1_0_0._xlink.STD_ANON_1)
    
    show = property(__show.value, __show.set, None, u"\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.opengis.net/ows/1.1}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_opengis_netows1_1type', pyxb.binding.datatypes.string, fixed=True, unicode_default=u'simple')
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'actuate'), 'actuate', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkactuate', WPS_1_0_0._xlink.STD_ANON_2)
    
    actuate = property(__actuate.value, __actuate.set, None, u"\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'role'), 'role', '__httpwww_opengis_netows1_1_AbstractReferenceBaseType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    
    role = property(__role.value, __role.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __href.name() : __href,
        __show.name() : __show,
        __type.name() : __type,
        __actuate.name() : __actuate,
        __role.name() : __role
    }
Namespace.addCategoryObject('typeBinding', u'AbstractReferenceBaseType', AbstractReferenceBaseType)


# Complex type IdentificationType with content type ELEMENT_ONLY
class IdentificationType (BasicIdentificationType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IdentificationType')
    # Base type is BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/1.1}AvailableCRS uses Python identifier AvailableCRS
    __AvailableCRS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AvailableCRS'), 'AvailableCRS', '__httpwww_opengis_netows1_1_IdentificationType_httpwww_opengis_netows1_1AvailableCRS', True)

    
    AvailableCRS = property(__AvailableCRS.value, __AvailableCRS.set, None, None)

    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/1.1}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netows1_1_IdentificationType_httpwww_opengis_netows1_1BoundingBox', True)

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, None)

    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element {http://www.opengis.net/ows/1.1}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows1_1_IdentificationType_httpwww_opengis_netows1_1OutputFormat', True)

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, u'Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ')


    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _ElementMap.update({
        __AvailableCRS.name() : __AvailableCRS,
        __BoundingBox.name() : __BoundingBox,
        __OutputFormat.name() : __OutputFormat
    })
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'IdentificationType', IdentificationType)


# Complex type CTD_ANON_6 with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Post uses Python identifier Post
    __Post = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Post'), 'Post', '__httpwww_opengis_netows1_1_CTD_ANON_6_httpwww_opengis_netows1_1Post', True)

    
    Post = property(__Post.value, __Post.set, None, u'Connect point URL and any constraints for the HTTP "Post" request method for this operation request. ')

    
    # Element {http://www.opengis.net/ows/1.1}Get uses Python identifier Get
    __Get = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Get'), 'Get', '__httpwww_opengis_netows1_1_CTD_ANON_6_httpwww_opengis_netows1_1Get', True)

    
    Get = property(__Get.value, __Get.set, None, u'Connect point URL prefix and any constraints for the HTTP "Get" request method for this operation request. ')


    _ElementMap = {
        __Post.name() : __Post,
        __Get.name() : __Get
    }
    _AttributeMap = {
        
    }



# Complex type ResponsiblePartySubsetType with content type ELEMENT_ONLY
class ResponsiblePartySubsetType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResponsiblePartySubsetType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}IndividualName uses Python identifier IndividualName
    __IndividualName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IndividualName'), 'IndividualName', '__httpwww_opengis_netows1_1_ResponsiblePartySubsetType_httpwww_opengis_netows1_1IndividualName', False)

    
    IndividualName = property(__IndividualName.value, __IndividualName.set, None, u'Name of the responsible person: surname, given name, title separated by a delimiter. ')

    
    # Element {http://www.opengis.net/ows/1.1}PositionName uses Python identifier PositionName
    __PositionName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PositionName'), 'PositionName', '__httpwww_opengis_netows1_1_ResponsiblePartySubsetType_httpwww_opengis_netows1_1PositionName', False)

    
    PositionName = property(__PositionName.value, __PositionName.set, None, u'Role or position of the responsible person. ')

    
    # Element {http://www.opengis.net/ows/1.1}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Role'), 'Role', '__httpwww_opengis_netows1_1_ResponsiblePartySubsetType_httpwww_opengis_netows1_1Role', False)

    
    Role = property(__Role.value, __Role.set, None, u'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ')

    
    # Element {http://www.opengis.net/ows/1.1}ContactInfo uses Python identifier ContactInfo
    __ContactInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'), 'ContactInfo', '__httpwww_opengis_netows1_1_ResponsiblePartySubsetType_httpwww_opengis_netows1_1ContactInfo', False)

    
    ContactInfo = property(__ContactInfo.value, __ContactInfo.set, None, u'Address of the responsible party. ')


    _ElementMap = {
        __IndividualName.name() : __IndividualName,
        __PositionName.name() : __PositionName,
        __Role.name() : __Role,
        __ContactInfo.name() : __ContactInfo
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ResponsiblePartySubsetType', ResponsiblePartySubsetType)


# Complex type ContactType with content type ELEMENT_ONLY
class ContactType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContactType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}HoursOfService uses Python identifier HoursOfService
    __HoursOfService = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HoursOfService'), 'HoursOfService', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1HoursOfService', False)

    
    HoursOfService = property(__HoursOfService.value, __HoursOfService.set, None, u'Time period (including time zone) when individuals can contact the organization or individual. ')

    
    # Element {http://www.opengis.net/ows/1.1}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1OnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'On-line information that can be used to contact the individual or organization. OWS specifics: The xlink:href attribute in the xlink:simpleLink attribute group shall be used to reference this resource. Whenever practical, the xlink:href attribute with type anyURI should be a URL from which more contact information can be electronically retrieved. The xlink:title attribute with type "string" can be used to name this set of information. The other attributes in the xlink:simpleLink attribute group should not be used. ')

    
    # Element {http://www.opengis.net/ows/1.1}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Address'), 'Address', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1Address', False)

    
    Address = property(__Address.value, __Address.set, None, u'Physical and email address at which the organization or individual may be contacted. ')

    
    # Element {http://www.opengis.net/ows/1.1}Phone uses Python identifier Phone
    __Phone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Phone'), 'Phone', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1Phone', False)

    
    Phone = property(__Phone.value, __Phone.set, None, u'Telephone numbers at which the organization or individual may be contacted. ')

    
    # Element {http://www.opengis.net/ows/1.1}ContactInstructions uses Python identifier ContactInstructions
    __ContactInstructions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactInstructions'), 'ContactInstructions', '__httpwww_opengis_netows1_1_ContactType_httpwww_opengis_netows1_1ContactInstructions', False)

    
    ContactInstructions = property(__ContactInstructions.value, __ContactInstructions.set, None, u'Supplemental instructions on how or when to contact the individual or organization. ')


    _ElementMap = {
        __HoursOfService.name() : __HoursOfService,
        __OnlineResource.name() : __OnlineResource,
        __Address.name() : __Address,
        __Phone.name() : __Phone,
        __ContactInstructions.name() : __ContactInstructions
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ContactType', ContactType)


# Complex type ManifestType with content type ELEMENT_ONLY
class ManifestType (BasicIdentificationType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ManifestType')
    # Base type is BasicIdentificationType
    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Keywords ({http://www.opengis.net/ows/1.1}Keywords) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}BasicIdentificationType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}DescriptionType
    
    # Element {http://www.opengis.net/ows/1.1}ReferenceGroup uses Python identifier ReferenceGroup
    __ReferenceGroup = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReferenceGroup'), 'ReferenceGroup', '__httpwww_opengis_netows1_1_ManifestType_httpwww_opengis_netows1_1ReferenceGroup', True)

    
    ReferenceGroup = property(__ReferenceGroup.value, __ReferenceGroup.set, None, None)


    _ElementMap = BasicIdentificationType._ElementMap.copy()
    _ElementMap.update({
        __ReferenceGroup.name() : __ReferenceGroup
    })
    _AttributeMap = BasicIdentificationType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ManifestType', ManifestType)


# Complex type CTD_ANON_7 with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Range uses Python identifier Range
    __Range = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Range'), 'Range', '__httpwww_opengis_netows1_1_CTD_ANON_7_httpwww_opengis_netows1_1Range', True)

    
    Range = property(__Range.value, __Range.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpwww_opengis_netows1_1_CTD_ANON_7_httpwww_opengis_netows1_1Value', True)

    
    Value = property(__Value.value, __Value.set, None, None)


    _ElementMap = {
        __Range.name() : __Range,
        __Value.name() : __Value
    }
    _AttributeMap = {
        
    }



# Complex type AcceptFormatsType with content type ELEMENT_ONLY
class AcceptFormatsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AcceptFormatsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows1_1_AcceptFormatsType_httpwww_opengis_netows1_1OutputFormat', True)

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, None)


    _ElementMap = {
        __OutputFormat.name() : __OutputFormat
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'AcceptFormatsType', AcceptFormatsType)


# Complex type CTD_ANON_8 with content type SIMPLE
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.opengis.net/ows/1.1}reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'reference'), 'reference', '__httpwww_opengis_netows1_1_CTD_ANON_8_httpwww_opengis_netows1_1reference', pyxb.binding.datatypes.anyURI, required=True)
    
    reference = property(__reference.value, __reference.set, None, u'Reference to data or metadata recorded elsewhere, either external to this XML document or within it. Whenever practical, this attribute should be a URL from which this metadata can be electronically retrieved. Alternately, this attribute can reference a URN for well-known metadata. For example, such a URN could be a URN defined in the "ogc" URN namespace. ')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __reference.name() : __reference
    }



# Complex type CapabilitiesBaseType with content type ELEMENT_ONLY
class CapabilitiesBaseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CapabilitiesBaseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}OperationsMetadata uses Python identifier OperationsMetadata
    __OperationsMetadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OperationsMetadata'), 'OperationsMetadata', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_httpwww_opengis_netows1_1OperationsMetadata', False)

    
    OperationsMetadata = property(__OperationsMetadata.value, __OperationsMetadata.set, None, u'Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceProvider uses Python identifier ServiceProvider
    __ServiceProvider = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ServiceProvider'), 'ServiceProvider', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_httpwww_opengis_netows1_1ServiceProvider', False)

    
    ServiceProvider = property(__ServiceProvider.value, __ServiceProvider.set, None, u'Metadata about the organization that provides this specific service instance or server. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceIdentification uses Python identifier ServiceIdentification
    __ServiceIdentification = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ServiceIdentification'), 'ServiceIdentification', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_httpwww_opengis_netows1_1ServiceIdentification', False)

    
    ServiceIdentification = property(__ServiceIdentification.value, __ServiceIdentification.set, None, u'General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_version', VersionType, required=True)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updateSequence'), 'updateSequence', '__httpwww_opengis_netows1_1_CapabilitiesBaseType_updateSequence', UpdateSequenceType)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, u'Service metadata document version, having values that are "increased" whenever any change is made in service metadata document. Values are selected by each server, and are always opaque to clients. When not supported by server, server shall not return this attribute. ')


    _ElementMap = {
        __OperationsMetadata.name() : __OperationsMetadata,
        __ServiceProvider.name() : __ServiceProvider,
        __ServiceIdentification.name() : __ServiceIdentification
    }
    _AttributeMap = {
        __version.name() : __version,
        __updateSequence.name() : __updateSequence
    }
Namespace.addCategoryObject('typeBinding', u'CapabilitiesBaseType', CapabilitiesBaseType)


# Complex type OnlineResourceType with content type EMPTY
class OnlineResourceType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OnlineResourceType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'type'), 'type', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default=u'simple')
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'show'), 'show', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkshow', WPS_1_0_0._xlink.STD_ANON_1)
    
    show = property(__show.value, __show.set, None, u"\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'title'), 'title', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'role'), 'role', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'arcrole'), 'arcrole', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'href'), 'href', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'actuate'), 'actuate', '__httpwww_opengis_netows1_1_OnlineResourceType_httpwww_w3_org1999xlinkactuate', WPS_1_0_0._xlink.STD_ANON_2)
    
    actuate = property(__actuate.value, __actuate.set, None, u"\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")


    _ElementMap = {
        
    }
    _AttributeMap = {
        __type.name() : __type,
        __show.name() : __show,
        __title.name() : __title,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __href.name() : __href,
        __actuate.name() : __actuate
    }
Namespace.addCategoryObject('typeBinding', u'OnlineResourceType', OnlineResourceType)


# Complex type RequestMethodType with content type ELEMENT_ONLY
class RequestMethodType (OnlineResourceType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RequestMethodType')
    # Base type is OnlineResourceType
    
    # Element {http://www.opengis.net/ows/1.1}Constraint uses Python identifier Constraint
    __Constraint = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Constraint'), 'Constraint', '__httpwww_opengis_netows1_1_RequestMethodType_httpwww_opengis_netows1_1Constraint', True)

    
    Constraint = property(__Constraint.value, __Constraint.set, None, u'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this request method for this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata or Operation element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this request method for this operation shall be specified in the Implementation Specification for this service. ')

    
    # Attribute type inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute show inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute href inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute role inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute title inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/1.1}OnlineResourceType

    _ElementMap = OnlineResourceType._ElementMap.copy()
    _ElementMap.update({
        __Constraint.name() : __Constraint
    })
    _AttributeMap = OnlineResourceType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'RequestMethodType', RequestMethodType)


# Complex type ReferenceType with content type ELEMENT_ONLY
class ReferenceType (AbstractReferenceBaseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReferenceType')
    # Base type is AbstractReferenceBaseType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpwww_opengis_netows1_1_ReferenceType_httpwww_opengis_netows1_1Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), 'Metadata', '__httpwww_opengis_netows1_1_ReferenceType_httpwww_opengis_netows1_1Metadata', True)

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), 'Abstract', '__httpwww_opengis_netows1_1_ReferenceType_httpwww_opengis_netows1_1Abstract', True)

    
    Abstract = property(__Abstract.value, __Abstract.set, None, u'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netows1_1_ReferenceType_httpwww_opengis_netows1_1Format', False)

    
    Format = property(__Format.value, __Format.set, None, u'The format of the referenced resource. This element is omitted when the mime type is indicated in the http header of the reference. ')

    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute title inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute href inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute show inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute type inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute role inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType

    _ElementMap = AbstractReferenceBaseType._ElementMap.copy()
    _ElementMap.update({
        __Identifier.name() : __Identifier,
        __Metadata.name() : __Metadata,
        __Abstract.name() : __Abstract,
        __Format.name() : __Format
    })
    _AttributeMap = AbstractReferenceBaseType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ReferenceType', ReferenceType)


# Complex type ExceptionType with content type ELEMENT_ONLY
class ExceptionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExceptionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}ExceptionText uses Python identifier ExceptionText
    __ExceptionText = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExceptionText'), 'ExceptionText', '__httpwww_opengis_netows1_1_ExceptionType_httpwww_opengis_netows1_1ExceptionText', True)

    
    ExceptionText = property(__ExceptionText.value, __ExceptionText.set, None, u'Ordered sequence of text strings that describe this specific exception or error. The contents of these strings are left open to definition by each server implementation. A server is strongly encouraged to include at least one ExceptionText value, to provide more information about the detected error than provided by the exceptionCode. When included, multiple ExceptionText values shall provide hierarchical information about one detected error, with the most significant information listed first. ')

    
    # Attribute exceptionCode uses Python identifier exceptionCode
    __exceptionCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'exceptionCode'), 'exceptionCode', '__httpwww_opengis_netows1_1_ExceptionType_exceptionCode', pyxb.binding.datatypes.string, required=True)
    
    exceptionCode = property(__exceptionCode.value, __exceptionCode.set, None, u'A code representing the type of this exception, which shall be selected from a set of exceptionCode values specified for the specific service operation and server. ')

    
    # Attribute locator uses Python identifier locator
    __locator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'locator'), 'locator', '__httpwww_opengis_netows1_1_ExceptionType_locator', pyxb.binding.datatypes.string)
    
    locator = property(__locator.value, __locator.set, None, u"When included, this locator shall indicate to the client where an exception was encountered in servicing the client's operation request. This locator should be included whenever meaningful information can be provided by the server. The contents of this locator will depend on the specific exceptionCode and OWS service, and shall be specified in the OWS Implementation Specification. ")


    _ElementMap = {
        __ExceptionText.name() : __ExceptionText
    }
    _AttributeMap = {
        __exceptionCode.name() : __exceptionCode,
        __locator.name() : __locator
    }
Namespace.addCategoryObject('typeBinding', u'ExceptionType', ExceptionType)


# Complex type CTD_ANON_9 with content type EMPTY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }



# Complex type ServiceReferenceType with content type ELEMENT_ONLY
class ServiceReferenceType (ReferenceType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ServiceReferenceType')
    # Base type is ReferenceType
    
    # Element Format ({http://www.opengis.net/ows/1.1}Format) inherited from {http://www.opengis.net/ows/1.1}ReferenceType
    
    # Element {http://www.opengis.net/ows/1.1}RequestMessage uses Python identifier RequestMessage
    __RequestMessage = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RequestMessage'), 'RequestMessage', '__httpwww_opengis_netows1_1_ServiceReferenceType_httpwww_opengis_netows1_1RequestMessage', False)

    
    RequestMessage = property(__RequestMessage.value, __RequestMessage.set, None, u'The XML-encoded operation request message to be sent to request this input data from another web server using HTTP Post. ')

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/ows/1.1}ReferenceType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/ows/1.1}ReferenceType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/ows/1.1}ReferenceType
    
    # Element {http://www.opengis.net/ows/1.1}RequestMessageReference uses Python identifier RequestMessageReference
    __RequestMessageReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RequestMessageReference'), 'RequestMessageReference', '__httpwww_opengis_netows1_1_ServiceReferenceType_httpwww_opengis_netows1_1RequestMessageReference', False)

    
    RequestMessageReference = property(__RequestMessageReference.value, __RequestMessageReference.set, None, u'Reference to the XML-encoded operation request message to be sent to request this input data from another web server using HTTP Post. The referenced message shall be attached to the same message (using the cid scheme), or be accessible using a URL. ')

    
    # Attribute arcrole inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute title inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute href inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute show inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute type inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute actuate inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType
    
    # Attribute role inherited from {http://www.opengis.net/ows/1.1}AbstractReferenceBaseType

    _ElementMap = ReferenceType._ElementMap.copy()
    _ElementMap.update({
        __RequestMessage.name() : __RequestMessage,
        __RequestMessageReference.name() : __RequestMessageReference
    })
    _AttributeMap = ReferenceType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ServiceReferenceType', ServiceReferenceType)


# Complex type CTD_ANON_10 with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}ProviderName uses Python identifier ProviderName
    __ProviderName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProviderName'), 'ProviderName', '__httpwww_opengis_netows1_1_CTD_ANON_10_httpwww_opengis_netows1_1ProviderName', False)

    
    ProviderName = property(__ProviderName.value, __ProviderName.set, None, u'A unique identifier for the service provider organization. ')

    
    # Element {http://www.opengis.net/ows/1.1}ProviderSite uses Python identifier ProviderSite
    __ProviderSite = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProviderSite'), 'ProviderSite', '__httpwww_opengis_netows1_1_CTD_ANON_10_httpwww_opengis_netows1_1ProviderSite', False)

    
    ProviderSite = property(__ProviderSite.value, __ProviderSite.set, None, u'Reference to the most relevant web site of the service provider. ')

    
    # Element {http://www.opengis.net/ows/1.1}ServiceContact uses Python identifier ServiceContact
    __ServiceContact = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ServiceContact'), 'ServiceContact', '__httpwww_opengis_netows1_1_CTD_ANON_10_httpwww_opengis_netows1_1ServiceContact', False)

    
    ServiceContact = property(__ServiceContact.value, __ServiceContact.set, None, u'Information for contacting the service provider. The OnlineResource element within this ServiceContact element should not be used to reference a web site of the service provider. ')


    _ElementMap = {
        __ProviderName.name() : __ProviderName,
        __ProviderSite.name() : __ProviderSite,
        __ServiceContact.name() : __ServiceContact
    }
    _AttributeMap = {
        
    }



# Complex type TelephoneType with content type ELEMENT_ONLY
class TelephoneType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TelephoneType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Voice uses Python identifier Voice
    __Voice = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Voice'), 'Voice', '__httpwww_opengis_netows1_1_TelephoneType_httpwww_opengis_netows1_1Voice', True)

    
    Voice = property(__Voice.value, __Voice.set, None, u'Telephone number by which individuals can speak to the responsible organization or individual. ')

    
    # Element {http://www.opengis.net/ows/1.1}Facsimile uses Python identifier Facsimile
    __Facsimile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Facsimile'), 'Facsimile', '__httpwww_opengis_netows1_1_TelephoneType_httpwww_opengis_netows1_1Facsimile', True)

    
    Facsimile = property(__Facsimile.value, __Facsimile.set, None, u'Telephone number of a facsimile machine for the responsible\norganization or individual. ')


    _ElementMap = {
        __Voice.name() : __Voice,
        __Facsimile.name() : __Facsimile
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'TelephoneType', TelephoneType)


# Complex type GetResourceByIdType with content type ELEMENT_ONLY
class GetResourceByIdType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GetResourceByIdType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}ResourceID uses Python identifier ResourceID
    __ResourceID = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ResourceID'), 'ResourceID', '__httpwww_opengis_netows1_1_GetResourceByIdType_httpwww_opengis_netows1_1ResourceID', True)

    
    ResourceID = property(__ResourceID.value, __ResourceID.set, None, u'Unordered list of zero or more resource identifiers. These identifiers can be listed in the Contents section of the service metadata (Capabilities) document. For more information on this parameter, see Subclause 9.4.2.1 of the OWS Common specification. ')

    
    # Element {http://www.opengis.net/ows/1.1}OutputFormat uses Python identifier OutputFormat
    __OutputFormat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'), 'OutputFormat', '__httpwww_opengis_netows1_1_GetResourceByIdType_httpwww_opengis_netows1_1OutputFormat', False)

    
    OutputFormat = property(__OutputFormat.value, __OutputFormat.set, None, u'Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ')

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'service'), 'service', '__httpwww_opengis_netows1_1_GetResourceByIdType_service', ServiceType, required=True)
    
    service = property(__service.value, __service.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_opengis_netows1_1_GetResourceByIdType_version', VersionType, required=True)
    
    version = property(__version.value, __version.set, None, None)


    _ElementMap = {
        __ResourceID.name() : __ResourceID,
        __OutputFormat.name() : __OutputFormat
    }
    _AttributeMap = {
        __service.name() : __service,
        __version.name() : __version
    }
Namespace.addCategoryObject('typeBinding', u'GetResourceByIdType', GetResourceByIdType)


# Complex type CTD_ANON_11 with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}HTTP uses Python identifier HTTP
    __HTTP = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HTTP'), 'HTTP', '__httpwww_opengis_netows1_1_CTD_ANON_11_httpwww_opengis_netows1_1HTTP', False)

    
    HTTP = property(__HTTP.value, __HTTP.set, None, u'Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. ')


    _ElementMap = {
        __HTTP.name() : __HTTP
    }
    _AttributeMap = {
        
    }



# Complex type AcceptVersionsType with content type ELEMENT_ONLY
class AcceptVersionsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AcceptVersionsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httpwww_opengis_netows1_1_AcceptVersionsType_httpwww_opengis_netows1_1Version', True)

    
    Version = property(__Version.value, __Version.set, None, None)


    _ElementMap = {
        __Version.name() : __Version
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'AcceptVersionsType', AcceptVersionsType)


# Complex type ResponsiblePartyType with content type ELEMENT_ONLY
class ResponsiblePartyType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResponsiblePartyType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}ContactInfo uses Python identifier ContactInfo
    __ContactInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'), 'ContactInfo', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1ContactInfo', False)

    
    ContactInfo = property(__ContactInfo.value, __ContactInfo.set, None, u'Address of the responsible party. ')

    
    # Element {http://www.opengis.net/ows/1.1}OrganisationName uses Python identifier OrganisationName
    __OrganisationName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OrganisationName'), 'OrganisationName', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1OrganisationName', False)

    
    OrganisationName = property(__OrganisationName.value, __OrganisationName.set, None, u'Name of the responsible organization. ')

    
    # Element {http://www.opengis.net/ows/1.1}Role uses Python identifier Role
    __Role = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Role'), 'Role', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1Role', False)

    
    Role = property(__Role.value, __Role.set, None, u'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ')

    
    # Element {http://www.opengis.net/ows/1.1}PositionName uses Python identifier PositionName
    __PositionName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PositionName'), 'PositionName', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1PositionName', False)

    
    PositionName = property(__PositionName.value, __PositionName.set, None, u'Role or position of the responsible person. ')

    
    # Element {http://www.opengis.net/ows/1.1}IndividualName uses Python identifier IndividualName
    __IndividualName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IndividualName'), 'IndividualName', '__httpwww_opengis_netows1_1_ResponsiblePartyType_httpwww_opengis_netows1_1IndividualName', False)

    
    IndividualName = property(__IndividualName.value, __IndividualName.set, None, u'Name of the responsible person: surname, given name, title separated by a delimiter. ')


    _ElementMap = {
        __ContactInfo.name() : __ContactInfo,
        __OrganisationName.name() : __OrganisationName,
        __Role.name() : __Role,
        __PositionName.name() : __PositionName,
        __IndividualName.name() : __IndividualName
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ResponsiblePartyType', ResponsiblePartyType)


AvailableCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AvailableCRS'), pyxb.binding.datatypes.anyURI)
Namespace.addCategoryObject('elementBinding', AvailableCRS.name().localName(), AvailableCRS)

DatasetDescriptionSummary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType)
Namespace.addCategoryObject('elementBinding', DatasetDescriptionSummary.name().localName(), DatasetDescriptionSummary)

Value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), ValueType)
Namespace.addCategoryObject('elementBinding', Value.name().localName(), Value)

ServiceIdentification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceIdentification'), CTD_ANON_1, documentation=u'General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. ')
Namespace.addCategoryObject('elementBinding', ServiceIdentification.name().localName(), ServiceIdentification)

AnyValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnyValue'), CTD_ANON_2, documentation=u'Specifies that any value is allowed for this parameter.')
Namespace.addCategoryObject('elementBinding', AnyValue.name().localName(), AnyValue)

Operation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Operation'), CTD_ANON_3, documentation=u'Metadata for one operation that this server implements. ')
Namespace.addCategoryObject('elementBinding', Operation.name().localName(), Operation)

MaximumValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumValue'), ValueType, documentation=u'Maximum value of this numeric parameter. ')
Namespace.addCategoryObject('elementBinding', MaximumValue.name().localName(), MaximumValue)

Keywords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Keywords'), KeywordsType)
Namespace.addCategoryObject('elementBinding', Keywords.name().localName(), Keywords)

Metadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), MetadataType)
Namespace.addCategoryObject('elementBinding', Metadata.name().localName(), Metadata)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetCapabilities'), GetCapabilitiesType)
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

Range = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Range'), RangeType)
Namespace.addCategoryObject('elementBinding', Range.name().localName(), Range)

ReferenceGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceGroup'), ReferenceGroupType)
Namespace.addCategoryObject('elementBinding', ReferenceGroup.name().localName(), ReferenceGroup)

Title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Title'), LanguageStringType, documentation=u'Title of this resource, normally used for display to a human. ')
Namespace.addCategoryObject('elementBinding', Title.name().localName(), Title)

IndividualName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndividualName'), pyxb.binding.datatypes.string, documentation=u'Name of the responsible person: surname, given name, title separated by a delimiter. ')
Namespace.addCategoryObject('elementBinding', IndividualName.name().localName(), IndividualName)

Spacing = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Spacing'), ValueType, documentation=u'The regular distance or spacing between the allowed values in a range. ')
Namespace.addCategoryObject('elementBinding', Spacing.name().localName(), Spacing)

AbstractReferenceBase = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AbstractReferenceBase'), AbstractReferenceBaseType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', AbstractReferenceBase.name().localName(), AbstractReferenceBase)

Manifest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Manifest'), ManifestType)
Namespace.addCategoryObject('elementBinding', Manifest.name().localName(), Manifest)

OtherSource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OtherSource'), MetadataType, documentation=u'Reference to a source of metadata describing  coverage offerings available from this server. This  parameter can reference a catalogue server from which dataset metadata is available. This ability is expected to be used by servers with thousands or millions of datasets, for which searching a catalogue is more feasible than fetching a long Capabilities XML document. When no DatasetDescriptionSummaries are included, and one or more catalogue servers are referenced, this set of catalogues shall contain current metadata summaries for all the datasets currently available from this OWS server, with the metadata for each such dataset referencing this OWS server. ')
Namespace.addCategoryObject('elementBinding', OtherSource.name().localName(), OtherSource)

Role = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Role'), CodeType, documentation=u'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. ')
Namespace.addCategoryObject('elementBinding', Role.name().localName(), Role)

InputData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InputData'), ManifestType, documentation=u'Input data in a XML-encoded OWS operation request, allowing including multiple data items with each data item either included or referenced. This InputData element, or an element using the ManifestType with a more-specific element name (TBR), shall be used whenever applicable within XML-encoded OWS operation requests. ')
Namespace.addCategoryObject('elementBinding', InputData.name().localName(), InputData)

ReferenceSystem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'), DomainMetadataType, documentation=u'Definition of the reference system used by this set of values, including the unit of measure whenever applicable (as is normal). In this case, the xlink:href attribute can reference a URN for a well-known reference system, such as for a coordinate reference system (CRS). For example, such a URN could be a CRS identification URN defined in the "ogc" URN namespace. ')
Namespace.addCategoryObject('elementBinding', ReferenceSystem.name().localName(), ReferenceSystem)

MinimumValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinimumValue'), ValueType, documentation=u'Minimum value of this numeric parameter. ')
Namespace.addCategoryObject('elementBinding', MinimumValue.name().localName(), MinimumValue)

OperationResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OperationResponse'), ManifestType, documentation=u'Response from an OWS operation, allowing including multiple output data items with each item either included or referenced. This OperationResponse element, or an element using the ManifestType with a more specific element name, shall be used whenever applicable for responses from OWS operations. This element is specified for use where the ManifestType contents are needed for an operation response, but the Manifest element name is not fully applicable. This element or the ManifestType shall be used instead of using the ows:ReferenceType proposed in OGC 04-105. ')
Namespace.addCategoryObject('elementBinding', OperationResponse.name().localName(), OperationResponse)

ValuesReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValuesReference'), CTD_ANON_8, documentation=u'Reference to externally specified list of all the valid values and/or ranges of values for this quantity. (Informative: This element was simplified from the metaDataProperty element in GML 3.0.) ')
Namespace.addCategoryObject('elementBinding', ValuesReference.name().localName(), ValuesReference)

DefaultValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DefaultValue'), ValueType, documentation=u'The default value for a quantity for which multiple values are allowed. ')
Namespace.addCategoryObject('elementBinding', DefaultValue.name().localName(), DefaultValue)

OrganisationName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrganisationName'), pyxb.binding.datatypes.string, documentation=u'Name of the responsible organization. ')
Namespace.addCategoryObject('elementBinding', OrganisationName.name().localName(), OrganisationName)

OperationsMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OperationsMetadata'), CTD_ANON_5, documentation=u'Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. ')
Namespace.addCategoryObject('elementBinding', OperationsMetadata.name().localName(), OperationsMetadata)

Reference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), ReferenceType)
Namespace.addCategoryObject('elementBinding', Reference.name().localName(), Reference)

OutputFormat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'), MimeType, documentation=u'Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ')
Namespace.addCategoryObject('elementBinding', OutputFormat.name().localName(), OutputFormat)

AbstractMetaData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AbstractMetaData'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), documentation=u'Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. ')
Namespace.addCategoryObject('elementBinding', AbstractMetaData.name().localName(), AbstractMetaData)

Abstract = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), LanguageStringType, documentation=u'Brief narrative description of this resource, normally used for display to a human. ')
Namespace.addCategoryObject('elementBinding', Abstract.name().localName(), Abstract)

NoValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NoValues'), CTD_ANON_9, documentation=u'Specifies that no values are allowed for this parameter or quantity.')
Namespace.addCategoryObject('elementBinding', NoValues.name().localName(), NoValues)

SupportedCRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SupportedCRS'), pyxb.binding.datatypes.anyURI, documentation=u'Coordinate reference system in which data from this data(set) or resource is available or supported. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. ')
Namespace.addCategoryObject('elementBinding', SupportedCRS.name().localName(), SupportedCRS)

HTTP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HTTP'), CTD_ANON_6, documentation=u'Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. ')
Namespace.addCategoryObject('elementBinding', HTTP.name().localName(), HTTP)

ExtendedCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtendedCapabilities'), pyxb.binding.datatypes.anyType, documentation=u'Individual software vendors and servers can use this element to provide metadata about any additional server abilities. ')
Namespace.addCategoryObject('elementBinding', ExtendedCapabilities.name().localName(), ExtendedCapabilities)

ServiceReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceReference'), ServiceReferenceType)
Namespace.addCategoryObject('elementBinding', ServiceReference.name().localName(), ServiceReference)

AccessConstraints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'), pyxb.binding.datatypes.string, documentation=u'Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. ')
Namespace.addCategoryObject('elementBinding', AccessConstraints.name().localName(), AccessConstraints)

Fees = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fees'), pyxb.binding.datatypes.string, documentation=u'Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. ')
Namespace.addCategoryObject('elementBinding', Fees.name().localName(), Fees)

ServiceProvider = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceProvider'), CTD_ANON_10, documentation=u'Metadata about the organization that provides this specific service instance or server. ')
Namespace.addCategoryObject('elementBinding', ServiceProvider.name().localName(), ServiceProvider)

GetResourceByID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetResourceByID'), GetResourceByIdType)
Namespace.addCategoryObject('elementBinding', GetResourceByID.name().localName(), GetResourceByID)

BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), BoundingBoxType)
Namespace.addCategoryObject('elementBinding', BoundingBox.name().localName(), BoundingBox)

Exception = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Exception'), ExceptionType)
Namespace.addCategoryObject('elementBinding', Exception.name().localName(), Exception)

Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), CodeType, documentation=u'Unique identifier or name of this dataset. ')
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

ExceptionReport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExceptionReport'), CTD_ANON_4, documentation=u'Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. ')
Namespace.addCategoryObject('elementBinding', ExceptionReport.name().localName(), ExceptionReport)

WGS84BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WGS84BoundingBox'), WGS84BoundingBoxType)
Namespace.addCategoryObject('elementBinding', WGS84BoundingBox.name().localName(), WGS84BoundingBox)

DataType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataType'), DomainMetadataType, documentation=u'Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ')
Namespace.addCategoryObject('elementBinding', DataType.name().localName(), DataType)

UOM = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UOM'), DomainMetadataType, documentation=u'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ')
Namespace.addCategoryObject('elementBinding', UOM.name().localName(), UOM)

DCP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DCP'), CTD_ANON_11, documentation=u'Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n')
Namespace.addCategoryObject('elementBinding', DCP.name().localName(), DCP)

AllowedValues = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AllowedValues'), CTD_ANON_7, documentation=u'List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. ')
Namespace.addCategoryObject('elementBinding', AllowedValues.name().localName(), AllowedValues)

PositionName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionName'), pyxb.binding.datatypes.string, documentation=u'Role or position of the responsible person. ')
Namespace.addCategoryObject('elementBinding', PositionName.name().localName(), PositionName)

Language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Language'), pyxb.binding.datatypes.language, documentation=u'Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. ')
Namespace.addCategoryObject('elementBinding', Language.name().localName(), Language)

ContactInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'), ContactType, documentation=u'Address of the responsible party. ')
Namespace.addCategoryObject('elementBinding', ContactInfo.name().localName(), ContactInfo)

Resource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Resource'), pyxb.binding.datatypes.anyType, documentation=u'XML encoded GetResourceByID operation response. The complexType used by this element shall be specified by each specific OWS.  ')
Namespace.addCategoryObject('elementBinding', Resource.name().localName(), Resource)

PointOfContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PointOfContact'), ResponsiblePartyType, documentation=u'Identification of, and means of communication with, person(s) responsible for the resource(s). For OWS use in the ServiceProvider section of a service metadata document, the optional organizationName element was removed, since this type is always used with the ProviderName element which provides that information. The optional individualName element was made mandatory, since either the organizationName or individualName element is mandatory. The mandatory "role" element was changed to optional, since no clear use of this information is known in the ServiceProvider section. ')
Namespace.addCategoryObject('elementBinding', PointOfContact.name().localName(), PointOfContact)

Meaning = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Meaning'), DomainMetadataType, documentation=u'Definition of the meaning or semantics of this set of values. This Meaning can provide more specific, complete, precise, machine accessible, and machine understandable semantics about this quantity, relative to other available semantic information. For example, other semantic information is often provided in "documentation" elements in XML Schemas or "description" elements in GML objects. ')
Namespace.addCategoryObject('elementBinding', Meaning.name().localName(), Meaning)



DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Keywords'), KeywordsType, scope=DescriptionType))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Title'), LanguageStringType, scope=DescriptionType, documentation=u'Title of this resource, normally used for display to a human. '))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), LanguageStringType, scope=DescriptionType, documentation=u'Brief narrative description of this resource, normally used for display to a human. '))
DescriptionType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keywords'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=DescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
    ])
})



DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WGS84BoundingBox'), WGS84BoundingBoxType, scope=DatasetDescriptionSummaryBaseType))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), MetadataType, scope=DatasetDescriptionSummaryBaseType))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), BoundingBoxType, scope=DatasetDescriptionSummaryBaseType))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), CodeType, scope=DatasetDescriptionSummaryBaseType, documentation=u'Unambiguous identifier or name of this coverage, unique for this server. '))

DatasetDescriptionSummaryBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType, scope=DatasetDescriptionSummaryBaseType))
DatasetDescriptionSummaryBaseType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keywords'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WGS84BoundingBox'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WGS84BoundingBox'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatasetDescriptionSummary'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=DatasetDescriptionSummaryBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'))),
    ])
})



BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LowerCorner'), PositionType, scope=BoundingBoxType, documentation=u'Position of the bounding box corner at which the value of each coordinate normally is the algebraic minimum within this bounding box. In some cases, this position is normally displayed at the top, such as the top left for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. '))

BoundingBoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UpperCorner'), PositionType, scope=BoundingBoxType, documentation=u'Position of the bounding box corner at which the value of each coordinate normally is the algebraic maximum within this bounding box. In some cases, this position is normally displayed at the bottom, such as the bottom right for some image coordinates. For more information, see Subclauses 10.2.5 and C.13. '))
BoundingBoxType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LowerCorner'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UpperCorner'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
    ])
})



CTD_ANON_1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fees'), pyxb.binding.datatypes.string, scope=CTD_ANON_1, documentation=u'Fees and terms for retrieving data from or otherwise using this server, including the monetary units as specified in ISO 4217. The reserved value NONE (case insensitive) shall be used to mean no fees or terms. '))

CTD_ANON_1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceTypeVersion'), VersionType, scope=CTD_ANON_1, documentation=u'Unordered list of one or more versions of this service type implemented by this server. This information is not adequate for version negotiation, and shall not be used for that purpose. '))

CTD_ANON_1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'), pyxb.binding.datatypes.string, scope=CTD_ANON_1, documentation=u'Access constraint applied to assure the protection of privacy or intellectual property, or any other restrictions on retrieving or using data from or otherwise using this server. The reserved value NONE (case insensitive) shall be used to mean no access constraints are imposed. '))

CTD_ANON_1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Profile'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_1, documentation=u'Unordered list of identifiers of Application Profiles that are implemented by this server. This element should be included for each specified application profile implemented by this server. The identifier value should be specified by each Application Profile. If this element is omitted, no meaning is implied. '))

CTD_ANON_1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceType'), CodeType, scope=CTD_ANON_1, documentation=u'A service type name from a registry of services. For example, the values of the codeSpace URI and name and code string may be "OGC" and "catalogue." This type name is normally used for machine-to-machine communication. '))
CTD_ANON_1._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keywords'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceType'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceTypeVersion'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceTypeVersion'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Profile'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fees'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'))),
    ])
    , 5 : pyxb.binding.content.ContentModelState(state=5, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Profile'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fees'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_1._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'))),
    ])
})



CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DCP'), CTD_ANON_11, scope=CTD_ANON_3, documentation=u'Information for one distributed Computing Platform (DCP) supported for this operation. At present, only the HTTP DCP is defined, so this element only includes the HTTP element.\n'))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), MetadataType, scope=CTD_ANON_3))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Constraint'), DomainType, scope=CTD_ANON_3, documentation=u'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this operation shall be specified in the Implementation Specification for this service. '))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Parameter'), DomainType, scope=CTD_ANON_3, documentation=u'Optional unordered list of parameter domains that each apply to this operation which this server implements. If one of these Parameter elements has the same "name" attribute as a Parameter element in the OperationsMetadata element, this Parameter element shall override the other one for this operation. The list of required and optional parameter domain limitations for this operation shall be specified in the Implementation Specification for this service. '))
CTD_ANON_3._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DCP'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DCP'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Constraint'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Parameter'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Constraint'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Parameter'))),
    ])
})



CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Exception'), ExceptionType, scope=CTD_ANON_4))
CTD_ANON_4._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Exception'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Exception'))),
    ])
})



KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Keyword'), LanguageStringType, scope=KeywordsType))

KeywordsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Type'), CodeType, scope=KeywordsType))
KeywordsType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keyword'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keyword'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=KeywordsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Type'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
    ])
})



MetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AbstractMetaData'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=MetadataType, documentation=u'Abstract element containing more metadata about the element that includes the containing "metadata" element. A specific server implementation, or an Implementation Specification, can define concrete elements in the AbstractMetaData substitution group. '))
MetadataType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=MetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AbstractMetaData'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
    ])
})


WGS84BoundingBoxType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=WGS84BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LowerCorner'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=WGS84BoundingBoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UpperCorner'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
    ])
})



GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AcceptFormats'), AcceptFormatsType, scope=GetCapabilitiesType, documentation=u'When omitted or not supported by server, server shall return service metadata document using the MIME type "text/xml". '))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sections'), SectionsType, scope=GetCapabilitiesType, documentation=u'When omitted or not supported by server, server shall return complete service metadata (Capabilities) document. '))

GetCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AcceptVersions'), AcceptVersionsType, scope=GetCapabilitiesType, documentation=u'When omitted, server shall return latest supported version. '))
GetCapabilitiesType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AcceptVersions'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sections'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AcceptFormats'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sections'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AcceptFormats'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=GetCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AcceptFormats'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
    ])
})



RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Spacing'), ValueType, scope=RangeType, documentation=u'The regular distance or spacing between the allowed values in a range. '))

RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaximumValue'), ValueType, scope=RangeType, documentation=u'Maximum value of this numeric parameter. '))

RangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinimumValue'), ValueType, scope=RangeType, documentation=u'Minimum value of this numeric parameter. '))
RangeType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinimumValue'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumValue'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Spacing'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaximumValue'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Spacing'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=RangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Spacing'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
    ])
})



SectionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Section'), pyxb.binding.datatypes.string, scope=SectionsType))
SectionsType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=SectionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Section'))),
    ])
})



UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Meaning'), DomainMetadataType, scope=UnNamedDomainType, documentation=u'Definition of the meaning or semantics of this set of values. This Meaning can provide more specific, complete, precise, machine accessible, and machine understandable semantics about this quantity, relative to other available semantic information. For example, other semantic information is often provided in "documentation" elements in XML Schemas or "description" elements in GML objects. '))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DefaultValue'), ValueType, scope=UnNamedDomainType, documentation=u'The default value for a quantity for which multiple values are allowed. '))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), MetadataType, scope=UnNamedDomainType))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AllowedValues'), CTD_ANON_7, scope=UnNamedDomainType, documentation=u'List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. '))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UOM'), DomainMetadataType, scope=UnNamedDomainType, documentation=u'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. '))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataType'), DomainMetadataType, scope=UnNamedDomainType, documentation=u'Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. '))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NoValues'), CTD_ANON_9, scope=UnNamedDomainType, documentation=u'Specifies that no values are allowed for this parameter or quantity.'))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'), DomainMetadataType, scope=UnNamedDomainType, documentation=u'Definition of the reference system used by this set of values, including the unit of measure whenever applicable (as is normal). In this case, the xlink:href attribute can reference a URN for a well-known reference system, such as for a coordinate reference system (CRS). For example, such a URN could be a CRS identification URN defined in the "ogc" URN namespace. '))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValuesReference'), CTD_ANON_8, scope=UnNamedDomainType, documentation=u'Reference to externally specified list of all the valid values and/or ranges of values for this quantity. (Informative: This element was simplified from the metaDataProperty element in GML 3.0.) '))

UnNamedDomainType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnyValue'), CTD_ANON_2, scope=UnNamedDomainType, documentation=u'Specifies that any value is allowed for this parameter.'))
UnNamedDomainType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValuesReference'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AnyValue'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AllowedValues'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NoValues'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UOM'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataType'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UOM'))),
    ])
    , 5 : pyxb.binding.content.ContentModelState(state=5, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Meaning'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataType'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UOM'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'))),
    ])
    , 6 : pyxb.binding.content.ContentModelState(state=6, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Meaning'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataType'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DefaultValue'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UOM'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=UnNamedDomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
})


DomainType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValuesReference'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AnyValue'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AllowedValues'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NoValues'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UOM'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataType'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UOM'))),
    ])
    , 5 : pyxb.binding.content.ContentModelState(state=5, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Meaning'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataType'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UOM'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'))),
    ])
    , 6 : pyxb.binding.content.ContentModelState(state=6, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Meaning'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataType'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DefaultValue'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UOM'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceSystem'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=DomainType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
})



CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Operation'), CTD_ANON_3, scope=CTD_ANON_5, documentation=u'Metadata for one operation that this server implements. '))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtendedCapabilities'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_5, documentation=u'Individual software vendors and servers can use this element to provide metadata about any additional server abilities. '))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Parameter'), DomainType, scope=CTD_ANON_5, documentation=u'Optional unordered list of parameter valid domains that each apply to one or more operations which this server interface implements. The list of required and optional parameter domain limitations shall be specified in the Implementation Specification for this service. '))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Constraint'), DomainType, scope=CTD_ANON_5, documentation=u'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this server. The list of required and optional constraints shall be specified in the Implementation Specification for this service. '))
CTD_ANON_5._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Operation'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Operation'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Parameter'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Operation'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Constraint'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtendedCapabilities'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Parameter'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Constraint'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtendedCapabilities'))),
    ])
    , 5 : pyxb.binding.content.ContentModelState(state=5, is_final=True, transitions=[
    ])
})



ContentsBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatasetDescriptionSummary'), DatasetDescriptionSummaryBaseType, scope=ContentsBaseType))

ContentsBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OtherSource'), MetadataType, scope=ContentsBaseType, documentation=u'Reference to a source of metadata describing  coverage offerings available from this server. This  parameter can reference a catalogue server from which dataset metadata is available. This ability is expected to be used by servers with thousands or millions of datasets, for which searching a catalogue is more feasible than fetching a long Capabilities XML document. When no DatasetDescriptionSummaries are included, and one or more catalogue servers are referenced, this set of catalogues shall contain current metadata summaries for all the datasets currently available from this OWS server, with the metadata for each such dataset referencing this OWS server. '))
ContentsBaseType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ContentsBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatasetDescriptionSummary'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ContentsBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OtherSource'))),
    ])
})



BasicIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), MetadataType, scope=BasicIdentificationType))

BasicIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), CodeType, scope=BasicIdentificationType, documentation=u'Unique identifier or name of this dataset. '))
BasicIdentificationType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keywords'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=BasicIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
})



ReferenceGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AbstractReferenceBase'), AbstractReferenceBaseType, abstract=pyxb.binding.datatypes.boolean(1), scope=ReferenceGroupType))
ReferenceGroupType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keywords'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AbstractReferenceBase'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AbstractReferenceBase'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ReferenceGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AbstractReferenceBase'))),
    ])
})



AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Country'), pyxb.binding.datatypes.string, scope=AddressType, documentation=u'Country of the physical address. '))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DeliveryPoint'), pyxb.binding.datatypes.string, scope=AddressType, documentation=u'Address line for the location. '))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostalCode'), pyxb.binding.datatypes.string, scope=AddressType, documentation=u'ZIP or other postal code. '))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdministrativeArea'), pyxb.binding.datatypes.string, scope=AddressType, documentation=u'State or province of the location. '))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ElectronicMailAddress'), pyxb.binding.datatypes.string, scope=AddressType, documentation=u'Address of the electronic mailbox of the responsible organization or individual. '))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'City'), pyxb.binding.datatypes.string, scope=AddressType, documentation=u'City of the location. '))
AddressType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Country'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ElectronicMailAddress'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PostalCode'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DeliveryPoint'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdministrativeArea'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'City'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ElectronicMailAddress'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Country'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PostalCode'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ElectronicMailAddress'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdministrativeArea'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Country'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ElectronicMailAddress'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PostalCode'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Country'))),
    ])
    , 5 : pyxb.binding.content.ContentModelState(state=5, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ElectronicMailAddress'))),
    ])
})



IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AvailableCRS'), pyxb.binding.datatypes.anyURI, scope=IdentificationType))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), BoundingBoxType, scope=IdentificationType))

IdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'), MimeType, scope=IdentificationType, documentation=u'Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. '))
IdentificationType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AvailableCRS'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keywords'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AvailableCRS'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AvailableCRS'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=IdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'))),
    ])
})



CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Post'), RequestMethodType, scope=CTD_ANON_6, documentation=u'Connect point URL and any constraints for the HTTP "Post" request method for this operation request. '))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Get'), RequestMethodType, scope=CTD_ANON_6, documentation=u'Connect point URL prefix and any constraints for the HTTP "Get" request method for this operation request. '))
CTD_ANON_6._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Post'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Get'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Post'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Get'))),
    ])
})



ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndividualName'), pyxb.binding.datatypes.string, scope=ResponsiblePartySubsetType, documentation=u'Name of the responsible person: surname, given name, title separated by a delimiter. '))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionName'), pyxb.binding.datatypes.string, scope=ResponsiblePartySubsetType, documentation=u'Role or position of the responsible person. '))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Role'), CodeType, scope=ResponsiblePartySubsetType, documentation=u'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. '))

ResponsiblePartySubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'), ContactType, scope=ResponsiblePartySubsetType, documentation=u'Address of the responsible party. '))
ResponsiblePartySubsetType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndividualName'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionName'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionName'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
    ])
    , 5 : pyxb.binding.content.ContentModelState(state=5, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartySubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
    ])
})



ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HoursOfService'), pyxb.binding.datatypes.string, scope=ContactType, documentation=u'Time period (including time zone) when individuals can contact the organization or individual. '))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), OnlineResourceType, scope=ContactType, documentation=u'On-line information that can be used to contact the individual or organization. OWS specifics: The xlink:href attribute in the xlink:simpleLink attribute group shall be used to reference this resource. Whenever practical, the xlink:href attribute with type anyURI should be a URL from which more contact information can be electronically retrieved. The xlink:title attribute with type "string" can be used to name this set of information. The other attributes in the xlink:simpleLink attribute group should not be used. '))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), AddressType, scope=ContactType, documentation=u'Physical and email address at which the organization or individual may be contacted. '))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Phone'), TelephoneType, scope=ContactType, documentation=u'Telephone numbers at which the organization or individual may be contacted. '))

ContactType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactInstructions'), pyxb.binding.datatypes.string, scope=ContactType, documentation=u'Supplemental instructions on how or when to contact the individual or organization. '))
ContactType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HoursOfService'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInstructions'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Phone'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HoursOfService'))),
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInstructions'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HoursOfService'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInstructions'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInstructions'))),
    ])
    , 5 : pyxb.binding.content.ContentModelState(state=5, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HoursOfService'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=ContactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInstructions'))),
    ])
    , 6 : pyxb.binding.content.ContentModelState(state=6, is_final=True, transitions=[
    ])
})



ManifestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceGroup'), ReferenceGroupType, scope=ManifestType))
ManifestType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keywords'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceGroup'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceGroup'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceGroup'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ManifestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
})



CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Range'), RangeType, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), ValueType, scope=CTD_ANON_7))
CTD_ANON_7._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Range'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Range'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value'))),
    ])
})



AcceptFormatsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'), MimeType, scope=AcceptFormatsType))
AcceptFormatsType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=AcceptFormatsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'))),
    ])
})



CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OperationsMetadata'), CTD_ANON_5, scope=CapabilitiesBaseType, documentation=u'Metadata about the operations and related abilities specified by this service and implemented by this server, including the URLs for operation requests. The basic contents of this section shall be the same for all OWS types, but individual services can add elements and/or change the optionality of optional elements. '))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceProvider'), CTD_ANON_10, scope=CapabilitiesBaseType, documentation=u'Metadata about the organization that provides this specific service instance or server. '))

CapabilitiesBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceIdentification'), CTD_ANON_1, scope=CapabilitiesBaseType, documentation=u'General metadata for this specific server. This XML Schema of this section shall be the same for all OWS. '))
CapabilitiesBaseType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceIdentification'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceProvider'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OperationsMetadata'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceProvider'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OperationsMetadata'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CapabilitiesBaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OperationsMetadata'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
    ])
})



RequestMethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Constraint'), DomainType, scope=RequestMethodType, documentation=u'Optional unordered list of valid domain constraints on non-parameter quantities that each apply to this request method for this operation. If one of these Constraint elements has the same "name" attribute as a Constraint element in the OperationsMetadata or Operation element, this Constraint element shall override the other one for this operation. The list of required and optional constraints for this request method for this operation shall be specified in the Implementation Specification for this service. '))
RequestMethodType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=RequestMethodType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Constraint'))),
    ])
})



ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), CodeType, scope=ReferenceType, documentation=u'Unique identifier or name of this dataset. '))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), MetadataType, scope=ReferenceType))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), LanguageStringType, scope=ReferenceType, documentation=u'Brief narrative description of this resource, normally used for display to a human. '))

ReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), MimeType, scope=ReferenceType, documentation=u'The format of the referenced resource. This element is omitted when the mime type is indicated in the http header of the reference. '))
ReferenceType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format'))),
    ])
})



ExceptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExceptionText'), pyxb.binding.datatypes.string, scope=ExceptionType, documentation=u'Ordered sequence of text strings that describe this specific exception or error. The contents of these strings are left open to definition by each server implementation. A server is strongly encouraged to include at least one ExceptionText value, to provide more information about the detected error than provided by the exceptionCode. When included, multiple ExceptionText values shall provide hierarchical information about one detected error, with the most significant information listed first. '))
ExceptionType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=ExceptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExceptionText'))),
    ])
})



ServiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequestMessage'), pyxb.binding.datatypes.anyType, scope=ServiceReferenceType, documentation=u'The XML-encoded operation request message to be sent to request this input data from another web server using HTTP Post. '))

ServiceReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequestMessageReference'), pyxb.binding.datatypes.anyURI, scope=ServiceReferenceType, documentation=u'Reference to the XML-encoded operation request message to be sent to request this input data from another web server using HTTP Post. The referenced message shall be attached to the same message (using the cid scheme), or be accessible using a URL. '))
ServiceReferenceType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RequestMessage'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RequestMessageReference'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RequestMessageReference'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RequestMessage'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RequestMessage'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RequestMessageReference'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ServiceReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
    ])
})



CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProviderName'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, documentation=u'A unique identifier for the service provider organization. '))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProviderSite'), OnlineResourceType, scope=CTD_ANON_10, documentation=u'Reference to the most relevant web site of the service provider. '))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceContact'), ResponsiblePartySubsetType, scope=CTD_ANON_10, documentation=u'Information for contacting the service provider. The OnlineResource element within this ServiceContact element should not be used to reference a web site of the service provider. '))
CTD_ANON_10._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProviderName'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProviderSite'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceContact'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceContact'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
    ])
})



TelephoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Voice'), pyxb.binding.datatypes.string, scope=TelephoneType, documentation=u'Telephone number by which individuals can speak to the responsible organization or individual. '))

TelephoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Facsimile'), pyxb.binding.datatypes.string, scope=TelephoneType, documentation=u'Telephone number of a facsimile machine for the responsible\norganization or individual. '))
TelephoneType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=TelephoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Voice'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=TelephoneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Facsimile'))),
    ])
})



GetResourceByIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ResourceID'), pyxb.binding.datatypes.anyURI, scope=GetResourceByIdType, documentation=u'Unordered list of zero or more resource identifiers. These identifiers can be listed in the Contents section of the service metadata (Capabilities) document. For more information on this parameter, see Subclause 9.4.2.1 of the OWS Common specification. '))

GetResourceByIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'), MimeType, scope=GetResourceByIdType, documentation=u'Reference to a format in which this data can be encoded and transferred. More specific parameter names should be used by specific OWS specifications wherever applicable. More than one such parameter can be included for different purposes. '))
GetResourceByIdType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=GetResourceByIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OutputFormat'))),
        pyxb.binding.content.ContentModelTransition(next_state=1, element_use=GetResourceByIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ResourceID'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
    ])
})



CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HTTP'), CTD_ANON_6, scope=CTD_ANON_11, documentation=u'Connect point URLs for the HTTP Distributed Computing Platform (DCP). Normally, only one Get and/or one Post is included in this element. More than one Get and/or Post is allowed to support including alternative URLs for uses such as load balancing or backup. '))
CTD_ANON_11._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HTTP'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
    ])
})



AcceptVersionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), VersionType, scope=AcceptVersionsType))
AcceptVersionsType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=AcceptVersionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=True, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=AcceptVersionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version'))),
    ])
})



ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'), ContactType, scope=ResponsiblePartyType, documentation=u'Address of the responsible party. '))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrganisationName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation=u'Name of the responsible organization. '))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Role'), CodeType, scope=ResponsiblePartyType, documentation=u'Function performed by the responsible party. Possible values of this Role shall include the values and the meanings listed in Subclause B.5.5 of ISO 19115:2003. '))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PositionName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation=u'Role or position of the responsible person. '))

ResponsiblePartyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndividualName'), pyxb.binding.datatypes.string, scope=ResponsiblePartyType, documentation=u'Name of the responsible person: surname, given name, title separated by a delimiter. '))
ResponsiblePartyType._ContentModel = pyxb.binding.content.ContentModel(state_map = {
      1 : pyxb.binding.content.ContentModelState(state=1, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OrganisationName'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionName'))),
        pyxb.binding.content.ContentModelTransition(next_state=6, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndividualName'))),
    ])
    , 2 : pyxb.binding.content.ContentModelState(state=2, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
    ])
    , 3 : pyxb.binding.content.ContentModelState(state=3, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
    ])
    , 4 : pyxb.binding.content.ContentModelState(state=4, is_final=True, transitions=[
    ])
    , 5 : pyxb.binding.content.ContentModelState(state=5, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionName'))),
    ])
    , 6 : pyxb.binding.content.ContentModelState(state=6, is_final=False, transitions=[
        pyxb.binding.content.ContentModelTransition(next_state=5, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OrganisationName'))),
        pyxb.binding.content.ContentModelTransition(next_state=4, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Role'))),
        pyxb.binding.content.ContentModelTransition(next_state=3, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInfo'))),
        pyxb.binding.content.ContentModelTransition(next_state=2, element_use=ResponsiblePartyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PositionName'))),
    ])
})

Reference._setSubstitutionGroup(AbstractReferenceBase)

SupportedCRS._setSubstitutionGroup(AvailableCRS)

ServiceReference._setSubstitutionGroup(Reference)

WGS84BoundingBox._setSubstitutionGroup(BoundingBox)
