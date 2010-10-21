# ./OGC_WPS_1_0_0.py
# PyXB bindings for NamespaceModule
# NSM:76ad5258aae86a5ac0f3bea350c0ef82976f8647
# Generated 2010-10-21 16:22:53.559131 by PyXB version 1.1.2
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
import _ows
import pyxb.binding.xml_

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/wps/1.0.0', create_if_missing=True)
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
class STD_ANON (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.integer(0L))
STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.integer(99L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive,
   STD_ANON._CF_maxInclusive)

# Atomic SimpleTypeDefinition
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.GET = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'GET')
STD_ANON_.POST = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'POST')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Complex type ProcessFailedType with content type ELEMENT_ONLY
class ProcessFailedType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProcessFailedType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}ExceptionReport uses Python identifier ExceptionReport
    __ExceptionReport = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'ExceptionReport'), 'ExceptionReport', '__httpwww_opengis_netwps1_0_0_ProcessFailedType_httpwww_opengis_netows1_1ExceptionReport', False)

    
    ExceptionReport = property(__ExceptionReport.value, __ExceptionReport.set, None, u'Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. ')


    _ElementMap = {
        __ExceptionReport.name() : __ExceptionReport
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ProcessFailedType', ProcessFailedType)


# Complex type StatusType with content type ELEMENT_ONLY
class StatusType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StatusType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessAccepted uses Python identifier ProcessAccepted
    __ProcessAccepted = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessAccepted'), 'ProcessAccepted', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessAccepted', False)

    
    ProcessAccepted = property(__ProcessAccepted.value, __ProcessAccepted.set, None, u'Indicates that this process has been accepted by the server, but is in a queue and has not yet started to execute. The contents of this human-readable text string is left open to definition by each server implementation, but is expected to include any messages the server may wish to let the clients know. Such information could include how long the queue is, or any warning conditions that may have been encountered. The client may display this text to a human user. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessStarted uses Python identifier ProcessStarted
    __ProcessStarted = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessStarted'), 'ProcessStarted', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessStarted', False)

    
    ProcessStarted = property(__ProcessStarted.value, __ProcessStarted.set, None, u'Indicates that this process has been accepted by the server, and processing has begun. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessFailed uses Python identifier ProcessFailed
    __ProcessFailed = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessFailed'), 'ProcessFailed', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessFailed', False)

    
    ProcessFailed = property(__ProcessFailed.value, __ProcessFailed.set, None, u'Indicates that execution of this process has failed, and includes error information. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessSucceeded uses Python identifier ProcessSucceeded
    __ProcessSucceeded = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessSucceeded'), 'ProcessSucceeded', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessSucceeded', False)

    
    ProcessSucceeded = property(__ProcessSucceeded.value, __ProcessSucceeded.set, None, u'Indicates that this process has successfully completed execution. The contents of this human-readable text string is left open to definition by each server, but is expected to include any messages the server may wish to let the clients know, such as how long the process took to execute, or any warning conditions that may have been encountered. The client may display this text string to a human user. The client should make use of the presence of this element to trigger automated or manual access to the results of the process. If manual access is intended, the client should use the presence of this element to present the results as downloadable links to the user. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessPaused uses Python identifier ProcessPaused
    __ProcessPaused = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessPaused'), 'ProcessPaused', '__httpwww_opengis_netwps1_0_0_StatusType_httpwww_opengis_netwps1_0_0ProcessPaused', False)

    
    ProcessPaused = property(__ProcessPaused.value, __ProcessPaused.set, None, u'Indicates that this process has been  accepted by the server, and processing has started but subsequently been paused by the server.')

    
    # Attribute creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'creationTime'), 'creationTime', '__httpwww_opengis_netwps1_0_0_StatusType_creationTime', pyxb.binding.datatypes.dateTime, required=True)
    
    creationTime = property(__creationTime.value, __creationTime.set, None, u'The time (UTC) that the process finished.  If the process is still executing or awaiting execution, this element shall contain the creation time of this document.')


    _ElementMap = {
        __ProcessAccepted.name() : __ProcessAccepted,
        __ProcessStarted.name() : __ProcessStarted,
        __ProcessFailed.name() : __ProcessFailed,
        __ProcessSucceeded.name() : __ProcessSucceeded,
        __ProcessPaused.name() : __ProcessPaused
    }
    _AttributeMap = {
        __creationTime.name() : __creationTime
    }
Namespace.addCategoryObject('typeBinding', u'StatusType', StatusType)


# Complex type CTD_ANON with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpwww_opengis_netwps1_0_0_CTD_ANON_value', pyxb.binding.datatypes.string, required=True)
    
    value_ = property(__value.value, __value.set, None, u'Value portion of the Key-Value pair in the HTTP request header.')

    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'key'), 'key', '__httpwww_opengis_netwps1_0_0_CTD_ANON_key', pyxb.binding.datatypes.string, required=True)
    
    key = property(__key.value, __key.set, None, u'Key portion of the Key-Value pair in the HTTP request header.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __value.name() : __value,
        __key.name() : __key
    }



# Complex type CTD_ANON_ with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Process uses Python identifier Process
    __Process = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Process'), 'Process', '__httpwww_opengis_netwps1_0_0_CTD_ANON__httpwww_opengis_netwps1_0_0Process', True)

    
    Process = property(__Process.value, __Process.set, None, u'Unordered list of one or more brief descriptions of all the processes offered by this WPS server. ')


    _ElementMap = {
        __Process.name() : __Process
    }
    _AttributeMap = {
        
    }



# Complex type DataType with content type ELEMENT_ONLY
class DataType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DataType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}ComplexData uses Python identifier ComplexData
    __ComplexData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComplexData'), 'ComplexData', '__httpwww_opengis_netwps1_0_0_DataType_httpwww_opengis_netwps1_0_0ComplexData', False)

    
    ComplexData = property(__ComplexData.value, __ComplexData.set, None, u'Identifies this input or output value as a complex data structure encoded in XML (e.g., using GML), and provides that complex data structure. For an input, this element may be used by a client for any process input coded as ComplexData in the ProcessDescription. For an output, this element shall be used by a server when "store" in the Execute request is "false". ')

    
    # Element {http://www.opengis.net/wps/1.0.0}LiteralData uses Python identifier LiteralData
    __LiteralData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LiteralData'), 'LiteralData', '__httpwww_opengis_netwps1_0_0_DataType_httpwww_opengis_netwps1_0_0LiteralData', False)

    
    LiteralData = property(__LiteralData.value, __LiteralData.set, None, u'Identifies this input or output data as literal data of a simple quantity (e.g., one number), and provides that data. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}BoundingBoxData uses Python identifier BoundingBoxData
    __BoundingBoxData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BoundingBoxData'), 'BoundingBoxData', '__httpwww_opengis_netwps1_0_0_DataType_httpwww_opengis_netwps1_0_0BoundingBoxData', False)

    
    BoundingBoxData = property(__BoundingBoxData.value, __BoundingBoxData.set, None, u'Identifies this input or output data as an ows:BoundingBox data structure, and provides that ows:BoundingBox data. ')


    _ElementMap = {
        __ComplexData.name() : __ComplexData,
        __LiteralData.name() : __LiteralData,
        __BoundingBoxData.name() : __BoundingBoxData
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DataType', DataType)


# Complex type DescriptionType with content type ELEMENT_ONLY
class DescriptionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DescriptionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Metadata'), 'Metadata', '__httpwww_opengis_netwps1_0_0_DescriptionType_httpwww_opengis_netows1_1Metadata', True)

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_DescriptionType_httpwww_opengis_netows1_1Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract'), 'Abstract', '__httpwww_opengis_netwps1_0_0_DescriptionType_httpwww_opengis_netows1_1Abstract', False)

    
    Abstract = property(__Abstract.value, __Abstract.set, None, u'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title'), 'Title', '__httpwww_opengis_netwps1_0_0_DescriptionType_httpwww_opengis_netows1_1Title', False)

    
    Title = property(__Title.value, __Title.set, None, u'Title of this resource, normally used for display to a human. ')


    _ElementMap = {
        __Metadata.name() : __Metadata,
        __Identifier.name() : __Identifier,
        __Abstract.name() : __Abstract,
        __Title.name() : __Title
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DescriptionType', DescriptionType)


# Complex type OutputDataType with content type ELEMENT_ONLY
class OutputDataType (DescriptionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OutputDataType')
    # Base type is DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element {http://www.opengis.net/wps/1.0.0}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reference'), 'Reference', '__httpwww_opengis_netwps1_0_0_OutputDataType_httpwww_opengis_netwps1_0_0Reference', False)

    
    Reference = property(__Reference.value, __Reference.set, None, u'Identifies this output as a web accessible resource, and references that resource.  This element shall only be used for complex data. This element shall be used by a server when "store" in the Execute request is "true". ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Data'), 'Data', '__httpwww_opengis_netwps1_0_0_OutputDataType_httpwww_opengis_netwps1_0_0Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'Identifies this output value as a data embedded in this response, and includes that data. This element shall be used by a server when "store" in the Execute request is "false". ')

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType

    _ElementMap = DescriptionType._ElementMap.copy()
    _ElementMap.update({
        __Reference.name() : __Reference,
        __Data.name() : __Data
    })
    _AttributeMap = DescriptionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'OutputDataType', OutputDataType)


# Complex type CTD_ANON_2 with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}AcceptVersions uses Python identifier AcceptVersions
    __AcceptVersions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AcceptVersions'), 'AcceptVersions', '__httpwww_opengis_netwps1_0_0_CTD_ANON_2_httpwww_opengis_netwps1_0_0AcceptVersions', False)

    
    AcceptVersions = property(__AcceptVersions.value, __AcceptVersions.set, None, u'When omitted, server shall return latest supported version. ')

    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'language'), 'language', '__httpwww_opengis_netwps1_0_0_CTD_ANON_2_language', pyxb.binding.datatypes.string)
    
    language = property(__language.value, __language.set, None, u'RFC 4646 language code of the human-readable text (e.g. "en-CA").')

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'service'), 'service', '__httpwww_opengis_netwps1_0_0_CTD_ANON_2_service', _ows.ServiceType, fixed=True, unicode_default=u'WPS', required=True)
    
    service = property(__service.value, __service.set, None, u'OGC service type identifier (WPS).')


    _ElementMap = {
        __AcceptVersions.name() : __AcceptVersions
    }
    _AttributeMap = {
        __language.name() : __language,
        __service.name() : __service
    }



# Complex type OutputDefinitionsType with content type ELEMENT_ONLY
class OutputDefinitionsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OutputDefinitionsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Output'), 'Output', '__httpwww_opengis_netwps1_0_0_OutputDefinitionsType_httpwww_opengis_netwps1_0_0Output', True)

    
    Output = property(__Output.value, __Output.set, None, u'Output definition as provided in the execute request ')


    _ElementMap = {
        __Output.name() : __Output
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'OutputDefinitionsType', OutputDefinitionsType)


# Complex type ProcessStartedType with content type SIMPLE
class ProcessStartedType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProcessStartedType')
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute percentCompleted uses Python identifier percentCompleted
    __percentCompleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'percentCompleted'), 'percentCompleted', '__httpwww_opengis_netwps1_0_0_ProcessStartedType_percentCompleted', STD_ANON)
    
    percentCompleted = property(__percentCompleted.value, __percentCompleted.set, None, u'Percentage of process that has been completed, where 0 means the process has just started, and 99 means the process is almost complete.  This value is expected to be accurate to within ten percent.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __percentCompleted.name() : __percentCompleted
    }
Namespace.addCategoryObject('typeBinding', u'ProcessStartedType', ProcessStartedType)


# Complex type OutputReferenceType with content type EMPTY
class OutputReferenceType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OutputReferenceType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mimeType'), 'mimeType', '__httpwww_opengis_netwps1_0_0_OutputReferenceType_mimeType', _ows.MimeType)
    
    mimeType = property(__mimeType.value, __mimeType.set, None, u'The Format of this input or requested for this output (e.g., text/xml). This element shall be omitted when the Format is indicated in the http header of the output. When included, this format shall be one published for this output or input in the Process full description. ')

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwww_opengis_netwps1_0_0_OutputReferenceType_href', pyxb.binding.datatypes.anyURI, required=True)
    
    href = property(__href.value, __href.set, None, u'Reference to a web-accessible resource that is provided by the process as output. This attribute shall contain a URL from which this output can be electronically retrieved. ')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'schema'), 'schema', '__httpwww_opengis_netwps1_0_0_OutputReferenceType_schema', pyxb.binding.datatypes.anyURI)
    
    schema = property(__schema.value, __schema.set, None, u'Web-accessible XML Schema Document that defines the content model of this complex resource (e.g., encoded using GML 2.2 Application Schema).  This reference should be included for XML encoded complex resources to facilitate validation. PS I changed the name of this attribute to be consistent with the ProcessDescription.  The original was giving me validation troubles in XMLSpy. ')

    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'encoding'), 'encoding', '__httpwww_opengis_netwps1_0_0_OutputReferenceType_encoding', pyxb.binding.datatypes.anyURI)
    
    encoding = property(__encoding.value, __encoding.set, None, u'The encoding of this input or requested for this output (e.g., UTF-8). This "encoding" shall be included whenever the encoding required is not the default encoding indicated in the Process full description. When included, this encoding shall be one published for this output or input in the Process full description. ')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __mimeType.name() : __mimeType,
        __href.name() : __href,
        __schema.name() : __schema,
        __encoding.name() : __encoding
    }
Namespace.addCategoryObject('typeBinding', u'OutputReferenceType', OutputReferenceType)


# Complex type DataInputsType with content type ELEMENT_ONLY
class DataInputsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DataInputsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Input'), 'Input', '__httpwww_opengis_netwps1_0_0_DataInputsType_httpwww_opengis_netwps1_0_0Input', True)

    
    Input = property(__Input.value, __Input.set, None, u'Unordered list of one or more inputs to be used by the process, including each of the Inputs needed to execute the process. ')


    _ElementMap = {
        __Input.name() : __Input
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DataInputsType', DataInputsType)


# Complex type LiteralOutputType with content type ELEMENT_ONLY
class LiteralOutputType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LiteralOutputType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element UOMs uses Python identifier UOMs
    __UOMs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'UOMs'), 'UOMs', '__httpwww_opengis_netwps1_0_0_LiteralOutputType_UOMs', False)

    
    UOMs = property(__UOMs.value, __UOMs.set, None, u'List of supported units of measure for this input or output. This element should be included when this literal has a unit of measure (e.g., "meters", without a more complete reference system). Not necessary for a count, which has no units. ')

    
    # Element {http://www.opengis.net/ows/1.1}DataType uses Python identifier DataType
    __DataType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'DataType'), 'DataType', '__httpwww_opengis_netwps1_0_0_LiteralOutputType_httpwww_opengis_netows1_1DataType', False)

    
    DataType = property(__DataType.value, __DataType.set, None, u'Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. ')


    _ElementMap = {
        __UOMs.name() : __UOMs,
        __DataType.name() : __DataType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'LiteralOutputType', LiteralOutputType)


# Complex type LiteralInputType with content type ELEMENT_ONLY
class LiteralInputType (LiteralOutputType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LiteralInputType')
    # Base type is LiteralOutputType
    
    # Element {http://www.opengis.net/ows/1.1}AllowedValues uses Python identifier AllowedValues
    __AllowedValues = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'AllowedValues'), 'AllowedValues', '__httpwww_opengis_netwps1_0_0_LiteralInputType_httpwww_opengis_netows1_1AllowedValues', False)

    
    AllowedValues = property(__AllowedValues.value, __AllowedValues.set, None, u'List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. ')

    
    # Element {http://www.opengis.net/ows/1.1}AnyValue uses Python identifier AnyValue
    __AnyValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'AnyValue'), 'AnyValue', '__httpwww_opengis_netwps1_0_0_LiteralInputType_httpwww_opengis_netows1_1AnyValue', False)

    
    AnyValue = property(__AnyValue.value, __AnyValue.set, None, u'Specifies that any value is allowed for this parameter.')

    
    # Element DefaultValue uses Python identifier DefaultValue
    __DefaultValue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'DefaultValue'), 'DefaultValue', '__httpwww_opengis_netwps1_0_0_LiteralInputType_DefaultValue', False)

    
    DefaultValue = property(__DefaultValue.value, __DefaultValue.set, None, u'Optional default value for this quantity, which should be included when this quantity has a default value.  The DefaultValue shall be understood to be consistent with the unit of measure selected in the Execute request. ')

    
    # Element DataType ({http://www.opengis.net/ows/1.1}DataType) inherited from {http://www.opengis.net/wps/1.0.0}LiteralOutputType
    
    # Element UOMs (UOMs) inherited from {http://www.opengis.net/wps/1.0.0}LiteralOutputType
    
    # Element ValuesReference uses Python identifier ValuesReference
    __ValuesReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ValuesReference'), 'ValuesReference', '__httpwww_opengis_netwps1_0_0_LiteralInputType_ValuesReference', False)

    
    ValuesReference = property(__ValuesReference.value, __ValuesReference.set, None, u'Indicates that there are a finite set of values and ranges allowed for this input, which are specified in the referenced list. ')


    _ElementMap = LiteralOutputType._ElementMap.copy()
    _ElementMap.update({
        __AllowedValues.name() : __AllowedValues,
        __AnyValue.name() : __AnyValue,
        __DefaultValue.name() : __DefaultValue,
        __ValuesReference.name() : __ValuesReference
    })
    _AttributeMap = LiteralOutputType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'LiteralInputType', LiteralInputType)


# Complex type LanguagesType with content type ELEMENT_ONLY
class LanguagesType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LanguagesType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Language uses Python identifier Language
    __Language = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Language'), 'Language', '__httpwww_opengis_netwps1_0_0_LanguagesType_httpwww_opengis_netows1_1Language', True)

    
    Language = property(__Language.value, __Language.set, None, u'Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. ')


    _ElementMap = {
        __Language.name() : __Language
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'LanguagesType', LanguagesType)


# Complex type ResponseBaseType with content type EMPTY
class ResponseBaseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResponseBaseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_opengis_netwps1_0_0_ResponseBaseType_version', _ows.VersionType, fixed=True, unicode_default=u'1.0.0', required=True)
    
    version = property(__version.value, __version.set, None, u'Version of the WPS interface specification implemented by the server (1.0.0)')

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'service'), 'service', '__httpwww_opengis_netwps1_0_0_ResponseBaseType_service', pyxb.binding.datatypes.string, fixed=True, unicode_default=u'WPS', required=True)
    
    service = property(__service.value, __service.set, None, u'Service type identifier (WPS)')

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netwps1_0_0_ResponseBaseType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    
    lang = property(__lang.value, __lang.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __version.name() : __version,
        __service.name() : __service,
        __lang.name() : __lang
    }
Namespace.addCategoryObject('typeBinding', u'ResponseBaseType', ResponseBaseType)


# Complex type CTD_ANON_3 with content type ELEMENT_ONLY
class CTD_ANON_3 (ResponseBaseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is ResponseBaseType
    
    # Element ProcessDescription uses Python identifier ProcessDescription
    __ProcessDescription = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ProcessDescription'), 'ProcessDescription', '__httpwww_opengis_netwps1_0_0_CTD_ANON_3_ProcessDescription', True)

    
    ProcessDescription = property(__ProcessDescription.value, __ProcessDescription.set, None, u'Ordered list of one or more full Process descriptions, listed in the order in which they were requested in the DescribeProcess operation request. ')

    
    # Attribute version inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute service inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute lang inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType

    _ElementMap = ResponseBaseType._ElementMap.copy()
    _ElementMap.update({
        __ProcessDescription.name() : __ProcessDescription
    })
    _AttributeMap = ResponseBaseType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type SupportedCRSsType with content type ELEMENT_ONLY
class SupportedCRSsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SupportedCRSsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Supported uses Python identifier Supported
    __Supported = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Supported'), 'Supported', '__httpwww_opengis_netwps1_0_0_SupportedCRSsType_Supported', False)

    
    Supported = property(__Supported.value, __Supported.set, None, u'Unordered list of references to all of the CRSs supported for this Input/Output. The default CRS shall be included in this list.')

    
    # Element Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Default'), 'Default', '__httpwww_opengis_netwps1_0_0_SupportedCRSsType_Default', False)

    
    Default = property(__Default.value, __Default.set, None, u'Identifies the default CRS that will be used unless the Execute operation request specifies another supported CRS. ')


    _ElementMap = {
        __Supported.name() : __Supported,
        __Default.name() : __Default
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SupportedCRSsType', SupportedCRSsType)


# Complex type CTD_ANON_4 with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'href'), 'href', '__httpwww_opengis_netwps1_0_0_CTD_ANON_4_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI, required=True)
    
    href = property(__href.value, __href.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __href.name() : __href
    }



# Complex type ComplexDataCombinationType with content type ELEMENT_ONLY
class ComplexDataCombinationType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComplexDataCombinationType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Format'), 'Format', '__httpwww_opengis_netwps1_0_0_ComplexDataCombinationType_Format', False)

    
    Format = property(__Format.value, __Format.set, None, u'The default combination of MimeType/Encoding/Schema supported for this Input/Output. ')


    _ElementMap = {
        __Format.name() : __Format
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ComplexDataCombinationType', ComplexDataCombinationType)


# Complex type UOMsType with content type ELEMENT_ONLY
class UOMsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UOMsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}UOM uses Python identifier UOM
    __UOM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'UOM'), 'UOM', '__httpwww_opengis_netwps1_0_0_UOMsType_httpwww_opengis_netows1_1UOM', True)

    
    UOM = property(__UOM.value, __UOM.set, None, u'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ')


    _ElementMap = {
        __UOM.name() : __UOM
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'UOMsType', UOMsType)


# Complex type OutputDefinitionType with content type ELEMENT_ONLY
class OutputDefinitionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OutputDefinitionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_httpwww_opengis_netows1_1Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'Unique identifier or name of this dataset. ')

    
    # Attribute mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mimeType'), 'mimeType', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_mimeType', _ows.MimeType)
    
    mimeType = property(__mimeType.value, __mimeType.set, None, u'The Format of this input or requested for this output (e.g., text/xml). This element shall be omitted when the Format is indicated in the http header of the output. When included, this format shall be one published for this output or input in the Process full description. ')

    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'encoding'), 'encoding', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_encoding', pyxb.binding.datatypes.anyURI)
    
    encoding = property(__encoding.value, __encoding.set, None, u'The encoding of this input or requested for this output (e.g., UTF-8). This "encoding" shall be included whenever the encoding required is not the default encoding indicated in the Process full description. When included, this encoding shall be one published for this output or input in the Process full description. ')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'schema'), 'schema', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_schema', pyxb.binding.datatypes.anyURI)
    
    schema = property(__schema.value, __schema.set, None, u'Web-accessible XML Schema Document that defines the content model of this complex resource (e.g., encoded using GML 2.2 Application Schema).  This reference should be included for XML encoded complex resources to facilitate validation. PS I changed the name of this attribute to be consistent with the ProcessDescription.  The original was giving me validation troubles in XMLSpy. ')

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_opengis_netwps1_0_0_OutputDefinitionType_uom', pyxb.binding.datatypes.anyURI)
    
    uom = property(__uom.value, __uom.set, None, u'Reference to the unit of measure (if any) requested for this output. A uom can be referenced when a client wants to specify one of the units of measure supported for this output. This uom shall be a unit of measure referenced for this output of this process in the Process full description. ')


    _ElementMap = {
        __Identifier.name() : __Identifier
    }
    _AttributeMap = {
        __mimeType.name() : __mimeType,
        __encoding.name() : __encoding,
        __schema.name() : __schema,
        __uom.name() : __uom
    }
Namespace.addCategoryObject('typeBinding', u'OutputDefinitionType', OutputDefinitionType)


# Complex type ValuesReferenceType with content type EMPTY
class ValuesReferenceType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValuesReferenceType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.opengis.net/ows/1.1}reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'reference'), 'reference', '__httpwww_opengis_netwps1_0_0_ValuesReferenceType_httpwww_opengis_netows1_1reference', pyxb.binding.datatypes.anyURI)
    
    reference = property(__reference.value, __reference.set, None, u'Reference to data or metadata recorded elsewhere, either external to this XML document or within it. Whenever practical, this attribute should be a URL from which this metadata can be electronically retrieved. Alternately, this attribute can reference a URN for well-known metadata. For example, such a URN could be a URN defined in the "ogc" URN namespace. ')

    
    # Attribute valuesForm uses Python identifier valuesForm
    __valuesForm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'valuesForm'), 'valuesForm', '__httpwww_opengis_netwps1_0_0_ValuesReferenceType_valuesForm', pyxb.binding.datatypes.anyURI)
    
    valuesForm = property(__valuesForm.value, __valuesForm.set, None, u'Reference to a description of the mimetype, encoding, and schema used for this set of values and ranges.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __reference.name() : __reference,
        __valuesForm.name() : __valuesForm
    }
Namespace.addCategoryObject('typeBinding', u'ValuesReferenceType', ValuesReferenceType)


# Complex type ComplexDataCombinationsType with content type ELEMENT_ONLY
class ComplexDataCombinationsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComplexDataCombinationsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Format'), 'Format', '__httpwww_opengis_netwps1_0_0_ComplexDataCombinationsType_Format', True)

    
    Format = property(__Format.value, __Format.set, None, u'A valid combination of MimeType/Encoding/Schema supported for this Input/Output. ')


    _ElementMap = {
        __Format.name() : __Format
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ComplexDataCombinationsType', ComplexDataCombinationsType)


# Complex type InputReferenceType with content type ELEMENT_ONLY
class InputReferenceType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InputReferenceType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Body'), 'Body', '__httpwww_opengis_netwps1_0_0_InputReferenceType_httpwww_opengis_netwps1_0_0Body', False)

    
    Body = property(__Body.value, __Body.set, None, u'The contents of this element to be used as the body of the HTTP request message to be sent to the service identified in ../Reference/@href.  For example, it could be an XML encoded WFS request using HTTP POST')

    
    # Element {http://www.opengis.net/wps/1.0.0}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Header'), 'Header', '__httpwww_opengis_netwps1_0_0_InputReferenceType_httpwww_opengis_netwps1_0_0Header', True)

    
    Header = property(__Header.value, __Header.set, None, u'Extra HTTP request headers needed by the service identified in ../Reference/@href.  For example, an HTTP SOAP request requires a SOAPAction header.  This permits the creation of a complete and valid POST request.')

    
    # Element {http://www.opengis.net/wps/1.0.0}BodyReference uses Python identifier BodyReference
    __BodyReference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BodyReference'), 'BodyReference', '__httpwww_opengis_netwps1_0_0_InputReferenceType_httpwww_opengis_netwps1_0_0BodyReference', False)

    
    BodyReference = property(__BodyReference.value, __BodyReference.set, None, u'Reference to a remote document to be used as the body of the an HTTP POST request message to the service identified in ../Reference/@href.')

    
    # Attribute mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mimeType'), 'mimeType', '__httpwww_opengis_netwps1_0_0_InputReferenceType_mimeType', _ows.MimeType)
    
    mimeType = property(__mimeType.value, __mimeType.set, None, u'The Format of this input or requested for this output (e.g., text/xml). This element shall be omitted when the Format is indicated in the http header of the output. When included, this format shall be one published for this output or input in the Process full description. ')

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'href'), 'href', '__httpwww_opengis_netwps1_0_0_InputReferenceType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI, required=True)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute method uses Python identifier method
    __method = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'method'), 'method', '__httpwww_opengis_netwps1_0_0_InputReferenceType_method', STD_ANON_, unicode_default=u'GET')
    
    method = property(__method.value, __method.set, None, u'Identifies the HTTP method.  Allows a choice of GET or POST.  Default is GET.')

    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'encoding'), 'encoding', '__httpwww_opengis_netwps1_0_0_InputReferenceType_encoding', pyxb.binding.datatypes.anyURI)
    
    encoding = property(__encoding.value, __encoding.set, None, u'The encoding of this input or requested for this output (e.g., UTF-8). This "encoding" shall be included whenever the encoding required is not the default encoding indicated in the Process full description. When included, this encoding shall be one published for this output or input in the Process full description. ')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'schema'), 'schema', '__httpwww_opengis_netwps1_0_0_InputReferenceType_schema', pyxb.binding.datatypes.anyURI)
    
    schema = property(__schema.value, __schema.set, None, u'Web-accessible XML Schema Document that defines the content model of this complex resource (e.g., encoded using GML 2.2 Application Schema).  This reference should be included for XML encoded complex resources to facilitate validation. PS I changed the name of this attribute to be consistent with the ProcessDescription.  The original was giving me validation troubles in XMLSpy. ')


    _ElementMap = {
        __Body.name() : __Body,
        __Header.name() : __Header,
        __BodyReference.name() : __BodyReference
    }
    _AttributeMap = {
        __mimeType.name() : __mimeType,
        __href.name() : __href,
        __method.name() : __method,
        __encoding.name() : __encoding,
        __schema.name() : __schema
    }
Namespace.addCategoryObject('typeBinding', u'InputReferenceType', InputReferenceType)


# Complex type DocumentOutputDefinitionType with content type ELEMENT_ONLY
class DocumentOutputDefinitionType (OutputDefinitionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DocumentOutputDefinitionType')
    # Base type is OutputDefinitionType
    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract'), 'Abstract', '__httpwww_opengis_netwps1_0_0_DocumentOutputDefinitionType_httpwww_opengis_netows1_1Abstract', False)

    
    Abstract = property(__Abstract.value, __Abstract.set, None, u'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title'), 'Title', '__httpwww_opengis_netwps1_0_0_DocumentOutputDefinitionType_httpwww_opengis_netows1_1Title', False)

    
    Title = property(__Title.value, __Title.set, None, u'Title of this resource, normally used for display to a human. ')

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    
    # Attribute mimeType inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    
    # Attribute encoding inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    
    # Attribute asReference uses Python identifier asReference
    __asReference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'asReference'), 'asReference', '__httpwww_opengis_netwps1_0_0_DocumentOutputDefinitionType_asReference', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    asReference = property(__asReference.value, __asReference.set, None, u'Specifies if this output should be stored by the process as a web-accessible resource. If asReference is "true", the server shall store this output so that the client can retrieve it as required. If store is "false", all the output shall be encoded in the Execute operation response document. This parameter only applies to ComplexData outputs.  This parameter shall not be included unless the corresponding "storeSupported" parameter is included and is "true" in the ProcessDescription for this process. ')

    
    # Attribute schema inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType
    
    # Attribute uom inherited from {http://www.opengis.net/wps/1.0.0}OutputDefinitionType

    _ElementMap = OutputDefinitionType._ElementMap.copy()
    _ElementMap.update({
        __Abstract.name() : __Abstract,
        __Title.name() : __Title
    })
    _AttributeMap = OutputDefinitionType._AttributeMap.copy()
    _AttributeMap.update({
        __asReference.name() : __asReference
    })
Namespace.addCategoryObject('typeBinding', u'DocumentOutputDefinitionType', DocumentOutputDefinitionType)


# Complex type CTD_ANON_5 with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Supported uses Python identifier Supported
    __Supported = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Supported'), 'Supported', '__httpwww_opengis_netwps1_0_0_CTD_ANON_5_httpwww_opengis_netwps1_0_0Supported', False)

    
    Supported = property(__Supported.value, __Supported.set, None, u'Unordered list of references to all of the languages supported by this service. The default language shall be included in this list.')

    
    # Element {http://www.opengis.net/wps/1.0.0}Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Default'), 'Default', '__httpwww_opengis_netwps1_0_0_CTD_ANON_5_httpwww_opengis_netwps1_0_0Default', False)

    
    Default = property(__Default.value, __Default.set, None, u'Identifies the default language that will be used unless the operation request specifies another supported language. ')


    _ElementMap = {
        __Supported.name() : __Supported,
        __Default.name() : __Default
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_6 with content type ELEMENT_ONLY
class CTD_ANON_6 (ResponseBaseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is ResponseBaseType
    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessOutputs uses Python identifier ProcessOutputs
    __ProcessOutputs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessOutputs'), 'ProcessOutputs', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_httpwww_opengis_netwps1_0_0ProcessOutputs', False)

    
    ProcessOutputs = property(__ProcessOutputs.value, __ProcessOutputs.set, None, u'List of values of the Process output parameters. Normally there would be at least one output when the process has completed successfully. If the process has not finished executing, the implementer can choose to include whatever final results are ready at the time the Execute response is provided. If the reference locations of outputs are known in advance, these URLs may be provided before they are populated. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Process uses Python identifier Process
    __Process = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Process'), 'Process', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_httpwww_opengis_netwps1_0_0Process', False)

    
    Process = property(__Process.value, __Process.set, None, u'Process description from the ProcessOfferings section of the GetCapabilities response. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Status'), 'Status', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_httpwww_opengis_netwps1_0_0Status', False)

    
    Status = property(__Status.value, __Status.set, None, u'Execution status of this process. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}OutputDefinitions uses Python identifier OutputDefinitions
    __OutputDefinitions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OutputDefinitions'), 'OutputDefinitions', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_httpwww_opengis_netwps1_0_0OutputDefinitions', False)

    
    OutputDefinitions = property(__OutputDefinitions.value, __OutputDefinitions.set, None, u'Complete list of Output data types that were requested as part of the Execute request. This element shall be omitted unless the lineage attribute of the execute request is set to "true".')

    
    # Element {http://www.opengis.net/wps/1.0.0}DataInputs uses Python identifier DataInputs
    __DataInputs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataInputs'), 'DataInputs', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_httpwww_opengis_netwps1_0_0DataInputs', False)

    
    DataInputs = property(__DataInputs.value, __DataInputs.set, None, u'Inputs that were provided as part of the execute request. This element shall be omitted unless the lineage attribute of the execute request is set to "true".')

    
    # Attribute lang inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute version inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute serviceInstance uses Python identifier serviceInstance
    __serviceInstance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'serviceInstance'), 'serviceInstance', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_serviceInstance', pyxb.binding.datatypes.anyURI, required=True)
    
    serviceInstance = property(__serviceInstance.value, __serviceInstance.set, None, u'This attribute shall contain the GetCapabilities URL of the WPS service which was invoked')

    
    # Attribute service inherited from {http://www.opengis.net/wps/1.0.0}ResponseBaseType
    
    # Attribute statusLocation uses Python identifier statusLocation
    __statusLocation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'statusLocation'), 'statusLocation', '__httpwww_opengis_netwps1_0_0_CTD_ANON_6_statusLocation', pyxb.binding.datatypes.anyURI)
    
    statusLocation = property(__statusLocation.value, __statusLocation.set, None, u'The URL referencing the location from which the ExecuteResponse can be retrieved. If "status" is "true" in the Execute request, the ExecuteResponse should also be found here as soon as the process returns the initial response to the client. It should persist at this location as long as the outputs are accessible from the server. The outputs may be stored for as long as the implementer of the server decides. If the process takes a long time, this URL can be repopulated on an ongoing basis in order to keep the client updated on progress. Before the process has succeeded, the ExecuteResponse contains information about the status of the process, including whether or not processing has started, and the percentage completed. It may also optionally contain the inputs and any ProcessStartedType interim results. When the process has succeeded, the ExecuteResponse found at this URL shall contain the output values or references to them. ')


    _ElementMap = ResponseBaseType._ElementMap.copy()
    _ElementMap.update({
        __ProcessOutputs.name() : __ProcessOutputs,
        __Process.name() : __Process,
        __Status.name() : __Status,
        __OutputDefinitions.name() : __OutputDefinitions,
        __DataInputs.name() : __DataInputs
    })
    _AttributeMap = ResponseBaseType._AttributeMap.copy()
    _AttributeMap.update({
        __serviceInstance.name() : __serviceInstance,
        __statusLocation.name() : __statusLocation
    })



# Complex type RequestBaseType with content type EMPTY
class RequestBaseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RequestBaseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_opengis_netwps1_0_0_RequestBaseType_version', _ows.VersionType, fixed=True, unicode_default=u'1.0.0', required=True)
    
    version = property(__version.value, __version.set, None, u'Version of the WPS interface specification implemented by the server (1.0.0)')

    
    # Attribute language uses Python identifier language
    __language = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'language'), 'language', '__httpwww_opengis_netwps1_0_0_RequestBaseType_language', pyxb.binding.datatypes.string)
    
    language = property(__language.value, __language.set, None, u'RFC 4646 language code of the human-readable text (e.g. "en-CA").')

    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'service'), 'service', '__httpwww_opengis_netwps1_0_0_RequestBaseType_service', pyxb.binding.datatypes.string, fixed=True, unicode_default=u'WPS', required=True)
    
    service = property(__service.value, __service.set, None, u'Service type identifier (WPS)')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __version.name() : __version,
        __language.name() : __language,
        __service.name() : __service
    }
Namespace.addCategoryObject('typeBinding', u'RequestBaseType', RequestBaseType)


# Complex type CTD_ANON_7 with content type ELEMENT_ONLY
class CTD_ANON_7 (RequestBaseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_CTD_ANON_7_httpwww_opengis_netows1_1Identifier', True)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'Unique identifier or name of this dataset. ')

    
    # Attribute version inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    
    # Attribute service inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    
    # Attribute language inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType

    _ElementMap = RequestBaseType._ElementMap.copy()
    _ElementMap.update({
        __Identifier.name() : __Identifier
    })
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type InputDescriptionType with content type ELEMENT_ONLY
class InputDescriptionType (DescriptionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InputDescriptionType')
    # Base type is DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element BoundingBoxData uses Python identifier BoundingBoxData
    __BoundingBoxData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'BoundingBoxData'), 'BoundingBoxData', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_BoundingBoxData', False)

    
    BoundingBoxData = property(__BoundingBoxData.value, __BoundingBoxData.set, None, u'Indicates that this Input shall be a BoundingBox data structure that is embedded in the execute request, and provides a list of the Coordinate Reference System support for this Bounding Box. ')

    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element ComplexData uses Python identifier ComplexData
    __ComplexData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ComplexData'), 'ComplexData', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_ComplexData', False)

    
    ComplexData = property(__ComplexData.value, __ComplexData.set, None, u'Indicates that this Input shall be a complex data structure (such as a GML document), and provides a list of Formats, Encodings, and Schemas supported for this Input. The value of this ComplexData structure can be input either embedded in the Execute request or remotely accessible to the server.  The client can select from among the identified combinations of Formats, Encodings, and Schemas to specify the form of the Input. This allows for complete specification of particular versions of GML, or image formats. ')

    
    # Element LiteralData uses Python identifier LiteralData
    __LiteralData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LiteralData'), 'LiteralData', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_LiteralData', False)

    
    LiteralData = property(__LiteralData.value, __LiteralData.set, None, u'Indicates that this Input shall be a simple numeric value or character string that is embedded in the execute request, and describes the possible values. ')

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Attribute maxOccurs uses Python identifier maxOccurs
    __maxOccurs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxOccurs'), 'maxOccurs', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_maxOccurs', pyxb.binding.datatypes.positiveInteger, required=True)
    
    maxOccurs = property(__maxOccurs.value, __maxOccurs.set, None, u'The maximum number of times that values for this parameter are permitted in an Execute request. If "1" then this parameter may appear only once in an Execute request.  If greater than "1", then this input parameter may appear that many times in an Execute request. ')

    
    # Attribute minOccurs uses Python identifier minOccurs
    __minOccurs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'minOccurs'), 'minOccurs', '__httpwww_opengis_netwps1_0_0_InputDescriptionType_minOccurs', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    
    minOccurs = property(__minOccurs.value, __minOccurs.set, None, u'The minimum number of times that values for this parameter are required in an Execute request.  If "0", this data input is optional. If greater than "0" then this process input is required. ')


    _ElementMap = DescriptionType._ElementMap.copy()
    _ElementMap.update({
        __BoundingBoxData.name() : __BoundingBoxData,
        __ComplexData.name() : __ComplexData,
        __LiteralData.name() : __LiteralData
    })
    _AttributeMap = DescriptionType._AttributeMap.copy()
    _AttributeMap.update({
        __maxOccurs.name() : __maxOccurs,
        __minOccurs.name() : __minOccurs
    })
Namespace.addCategoryObject('typeBinding', u'InputDescriptionType', InputDescriptionType)


# Complex type CTD_ANON_8 with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}UOM uses Python identifier UOM
    __UOM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'UOM'), 'UOM', '__httpwww_opengis_netwps1_0_0_CTD_ANON_8_httpwww_opengis_netows1_1UOM', False)

    
    UOM = property(__UOM.value, __UOM.set, None, u'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. ')


    _ElementMap = {
        __UOM.name() : __UOM
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_9 with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/ows/1.1}Language uses Python identifier Language
    __Language = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Language'), 'Language', '__httpwww_opengis_netwps1_0_0_CTD_ANON_9_httpwww_opengis_netows1_1Language', False)

    
    Language = property(__Language.value, __Language.set, None, u'Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. ')


    _ElementMap = {
        __Language.name() : __Language
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_10 with content type EMPTY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'href'), 'href', '__httpwww_opengis_netwps1_0_0_CTD_ANON_10_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI, required=True)
    
    href = property(__href.value, __href.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __href.name() : __href
    }



# Complex type SupportedComplexDataType with content type ELEMENT_ONLY
class SupportedComplexDataType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SupportedComplexDataType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Supported uses Python identifier Supported
    __Supported = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Supported'), 'Supported', '__httpwww_opengis_netwps1_0_0_SupportedComplexDataType_Supported', False)

    
    Supported = property(__Supported.value, __Supported.set, None, u'Unordered list of combinations of format, encoding, and schema supported for this Input/Output. This element shall be repeated for each combination of MimeType/Encoding/Schema that is supported for this Input/Output. This list shall include the default MimeType/Encoding/Schema. ')

    
    # Element Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Default'), 'Default', '__httpwww_opengis_netwps1_0_0_SupportedComplexDataType_Default', False)

    
    Default = property(__Default.value, __Default.set, None, u'Identifies the default combination of Format, Encoding, and Schema supported for this Input/Output. The process shall expect input in or produce output in this combination of MimeType/Encoding/Schema unless the Execute request specifies otherwise.  ')


    _ElementMap = {
        __Supported.name() : __Supported,
        __Default.name() : __Default
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SupportedComplexDataType', SupportedComplexDataType)


# Complex type ResponseFormType with content type ELEMENT_ONLY
class ResponseFormType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResponseFormType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}ResponseDocument uses Python identifier ResponseDocument
    __ResponseDocument = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ResponseDocument'), 'ResponseDocument', '__httpwww_opengis_netwps1_0_0_ResponseFormType_httpwww_opengis_netwps1_0_0ResponseDocument', False)

    
    ResponseDocument = property(__ResponseDocument.value, __ResponseDocument.set, None, u'Indicates that the outputs shall be returned as part of a WPS response document.')

    
    # Element {http://www.opengis.net/wps/1.0.0}RawDataOutput uses Python identifier RawDataOutput
    __RawDataOutput = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RawDataOutput'), 'RawDataOutput', '__httpwww_opengis_netwps1_0_0_ResponseFormType_httpwww_opengis_netwps1_0_0RawDataOutput', False)

    
    RawDataOutput = property(__RawDataOutput.value, __RawDataOutput.set, None, u'Indicates that the output shall be returned directly as raw data, without a WPS response document.')


    _ElementMap = {
        __ResponseDocument.name() : __ResponseDocument,
        __RawDataOutput.name() : __RawDataOutput
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ResponseFormType', ResponseFormType)


# Complex type ProcessBriefType with content type ELEMENT_ONLY
class ProcessBriefType (DescriptionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProcessBriefType')
    # Base type is DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element {http://www.opengis.net/wps/1.0.0}WSDL uses Python identifier WSDL
    __WSDL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WSDL'), 'WSDL', '__httpwww_opengis_netwps1_0_0_ProcessBriefType_httpwww_opengis_netwps1_0_0WSDL', False)

    
    WSDL = property(__WSDL.value, __WSDL.set, None, u'Location of a WSDL document.')

    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element {http://www.opengis.net/wps/1.0.0}Profile uses Python identifier Profile
    __Profile = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Profile'), 'Profile', '__httpwww_opengis_netwps1_0_0_ProcessBriefType_httpwww_opengis_netwps1_0_0Profile', True)

    
    Profile = property(__Profile.value, __Profile.set, None, u'Optional unordered list of application profiles to which this process complies.')

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Attribute {http://www.opengis.net/wps/1.0.0}processVersion uses Python identifier processVersion
    __processVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'processVersion'), 'processVersion', '__httpwww_opengis_netwps1_0_0_ProcessBriefType_httpwww_opengis_netwps1_0_0processVersion', pyxb.binding.datatypes.string, required=True)
    
    processVersion = property(__processVersion.value, __processVersion.set, None, u'Release version of this Process, included when a process version needs to be included for clarification about the process to be used. It is possible that a WPS supports a process with different versions due to reasons such as modifications of process algorithms.  Notice that this is the version identifier for the process, not the version of the WPS interface. The processVersion is informative only.  Version negotiation for processVersion is not available.  Requests to Execute a process do not include a processVersion identifier.')


    _ElementMap = DescriptionType._ElementMap.copy()
    _ElementMap.update({
        __WSDL.name() : __WSDL,
        __Profile.name() : __Profile
    })
    _AttributeMap = DescriptionType._AttributeMap.copy()
    _AttributeMap.update({
        __processVersion.name() : __processVersion
    })
Namespace.addCategoryObject('typeBinding', u'ProcessBriefType', ProcessBriefType)


# Complex type SupportedComplexDataInputType with content type ELEMENT_ONLY
class SupportedComplexDataInputType (SupportedComplexDataType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SupportedComplexDataInputType')
    # Base type is SupportedComplexDataType
    
    # Element Supported (Supported) inherited from {http://www.opengis.net/wps/1.0.0}SupportedComplexDataType
    
    # Element Default (Default) inherited from {http://www.opengis.net/wps/1.0.0}SupportedComplexDataType
    
    # Attribute maximumMegabytes uses Python identifier maximumMegabytes
    __maximumMegabytes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maximumMegabytes'), 'maximumMegabytes', '__httpwww_opengis_netwps1_0_0_SupportedComplexDataInputType_maximumMegabytes', pyxb.binding.datatypes.integer)
    
    maximumMegabytes = property(__maximumMegabytes.value, __maximumMegabytes.set, None, u'The maximum file size, in megabytes, of this input.  If the input exceeds this size, the server will return an error instead of processing the inputs. ')


    _ElementMap = SupportedComplexDataType._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = SupportedComplexDataType._AttributeMap.copy()
    _AttributeMap.update({
        __maximumMegabytes.name() : __maximumMegabytes
    })
Namespace.addCategoryObject('typeBinding', u'SupportedComplexDataInputType', SupportedComplexDataInputType)


# Complex type CRSsType with content type ELEMENT_ONLY
class CRSsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CRSsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CRS uses Python identifier CRS
    __CRS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CRS'), 'CRS', '__httpwww_opengis_netwps1_0_0_CRSsType_CRS', True)

    
    CRS = property(__CRS.value, __CRS.set, None, u'Reference to a CRS supported for this Input/Output. ')


    _ElementMap = {
        __CRS.name() : __CRS
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CRSsType', CRSsType)


# Complex type ComplexDataType with content type MIXED
class ComplexDataType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComplexDataType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mimeType'), 'mimeType', '__httpwww_opengis_netwps1_0_0_ComplexDataType_mimeType', _ows.MimeType)
    
    mimeType = property(__mimeType.value, __mimeType.set, None, u'The Format of this input or requested for this output (e.g., text/xml). This element shall be omitted when the Format is indicated in the http header of the output. When included, this format shall be one published for this output or input in the Process full description. ')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'schema'), 'schema', '__httpwww_opengis_netwps1_0_0_ComplexDataType_schema', pyxb.binding.datatypes.anyURI)
    
    schema = property(__schema.value, __schema.set, None, u'Web-accessible XML Schema Document that defines the content model of this complex resource (e.g., encoded using GML 2.2 Application Schema).  This reference should be included for XML encoded complex resources to facilitate validation. PS I changed the name of this attribute to be consistent with the ProcessDescription.  The original was giving me validation troubles in XMLSpy. ')

    
    # Attribute encoding uses Python identifier encoding
    __encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'encoding'), 'encoding', '__httpwww_opengis_netwps1_0_0_ComplexDataType_encoding', pyxb.binding.datatypes.anyURI)
    
    encoding = property(__encoding.value, __encoding.set, None, u'The encoding of this input or requested for this output (e.g., UTF-8). This "encoding" shall be included whenever the encoding required is not the default encoding indicated in the Process full description. When included, this encoding shall be one published for this output or input in the Process full description. ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __mimeType.name() : __mimeType,
        __schema.name() : __schema,
        __encoding.name() : __encoding
    }
Namespace.addCategoryObject('typeBinding', u'ComplexDataType', ComplexDataType)


# Complex type WPSCapabilitiesType with content type ELEMENT_ONLY
class WPSCapabilitiesType (_ows.CapabilitiesBaseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WPSCapabilitiesType')
    # Base type is _ows.CapabilitiesBaseType
    
    # Element {http://www.opengis.net/wps/1.0.0}WSDL uses Python identifier WSDL
    __WSDL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'WSDL'), 'WSDL', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_httpwww_opengis_netwps1_0_0WSDL', False)

    
    WSDL = property(__WSDL.value, __WSDL.set, None, u'Location of a WSDL document.')

    
    # Element ServiceProvider ({http://www.opengis.net/ows/1.1}ServiceProvider) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element OperationsMetadata ({http://www.opengis.net/ows/1.1}OperationsMetadata) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element ServiceIdentification ({http://www.opengis.net/ows/1.1}ServiceIdentification) inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Element {http://www.opengis.net/wps/1.0.0}ProcessOfferings uses Python identifier ProcessOfferings
    __ProcessOfferings = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ProcessOfferings'), 'ProcessOfferings', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_httpwww_opengis_netwps1_0_0ProcessOfferings', False)

    
    ProcessOfferings = property(__ProcessOfferings.value, __ProcessOfferings.set, None, u'List of brief descriptions of the processes offered by this WPS server. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Languages uses Python identifier Languages
    __Languages = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Languages'), 'Languages', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_httpwww_opengis_netwps1_0_0Languages', False)

    
    Languages = property(__Languages.value, __Languages.set, None, u'Listing of the default and other languages supported by this service. ')

    
    # Attribute updateSequence inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute version inherited from {http://www.opengis.net/ows/1.1}CapabilitiesBaseType
    
    # Attribute service uses Python identifier service
    __service = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'service'), 'service', '__httpwww_opengis_netwps1_0_0_WPSCapabilitiesType_service', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default=u'WPS', required=True)
    
    service = property(__service.value, __service.set, None, None)


    _ElementMap = _ows.CapabilitiesBaseType._ElementMap.copy()
    _ElementMap.update({
        __WSDL.name() : __WSDL,
        __ProcessOfferings.name() : __ProcessOfferings,
        __Languages.name() : __Languages
    })
    _AttributeMap = _ows.CapabilitiesBaseType._AttributeMap.copy()
    _AttributeMap.update({
        __lang.name() : __lang,
        __service.name() : __service
    })
Namespace.addCategoryObject('typeBinding', u'WPSCapabilitiesType', WPSCapabilitiesType)


# Complex type CTD_ANON_11 with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Output'), 'Output', '__httpwww_opengis_netwps1_0_0_CTD_ANON_11_httpwww_opengis_netwps1_0_0Output', True)

    
    Output = property(__Output.value, __Output.set, None, u'Unordered list of values of all the outputs produced by this process. It is not necessary to include an output until the Status is ProcessSucceeded. ')


    _ElementMap = {
        __Output.name() : __Output
    }
    _AttributeMap = {
        
    }



# Complex type ComplexDataDescriptionType with content type ELEMENT_ONLY
class ComplexDataDescriptionType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComplexDataDescriptionType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Schema uses Python identifier Schema
    __Schema = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Schema'), 'Schema', '__httpwww_opengis_netwps1_0_0_ComplexDataDescriptionType_Schema', False)

    
    Schema = property(__Schema.value, __Schema.set, None, u'Reference to a definition of XML elements or types supported for this Input/Output (e.g., GML 2.1 Application Schema). Each of these XML elements or types shall be defined in a separate XML Schema Document. This parameter shall be included when this input/output is XML encoded using an XML schema. When included, the input/output shall validate against the referenced XML Schema. This element shall be omitted if Schema does not apply to this Input/Output. Note: If the Input/Output uses a profile of a larger schema, the server administrator should provide that schema profile for validation purposes. ')

    
    # Element MimeType uses Python identifier MimeType
    __MimeType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'MimeType'), 'MimeType', '__httpwww_opengis_netwps1_0_0_ComplexDataDescriptionType_MimeType', False)

    
    MimeType = property(__MimeType.value, __MimeType.set, None, u'Mime type supported for this input or output (e.g., text/xml). ')

    
    # Element Encoding uses Python identifier Encoding
    __Encoding = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Encoding'), 'Encoding', '__httpwww_opengis_netwps1_0_0_ComplexDataDescriptionType_Encoding', False)

    
    Encoding = property(__Encoding.value, __Encoding.set, None, u'Reference to an encoding supported for this input or output (e.g., UTF-8).  This element shall be omitted if Encoding does not apply to this Input/Output. ')


    _ElementMap = {
        __Schema.name() : __Schema,
        __MimeType.name() : __MimeType,
        __Encoding.name() : __Encoding
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ComplexDataDescriptionType', ComplexDataDescriptionType)


# Complex type CTD_ANON_12 with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Output'), 'Output', '__httpwww_opengis_netwps1_0_0_CTD_ANON_12_Output', True)

    
    Output = property(__Output.value, __Output.set, None, u'Unordered list of one or more descriptions of all the outputs that can result from executing this process. At least one output is required from each process. ')


    _ElementMap = {
        __Output.name() : __Output
    }
    _AttributeMap = {
        
    }



# Complex type OutputDescriptionType with content type ELEMENT_ONLY
class OutputDescriptionType (DescriptionType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OutputDescriptionType')
    # Base type is DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element LiteralOutput uses Python identifier LiteralOutput
    __LiteralOutput = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'LiteralOutput'), 'LiteralOutput', '__httpwww_opengis_netwps1_0_0_OutputDescriptionType_LiteralOutput', False)

    
    LiteralOutput = property(__LiteralOutput.value, __LiteralOutput.set, None, u'Indicates that this output shall be a simple literal value (such as an integer) that is embedded in the execute response, and describes that output. ')

    
    # Element ComplexOutput uses Python identifier ComplexOutput
    __ComplexOutput = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ComplexOutput'), 'ComplexOutput', '__httpwww_opengis_netwps1_0_0_OutputDescriptionType_ComplexOutput', False)

    
    ComplexOutput = property(__ComplexOutput.value, __ComplexOutput.set, None, u'Indicates that this Output shall be a complex data structure (such as a GML fragment) that is returned by the execute operation response. The value of this complex data structure can be output either embedded in the execute operation response or remotely accessible to the client. When this output form is indicated, the process produces only a single output, and "store" is "false, the output shall be returned directly, without being embedded in the XML document that is otherwise provided by execute operation response. \n\t\t\t\t\tThis element also provides a list of format, encoding, and schema combinations supported for this output. The client can select from among the identified combinations of formats, encodings, and schemas to specify the form of the output. This allows for complete specification of particular versions of GML, or image formats. ')

    
    # Element BoundingBoxOutput uses Python identifier BoundingBoxOutput
    __BoundingBoxOutput = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'BoundingBoxOutput'), 'BoundingBoxOutput', '__httpwww_opengis_netwps1_0_0_OutputDescriptionType_BoundingBoxOutput', False)

    
    BoundingBoxOutput = property(__BoundingBoxOutput.value, __BoundingBoxOutput.set, None, u'Indicates that this output shall be a BoundingBox data structure, and provides a list of the CRSs supported in these Bounding Boxes. This element shall be included when this process output is an ows:BoundingBox element. ')

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType

    _ElementMap = DescriptionType._ElementMap.copy()
    _ElementMap.update({
        __LiteralOutput.name() : __LiteralOutput,
        __ComplexOutput.name() : __ComplexOutput,
        __BoundingBoxOutput.name() : __BoundingBoxOutput
    })
    _AttributeMap = DescriptionType._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'OutputDescriptionType', OutputDescriptionType)


# Complex type CTD_ANON_13 with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CRS uses Python identifier CRS
    __CRS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'CRS'), 'CRS', '__httpwww_opengis_netwps1_0_0_CTD_ANON_13_CRS', False)

    
    CRS = property(__CRS.value, __CRS.set, None, u'Reference to the default CRS supported for this Input/Output')


    _ElementMap = {
        __CRS.name() : __CRS
    }
    _AttributeMap = {
        
    }



# Complex type SupportedUOMsType with content type ELEMENT_ONLY
class SupportedUOMsType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SupportedUOMsType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Supported uses Python identifier Supported
    __Supported = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Supported'), 'Supported', '__httpwww_opengis_netwps1_0_0_SupportedUOMsType_Supported', False)

    
    Supported = property(__Supported.value, __Supported.set, None, u'Unordered list of references to all of the UOMs supported for this input or output, if UOM is applicable. The default UOM shall be included in this list. ')

    
    # Element Default uses Python identifier Default
    __Default = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Default'), 'Default', '__httpwww_opengis_netwps1_0_0_SupportedUOMsType_Default', False)

    
    Default = property(__Default.value, __Default.set, None, u'Reference to the default UOM supported for this input or output, if UoM is applicable. The process shall expect input in or produce output in this UOM unless the Execute request specifies another supported UOM. ')


    _ElementMap = {
        __Supported.name() : __Supported,
        __Default.name() : __Default
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'SupportedUOMsType', SupportedUOMsType)


# Complex type ProcessDescriptionType with content type ELEMENT_ONLY
class ProcessDescriptionType (ProcessBriefType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProcessDescriptionType')
    # Base type is ProcessBriefType
    
    # Element Title ({http://www.opengis.net/ows/1.1}Title) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element WSDL ({http://www.opengis.net/wps/1.0.0}WSDL) inherited from {http://www.opengis.net/wps/1.0.0}ProcessBriefType
    
    # Element DataInputs uses Python identifier DataInputs
    __DataInputs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'DataInputs'), 'DataInputs', '__httpwww_opengis_netwps1_0_0_ProcessDescriptionType_DataInputs', False)

    
    DataInputs = property(__DataInputs.value, __DataInputs.set, None, u'List of the inputs to this process. In almost all cases, at least one process input is required. However, no process inputs may be identified when all the inputs are predetermined fixed resources.  In this case, those resources shall be identified in the ows:Abstract element that describes the process.')

    
    # Element Abstract ({http://www.opengis.net/ows/1.1}Abstract) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Metadata ({http://www.opengis.net/ows/1.1}Metadata) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Element Profile ({http://www.opengis.net/wps/1.0.0}Profile) inherited from {http://www.opengis.net/wps/1.0.0}ProcessBriefType
    
    # Element ProcessOutputs uses Python identifier ProcessOutputs
    __ProcessOutputs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'ProcessOutputs'), 'ProcessOutputs', '__httpwww_opengis_netwps1_0_0_ProcessDescriptionType_ProcessOutputs', False)

    
    ProcessOutputs = property(__ProcessOutputs.value, __ProcessOutputs.set, None, u'List of outputs which will or can result from executing the process. ')

    
    # Element Identifier ({http://www.opengis.net/ows/1.1}Identifier) inherited from {http://www.opengis.net/wps/1.0.0}DescriptionType
    
    # Attribute storeSupported uses Python identifier storeSupported
    __storeSupported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'storeSupported'), 'storeSupported', '__httpwww_opengis_netwps1_0_0_ProcessDescriptionType_storeSupported', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    storeSupported = property(__storeSupported.value, __storeSupported.set, None, u'Indicates if ComplexData outputs from this process can be stored by the WPS server as web-accessible resources. If "storeSupported" is "true", the Execute operation request may include "asReference" equals "true" for any complex output, directing that the output of the process be stored so that the client can retrieve it as required. By default for this process, storage is not supported and all outputs are returned encoded in the Execute response. ')

    
    # Attribute processVersion inherited from {http://www.opengis.net/wps/1.0.0}ProcessBriefType
    
    # Attribute statusSupported uses Python identifier statusSupported
    __statusSupported = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'statusSupported'), 'statusSupported', '__httpwww_opengis_netwps1_0_0_ProcessDescriptionType_statusSupported', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    statusSupported = property(__statusSupported.value, __statusSupported.set, None, u'Indicates if ongoing status information can be provided for this process.  If "true", the Status element of the stored Execute response document shall be kept up to date.  If "false" then the Status element shall not be updated until processing is complete. By default, status information is not provided for this process. ')


    _ElementMap = ProcessBriefType._ElementMap.copy()
    _ElementMap.update({
        __DataInputs.name() : __DataInputs,
        __ProcessOutputs.name() : __ProcessOutputs
    })
    _AttributeMap = ProcessBriefType._AttributeMap.copy()
    _AttributeMap.update({
        __storeSupported.name() : __storeSupported,
        __statusSupported.name() : __statusSupported
    })
Namespace.addCategoryObject('typeBinding', u'ProcessDescriptionType', ProcessDescriptionType)


# Complex type CTD_ANON_14 with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(None, u'Input'), 'Input', '__httpwww_opengis_netwps1_0_0_CTD_ANON_14_Input', True)

    
    Input = property(__Input.value, __Input.set, None, u'Unordered list of one or more descriptions of the inputs that can be accepted by this process, including all required and optional inputs.  Where an input is optional because a default value exists, that default value must be identified in the "ows:Abstract" element for that input, except in the case of LiteralData, where the default must be indicated in the corresponding ows:DefaultValue element. Where an input is optional because it depends on the value(s) of other inputs, this must be indicated in the ows:Abstract element for that input. ')


    _ElementMap = {
        __Input.name() : __Input
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_15 with content type ELEMENT_ONLY
class CTD_ANON_15 (RequestBaseType):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is RequestBaseType
    
    # Element {http://www.opengis.net/wps/1.0.0}ResponseForm uses Python identifier ResponseForm
    __ResponseForm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ResponseForm'), 'ResponseForm', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_httpwww_opengis_netwps1_0_0ResponseForm', False)

    
    ResponseForm = property(__ResponseForm.value, __ResponseForm.set, None, u'Defines the response type of the WPS, either raw data or XML document.  If absent, the response shall be a response document which includes all outputs encoded in the response.')

    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_httpwww_opengis_netows1_1Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}DataInputs uses Python identifier DataInputs
    __DataInputs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataInputs'), 'DataInputs', '__httpwww_opengis_netwps1_0_0_CTD_ANON_15_httpwww_opengis_netwps1_0_0DataInputs', False)

    
    DataInputs = property(__DataInputs.value, __DataInputs.set, None, u'List of input (or parameter) values provided to the process, including each of the Inputs needed to execute the process. It is possible to have no inputs provided only when all the inputs are predetermined fixed resources. In all other cases, at least one input is required. ')

    
    # Attribute version inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    
    # Attribute service inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType
    
    # Attribute language inherited from {http://www.opengis.net/wps/1.0.0}RequestBaseType

    _ElementMap = RequestBaseType._ElementMap.copy()
    _ElementMap.update({
        __ResponseForm.name() : __ResponseForm,
        __Identifier.name() : __Identifier,
        __DataInputs.name() : __DataInputs
    })
    _AttributeMap = RequestBaseType._AttributeMap.copy()
    _AttributeMap.update({
        
    })



# Complex type LiteralDataType with content type SIMPLE
class LiteralDataType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LiteralDataType')
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dataType'), 'dataType', '__httpwww_opengis_netwps1_0_0_LiteralDataType_dataType', pyxb.binding.datatypes.anyURI)
    
    dataType = property(__dataType.value, __dataType.set, None, u'Identifies the data type of this literal input or output. This dataType should be included for each quantity whose value is not a simple string. ')

    
    # Attribute uom uses Python identifier uom
    __uom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uom'), 'uom', '__httpwww_opengis_netwps1_0_0_LiteralDataType_uom', pyxb.binding.datatypes.anyURI)
    
    uom = property(__uom.value, __uom.set, None, u'Identifies the unit of measure of this literal input or output. This unit of measure should be referenced for any numerical value that has units (e.g., "meters", but not a more complete reference system). Shall be a UOM identified in the Process description for this input or output. ')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __dataType.name() : __dataType,
        __uom.name() : __uom
    }
Namespace.addCategoryObject('typeBinding', u'LiteralDataType', LiteralDataType)


# Complex type InputType with content type ELEMENT_ONLY
class InputType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InputType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reference'), 'Reference', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netwps1_0_0Reference', False)

    
    Reference = property(__Reference.value, __Reference.set, None, u'Identifies this input value as a web accessible resource, and references that resource. ')

    
    # Element {http://www.opengis.net/ows/1.1}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), 'Identifier', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netows1_1Identifier', False)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, u'Unique identifier or name of this dataset. ')

    
    # Element {http://www.opengis.net/ows/1.1}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract'), 'Abstract', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netows1_1Abstract', False)

    
    Abstract = property(__Abstract.value, __Abstract.set, None, u'Brief narrative description of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/ows/1.1}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title'), 'Title', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netows1_1Title', False)

    
    Title = property(__Title.value, __Title.set, None, u'Title of this resource, normally used for display to a human. ')

    
    # Element {http://www.opengis.net/wps/1.0.0}Data uses Python identifier Data
    __Data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Data'), 'Data', '__httpwww_opengis_netwps1_0_0_InputType_httpwww_opengis_netwps1_0_0Data', False)

    
    Data = property(__Data.value, __Data.set, None, u'Identifies this input value as a data embedded in this request, and includes that data. ')


    _ElementMap = {
        __Reference.name() : __Reference,
        __Identifier.name() : __Identifier,
        __Abstract.name() : __Abstract,
        __Title.name() : __Title,
        __Data.name() : __Data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'InputType', InputType)


# Complex type ResponseDocumentType with content type ELEMENT_ONLY
class ResponseDocumentType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResponseDocumentType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wps/1.0.0}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Output'), 'Output', '__httpwww_opengis_netwps1_0_0_ResponseDocumentType_httpwww_opengis_netwps1_0_0Output', True)

    
    Output = property(__Output.value, __Output.set, None, u'Unordered list of definitions of the outputs (or parameters) requested from the process. These outputs are not normally identified, unless the client is specifically requesting a limited subset of outputs, and/or is requesting output formats and/or schemas and/or encodings different from the defaults and selected from the alternatives identified in the process description, or wishes to customize the descriptive information about the output. ')

    
    # Attribute lineage uses Python identifier lineage
    __lineage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lineage'), 'lineage', '__httpwww_opengis_netwps1_0_0_ResponseDocumentType_lineage', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    lineage = property(__lineage.value, __lineage.set, None, u'Indicates if the Execute operation response shall include the DataInputs and OutputDefinitions elements.  If lineage is "true" the server shall include in the execute response a complete copy of the DataInputs and OutputDefinition elements as received in the execute request.  If lineage is "false" then these elements shall be omitted from the response.  ')

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpwww_opengis_netwps1_0_0_ResponseDocumentType_status', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    status = property(__status.value, __status.set, None, u'Indicates if the stored execute response document shall be updated to provide ongoing reports on the status of execution.  If status is "true" and storeExecuteResponse is "true" (and the server has indicated that both storeSupported and statusSupported are "true")  then the Status element of the execute response document stored at executeResponseLocation is kept up to date by the process.  While the execute response contains ProcessAccepted, ProcessStarted, or ProcessPaused, updates shall be made to the executeResponse document until either the process completes successfully (in which case ProcessSucceeded is populated), or the process fails (in which case ProcessFailed is populated).  If status is "false" then the Status element shall not be updated until the process either completes successfully or fails.  If status="true" and storeExecuteResponse is "false" then the service shall raise an exception.')

    
    # Attribute storeExecuteResponse uses Python identifier storeExecuteResponse
    __storeExecuteResponse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'storeExecuteResponse'), 'storeExecuteResponse', '__httpwww_opengis_netwps1_0_0_ResponseDocumentType_storeExecuteResponse', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    storeExecuteResponse = property(__storeExecuteResponse.value, __storeExecuteResponse.set, None, u'Indicates if the execute response document shall be stored.  If "true" then the executeResponseLocation attribute in the execute response becomes mandatory, which will point to the location where the executeResponseDocument is stored.  The service shall respond immediately to the request and return an executeResponseDocument containing the executeResponseLocation and the status element which has five possible subelements (choice):ProcessAccepted, ProcessStarted, ProcessPaused, ProcessFailed and ProcessSucceeded, which are chosen and populated as follows:   1) If the process is completed when the initial executeResponseDocument is returned, the element ProcessSucceeded is populated with the process results.  2) If the process already failed when the initial executeResponseDocument is returned, the element ProcessFailed is populated with the Exception.  3) If the process has been paused when the initial executeResponseDocument is returned, the element ProcessPaused is populated.  4) If the process has been accepted when the initial executeResponseDocument is returned, the element ProcessAccepted is populated, including percentage information. 5) If the process execution is ongoing when the initial executeResponseDocument is returned, the element ProcessStarted is populated.  In case 3, 4, and 5, if status updating is requested, updates are made to the executeResponseDocument at the executeResponseLocation until either the process completes successfully or fails.  Regardless, once the process completes successfully, the ProcessSucceeded element is populated, and if it fails, the ProcessFailed element is populated.Specifies if the Execute operation response shall be returned quickly with status information, or not returned until process execution is complete. This parameter shall not be included unless the corresponding "statusSupported" parameter is included and is "true" in the ProcessDescription for this process. ')


    _ElementMap = {
        __Output.name() : __Output
    }
    _AttributeMap = {
        __lineage.name() : __lineage,
        __status.name() : __status,
        __storeExecuteResponse.name() : __storeExecuteResponse
    }
Namespace.addCategoryObject('typeBinding', u'ResponseDocumentType', ResponseDocumentType)


GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetCapabilities'), CTD_ANON_2)
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

ProcessDescriptions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessDescriptions'), CTD_ANON_3, documentation=u'WPS DescribeProcess operation response. ')
Namespace.addCategoryObject('elementBinding', ProcessDescriptions.name().localName(), ProcessDescriptions)

WSDL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WSDL'), CTD_ANON_4, documentation=u'Location of a WSDL document.')
Namespace.addCategoryObject('elementBinding', WSDL.name().localName(), WSDL)

ExecuteResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExecuteResponse'), CTD_ANON_6, documentation=u'WPS Execute operation response. By default, this XML document is delivered to the client in response to an Execute request. If "status" is "false" in the Execute operation request, this document is normally returned when process execution has been completed.\n\t\t\tIf "status" in the Execute request is "true", this response shall be returned as soon as the Execute request has been accepted for processing. In this case, the same XML document is also made available as a web-accessible resource from the URL identified in the statusLocation, and the WPS server shall repopulate it once the process has completed. It may repopulate it on an ongoing basis while the process is executing.\n\t\t\tHowever, the response to an Execute request will not include this element in the special case where the output is a single complex value result and the Execute request indicates that "store" is "false". Instead, the server shall return the complex result (e.g., GIF image or GML) directly, without encoding it in the ExecuteResponse. If processing fails in this special case, the normal ExecuteResponse shall be sent, with the error condition indicated. This option is provided to simplify the programming required for simple clients and for service chaining. ')
Namespace.addCategoryObject('elementBinding', ExecuteResponse.name().localName(), ExecuteResponse)

DescribeProcess = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescribeProcess'), CTD_ANON_7, documentation=u'WPS DescribeProcess operation request. ')
Namespace.addCategoryObject('elementBinding', DescribeProcess.name().localName(), DescribeProcess)

Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Capabilities'), WPSCapabilitiesType, documentation=u'WPS GetCapabilities operation response. This document provides clients with service metadata about a specific service instance, including metadata about the processes that can be executed. Since the server does not implement the updateSequence and Sections parameters, the server shall always return the complete Capabilities document, without the updateSequence parameter. ')
Namespace.addCategoryObject('elementBinding', Capabilities.name().localName(), Capabilities)

Languages = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Languages'), CTD_ANON_5, documentation=u'Listing of the default and other languages supported by this service. ')
Namespace.addCategoryObject('elementBinding', Languages.name().localName(), Languages)

Execute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Execute'), CTD_ANON_15, documentation=u'WPS Execute operation request, to execute one identified Process. If a process is to be run multiple times, each run shall be submitted as a separate Execute request. ')
Namespace.addCategoryObject('elementBinding', Execute.name().localName(), Execute)

ProcessOfferings = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessOfferings'), CTD_ANON_, documentation=u'List of brief descriptions of the processes offered by this WPS server. ')
Namespace.addCategoryObject('elementBinding', ProcessOfferings.name().localName(), ProcessOfferings)



ProcessFailedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'ExceptionReport'), _ows.CTD_ANON_3, scope=ProcessFailedType, documentation=u'Report message returned to the client that requested any OWS operation when the server detects an error while processing that operation request. '))
ProcessFailedType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessFailedType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'ExceptionReport')), min_occurs=1, max_occurs=1)
    )
ProcessFailedType._ContentModel = pyxb.binding.content.ParticleModel(ProcessFailedType._GroupModel, min_occurs=1, max_occurs=1)



StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessAccepted'), pyxb.binding.datatypes.string, scope=StatusType, documentation=u'Indicates that this process has been accepted by the server, but is in a queue and has not yet started to execute. The contents of this human-readable text string is left open to definition by each server implementation, but is expected to include any messages the server may wish to let the clients know. Such information could include how long the queue is, or any warning conditions that may have been encountered. The client may display this text to a human user. '))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessStarted'), ProcessStartedType, scope=StatusType, documentation=u'Indicates that this process has been accepted by the server, and processing has begun. '))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessFailed'), ProcessFailedType, scope=StatusType, documentation=u'Indicates that execution of this process has failed, and includes error information. '))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessSucceeded'), pyxb.binding.datatypes.string, scope=StatusType, documentation=u'Indicates that this process has successfully completed execution. The contents of this human-readable text string is left open to definition by each server, but is expected to include any messages the server may wish to let the clients know, such as how long the process took to execute, or any warning conditions that may have been encountered. The client may display this text string to a human user. The client should make use of the presence of this element to trigger automated or manual access to the results of the process. If manual access is intended, the client should use the presence of this element to present the results as downloadable links to the user. '))

StatusType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessPaused'), ProcessStartedType, scope=StatusType, documentation=u'Indicates that this process has been  accepted by the server, and processing has started but subsequently been paused by the server.'))
StatusType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessAccepted')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessStarted')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessPaused')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessSucceeded')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(StatusType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessFailed')), min_occurs=1, max_occurs=1)
    )
StatusType._ContentModel = pyxb.binding.content.ParticleModel(StatusType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Process'), ProcessBriefType, scope=CTD_ANON_, documentation=u'Unordered list of one or more brief descriptions of all the processes offered by this WPS server. '))
CTD_ANON_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Process')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_._GroupModel, min_occurs=1, max_occurs=1)



DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexData'), ComplexDataType, scope=DataType, documentation=u'Identifies this input or output value as a complex data structure encoded in XML (e.g., using GML), and provides that complex data structure. For an input, this element may be used by a client for any process input coded as ComplexData in the ProcessDescription. For an output, this element shall be used by a server when "store" in the Execute request is "false". '))

DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LiteralData'), LiteralDataType, scope=DataType, documentation=u'Identifies this input or output data as literal data of a simple quantity (e.g., one number), and provides that data. '))

DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BoundingBoxData'), _ows.BoundingBoxType, scope=DataType, documentation=u'Identifies this input or output data as an ows:BoundingBox data structure, and provides that ows:BoundingBox data. '))
DataType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(DataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComplexData')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LiteralData')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BoundingBoxData')), min_occurs=1, max_occurs=1)
    )
DataType._ContentModel = pyxb.binding.content.ParticleModel(DataType._GroupModel, min_occurs=1, max_occurs=1)



DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Metadata'), _ows.MetadataType, scope=DescriptionType))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), _ows.CodeType, scope=DescriptionType, documentation=u'Unique identifier or name of this dataset. '))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract'), _ows.LanguageStringType, scope=DescriptionType, documentation=u'Brief narrative description of this resource, normally used for display to a human. '))

DescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title'), _ows.LanguageStringType, scope=DescriptionType, documentation=u'Title of this resource, normally used for display to a human. '))
DescriptionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Metadata')), min_occurs=0L, max_occurs=None)
    )
DescriptionType._ContentModel = pyxb.binding.content.ParticleModel(DescriptionType._GroupModel, min_occurs=1, max_occurs=1)



OutputDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), OutputReferenceType, scope=OutputDataType, documentation=u'Identifies this output as a web accessible resource, and references that resource.  This element shall only be used for complex data. This element shall be used by a server when "store" in the Execute request is "true". '))

OutputDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Data'), DataType, scope=OutputDataType, documentation=u'Identifies this output value as a data embedded in this response, and includes that data. This element shall be used by a server when "store" in the Execute request is "false". '))
OutputDataType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Metadata')), min_occurs=0L, max_occurs=None)
    )
OutputDataType._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Data')), min_occurs=1, max_occurs=1)
    )
OutputDataType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OutputDataType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDataType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
OutputDataType._ContentModel = pyxb.binding.content.ParticleModel(OutputDataType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AcceptVersions'), _ows.AcceptVersionsType, scope=CTD_ANON_2, documentation=u'When omitted, server shall return latest supported version. '))
CTD_ANON_2._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AcceptVersions')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_2._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_2._GroupModel, min_occurs=1, max_occurs=1)



OutputDefinitionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Output'), DocumentOutputDefinitionType, scope=OutputDefinitionsType, documentation=u'Output definition as provided in the execute request '))
OutputDefinitionsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OutputDefinitionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=1, max_occurs=None)
    )
OutputDefinitionsType._ContentModel = pyxb.binding.content.ParticleModel(OutputDefinitionsType._GroupModel, min_occurs=1, max_occurs=1)



DataInputsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Input'), InputType, scope=DataInputsType, documentation=u'Unordered list of one or more inputs to be used by the process, including each of the Inputs needed to execute the process. '))
DataInputsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DataInputsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Input')), min_occurs=1, max_occurs=None)
    )
DataInputsType._ContentModel = pyxb.binding.content.ParticleModel(DataInputsType._GroupModel, min_occurs=1, max_occurs=1)



LiteralOutputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'UOMs'), SupportedUOMsType, scope=LiteralOutputType, documentation=u'List of supported units of measure for this input or output. This element should be included when this literal has a unit of measure (e.g., "meters", without a more complete reference system). Not necessary for a count, which has no units. '))

LiteralOutputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'DataType'), _ows.DomainMetadataType, scope=LiteralOutputType, documentation=u'Definition of the data type of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known data type. For example, such a URN could be a data type identification URN defined in the "ogc" URN namespace. '))
LiteralOutputType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(LiteralOutputType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'DataType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(LiteralOutputType._UseForTag(pyxb.namespace.ExpandedName(None, u'UOMs')), min_occurs=0L, max_occurs=1)
    )
LiteralOutputType._ContentModel = pyxb.binding.content.ParticleModel(LiteralOutputType._GroupModel, min_occurs=1, max_occurs=1)



LiteralInputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'AllowedValues'), _ows.CTD_ANON_10, scope=LiteralInputType, documentation=u'List of all the valid values and/or ranges of values for this quantity. For numeric quantities, signed values should be ordered from negative infinity to positive infinity. '))

LiteralInputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'AnyValue'), _ows.CTD_ANON_5, scope=LiteralInputType, documentation=u'Specifies that any value is allowed for this parameter.'))

LiteralInputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DefaultValue'), pyxb.binding.datatypes.string, scope=LiteralInputType, documentation=u'Optional default value for this quantity, which should be included when this quantity has a default value.  The DefaultValue shall be understood to be consistent with the unit of measure selected in the Execute request. '))

LiteralInputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ValuesReference'), ValuesReferenceType, scope=LiteralInputType, documentation=u'Indicates that there are a finite set of values and ranges allowed for this input, which are specified in the referenced list. '))
LiteralInputType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'DataType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(None, u'UOMs')), min_occurs=0L, max_occurs=1)
    )
LiteralInputType._GroupModel_3 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'AllowedValues')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'AnyValue')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(None, u'ValuesReference')), min_occurs=1, max_occurs=1)
    )
LiteralInputType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(LiteralInputType._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(LiteralInputType._UseForTag(pyxb.namespace.ExpandedName(None, u'DefaultValue')), min_occurs=0L, max_occurs=1)
    )
LiteralInputType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(LiteralInputType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(LiteralInputType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
LiteralInputType._ContentModel = pyxb.binding.content.ParticleModel(LiteralInputType._GroupModel, min_occurs=1, max_occurs=1)



LanguagesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Language'), pyxb.binding.datatypes.language, scope=LanguagesType, documentation=u'Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. '))
LanguagesType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(LanguagesType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Language')), min_occurs=1, max_occurs=None)
    )
LanguagesType._ContentModel = pyxb.binding.content.ParticleModel(LanguagesType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ProcessDescription'), ProcessDescriptionType, scope=CTD_ANON_3, documentation=u'Ordered list of one or more full Process descriptions, listed in the order in which they were requested in the DescribeProcess operation request. '))
CTD_ANON_3._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'ProcessDescription')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_3._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_3._GroupModel, min_occurs=1, max_occurs=1)



SupportedCRSsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Supported'), CRSsType, scope=SupportedCRSsType, documentation=u'Unordered list of references to all of the CRSs supported for this Input/Output. The default CRS shall be included in this list.'))

SupportedCRSsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Default'), CTD_ANON_13, scope=SupportedCRSsType, documentation=u'Identifies the default CRS that will be used unless the Execute operation request specifies another supported CRS. '))
SupportedCRSsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SupportedCRSsType._UseForTag(pyxb.namespace.ExpandedName(None, u'Default')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SupportedCRSsType._UseForTag(pyxb.namespace.ExpandedName(None, u'Supported')), min_occurs=1, max_occurs=1)
    )
SupportedCRSsType._ContentModel = pyxb.binding.content.ParticleModel(SupportedCRSsType._GroupModel, min_occurs=1, max_occurs=1)



ComplexDataCombinationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Format'), ComplexDataDescriptionType, scope=ComplexDataCombinationType, documentation=u'The default combination of MimeType/Encoding/Schema supported for this Input/Output. '))
ComplexDataCombinationType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ComplexDataCombinationType._UseForTag(pyxb.namespace.ExpandedName(None, u'Format')), min_occurs=1, max_occurs=1)
    )
ComplexDataCombinationType._ContentModel = pyxb.binding.content.ParticleModel(ComplexDataCombinationType._GroupModel, min_occurs=1, max_occurs=1)



UOMsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'UOM'), _ows.DomainMetadataType, scope=UOMsType, documentation=u'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. '))
UOMsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(UOMsType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'UOM')), min_occurs=1, max_occurs=None)
    )
UOMsType._ContentModel = pyxb.binding.content.ParticleModel(UOMsType._GroupModel, min_occurs=1, max_occurs=1)



OutputDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), _ows.CodeType, scope=OutputDefinitionType, documentation=u'Unique identifier or name of this dataset. '))
OutputDefinitionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OutputDefinitionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1)
    )
OutputDefinitionType._ContentModel = pyxb.binding.content.ParticleModel(OutputDefinitionType._GroupModel, min_occurs=1, max_occurs=1)



ComplexDataCombinationsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Format'), ComplexDataDescriptionType, scope=ComplexDataCombinationsType, documentation=u'A valid combination of MimeType/Encoding/Schema supported for this Input/Output. '))
ComplexDataCombinationsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ComplexDataCombinationsType._UseForTag(pyxb.namespace.ExpandedName(None, u'Format')), min_occurs=1, max_occurs=None)
    )
ComplexDataCombinationsType._ContentModel = pyxb.binding.content.ParticleModel(ComplexDataCombinationsType._GroupModel, min_occurs=1, max_occurs=1)



InputReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Body'), pyxb.binding.datatypes.anyType, scope=InputReferenceType, documentation=u'The contents of this element to be used as the body of the HTTP request message to be sent to the service identified in ../Reference/@href.  For example, it could be an XML encoded WFS request using HTTP POST'))

InputReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Header'), CTD_ANON, scope=InputReferenceType, documentation=u'Extra HTTP request headers needed by the service identified in ../Reference/@href.  For example, an HTTP SOAP request requires a SOAPAction header.  This permits the creation of a complete and valid POST request.'))

InputReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BodyReference'), CTD_ANON_10, scope=InputReferenceType, documentation=u'Reference to a remote document to be used as the body of the an HTTP POST request message to the service identified in ../Reference/@href.'))
InputReferenceType._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(InputReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Body')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BodyReference')), min_occurs=1, max_occurs=1)
    )
InputReferenceType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Header')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(InputReferenceType._GroupModel_, min_occurs=0L, max_occurs=1)
    )
InputReferenceType._ContentModel = pyxb.binding.content.ParticleModel(InputReferenceType._GroupModel, min_occurs=0L, max_occurs=1)



DocumentOutputDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract'), _ows.LanguageStringType, scope=DocumentOutputDefinitionType, documentation=u'Brief narrative description of this resource, normally used for display to a human. '))

DocumentOutputDefinitionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title'), _ows.LanguageStringType, scope=DocumentOutputDefinitionType, documentation=u'Title of this resource, normally used for display to a human. '))
DocumentOutputDefinitionType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DocumentOutputDefinitionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1)
    )
DocumentOutputDefinitionType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DocumentOutputDefinitionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DocumentOutputDefinitionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract')), min_occurs=0L, max_occurs=1)
    )
DocumentOutputDefinitionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DocumentOutputDefinitionType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DocumentOutputDefinitionType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
DocumentOutputDefinitionType._ContentModel = pyxb.binding.content.ParticleModel(DocumentOutputDefinitionType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Supported'), LanguagesType, scope=CTD_ANON_5, documentation=u'Unordered list of references to all of the languages supported by this service. The default language shall be included in this list.'))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Default'), CTD_ANON_9, scope=CTD_ANON_5, documentation=u'Identifies the default language that will be used unless the operation request specifies another supported language. '))
CTD_ANON_5._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Default')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Supported')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_5._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_5._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessOutputs'), CTD_ANON_11, scope=CTD_ANON_6, documentation=u'List of values of the Process output parameters. Normally there would be at least one output when the process has completed successfully. If the process has not finished executing, the implementer can choose to include whatever final results are ready at the time the Execute response is provided. If the reference locations of outputs are known in advance, these URLs may be provided before they are populated. '))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Process'), ProcessBriefType, scope=CTD_ANON_6, documentation=u'Process description from the ProcessOfferings section of the GetCapabilities response. '))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Status'), StatusType, scope=CTD_ANON_6, documentation=u'Execution status of this process. '))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OutputDefinitions'), OutputDefinitionsType, scope=CTD_ANON_6, documentation=u'Complete list of Output data types that were requested as part of the Execute request. This element shall be omitted unless the lineage attribute of the execute request is set to "true".'))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataInputs'), DataInputsType, scope=CTD_ANON_6, documentation=u'Inputs that were provided as part of the execute request. This element shall be omitted unless the lineage attribute of the execute request is set to "true".'))
CTD_ANON_6._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Process')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Status')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataInputs')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OutputDefinitions')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessOutputs')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_6._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_6._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), _ows.CodeType, scope=CTD_ANON_7, documentation=u'Unique identifier or name of this dataset. '))
CTD_ANON_7._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_7._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_7._GroupModel, min_occurs=1, max_occurs=1)



InputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'BoundingBoxData'), SupportedCRSsType, scope=InputDescriptionType, documentation=u'Indicates that this Input shall be a BoundingBox data structure that is embedded in the execute request, and provides a list of the Coordinate Reference System support for this Bounding Box. '))

InputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ComplexData'), SupportedComplexDataInputType, scope=InputDescriptionType, documentation=u'Indicates that this Input shall be a complex data structure (such as a GML document), and provides a list of Formats, Encodings, and Schemas supported for this Input. The value of this ComplexData structure can be input either embedded in the Execute request or remotely accessible to the server.  The client can select from among the identified combinations of Formats, Encodings, and Schemas to specify the form of the Input. This allows for complete specification of particular versions of GML, or image formats. '))

InputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LiteralData'), LiteralInputType, scope=InputDescriptionType, documentation=u'Indicates that this Input shall be a simple numeric value or character string that is embedded in the execute request, and describes the possible values. '))
InputDescriptionType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Metadata')), min_occurs=0L, max_occurs=None)
    )
InputDescriptionType._GroupModel_3 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'ComplexData')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'LiteralData')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'BoundingBoxData')), min_occurs=1, max_occurs=1)
    )
InputDescriptionType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputDescriptionType._GroupModel_3, min_occurs=1, max_occurs=1)
    )
InputDescriptionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputDescriptionType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputDescriptionType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
InputDescriptionType._ContentModel = pyxb.binding.content.ParticleModel(InputDescriptionType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'UOM'), _ows.DomainMetadataType, scope=CTD_ANON_8, documentation=u'Definition of the unit of measure of this set of values. In this case, the xlink:href attribute can reference a URN for a well-known unit of measure (uom). For example, such a URN could be a UOM identification URN defined in the "ogc" URN namespace. '))
CTD_ANON_8._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'UOM')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_8._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_8._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Language'), pyxb.binding.datatypes.language, scope=CTD_ANON_9, documentation=u'Identifier of a language used by the data(set) contents. This language identifier shall be as specified in IETF RFC 4646. When this element is omitted, the language used is not identified. '))
CTD_ANON_9._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Language')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_9._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_9._GroupModel, min_occurs=1, max_occurs=1)



SupportedComplexDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Supported'), ComplexDataCombinationsType, scope=SupportedComplexDataType, documentation=u'Unordered list of combinations of format, encoding, and schema supported for this Input/Output. This element shall be repeated for each combination of MimeType/Encoding/Schema that is supported for this Input/Output. This list shall include the default MimeType/Encoding/Schema. '))

SupportedComplexDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Default'), ComplexDataCombinationType, scope=SupportedComplexDataType, documentation=u'Identifies the default combination of Format, Encoding, and Schema supported for this Input/Output. The process shall expect input in or produce output in this combination of MimeType/Encoding/Schema unless the Execute request specifies otherwise.  '))
SupportedComplexDataType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SupportedComplexDataType._UseForTag(pyxb.namespace.ExpandedName(None, u'Default')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SupportedComplexDataType._UseForTag(pyxb.namespace.ExpandedName(None, u'Supported')), min_occurs=1, max_occurs=1)
    )
SupportedComplexDataType._ContentModel = pyxb.binding.content.ParticleModel(SupportedComplexDataType._GroupModel, min_occurs=1, max_occurs=1)



ResponseFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ResponseDocument'), ResponseDocumentType, scope=ResponseFormType, documentation=u'Indicates that the outputs shall be returned as part of a WPS response document.'))

ResponseFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RawDataOutput'), OutputDefinitionType, scope=ResponseFormType, documentation=u'Indicates that the output shall be returned directly as raw data, without a WPS response document.'))
ResponseFormType._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(ResponseFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ResponseDocument')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ResponseFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RawDataOutput')), min_occurs=1, max_occurs=1)
    )
ResponseFormType._ContentModel = pyxb.binding.content.ParticleModel(ResponseFormType._GroupModel, min_occurs=1, max_occurs=1)



ProcessBriefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WSDL'), CTD_ANON_4, scope=ProcessBriefType, documentation=u'Location of a WSDL document.'))

ProcessBriefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Profile'), pyxb.binding.datatypes.anyURI, scope=ProcessBriefType, documentation=u'Optional unordered list of application profiles to which this process complies.'))
ProcessBriefType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Metadata')), min_occurs=0L, max_occurs=None)
    )
ProcessBriefType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Profile')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ProcessBriefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WSDL')), min_occurs=0L, max_occurs=1)
    )
ProcessBriefType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessBriefType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessBriefType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
ProcessBriefType._ContentModel = pyxb.binding.content.ParticleModel(ProcessBriefType._GroupModel, min_occurs=1, max_occurs=1)


SupportedComplexDataInputType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SupportedComplexDataInputType._UseForTag(pyxb.namespace.ExpandedName(None, u'Default')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SupportedComplexDataInputType._UseForTag(pyxb.namespace.ExpandedName(None, u'Supported')), min_occurs=1, max_occurs=1)
    )
SupportedComplexDataInputType._ContentModel = pyxb.binding.content.ParticleModel(SupportedComplexDataInputType._GroupModel, min_occurs=1, max_occurs=1)



CRSsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CRS'), pyxb.binding.datatypes.anyURI, scope=CRSsType, documentation=u'Reference to a CRS supported for this Input/Output. '))
CRSsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CRSsType._UseForTag(pyxb.namespace.ExpandedName(None, u'CRS')), min_occurs=1, max_occurs=None)
    )
CRSsType._ContentModel = pyxb.binding.content.ParticleModel(CRSsType._GroupModel, min_occurs=1, max_occurs=1)


ComplexDataType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), min_occurs=0, max_occurs=None)
    )
ComplexDataType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    
    )
ComplexDataType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ComplexDataType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ComplexDataType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
ComplexDataType._ContentModel = pyxb.binding.content.ParticleModel(ComplexDataType._GroupModel, min_occurs=1, max_occurs=1)



WPSCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WSDL'), CTD_ANON_4, scope=WPSCapabilitiesType, documentation=u'Location of a WSDL document.'))

WPSCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProcessOfferings'), CTD_ANON_, scope=WPSCapabilitiesType, documentation=u'List of brief descriptions of the processes offered by this WPS server. '))

WPSCapabilitiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Languages'), CTD_ANON_5, scope=WPSCapabilitiesType, documentation=u'Listing of the default and other languages supported by this service. '))
WPSCapabilitiesType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'ServiceIdentification')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'ServiceProvider')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'OperationsMetadata')), min_occurs=0L, max_occurs=1)
    )
WPSCapabilitiesType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProcessOfferings')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Languages')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(WPSCapabilitiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WSDL')), min_occurs=0L, max_occurs=1)
    )
WPSCapabilitiesType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(WPSCapabilitiesType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(WPSCapabilitiesType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
WPSCapabilitiesType._ContentModel = pyxb.binding.content.ParticleModel(WPSCapabilitiesType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Output'), OutputDataType, scope=CTD_ANON_11, documentation=u'Unordered list of values of all the outputs produced by this process. It is not necessary to include an output until the Status is ProcessSucceeded. '))
CTD_ANON_11._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_11._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_11._GroupModel, min_occurs=1, max_occurs=1)



ComplexDataDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Schema'), pyxb.binding.datatypes.anyURI, scope=ComplexDataDescriptionType, documentation=u'Reference to a definition of XML elements or types supported for this Input/Output (e.g., GML 2.1 Application Schema). Each of these XML elements or types shall be defined in a separate XML Schema Document. This parameter shall be included when this input/output is XML encoded using an XML schema. When included, the input/output shall validate against the referenced XML Schema. This element shall be omitted if Schema does not apply to this Input/Output. Note: If the Input/Output uses a profile of a larger schema, the server administrator should provide that schema profile for validation purposes. '))

ComplexDataDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MimeType'), _ows.MimeType, scope=ComplexDataDescriptionType, documentation=u'Mime type supported for this input or output (e.g., text/xml). '))

ComplexDataDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Encoding'), pyxb.binding.datatypes.anyURI, scope=ComplexDataDescriptionType, documentation=u'Reference to an encoding supported for this input or output (e.g., UTF-8).  This element shall be omitted if Encoding does not apply to this Input/Output. '))
ComplexDataDescriptionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ComplexDataDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'MimeType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ComplexDataDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Encoding')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ComplexDataDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Schema')), min_occurs=0L, max_occurs=1)
    )
ComplexDataDescriptionType._ContentModel = pyxb.binding.content.ParticleModel(ComplexDataDescriptionType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Output'), OutputDescriptionType, scope=CTD_ANON_12, documentation=u'Unordered list of one or more descriptions of all the outputs that can result from executing this process. At least one output is required from each process. '))
CTD_ANON_12._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, u'Output')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_12._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_12._GroupModel, min_occurs=1, max_occurs=1)



OutputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'LiteralOutput'), LiteralOutputType, scope=OutputDescriptionType, documentation=u'Indicates that this output shall be a simple literal value (such as an integer) that is embedded in the execute response, and describes that output. '))

OutputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ComplexOutput'), SupportedComplexDataType, scope=OutputDescriptionType, documentation=u'Indicates that this Output shall be a complex data structure (such as a GML fragment) that is returned by the execute operation response. The value of this complex data structure can be output either embedded in the execute operation response or remotely accessible to the client. When this output form is indicated, the process produces only a single output, and "store" is "false, the output shall be returned directly, without being embedded in the XML document that is otherwise provided by execute operation response. \n\t\t\t\t\tThis element also provides a list of format, encoding, and schema combinations supported for this output. The client can select from among the identified combinations of formats, encodings, and schemas to specify the form of the output. This allows for complete specification of particular versions of GML, or image formats. '))

OutputDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'BoundingBoxOutput'), SupportedCRSsType, scope=OutputDescriptionType, documentation=u'Indicates that this output shall be a BoundingBox data structure, and provides a list of the CRSs supported in these Bounding Boxes. This element shall be included when this process output is an ows:BoundingBox element. '))
OutputDescriptionType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Metadata')), min_occurs=0L, max_occurs=None)
    )
OutputDescriptionType._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'ComplexOutput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'LiteralOutput')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'BoundingBoxOutput')), min_occurs=1, max_occurs=1)
    )
OutputDescriptionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OutputDescriptionType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OutputDescriptionType._GroupModel_2, min_occurs=1, max_occurs=1)
    )
OutputDescriptionType._ContentModel = pyxb.binding.content.ParticleModel(OutputDescriptionType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CRS'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_13, documentation=u'Reference to the default CRS supported for this Input/Output'))
CTD_ANON_13._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'CRS')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_13._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_13._GroupModel, min_occurs=1, max_occurs=1)



SupportedUOMsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Supported'), UOMsType, scope=SupportedUOMsType, documentation=u'Unordered list of references to all of the UOMs supported for this input or output, if UOM is applicable. The default UOM shall be included in this list. '))

SupportedUOMsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Default'), CTD_ANON_8, scope=SupportedUOMsType, documentation=u'Reference to the default UOM supported for this input or output, if UoM is applicable. The process shall expect input in or produce output in this UOM unless the Execute request specifies another supported UOM. '))
SupportedUOMsType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SupportedUOMsType._UseForTag(pyxb.namespace.ExpandedName(None, u'Default')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SupportedUOMsType._UseForTag(pyxb.namespace.ExpandedName(None, u'Supported')), min_occurs=1, max_occurs=1)
    )
SupportedUOMsType._ContentModel = pyxb.binding.content.ParticleModel(SupportedUOMsType._GroupModel, min_occurs=1, max_occurs=1)



ProcessDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'DataInputs'), CTD_ANON_14, scope=ProcessDescriptionType, documentation=u'List of the inputs to this process. In almost all cases, at least one process input is required. However, no process inputs may be identified when all the inputs are predetermined fixed resources.  In this case, those resources shall be identified in the ows:Abstract element that describes the process.'))

ProcessDescriptionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ProcessOutputs'), CTD_ANON_12, scope=ProcessDescriptionType, documentation=u'List of outputs which will or can result from executing the process. '))
ProcessDescriptionType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Metadata')), min_occurs=0L, max_occurs=None)
    )
ProcessDescriptionType._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Profile')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WSDL')), min_occurs=0L, max_occurs=1)
    )
ProcessDescriptionType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._GroupModel_3, min_occurs=1, max_occurs=1)
    )
ProcessDescriptionType._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'DataInputs')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._UseForTag(pyxb.namespace.ExpandedName(None, u'ProcessOutputs')), min_occurs=1, max_occurs=1)
    )
ProcessDescriptionType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ProcessDescriptionType._GroupModel_4, min_occurs=1, max_occurs=1)
    )
ProcessDescriptionType._ContentModel = pyxb.binding.content.ParticleModel(ProcessDescriptionType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Input'), InputDescriptionType, scope=CTD_ANON_14, documentation=u'Unordered list of one or more descriptions of the inputs that can be accepted by this process, including all required and optional inputs.  Where an input is optional because a default value exists, that default value must be identified in the "ows:Abstract" element for that input, except in the case of LiteralData, where the default must be indicated in the corresponding ows:DefaultValue element. Where an input is optional because it depends on the value(s) of other inputs, this must be indicated in the ows:Abstract element for that input. '))
CTD_ANON_14._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, u'Input')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_14._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ResponseForm'), ResponseFormType, scope=CTD_ANON_15, documentation=u'Defines the response type of the WPS, either raw data or XML document.  If absent, the response shall be a response document which includes all outputs encoded in the response.'))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), _ows.CodeType, scope=CTD_ANON_15, documentation=u'Unique identifier or name of this dataset. '))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataInputs'), DataInputsType, scope=CTD_ANON_15, documentation=u'List of input (or parameter) values provided to the process, including each of the Inputs needed to execute the process. It is possible to have no inputs provided only when all the inputs are predetermined fixed resources. In all other cases, at least one input is required. '))
CTD_ANON_15._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataInputs')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ResponseForm')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_15._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_15._GroupModel, min_occurs=1, max_occurs=1)



InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), InputReferenceType, scope=InputType, documentation=u'Identifies this input value as a web accessible resource, and references that resource. '))

InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier'), _ows.CodeType, scope=InputType, documentation=u'Unique identifier or name of this dataset. '))

InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract'), _ows.LanguageStringType, scope=InputType, documentation=u'Brief narrative description of this resource, normally used for display to a human. '))

InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title'), _ows.LanguageStringType, scope=InputType, documentation=u'Title of this resource, normally used for display to a human. '))

InputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Data'), DataType, scope=InputType, documentation=u'Identifies this input value as a data embedded in this request, and includes that data. '))
InputType._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(InputType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reference')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Data')), min_occurs=1, max_occurs=1)
    )
InputType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Identifier')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Title')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputType._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/ows/1.1'), u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputType._GroupModel_, min_occurs=1, max_occurs=1)
    )
InputType._ContentModel = pyxb.binding.content.ParticleModel(InputType._GroupModel, min_occurs=1, max_occurs=1)



ResponseDocumentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Output'), DocumentOutputDefinitionType, scope=ResponseDocumentType, documentation=u'Unordered list of definitions of the outputs (or parameters) requested from the process. These outputs are not normally identified, unless the client is specifically requesting a limited subset of outputs, and/or is requesting output formats and/or schemas and/or encodings different from the defaults and selected from the alternatives identified in the process description, or wishes to customize the descriptive information about the output. '))
ResponseDocumentType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ResponseDocumentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Output')), min_occurs=1, max_occurs=None)
    )
ResponseDocumentType._ContentModel = pyxb.binding.content.ParticleModel(ResponseDocumentType._GroupModel, min_occurs=1, max_occurs=1)
