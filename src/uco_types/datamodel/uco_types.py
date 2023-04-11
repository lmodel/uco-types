# Auto generated from uco_types.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-11T23:11:54
# Schema: uco-types
#
# id: https://w3id.org/lmodel/uco-types
# description:
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "1.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AFC = CurieNamespace('AFC', 'http://purl.allotrope.org/ontologies/common#AFC_')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ERO = CurieNamespace('ERO', 'http://purl.obolibrary.org/obo/ERO_')
GSSO = CurieNamespace('GSSO', 'http://purl.obolibrary.org/obo/GSSO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://identifiers.org/wikidata/')
CO = CurieNamespace('co', 'http://purl.org/co/')
COLLECTIONS = CurieNamespace('collections', 'https://w3id.org/lmodel/collections/')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/uco-core/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EDAM_DATA = CurieNamespace('edam_data', 'http://edamontology.org/data_')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LM_CORE = CurieNamespace('lm_core', 'https://w3id.org/lmodel/core/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SCHEMA_COLLECTIONS = CurieNamespace('schema_collections', 'https://w3id.org/lmodel/collections/schema/')
SCHEMA_UCO_CORE = CurieNamespace('schema_uco_core', 'https://w3id.org/lmodel/uco-core/schema/')
SCHEMA_UCO_VOCABULARY = CurieNamespace('schema_uco_vocabulary', 'https://w3id.org/lmodel/uco-vocabulary/schema/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
TYPES = CurieNamespace('types', 'https://w3id.org/lmodel/uco-types/')
VOCABULARY = CurieNamespace('vocabulary', 'https://w3id.org/lmodel/uco-vocabulary/')
WIKIDATA = CurieNamespace('wikidata', 'http://identifiers.org/wikidata/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TYPES


# Types
class PositiveInteger(Integer):
    """ integer greater than zero; natural number explicitly excluding zero """
    type_class_uri = XSD.positiveInteger
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive integer"
    type_model_uri = TYPES.PositiveInteger


class StringType(String):
    """ A string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string type"
    type_model_uri = TYPES.StringType


class LiteralType(String):
    """ Literals are used for values such as strings, numbers, and dates. """
    type_class_uri = RDF.literal
    type_class_curie = "rdf:literal"
    type_name = "literal type"
    type_model_uri = TYPES.LiteralType


class NonNegativeIntegerType(Integer):
    """ real number strictly greater than zero """
    type_class_uri = XSD.nonNegativeInteger
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "non negative integer type"
    type_model_uri = TYPES.NonNegativeIntegerType


class StatementType(StringType):
    """ "meaningful declarative sentence that is either true or false, or that which a true or false declarative sentence asserts" """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "statement type"
    type_model_uri = TYPES.StatementType


class IriType(Uriorcurie):
    """ A IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = TYPES.IriType


class BooleanType(Boolean):
    """ A boolean value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean type"
    type_model_uri = TYPES.BooleanType


class HexBinaryType(hex):
    """ "Represents arbitrary hex-encoded binary data" """
    type_class_uri = XSD.hexBinary
    type_class_curie = "xsd:hexBinary"
    type_name = "hex binary type"
    type_model_uri = TYPES.HexBinaryType


# Class references



@dataclass
class ThreadItem(YAMLRoot):
    """
    "A ThreadItem is a member of a thread."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.CoItem
    class_class_curie: ClassVar[str] = "collections:CoItem"
    class_name: ClassVar[str] = "ThreadItem"
    class_model_uri: ClassVar[URIRef] = TYPES.ThreadItem

    itemContent: Optional[Union[Union[dict, "CoItem"], List[Union[dict, "CoItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.itemContent, list):
            self.itemContent = [self.itemContent] if self.itemContent is not None else []
        self.itemContent = [v if isinstance(v, CoItem) else CoItem(**as_dict(v)) for v in self.itemContent]

        super().__post_init__(**kwargs)


class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Thing
    class_class_curie: ClassVar[str] = "collections:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = TYPES.Thing


@dataclass
class Collection(Thing):
    """
    A group of objects that can be considered as a whole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Collection
    class_class_curie: ClassVar[str] = "collections:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = TYPES.Collection

    element: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    size: Optional[Union[int, PositiveInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.element]

        if self.size is not None and not isinstance(self.size, PositiveInteger):
            self.size = PositiveInteger(self.size)

        super().__post_init__(**kwargs)


class Bag(Collection):
    """
    Collection that can have a number of copies of each object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Bag
    class_class_curie: ClassVar[str] = "collections:Bag"
    class_name: ClassVar[str] = "Bag"
    class_model_uri: ClassVar[URIRef] = TYPES.Bag


@dataclass
class Thread(Bag):
    """
    "A semi-ordered array of items, that can be present in multiple copies. Implemetation of a UCO Thread is similar
    to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or
    more direct successors, and two or more direct predecessors."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Thread
    class_class_curie: ClassVar[str] = "types:Thread"
    class_name: ClassVar[str] = "Thread"
    class_model_uri: ClassVar[URIRef] = TYPES.Thread

    item: Optional[Union[Union[dict, "ThreadItem"], List[Union[dict, "ThreadItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.item, list):
            self.item = [self.item] if self.item is not None else []
        self.item = [v if isinstance(v, ThreadItem) else ThreadItem(**as_dict(v)) for v in self.item]

        super().__post_init__(**kwargs)


@dataclass
class CoItem(Thing):
    """
    Element belonging to a bag
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.CoItem
    class_class_curie: ClassVar[str] = "collections:CoItem"
    class_name: ClassVar[str] = "CoItem"
    class_model_uri: ClassVar[URIRef] = TYPES.CoItem

    itemOf: Optional[Union[dict, Bag]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.itemOf is not None and not isinstance(self.itemOf, Bag):
            self.itemOf = Bag(**as_dict(self.itemOf))

        super().__post_init__(**kwargs)


@dataclass
class List(Bag):
    """
    An ordered array of items, that can be present in multiple copies
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.List
    class_class_curie: ClassVar[str] = "collections:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = TYPES.List

    item: Optional[Union[Union[dict, "ListItem"], List[Union[dict, "ListItem"]]]] = empty_list()
    lastItem: Optional[Union[dict, "ListItem"]] = None
    firstItem: Optional[Union[dict, "ListItem"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="item", slot_type=ListItem, key_name="_index", keyed=False)

        if self.lastItem is not None and not isinstance(self.lastItem, ListItem):
            self.lastItem = ListItem(**as_dict(self.lastItem))

        if self.firstItem is not None and not isinstance(self.firstItem, ListItem):
            self.firstItem = ListItem(**as_dict(self.firstItem))

        super().__post_init__(**kwargs)


@dataclass
class ListItem(CoItem):
    """
    element belonging to a list
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.ListItem
    class_class_curie: ClassVar[str] = "collections:ListItem"
    class_name: ClassVar[str] = "ListItem"
    class_model_uri: ClassVar[URIRef] = TYPES.ListItem

    _index: Union[int, PositiveInteger] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self._index):
            self.MissingRequiredField("_index")
        if not isinstance(self._index, PositiveInteger):
            self._index = PositiveInteger(self._index)

        super().__post_init__(**kwargs)


class Set(Collection):
    """
    A collection that cannot contain duplicate elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Set
    class_class_curie: ClassVar[str] = "collections:Set"
    class_name: ClassVar[str] = "Set"
    class_model_uri: ClassVar[URIRef] = TYPES.Set


class UcoThing(YAMLRoot):
    """
    UcoThing is the top-level class within UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoThing
    class_class_curie: ClassVar[str] = "core:UcoThing"
    class_name: ClassVar[str] = "UcoThing"
    class_model_uri: ClassVar[URIRef] = TYPES.UcoThing


class UcoInherentCharacterizationThing(UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a
    UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoInherentCharacterizationThing
    class_class_curie: ClassVar[str] = "core:UcoInherentCharacterizationThing"
    class_name: ClassVar[str] = "UcoInherentCharacterizationThing"
    class_model_uri: ClassVar[URIRef] = TYPES.UcoInherentCharacterizationThing


@dataclass
class Dictionary(UcoInherentCharacterizationThing):
    """
    "A dictionary is list of (term/key, value) pairs with each term/key existing no more than once."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Dictionary
    class_class_curie: ClassVar[str] = "types:Dictionary"
    class_name: ClassVar[str] = "Dictionary"
    class_model_uri: ClassVar[URIRef] = TYPES.Dictionary

    entry: Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.entry):
            self.MissingRequiredField("entry")
        self._normalize_inlined_as_dict(slot_name="entry", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ControlledDictionary(Dictionary):
    """
    "A controlled dictionary is a list of (term/key, value) pairs where each term/key exists no more than once and is
    constrained to an explicitly defined set of values."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.ControlledDictionary
    class_class_curie: ClassVar[str] = "types:ControlledDictionary"
    class_name: ClassVar[str] = "ControlledDictionary"
    class_model_uri: ClassVar[URIRef] = TYPES.ControlledDictionary

    entry: Optional[Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entry", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DictionaryEntry(UcoInherentCharacterizationThing):
    """
    "A dictionary entry is a single (term/key, value) pair."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.DictionaryEntry
    class_class_curie: ClassVar[str] = "types:DictionaryEntry"
    class_name: ClassVar[str] = "DictionaryEntry"
    class_model_uri: ClassVar[URIRef] = TYPES.DictionaryEntry

    key: str = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class ControlledDictionaryEntry(DictionaryEntry):
    """
    "A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an
    explicitly defined set of values."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.ControlledDictionaryEntry
    class_class_curie: ClassVar[str] = "types:ControlledDictionaryEntry"
    class_name: ClassVar[str] = "ControlledDictionaryEntry"
    class_model_uri: ClassVar[URIRef] = TYPES.ControlledDictionaryEntry

    key: str = None
    value: str = None

@dataclass
class Hash(UcoInherentCharacterizationThing):
    """
    "A hash is a grouping of characteristics unique to the result of applying a mathematical algorithm that maps data
    of arbitrary size to a bit string (the 'hash') and is a one-way function, that is, a function which is practically
    infeasible to invert. This is commonly used for integrity checking of data. [based on
    https://en.wikipedia.org/wiki/Cryptographic_hash_function]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Hash
    class_class_curie: ClassVar[str] = "types:Hash"
    class_name: ClassVar[str] = "Hash"
    class_model_uri: ClassVar[URIRef] = TYPES.Hash

    hashValue: hex = None
    hashMethod: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.hashValue):
            self.MissingRequiredField("hashValue")
        if not isinstance(self.hashValue, hex):
            self.hashValue = hex(self.hashValue)

        if self._is_empty(self.hashMethod):
            self.MissingRequiredField("hashMethod")
        if not isinstance(self.hashMethod, str):
            self.hashMethod = str(self.hashMethod)

        super().__post_init__(**kwargs)


@dataclass
class ExternalReference(UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ExternalReference
    class_class_curie: ClassVar[str] = "core:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = TYPES.ExternalReference

    referenceURL: Optional[Union[str, IriType]] = None
    definingContext: Optional[str] = None
    externalIdentifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.referenceURL is not None and not isinstance(self.referenceURL, IriType):
            self.referenceURL = IriType(self.referenceURL)

        if self.definingContext is not None and not isinstance(self.definingContext, str):
            self.definingContext = str(self.definingContext)

        if self.externalIdentifier is not None and not isinstance(self.externalIdentifier, str):
            self.externalIdentifier = str(self.externalIdentifier)

        super().__post_init__(**kwargs)


class Facet(UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Facet
    class_class_curie: ClassVar[str] = "core:Facet"
    class_name: ClassVar[str] = "Facet"
    class_model_uri: ClassVar[URIRef] = TYPES.Facet


@dataclass
class ConfidenceFacet(Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some
    information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ConfidenceFacet
    class_class_curie: ClassVar[str] = "core:ConfidenceFacet"
    class_name: ClassVar[str] = "ConfidenceFacet"
    class_model_uri: ClassVar[URIRef] = TYPES.ConfidenceFacet

    confidence: Union[int, NonNegativeIntegerType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.confidence):
            self.MissingRequiredField("confidence")
        if not isinstance(self.confidence, NonNegativeIntegerType):
            self.confidence = NonNegativeIntegerType(self.confidence)

        super().__post_init__(**kwargs)


@dataclass
class UcoObject(UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or
    indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and
    relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent,
    unifying and interoperable foundation for all explicit and inter-relatable content objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoObject
    class_class_curie: ClassVar[str] = "core:UcoObject"
    class_name: ClassVar[str] = "UcoObject"
    class_model_uri: ClassVar[URIRef] = TYPES.UcoObject

    createdBy: Optional[str] = None
    description: Optional[Union[str, List[str]]] = empty_list()
    externalReference: Optional[Union[str, List[str]]] = empty_list()
    hasFacet: Optional[Union[str, List[str]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectMarking: Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]] = empty_list()
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.createdBy is not None and not isinstance(self.createdBy, str):
            self.createdBy = str(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, str) else str(v) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, str) else str(v) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstraction) else MarkingDefinitionAbstraction(**as_dict(v)) for v in self.objectMarking]

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        super().__post_init__(**kwargs)


@dataclass
class Assertion(UcoObject):
    """
    An assertion is a statement declared to be true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Assertion
    class_class_curie: ClassVar[str] = "core:Assertion"
    class_name: ClassVar[str] = "Assertion"
    class_model_uri: ClassVar[URIRef] = TYPES.Assertion

    statement: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.statement, list):
            self.statement = [self.statement] if self.statement is not None else []
        self.statement = [v if isinstance(v, str) else str(v) for v in self.statement]

        super().__post_init__(**kwargs)


@dataclass
class Annotation(Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Annotation
    class_class_curie: ClassVar[str] = "core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = TYPES.Annotation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class AttributedName(UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming authority.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.AttributedName
    class_class_curie: ClassVar[str] = "core:AttributedName"
    class_name: ClassVar[str] = "AttributedName"
    class_model_uri: ClassVar[URIRef] = TYPES.AttributedName

    namingAuthority: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.namingAuthority is not None and not isinstance(self.namingAuthority, str):
            self.namingAuthority = str(self.namingAuthority)

        super().__post_init__(**kwargs)


class Compilation(UcoObject):
    """
    A compilation is a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Compilation
    class_class_curie: ClassVar[str] = "core:Compilation"
    class_name: ClassVar[str] = "Compilation"
    class_model_uri: ClassVar[URIRef] = TYPES.Compilation


@dataclass
class ContextualCompilation(Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed
    on a given day, all accounts associated with a given person).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ContextualCompilation
    class_class_curie: ClassVar[str] = "core:ContextualCompilation"
    class_name: ClassVar[str] = "ContextualCompilation"
    class_model_uri: ClassVar[URIRef] = TYPES.ContextualCompilation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class ControlledVocabulary(UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ControlledVocabulary
    class_class_curie: ClassVar[str] = "core:ControlledVocabulary"
    class_name: ClassVar[str] = "ControlledVocabulary"
    class_model_uri: ClassVar[URIRef] = TYPES.ControlledVocabulary

    value: str = None
    constrainingVocabularyReference: Optional[Union[str, IriType]] = None
    constrainingVocabularyName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.constrainingVocabularyReference is not None and not isinstance(self.constrainingVocabularyReference, IriType):
            self.constrainingVocabularyReference = IriType(self.constrainingVocabularyReference)

        if self.constrainingVocabularyName is not None and not isinstance(self.constrainingVocabularyName, str):
            self.constrainingVocabularyName = str(self.constrainingVocabularyName)

        super().__post_init__(**kwargs)


@dataclass
class EnclosingCompilation(Compilation):
    """
    An enclosing compilation is a container for a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.EnclosingCompilation
    class_class_curie: ClassVar[str] = "core:EnclosingCompilation"
    class_name: ClassVar[str] = "EnclosingCompilation"
    class_model_uri: ClassVar[URIRef] = TYPES.EnclosingCompilation

    object: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


class Bundle(EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Bundle
    class_class_curie: ClassVar[str] = "core:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = TYPES.Bundle


@dataclass
class Grouping(ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Grouping
    class_class_curie: ClassVar[str] = "core:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = TYPES.Grouping

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    context: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.context, list):
            self.context = [self.context] if self.context is not None else []
        self.context = [v if isinstance(v, str) else str(v) for v in self.context]

        super().__post_init__(**kwargs)


class IdentityAbstraction(UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the identity:Identity class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.IdentityAbstraction
    class_class_curie: ClassVar[str] = "core:IdentityAbstraction"
    class_name: ClassVar[str] = "IdentityAbstraction"
    class_model_uri: ClassVar[URIRef] = TYPES.IdentityAbstraction


class Item(UcoObject):
    """
    An item is a distinct article or unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Item
    class_class_curie: ClassVar[str] = "core:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = TYPES.Item


class MarkingDefinitionAbstraction(UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data
    marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the marking MarkingDefinition class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.MarkingDefinitionAbstraction
    class_class_curie: ClassVar[str] = "core:MarkingDefinitionAbstraction"
    class_name: ClassVar[str] = "MarkingDefinitionAbstraction"
    class_model_uri: ClassVar[URIRef] = TYPES.MarkingDefinitionAbstraction


class ModusOperandi(UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ModusOperandi
    class_class_curie: ClassVar[str] = "core:ModusOperandi"
    class_name: ClassVar[str] = "ModusOperandi"
    class_model_uri: ClassVar[URIRef] = TYPES.ModusOperandi


@dataclass
class Relationship(UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to
    another object in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Relationship
    class_class_curie: ClassVar[str] = "core:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = TYPES.Relationship

    isDirectional: Union[bool, BooleanType] = None
    source: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    target: Union[dict, "UcoObject"] = None
    endTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    kindOfRelationship: Optional[str] = None
    startTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.isDirectional):
            self.MissingRequiredField("isDirectional")
        if not isinstance(self.isDirectional, BooleanType):
            self.isDirectional = BooleanType(self.isDirectional)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.source]

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, UcoObject):
            self.target = UcoObject(**as_dict(self.target))

        if not isinstance(self.endTime, list):
            self.endTime = [self.endTime] if self.endTime is not None else []
        self.endTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.endTime]

        if self.kindOfRelationship is not None and not isinstance(self.kindOfRelationship, str):
            self.kindOfRelationship = str(self.kindOfRelationship)

        if not isinstance(self.startTime, list):
            self.startTime = [self.startTime] if self.startTime is not None else []
        self.startTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.startTime]

        super().__post_init__(**kwargs)


# Enumerations
class AccountTypeEnum(EnumDefinitionImpl):
    """
    "An account type represents the endpoint type where the account is located; for example, ADS for an
    ActiveDirectory endpoint type, or LDAP for an LDAP, etc."
    """
    ldap = PermissibleValue(text="ldap")
    nis = PermissibleValue(text="nis")
    openid = PermissibleValue(text="openid")
    radius = PermissibleValue(text="radius")
    tacacs = PermissibleValue(text="tacacs")
    unix = PermissibleValue(text="unix")
    windows_domain = PermissibleValue(text="windows_domain")
    windows_local = PermissibleValue(text="windows_local")

    _defn = EnumDefinition(
        name="AccountTypeEnum",
        description="\"An account type represents the endpoint type where the account is located; for example, ADS for an ActiveDirectory endpoint type, or LDAP for an LDAP, etc.\"",
    )

class ActionArgumentNameEnum(EnumDefinitionImpl):

    API = PermissibleValue(text="API")
    Command = PermissibleValue(text="Command")
    Flags = PermissibleValue(text="Flags")
    Hostname = PermissibleValue(text="Hostname")
    Options = PermissibleValue(text="Options")
    Password = PermissibleValue(text="Password")
    Protection = PermissibleValue(text="Protection")
    Reason = PermissibleValue(text="Reason")
    Server = PermissibleValue(text="Server")
    Username = PermissibleValue(text="Username")

    _defn = EnumDefinition(
        name="ActionArgumentNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "APC Address",
                PermissibleValue(text="APC Address") )
        setattr(cls, "APC Mode",
                PermissibleValue(text="APC Mode") )
        setattr(cls, "Access Mode",
                PermissibleValue(text="Access Mode") )
        setattr(cls, "Application Name",
                PermissibleValue(text="Application Name") )
        setattr(cls, "Base Address",
                PermissibleValue(text="Base Address") )
        setattr(cls, "Callback Address",
                PermissibleValue(text="Callback Address") )
        setattr(cls, "Code Address",
                PermissibleValue(text="Code Address") )
        setattr(cls, "Control Code",
                PermissibleValue(text="Control Code") )
        setattr(cls, "Control Parameter",
                PermissibleValue(text="Control Parameter") )
        setattr(cls, "Creation Flags",
                PermissibleValue(text="Creation Flags") )
        setattr(cls, "Database Name",
                PermissibleValue(text="Database Name") )
        setattr(cls, "Delay Time (ms)",
                PermissibleValue(text="Delay Time (ms)") )
        setattr(cls, "Destination Address",
                PermissibleValue(text="Destination Address") )
        setattr(cls, "Error Control",
                PermissibleValue(text="Error Control") )
        setattr(cls, "File Information Class",
                PermissibleValue(text="File Information Class") )
        setattr(cls, "Function Address",
                PermissibleValue(text="Function Address") )
        setattr(cls, "Function Name",
                PermissibleValue(text="Function Name") )
        setattr(cls, "Function Ordinal",
                PermissibleValue(text="Function Ordinal") )
        setattr(cls, "Hook Type",
                PermissibleValue(text="Hook Type") )
        setattr(cls, "Host Name",
                PermissibleValue(text="Host Name") )
        setattr(cls, "Initial Owner",
                PermissibleValue(text="Initial Owner") )
        setattr(cls, "Mapping Offset",
                PermissibleValue(text="Mapping Offset") )
        setattr(cls, "Number of Bytes Per Send",
                PermissibleValue(text="Number of Bytes Per Send") )
        setattr(cls, "Parameter Address",
                PermissibleValue(text="Parameter Address") )
        setattr(cls, "Privilege Name",
                PermissibleValue(text="Privilege Name") )
        setattr(cls, "Proxy Bypass",
                PermissibleValue(text="Proxy Bypass") )
        setattr(cls, "Proxy Name",
                PermissibleValue(text="Proxy Name") )
        setattr(cls, "Request Size",
                PermissibleValue(text="Request Size") )
        setattr(cls, "Requested Version",
                PermissibleValue(text="Requested Version") )
        setattr(cls, "Service Name",
                PermissibleValue(text="Service Name") )
        setattr(cls, "Service State",
                PermissibleValue(text="Service State") )
        setattr(cls, "Service Type",
                PermissibleValue(text="Service Type") )
        setattr(cls, "Share Mode",
                PermissibleValue(text="Share Mode") )
        setattr(cls, "Shutdown Flag",
                PermissibleValue(text="Shutdown Flag") )
        setattr(cls, "Size (bytes)",
                PermissibleValue(text="Size (bytes)") )
        setattr(cls, "Sleep Time (ms)",
                PermissibleValue(text="Sleep Time (ms)") )
        setattr(cls, "Source Address",
                PermissibleValue(text="Source Address") )
        setattr(cls, "Starting Address",
                PermissibleValue(text="Starting Address") )
        setattr(cls, "System Metric Index",
                PermissibleValue(text="System Metric Index") )
        setattr(cls, "Target PID",
                PermissibleValue(text="Target PID") )
        setattr(cls, "Transfer Flags",
                PermissibleValue(text="Transfer Flags") )

class ActionNameEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ActionNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Accept Socket Connection",
                PermissibleValue(text="Accept Socket Connection") )
        setattr(cls, "Add Connection to Network Share",
                PermissibleValue(text="Add Connection to Network Share") )
        setattr(cls, "Add Network Share",
                PermissibleValue(text="Add Network Share") )
        setattr(cls, "Add Scheduled Task",
                PermissibleValue(text="Add Scheduled Task") )
        setattr(cls, "Add System Call Hook",
                PermissibleValue(text="Add System Call Hook") )
        setattr(cls, "Add User",
                PermissibleValue(text="Add User") )
        setattr(cls, "Add Windows Hook",
                PermissibleValue(text="Add Windows Hook") )
        setattr(cls, "Allocate Virtual Memory in Process",
                PermissibleValue(text="Allocate Virtual Memory in Process") )
        setattr(cls, "Bind Address to Socket",
                PermissibleValue(text="Bind Address to Socket") )
        setattr(cls, "Change Service Configuration",
                PermissibleValue(text="Change Service Configuration") )
        setattr(cls, "Check for Remote Debugger",
                PermissibleValue(text="Check for Remote Debugger") )
        setattr(cls, "Close Port",
                PermissibleValue(text="Close Port") )
        setattr(cls, "Close Registry Key",
                PermissibleValue(text="Close Registry Key") )
        setattr(cls, "Close Socket",
                PermissibleValue(text="Close Socket") )
        setattr(cls, "Configure Service",
                PermissibleValue(text="Configure Service") )
        setattr(cls, "Connect to IP",
                PermissibleValue(text="Connect to IP") )
        setattr(cls, "Connect to Named Pipe",
                PermissibleValue(text="Connect to Named Pipe") )
        setattr(cls, "Connect to Network Share",
                PermissibleValue(text="Connect to Network Share") )
        setattr(cls, "Connect to Socket",
                PermissibleValue(text="Connect to Socket") )
        setattr(cls, "Connect to URL",
                PermissibleValue(text="Connect to URL") )
        setattr(cls, "Control Driver",
                PermissibleValue(text="Control Driver") )
        setattr(cls, "Control Service",
                PermissibleValue(text="Control Service") )
        setattr(cls, "Copy File",
                PermissibleValue(text="Copy File") )
        setattr(cls, "Create Dialog Box",
                PermissibleValue(text="Create Dialog Box") )
        setattr(cls, "Create Directory",
                PermissibleValue(text="Create Directory") )
        setattr(cls, "Create Event",
                PermissibleValue(text="Create Event") )
        setattr(cls, "Create File",
                PermissibleValue(text="Create File") )
        setattr(cls, "Create File Alternate Data Stream",
                PermissibleValue(text="Create File Alternate Data Stream") )
        setattr(cls, "Create File Mapping",
                PermissibleValue(text="Create File Mapping") )
        setattr(cls, "Create File Symbolic Link",
                PermissibleValue(text="Create File Symbolic Link") )
        setattr(cls, "Create Hidden File",
                PermissibleValue(text="Create Hidden File") )
        setattr(cls, "Create Mailslot",
                PermissibleValue(text="Create Mailslot") )
        setattr(cls, "Create Module",
                PermissibleValue(text="Create Module") )
        setattr(cls, "Create Mutex",
                PermissibleValue(text="Create Mutex") )
        setattr(cls, "Create Named Pipe",
                PermissibleValue(text="Create Named Pipe") )
        setattr(cls, "Create Process",
                PermissibleValue(text="Create Process") )
        setattr(cls, "Create Process as User",
                PermissibleValue(text="Create Process as User") )
        setattr(cls, "Create Registry Key",
                PermissibleValue(text="Create Registry Key") )
        setattr(cls, "Create Registry Key Value",
                PermissibleValue(text="Create Registry Key Value") )
        setattr(cls, "Create Remote Thread in Process",
                PermissibleValue(text="Create Remote Thread in Process") )
        setattr(cls, "Create Service",
                PermissibleValue(text="Create Service") )
        setattr(cls, "Create Socket",
                PermissibleValue(text="Create Socket") )
        setattr(cls, "Create Symbolic Link",
                PermissibleValue(text="Create Symbolic Link") )
        setattr(cls, "Create Thread",
                PermissibleValue(text="Create Thread") )
        setattr(cls, "Create Window",
                PermissibleValue(text="Create Window") )
        setattr(cls, "Delete Directory",
                PermissibleValue(text="Delete Directory") )
        setattr(cls, "Delete File",
                PermissibleValue(text="Delete File") )
        setattr(cls, "Delete Named Pipe",
                PermissibleValue(text="Delete Named Pipe") )
        setattr(cls, "Delete Network Share",
                PermissibleValue(text="Delete Network Share") )
        setattr(cls, "Delete Registry Key",
                PermissibleValue(text="Delete Registry Key") )
        setattr(cls, "Delete Registry Key Value",
                PermissibleValue(text="Delete Registry Key Value") )
        setattr(cls, "Delete Service",
                PermissibleValue(text="Delete Service") )
        setattr(cls, "Delete User",
                PermissibleValue(text="Delete User") )
        setattr(cls, "Disconnect from Named Pipe",
                PermissibleValue(text="Disconnect from Named Pipe") )
        setattr(cls, "Disconnect from Network Share",
                PermissibleValue(text="Disconnect from Network Share") )
        setattr(cls, "Disconnect from Socket",
                PermissibleValue(text="Disconnect from Socket") )
        setattr(cls, "Download File",
                PermissibleValue(text="Download File") )
        setattr(cls, "Enumerate DLLs",
                PermissibleValue(text="Enumerate DLLs") )
        setattr(cls, "Enumerate Network Shares",
                PermissibleValue(text="Enumerate Network Shares") )
        setattr(cls, "Enumerate Processes",
                PermissibleValue(text="Enumerate Processes") )
        setattr(cls, "Enumerate Protocols",
                PermissibleValue(text="Enumerate Protocols") )
        setattr(cls, "Enumerate Registry Key Subkeys",
                PermissibleValue(text="Enumerate Registry Key Subkeys") )
        setattr(cls, "Enumerate Registry Key Values",
                PermissibleValue(text="Enumerate Registry Key Values") )
        setattr(cls, "Enumerate Services",
                PermissibleValue(text="Enumerate Services") )
        setattr(cls, "Enumerate System Handles",
                PermissibleValue(text="Enumerate System Handles") )
        setattr(cls, "Enumerate Threads",
                PermissibleValue(text="Enumerate Threads") )
        setattr(cls, "Enumerate Threads in Process",
                PermissibleValue(text="Enumerate Threads in Process") )
        setattr(cls, "Enumerate Users",
                PermissibleValue(text="Enumerate Users") )
        setattr(cls, "Enumerate Windows",
                PermissibleValue(text="Enumerate Windows") )
        setattr(cls, "Find File",
                PermissibleValue(text="Find File") )
        setattr(cls, "Find Window",
                PermissibleValue(text="Find Window") )
        setattr(cls, "Flush Process Instruction Cache",
                PermissibleValue(text="Flush Process Instruction Cache") )
        setattr(cls, "Free Library",
                PermissibleValue(text="Free Library") )
        setattr(cls, "Free Process Virtual Memory",
                PermissibleValue(text="Free Process Virtual Memory") )
        setattr(cls, "Get Disk Free Space",
                PermissibleValue(text="Get Disk Free Space") )
        setattr(cls, "Get Disk Type",
                PermissibleValue(text="Get Disk Type") )
        setattr(cls, "Get Elapsed System Up Time",
                PermissibleValue(text="Get Elapsed System Up Time") )
        setattr(cls, "Get File Attributes",
                PermissibleValue(text="Get File Attributes") )
        setattr(cls, "Get Function Address",
                PermissibleValue(text="Get Function Address") )
        setattr(cls, "Get Host By Address",
                PermissibleValue(text="Get Host By Address") )
        setattr(cls, "Get Host By Name",
                PermissibleValue(text="Get Host By Name") )
        setattr(cls, "Get Host Name",
                PermissibleValue(text="Get Host Name") )
        setattr(cls, "Get Library File Name",
                PermissibleValue(text="Get Library File Name") )
        setattr(cls, "Get Library Handle",
                PermissibleValue(text="Get Library Handle") )
        setattr(cls, "Get NetBIOS Name",
                PermissibleValue(text="Get NetBIOS Name") )
        setattr(cls, "Get Process Current Directory",
                PermissibleValue(text="Get Process Current Directory") )
        setattr(cls, "Get Process Environment Variable",
                PermissibleValue(text="Get Process Environment Variable") )
        setattr(cls, "Get Process Startup Information",
                PermissibleValue(text="Get Process Startup Information") )
        setattr(cls, "Get Processes Snapshot",
                PermissibleValue(text="Get Processes Snapshot") )
        setattr(cls, "Get Registry Key Attributes",
                PermissibleValue(text="Get Registry Key Attributes") )
        setattr(cls, "Get Service Status",
                PermissibleValue(text="Get Service Status") )
        setattr(cls, "Get System Global Flags",
                PermissibleValue(text="Get System Global Flags") )
        setattr(cls, "Get System Host Name",
                PermissibleValue(text="Get System Host Name") )
        setattr(cls, "Get System Local Time",
                PermissibleValue(text="Get System Local Time") )
        setattr(cls, "Get System NetBIOS Name",
                PermissibleValue(text="Get System NetBIOS Name") )
        setattr(cls, "Get System Network Parameters",
                PermissibleValue(text="Get System Network Parameters") )
        setattr(cls, "Get System Time",
                PermissibleValue(text="Get System Time") )
        setattr(cls, "Get Thread Context",
                PermissibleValue(text="Get Thread Context") )
        setattr(cls, "Get Thread Username",
                PermissibleValue(text="Get Thread Username") )
        setattr(cls, "Get User Attributes",
                PermissibleValue(text="Get User Attributes") )
        setattr(cls, "Get Username",
                PermissibleValue(text="Get Username") )
        setattr(cls, "Get Windows Directory",
                PermissibleValue(text="Get Windows Directory") )
        setattr(cls, "Get Windows System Directory",
                PermissibleValue(text="Get Windows System Directory") )
        setattr(cls, "Get Windows Temporary Files Directory",
                PermissibleValue(text="Get Windows Temporary Files Directory") )
        setattr(cls, "Hide Window",
                PermissibleValue(text="Hide Window") )
        setattr(cls, "Impersonate Process",
                PermissibleValue(text="Impersonate Process") )
        setattr(cls, "Impersonate Thread",
                PermissibleValue(text="Impersonate Thread") )
        setattr(cls, "Inject Memory Page",
                PermissibleValue(text="Inject Memory Page") )
        setattr(cls, "Kill Process",
                PermissibleValue(text="Kill Process") )
        setattr(cls, "Kill Thread",
                PermissibleValue(text="Kill Thread") )
        setattr(cls, "Kill Window",
                PermissibleValue(text="Kill Window") )
        setattr(cls, "Listen on Port",
                PermissibleValue(text="Listen on Port") )
        setattr(cls, "Listen on Socket",
                PermissibleValue(text="Listen on Socket") )
        setattr(cls, "Load Driver",
                PermissibleValue(text="Load Driver") )
        setattr(cls, "Load Library",
                PermissibleValue(text="Load Library") )
        setattr(cls, "Load Module",
                PermissibleValue(text="Load Module") )
        setattr(cls, "Load and Call Driver",
                PermissibleValue(text="Load and Call Driver") )
        setattr(cls, "Lock File",
                PermissibleValue(text="Lock File") )
        setattr(cls, "Logon as User",
                PermissibleValue(text="Logon as User") )
        setattr(cls, "Map File",
                PermissibleValue(text="Map File") )
        setattr(cls, "Map Library",
                PermissibleValue(text="Map Library") )
        setattr(cls, "Map View of File",
                PermissibleValue(text="Map View of File") )
        setattr(cls, "Modify File",
                PermissibleValue(text="Modify File") )
        setattr(cls, "Modify Named Pipe",
                PermissibleValue(text="Modify Named Pipe") )
        setattr(cls, "Modify Process",
                PermissibleValue(text="Modify Process") )
        setattr(cls, "Modify Registry Key",
                PermissibleValue(text="Modify Registry Key") )
        setattr(cls, "Modify Registry Key Value",
                PermissibleValue(text="Modify Registry Key Value") )
        setattr(cls, "Modify Service",
                PermissibleValue(text="Modify Service") )
        setattr(cls, "Monitor Registry Key",
                PermissibleValue(text="Monitor Registry Key") )
        setattr(cls, "Move File",
                PermissibleValue(text="Move File") )
        setattr(cls, "Open File",
                PermissibleValue(text="Open File") )
        setattr(cls, "Open File Mapping",
                PermissibleValue(text="Open File Mapping") )
        setattr(cls, "Open Mutex",
                PermissibleValue(text="Open Mutex") )
        setattr(cls, "Open Port",
                PermissibleValue(text="Open Port") )
        setattr(cls, "Open Process",
                PermissibleValue(text="Open Process") )
        setattr(cls, "Open Registry Key",
                PermissibleValue(text="Open Registry Key") )
        setattr(cls, "Open Service",
                PermissibleValue(text="Open Service") )
        setattr(cls, "Open Service Control Manager",
                PermissibleValue(text="Open Service Control Manager") )
        setattr(cls, "Protect Virtual Memory",
                PermissibleValue(text="Protect Virtual Memory") )
        setattr(cls, "Query DNS",
                PermissibleValue(text="Query DNS") )
        setattr(cls, "Query Disk Attributes",
                PermissibleValue(text="Query Disk Attributes") )
        setattr(cls, "Query Process Virtual Memory",
                PermissibleValue(text="Query Process Virtual Memory") )
        setattr(cls, "Queue APC in Thread",
                PermissibleValue(text="Queue APC in Thread") )
        setattr(cls, "Read File",
                PermissibleValue(text="Read File") )
        setattr(cls, "Read From Named Pipe",
                PermissibleValue(text="Read From Named Pipe") )
        setattr(cls, "Read From Process Memory",
                PermissibleValue(text="Read From Process Memory") )
        setattr(cls, "Read Registry Key Value",
                PermissibleValue(text="Read Registry Key Value") )
        setattr(cls, "Receive Data on Socket",
                PermissibleValue(text="Receive Data on Socket") )
        setattr(cls, "Receive Email Message",
                PermissibleValue(text="Receive Email Message") )
        setattr(cls, "Release Mutex",
                PermissibleValue(text="Release Mutex") )
        setattr(cls, "Rename File",
                PermissibleValue(text="Rename File") )
        setattr(cls, "Revert Thread to Self",
                PermissibleValue(text="Revert Thread to Self") )
        setattr(cls, "Send Control Code to File",
                PermissibleValue(text="Send Control Code to File") )
        setattr(cls, "Send Control Code to Pipe",
                PermissibleValue(text="Send Control Code to Pipe") )
        setattr(cls, "Send Control Code to Service",
                PermissibleValue(text="Send Control Code to Service") )
        setattr(cls, "Send DNS Query",
                PermissibleValue(text="Send DNS Query") )
        setattr(cls, "Send Data on Socket",
                PermissibleValue(text="Send Data on Socket") )
        setattr(cls, "Send Data to Address on Socket",
                PermissibleValue(text="Send Data to Address on Socket") )
        setattr(cls, "Send Email Message",
                PermissibleValue(text="Send Email Message") )
        setattr(cls, "Send ICMP Request",
                PermissibleValue(text="Send ICMP Request") )
        setattr(cls, "Send Reverse DNS Query",
                PermissibleValue(text="Send Reverse DNS Query") )
        setattr(cls, "Set File Attributes",
                PermissibleValue(text="Set File Attributes") )
        setattr(cls, "Set NetBIOS Name",
                PermissibleValue(text="Set NetBIOS Name") )
        setattr(cls, "Set Process Current Directory",
                PermissibleValue(text="Set Process Current Directory") )
        setattr(cls, "Set Process Environment Variable",
                PermissibleValue(text="Set Process Environment Variable") )
        setattr(cls, "Set System Global Flags",
                PermissibleValue(text="Set System Global Flags") )
        setattr(cls, "Set System Host Name",
                PermissibleValue(text="Set System Host Name") )
        setattr(cls, "Set System Time",
                PermissibleValue(text="Set System Time") )
        setattr(cls, "Set Thread Context",
                PermissibleValue(text="Set Thread Context") )
        setattr(cls, "Show Window",
                PermissibleValue(text="Show Window") )
        setattr(cls, "Shutdown System",
                PermissibleValue(text="Shutdown System") )
        setattr(cls, "Sleep Process",
                PermissibleValue(text="Sleep Process") )
        setattr(cls, "Sleep System",
                PermissibleValue(text="Sleep System") )
        setattr(cls, "Start Service",
                PermissibleValue(text="Start Service") )
        setattr(cls, "Unload Driver",
                PermissibleValue(text="Unload Driver") )
        setattr(cls, "Unload Module",
                PermissibleValue(text="Unload Module") )
        setattr(cls, "Unlock File",
                PermissibleValue(text="Unlock File") )
        setattr(cls, "Unmap File",
                PermissibleValue(text="Unmap File") )
        setattr(cls, "Upload File",
                PermissibleValue(text="Upload File") )
        setattr(cls, "Write to File",
                PermissibleValue(text="Write to File") )
        setattr(cls, "Write to Process Virtual Memory",
                PermissibleValue(text="Write to Process Virtual Memory") )

class ActionRelationshipTypeEnum(EnumDefinitionImpl):

    Dependent_On = PermissibleValue(text="Dependent_On")
    Equivalent_To = PermissibleValue(text="Equivalent_To")
    Followed_By = PermissibleValue(text="Followed_By")
    Initiated = PermissibleValue(text="Initiated")
    Initiated_By = PermissibleValue(text="Initiated_By")
    Preceded_By = PermissibleValue(text="Preceded_By")
    Related_To = PermissibleValue(text="Related_To")

    _defn = EnumDefinition(
        name="ActionRelationshipTypeEnum",
    )

class ActionStatusTypeEnum(EnumDefinitionImpl):

    Error = PermissibleValue(text="Error")
    Fail = PermissibleValue(text="Fail")
    Ongoing = PermissibleValue(text="Ongoing")
    Pending = PermissibleValue(text="Pending")
    Success = PermissibleValue(text="Success")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="ActionStatusTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete/Finish",
                PermissibleValue(text="Complete/Finish") )

class ActionTypeEnum(EnumDefinitionImpl):

    Accept = PermissibleValue(text="Accept")
    Access = PermissibleValue(text="Access")
    Add = PermissibleValue(text="Add")
    Alert = PermissibleValue(text="Alert")
    Allocate = PermissibleValue(text="Allocate")
    Archive = PermissibleValue(text="Archive")
    Assign = PermissibleValue(text="Assign")
    Audit = PermissibleValue(text="Audit")
    Backup = PermissibleValue(text="Backup")
    Bind = PermissibleValue(text="Bind")
    Block = PermissibleValue(text="Block")
    Call = PermissibleValue(text="Call")
    Change = PermissibleValue(text="Change")
    Check = PermissibleValue(text="Check")
    Clean = PermissibleValue(text="Clean")
    Click = PermissibleValue(text="Click")
    Close = PermissibleValue(text="Close")
    Compare = PermissibleValue(text="Compare")
    Compress = PermissibleValue(text="Compress")
    Configure = PermissibleValue(text="Configure")
    Connect = PermissibleValue(text="Connect")
    Control = PermissibleValue(text="Control")
    Create = PermissibleValue(text="Create")
    Decode = PermissibleValue(text="Decode")
    Decompress = PermissibleValue(text="Decompress")
    Decrypt = PermissibleValue(text="Decrypt")
    Deny = PermissibleValue(text="Deny")
    Depress = PermissibleValue(text="Depress")
    Detect = PermissibleValue(text="Detect")
    Disconnect = PermissibleValue(text="Disconnect")
    Download = PermissibleValue(text="Download")
    Draw = PermissibleValue(text="Draw")
    Drop = PermissibleValue(text="Drop")
    Encode = PermissibleValue(text="Encode")
    Encrypt = PermissibleValue(text="Encrypt")
    Enumerate = PermissibleValue(text="Enumerate")
    Execute = PermissibleValue(text="Execute")
    Extract = PermissibleValue(text="Extract")
    Filter = PermissibleValue(text="Filter")
    Find = PermissibleValue(text="Find")
    Flush = PermissibleValue(text="Flush")
    Fork = PermissibleValue(text="Fork")
    Free = PermissibleValue(text="Free")
    Get = PermissibleValue(text="Get")
    Hide = PermissibleValue(text="Hide")
    Hook = PermissibleValue(text="Hook")
    Impersonate = PermissibleValue(text="Impersonate")
    Initialize = PermissibleValue(text="Initialize")
    Inject = PermissibleValue(text="Inject")
    Install = PermissibleValue(text="Install")
    Interleave = PermissibleValue(text="Interleave")
    Join = PermissibleValue(text="Join")
    Kill = PermissibleValue(text="Kill")
    Listen = PermissibleValue(text="Listen")
    Load = PermissibleValue(text="Load")
    Lock = PermissibleValue(text="Lock")
    Map = PermissibleValue(text="Map")
    Merge = PermissibleValue(text="Merge")
    Modify = PermissibleValue(text="Modify")
    Monitor = PermissibleValue(text="Monitor")
    Move = PermissibleValue(text="Move")
    Open = PermissibleValue(text="Open")
    Pack = PermissibleValue(text="Pack")
    Pause = PermissibleValue(text="Pause")
    Press = PermissibleValue(text="Press")
    Protect = PermissibleValue(text="Protect")
    Quarantine = PermissibleValue(text="Quarantine")
    Query = PermissibleValue(text="Query")
    Queue = PermissibleValue(text="Queue")
    Raise = PermissibleValue(text="Raise")
    Read = PermissibleValue(text="Read")
    Receive = PermissibleValue(text="Receive")
    Release = PermissibleValue(text="Release")
    Rename = PermissibleValue(text="Rename")
    Replicate = PermissibleValue(text="Replicate")
    Restore = PermissibleValue(text="Restore")
    Resume = PermissibleValue(text="Resume")
    Revert = PermissibleValue(text="Revert")
    Run = PermissibleValue(text="Run")
    Save = PermissibleValue(text="Save")
    Scan = PermissibleValue(text="Scan")
    Schedule = PermissibleValue(text="Schedule")
    Search = PermissibleValue(text="Search")
    Send = PermissibleValue(text="Send")
    Set = PermissibleValue(text="Set")
    Shutdown = PermissibleValue(text="Shutdown")
    Sleep = PermissibleValue(text="Sleep")
    Snapshot = PermissibleValue(text="Snapshot")
    Start = PermissibleValue(text="Start")
    Stop = PermissibleValue(text="Stop")
    Suspend = PermissibleValue(text="Suspend")
    Synchronize = PermissibleValue(text="Synchronize")
    Throw = PermissibleValue(text="Throw")
    Transmit = PermissibleValue(text="Transmit")
    Unblock = PermissibleValue(text="Unblock")
    Unhide = PermissibleValue(text="Unhide")
    Unhook = PermissibleValue(text="Unhook")
    Uninstall = PermissibleValue(text="Uninstall")
    Unload = PermissibleValue(text="Unload")
    Unlock = PermissibleValue(text="Unlock")
    Unmap = PermissibleValue(text="Unmap")
    Unpack = PermissibleValue(text="Unpack")
    Update = PermissibleValue(text="Update")
    Upgrade = PermissibleValue(text="Upgrade")
    Upload = PermissibleValue(text="Upload")
    Write = PermissibleValue(text="Write")

    _defn = EnumDefinition(
        name="ActionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Copy/Duplicate",
                PermissibleValue(text="Copy/Duplicate") )
        setattr(cls, "Login/Logon",
                PermissibleValue(text="Login/Logon") )
        setattr(cls, "Logout/Logoff",
                PermissibleValue(text="Logout/Logoff") )
        setattr(cls, "Remove/Delete",
                PermissibleValue(text="Remove/Delete") )
        setattr(cls, "Wipe/Destroy/Purge",
                PermissibleValue(text="Wipe/Destroy/Purge") )

class BitnessEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="BitnessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "32",
                PermissibleValue(text="32") )
        setattr(cls, "64",
                PermissibleValue(text="64") )

class CharacterEncodingEnum(EnumDefinitionImpl):

    ASCII = PermissibleValue(text="ASCII")

    _defn = EnumDefinition(
        name="CharacterEncodingEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "UTF-16",
                PermissibleValue(text="UTF-16") )
        setattr(cls, "UTF-32",
                PermissibleValue(text="UTF-32") )
        setattr(cls, "UTF-8",
                PermissibleValue(text="UTF-8") )
        setattr(cls, "Windows-1250",
                PermissibleValue(text="Windows-1250") )
        setattr(cls, "Windows-1251",
                PermissibleValue(text="Windows-1251") )
        setattr(cls, "Windows-1252",
                PermissibleValue(text="Windows-1252") )
        setattr(cls, "Windows-1253",
                PermissibleValue(text="Windows-1253") )
        setattr(cls, "Windows-1254",
                PermissibleValue(text="Windows-1254") )
        setattr(cls, "Windows-1255",
                PermissibleValue(text="Windows-1255") )
        setattr(cls, "Windows-1256",
                PermissibleValue(text="Windows-1256") )
        setattr(cls, "Windows-1257",
                PermissibleValue(text="Windows-1257") )
        setattr(cls, "Windows-1258",
                PermissibleValue(text="Windows-1258") )

class ContactAddressScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactAddressScopeEnum",
    )

class ContactEmailScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    cloud = PermissibleValue(text="cloud")

    _defn = EnumDefinition(
        name="ContactEmailScopeEnum",
    )

class ContactPhoneEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    mobile = PermissibleValue(text="mobile")
    main = PermissibleValue(text="main")
    pager = PermissibleValue(text="pager")

    _defn = EnumDefinition(
        name="ContactPhoneEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "home fax",
                PermissibleValue(text="home fax") )
        setattr(cls, "work fax",
                PermissibleValue(text="work fax") )

class ContactSIPScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactSIPScopeEnum",
    )

class ContactURLScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    homepage = PermissibleValue(text="homepage")

    _defn = EnumDefinition(
        name="ContactURLScopeEnum",
    )

class DiskTypeEnum(EnumDefinitionImpl):

    CDRom = PermissibleValue(text="CDRom")
    Fixed = PermissibleValue(text="Fixed")
    RAMDisk = PermissibleValue(text="RAMDisk")
    Remote = PermissibleValue(text="Remote")
    Removable = PermissibleValue(text="Removable")

    _defn = EnumDefinition(
        name="DiskTypeEnum",
    )

class EndiannessTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EndiannessTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Big-endian",
                PermissibleValue(text="Big-endian") )
        setattr(cls, "Little-endian",
                PermissibleValue(text="Little-endian") )
        setattr(cls, "Middle-endian",
                PermissibleValue(text="Middle-endian") )

class HashNameEnum(EnumDefinitionImpl):

    MD5 = PermissibleValue(text="MD5")
    MD6 = PermissibleValue(text="MD6")
    SHA1 = PermissibleValue(text="SHA1")
    SHA224 = PermissibleValue(text="SHA224")
    SHA256 = PermissibleValue(text="SHA256")
    SHA384 = PermissibleValue(text="SHA384")
    SHA512 = PermissibleValue(text="SHA512")
    SSDEEP = PermissibleValue(text="SSDEEP")

    _defn = EnumDefinition(
        name="HashNameEnum",
    )

class LibraryTypeEnum(EnumDefinitionImpl):

    Dynamic = PermissibleValue(text="Dynamic")
    Other = PermissibleValue(text="Other")
    Remote = PermissibleValue(text="Remote")
    Shared = PermissibleValue(text="Shared")
    Static = PermissibleValue(text="Static")

    _defn = EnumDefinition(
        name="LibraryTypeEnum",
    )

class MemoryBlockTypeEnum(EnumDefinitionImpl):

    Initialized = PermissibleValue(text="Initialized")
    Overlay = PermissibleValue(text="Overlay")
    Uninitialized = PermissibleValue(text="Uninitialized")

    _defn = EnumDefinition(
        name="MemoryBlockTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bit-mapped",
                PermissibleValue(text="Bit-mapped") )
        setattr(cls, "Byte-mapped",
                PermissibleValue(text="Byte-mapped") )

class ObservableObjectRelationshipEnum(EnumDefinitionImpl):

    Allocated = PermissibleValue(text="Allocated")
    Allocated_By = PermissibleValue(text="Allocated_By")
    Attachment_Of = PermissibleValue(text="Attachment_Of")
    Bound = PermissibleValue(text="Bound")
    Bound_By = PermissibleValue(text="Bound_By")
    Characterized_By = PermissibleValue(text="Characterized_By")
    Characterizes = PermissibleValue(text="Characterizes")
    Child_Of = PermissibleValue(text="Child_Of")
    Closed = PermissibleValue(text="Closed")
    Closed_By = PermissibleValue(text="Closed_By")
    Compressed = PermissibleValue(text="Compressed")
    Compressed_By = PermissibleValue(text="Compressed_By")
    Compressed_From = PermissibleValue(text="Compressed_From")
    Compressed_Into = PermissibleValue(text="Compressed_Into")
    Connected_From = PermissibleValue(text="Connected_From")
    Connected_To = PermissibleValue(text="Connected_To")
    Contained_Within = PermissibleValue(text="Contained_Within")
    Contains = PermissibleValue(text="Contains")
    Copied = PermissibleValue(text="Copied")
    Copied_By = PermissibleValue(text="Copied_By")
    Copied_From = PermissibleValue(text="Copied_From")
    Copied_To = PermissibleValue(text="Copied_To")
    Created = PermissibleValue(text="Created")
    Created_By = PermissibleValue(text="Created_By")
    Decoded = PermissibleValue(text="Decoded")
    Decoded_By = PermissibleValue(text="Decoded_By")
    Decompressed = PermissibleValue(text="Decompressed")
    Decompressed_By = PermissibleValue(text="Decompressed_By")
    Decrypted = PermissibleValue(text="Decrypted")
    Decrypted_By = PermissibleValue(text="Decrypted_By")
    Deleted = PermissibleValue(text="Deleted")
    Deleted_By = PermissibleValue(text="Deleted_By")
    Deleted_From = PermissibleValue(text="Deleted_From")
    Downloaded = PermissibleValue(text="Downloaded")
    Downloaded_By = PermissibleValue(text="Downloaded_By")
    Downloaded_From = PermissibleValue(text="Downloaded_From")
    Downloaded_To = PermissibleValue(text="Downloaded_To")
    Dropped = PermissibleValue(text="Dropped")
    Dropped_By = PermissibleValue(text="Dropped_By")
    Encoded = PermissibleValue(text="Encoded")
    Encoded_By = PermissibleValue(text="Encoded_By")
    Encrypted = PermissibleValue(text="Encrypted")
    Encrypted_By = PermissibleValue(text="Encrypted_By")
    Encrypted_From = PermissibleValue(text="Encrypted_From")
    Encrypted_To = PermissibleValue(text="Encrypted_To")
    Extracted_From = PermissibleValue(text="Extracted_From")
    FQDN_Of = PermissibleValue(text="FQDN_Of")
    Freed = PermissibleValue(text="Freed")
    Freed_By = PermissibleValue(text="Freed_By")
    Had_Attachment = PermissibleValue(text="Had_Attachment")
    Hooked = PermissibleValue(text="Hooked")
    Hooked_By = PermissibleValue(text="Hooked_By")
    Initialized_By = PermissibleValue(text="Initialized_By")
    Initialized_To = PermissibleValue(text="Initialized_To")
    Injected = PermissibleValue(text="Injected")
    Injected_As = PermissibleValue(text="Injected_As")
    Injected_By = PermissibleValue(text="Injected_By")
    Injected_Into = PermissibleValue(text="Injected_Into")
    Installed = PermissibleValue(text="Installed")
    Installed_By = PermissibleValue(text="Installed_By")
    Joined = PermissibleValue(text="Joined")
    Joined_By = PermissibleValue(text="Joined_By")
    Killed = PermissibleValue(text="Killed")
    Killed_By = PermissibleValue(text="Killed_By")
    Listened_On = PermissibleValue(text="Listened_On")
    Listened_On_By = PermissibleValue(text="Listened_On_By")
    Loaded_From = PermissibleValue(text="Loaded_From")
    Loaded_Into = PermissibleValue(text="Loaded_Into")
    Locked = PermissibleValue(text="Locked")
    Locked_By = PermissibleValue(text="Locked_By")
    Mapped_By = PermissibleValue(text="Mapped_By")
    Mapped_Into = PermissibleValue(text="Mapped_Into")
    Merged = PermissibleValue(text="Merged")
    Merged_By = PermissibleValue(text="Merged_By")
    Modified_Properties_Of = PermissibleValue(text="Modified_Properties_Of")
    Monitored = PermissibleValue(text="Monitored")
    Monitored_By = PermissibleValue(text="Monitored_By")
    Moved = PermissibleValue(text="Moved")
    Moved_By = PermissibleValue(text="Moved_By")
    Moved_From = PermissibleValue(text="Moved_From")
    Moved_To = PermissibleValue(text="Moved_To")
    Opened = PermissibleValue(text="Opened")
    Opened_By = PermissibleValue(text="Opened_By")
    Packed = PermissibleValue(text="Packed")
    Packed_By = PermissibleValue(text="Packed_By")
    Packed_From = PermissibleValue(text="Packed_From")
    Packed_Into = PermissibleValue(text="Packed_Into")
    Parent_Of = PermissibleValue(text="Parent_Of")
    Paused = PermissibleValue(text="Paused")
    Paused_By = PermissibleValue(text="Paused_By")
    Previously_Contained = PermissibleValue(text="Previously_Contained")
    Properties_Modified_By = PermissibleValue(text="Properties_Modified_By")
    Properties_Queried = PermissibleValue(text="Properties_Queried")
    Properties_Queried_By = PermissibleValue(text="Properties_Queried_By")
    Read_From = PermissibleValue(text="Read_From")
    Read_From_By = PermissibleValue(text="Read_From_By")
    Received = PermissibleValue(text="Received")
    Received_By = PermissibleValue(text="Received_By")
    Received_From = PermissibleValue(text="Received_From")
    Received_Via_Upload = PermissibleValue(text="Received_Via_Upload")
    Redirects_To = PermissibleValue(text="Redirects_To")
    Related_To = PermissibleValue(text="Related_To")
    Renamed = PermissibleValue(text="Renamed")
    Renamed_By = PermissibleValue(text="Renamed_By")
    Renamed_From = PermissibleValue(text="Renamed_From")
    Renamed_To = PermissibleValue(text="Renamed_To")
    Resolved_To = PermissibleValue(text="Resolved_To")
    Resumed = PermissibleValue(text="Resumed")
    Resumed_By = PermissibleValue(text="Resumed_By")
    Root_Domain_Of = PermissibleValue(text="Root_Domain_Of")
    Searched_For = PermissibleValue(text="Searched_For")
    Searched_For_By = PermissibleValue(text="Searched_For_By")
    Sent = PermissibleValue(text="Sent")
    Sent_By = PermissibleValue(text="Sent_By")
    Sent_To = PermissibleValue(text="Sent_To")
    Sent_Via_Upload = PermissibleValue(text="Sent_Via_Upload")
    Set_From = PermissibleValue(text="Set_From")
    Set_To = PermissibleValue(text="Set_To")
    Suspended = PermissibleValue(text="Suspended")
    Suspended_By = PermissibleValue(text="Suspended_By")
    Unhooked = PermissibleValue(text="Unhooked")
    Unhooked_By = PermissibleValue(text="Unhooked_By")
    Unlocked = PermissibleValue(text="Unlocked")
    Unlocked_By = PermissibleValue(text="Unlocked_By")
    Unpacked = PermissibleValue(text="Unpacked")
    Unpacked_By = PermissibleValue(text="Unpacked_By")
    Uploaded = PermissibleValue(text="Uploaded")
    Uploaded_By = PermissibleValue(text="Uploaded_By")
    Uploaded_From = PermissibleValue(text="Uploaded_From")
    Uploaded_To = PermissibleValue(text="Uploaded_To")
    Used = PermissibleValue(text="Used")
    Used_By = PermissibleValue(text="Used_By")
    Values_Enumerated = PermissibleValue(text="Values_Enumerated")
    Values_Enumerated_By = PermissibleValue(text="Values_Enumerated_By")
    Written_To_By = PermissibleValue(text="Written_To_By")
    Wrote_To = PermissibleValue(text="Wrote_To")

    _defn = EnumDefinition(
        name="ObservableObjectRelationshipEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Sub-domain_Of",
                PermissibleValue(text="Sub-domain_Of") )
        setattr(cls, "Supra-domain_Of",
                PermissibleValue(text="Supra-domain_Of") )

class ObservableObjectStateEnum(EnumDefinitionImpl):

    Active = PermissibleValue(text="Active")
    Closed = PermissibleValue(text="Closed")
    Exists = PermissibleValue(text="Exists")
    Inactive = PermissibleValue(text="Inactive")
    Locked = PermissibleValue(text="Locked")
    Open = PermissibleValue(text="Open")
    Started = PermissibleValue(text="Started")
    Stopped = PermissibleValue(text="Stopped")
    Unlocked = PermissibleValue(text="Unlocked")

    _defn = EnumDefinition(
        name="ObservableObjectStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Does Not Exist",
                PermissibleValue(text="Does Not Exist") )

class PartitionTypeEnum(EnumDefinitionImpl):

    PARTITION_ENTRY_UNUSED = PermissibleValue(text="PARTITION_ENTRY_UNUSED")
    PARTITION_EXTENDED = PermissibleValue(text="PARTITION_EXTENDED")
    PARTITION_FAT32 = PermissibleValue(text="PARTITION_FAT32")
    PARTITION_FAT32_XINT13 = PermissibleValue(text="PARTITION_FAT32_XINT13")
    PARTITION_FAT_12 = PermissibleValue(text="PARTITION_FAT_12")
    PARTITION_FAT_16 = PermissibleValue(text="PARTITION_FAT_16")
    PARTITION_HUGE = PermissibleValue(text="PARTITION_HUGE")
    PARTITION_IFS = PermissibleValue(text="PARTITION_IFS")
    PARTITION_LDM = PermissibleValue(text="PARTITION_LDM")
    PARTITION_NTFT = PermissibleValue(text="PARTITION_NTFT")
    PARTITION_OS2BOOTMGR = PermissibleValue(text="PARTITION_OS2BOOTMGR")
    PARTITION_PREP = PermissibleValue(text="PARTITION_PREP")
    PARTITION_UNIX = PermissibleValue(text="PARTITION_UNIX")
    PARTITION_XENIX_1 = PermissibleValue(text="PARTITION_XENIX_1")
    PARTITION_XENIX_2 = PermissibleValue(text="PARTITION_XENIX_2")
    PARTITION_XINT13 = PermissibleValue(text="PARTITION_XINT13")
    PARTITION_XINT13_EXTENDED = PermissibleValue(text="PARTITION_XINT13_EXTENDED")
    UNKNOWN = PermissibleValue(text="UNKNOWN")
    VALID_NTFT = PermissibleValue(text="VALID_NTFT")

    _defn = EnumDefinition(
        name="PartitionTypeEnum",
    )

class ProcessorArchEnum(EnumDefinitionImpl):

    ARM = PermissibleValue(text="ARM")
    Alpha = PermissibleValue(text="Alpha")
    MIPS = PermissibleValue(text="MIPS")
    Other = PermissibleValue(text="Other")
    PowerPC = PermissibleValue(text="PowerPC")
    SPARC = PermissibleValue(text="SPARC")

    _defn = EnumDefinition(
        name="ProcessorArchEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "IA-64",
                PermissibleValue(text="IA-64") )
        setattr(cls, "Motorola 68k",
                PermissibleValue(text="Motorola 68k") )
        setattr(cls, "eSi-RISC",
                PermissibleValue(text="eSi-RISC") )
        setattr(cls, "x86-32",
                PermissibleValue(text="x86-32") )
        setattr(cls, "x86-64",
                PermissibleValue(text="x86-64") )
        setattr(cls, "z/Architecture",
                PermissibleValue(text="z/Architecture") )

class RecoveredObjectStatusEnum(EnumDefinitionImpl):

    recovered = PermissibleValue(text="recovered")
    overwritten = PermissibleValue(text="overwritten")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="RecoveredObjectStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "partially recovered",
                PermissibleValue(text="partially recovered") )

class RegionalRegistryTypeEnum(EnumDefinitionImpl):

    APNIC = PermissibleValue(text="APNIC")
    ARIN = PermissibleValue(text="ARIN")
    AfriNIC = PermissibleValue(text="AfriNIC")
    LACNIC = PermissibleValue(text="LACNIC")

    _defn = EnumDefinition(
        name="RegionalRegistryTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RIPE NCC",
                PermissibleValue(text="RIPE NCC") )

class RegistryDatatypeEnum(EnumDefinitionImpl):
    """
    "From https //learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types, https
    //learn.microsoft.com/en-us/windows/win32/shell/hkey-type"
    """
    reg_binary = PermissibleValue(text="reg_binary",
                                           description=""Binary data in any form."")
    reg_dword = PermissibleValue(text="reg_dword",
                                         description=""A 32-bit number."")
    reg_dword_big_endian = PermissibleValue(text="reg_dword_big_endian",
                                                               description=""A 32-bit number in big-endian format. Some UNIX systems support big-endian architectures."")
    reg_expand_sz = PermissibleValue(text="reg_expand_sz",
                                                 description=""A null-terminated string that contains unexpanded references to environment Variables (for example, '%PATH%'). It will be a Unicode or ANSI string depending on wh ether you use the Unicode or ANSI functions. To expand the environment variable refere nces, use the ExpandEnvironmentStrings function."")
    reg_full_resource_descriptor = PermissibleValue(text="reg_full_resource_descriptor",
                                                                               description=""A list of hardware resources that a physical device is using, detected and written into the \HardwareDescription tree by the system."")
    reg_invalid_type = PermissibleValue(text="reg_invalid_type",
                                                       description=""Specifies an invalid key."")
    reg_link = PermissibleValue(text="reg_link",
                                       description=""A null-terminated Unicode string that contains the target path of a symboli c link that was created by calling the RegCreateKeyEx function with REG_OPTION_CREATE_ LINK."")
    reg_multi_sz = PermissibleValue(text="reg_multi_sz",
                                               description=""A sequence of null-terminated strings, terminated by an empty string (\0). The following is an example: String1\0String2\0String3\0LastString\0\0 The first \0 terminates the first string, the second to the last \0 terminates the last string, and the final \0 terminates the sequence. Note that the final terminator must be factored into the length of the string."")
    reg_none = PermissibleValue(text="reg_none",
                                       description=""No defined value type."")
    reg_qword = PermissibleValue(text="reg_qword",
                                         description=""A 64-bit number."")
    reg_resource_list = PermissibleValue(text="reg_resource_list",
                                                         description=""Device-driver resource list."")
    reg_resource_requirements_list = PermissibleValue(text="reg_resource_requirements_list",
                                                                                   description=""A device driver's list of possible hardware resources it or one of the physical devices it controls can use, from which the system writes a subset into the \ResourceMap tree"")
    reg_sz = PermissibleValue(text="reg_sz",
                                   description=""A null-terminated string. This will be either a Unicode or an ANSI string, depending on whether you use the Unicode or ANSI functions."")

    _defn = EnumDefinition(
        name="RegistryDatatypeEnum",
        description="\"From https //learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types, https //learn.microsoft.com/en-us/windows/win32/shell/hkey-type\"",
    )

class SIMFormEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SIMFormEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Full-size SIM",
                PermissibleValue(text="Full-size SIM") )
        setattr(cls, "Micro SIM",
                PermissibleValue(text="Micro SIM") )
        setattr(cls, "Nano SIM",
                PermissibleValue(text="Nano SIM") )

class SIMTypeEnum(EnumDefinitionImpl):

    SIM = PermissibleValue(text="SIM")
    UICC = PermissibleValue(text="UICC")
    USIM = PermissibleValue(text="USIM")

    _defn = EnumDefinition(
        name="SIMTypeEnum",
    )

class TaskActionTypeEnum(EnumDefinitionImpl):

    TASK_ACTION_COM_HANDLER = PermissibleValue(text="TASK_ACTION_COM_HANDLER")
    TASK_ACTION_EXEC = PermissibleValue(text="TASK_ACTION_EXEC")
    TASK_ACTION_SEND_EMAIL = PermissibleValue(text="TASK_ACTION_SEND_EMAIL")
    TASK_ACTION_SHOW_MESSAGE = PermissibleValue(text="TASK_ACTION_SHOW_MESSAGE")

    _defn = EnumDefinition(
        name="TaskActionTypeEnum",
    )

class TaskFlagEnum(EnumDefinitionImpl):

    TASK_FLAG_DELETE_WHEN_DONE = PermissibleValue(text="TASK_FLAG_DELETE_WHEN_DONE")
    TASK_FLAG_DISABLED = PermissibleValue(text="TASK_FLAG_DISABLED")
    TASK_FLAG_DONT_START_IF_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_DONT_START_IF_ON_BATTERIES")
    TASK_FLAG_HIDDEN = PermissibleValue(text="TASK_FLAG_HIDDEN")
    TASK_FLAG_INTERACTIVE = PermissibleValue(text="TASK_FLAG_INTERACTIVE")
    TASK_FLAG_KILL_IF_GOING_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_KILL_IF_GOING_ON_BATTERIES")
    TASK_FLAG_KILL_ON_IDLE_END = PermissibleValue(text="TASK_FLAG_KILL_ON_IDLE_END")
    TASK_FLAG_RESTART_ON_IDLE_RESUME = PermissibleValue(text="TASK_FLAG_RESTART_ON_IDLE_RESUME")
    TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET = PermissibleValue(text="TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET")
    TASK_FLAG_RUN_ONLY_IF_LOGGED_ON = PermissibleValue(text="TASK_FLAG_RUN_ONLY_IF_LOGGED_ON")
    TASK_FLAG_START_ONLY_IF_IDLE = PermissibleValue(text="TASK_FLAG_START_ONLY_IF_IDLE")
    TASK_FLAG_SYSTEM_REQUIRED = PermissibleValue(text="TASK_FLAG_SYSTEM_REQUIRED")
    TASK_FLAG_ZERO = PermissibleValue(text="TASK_FLAG_ZERO")

    _defn = EnumDefinition(
        name="TaskFlagEnum",
    )

class TaskPriorityEnum(EnumDefinitionImpl):

    ABOVE_NORMAL_PRIORITY_CLASS = PermissibleValue(text="ABOVE_NORMAL_PRIORITY_CLASS")
    BELOW_NORMAL_PRIORITY_CLASS = PermissibleValue(text="BELOW_NORMAL_PRIORITY_CLASS")
    HIGH_PRIORITY_CLASS = PermissibleValue(text="HIGH_PRIORITY_CLASS")
    IDLE_PRIORITY_CLASS = PermissibleValue(text="IDLE_PRIORITY_CLASS")
    NORMAL_PRIORITY_CLASS = PermissibleValue(text="NORMAL_PRIORITY_CLASS")
    REALTIME_PRIORITY_CLASS = PermissibleValue(text="REALTIME_PRIORITY_CLASS")

    _defn = EnumDefinition(
        name="TaskPriorityEnum",
    )

class TaskStatusEnum(EnumDefinitionImpl):

    SCHED_E_ACCOUNT_DBASE_CORRUPT = PermissibleValue(text="SCHED_E_ACCOUNT_DBASE_CORRUPT")
    SCHED_E_ACCOUNT_INFORMATION_NOT_SET = PermissibleValue(text="SCHED_E_ACCOUNT_INFORMATION_NOT_SET")
    SCHED_E_ACCOUNT_NAME_NOT_FOUND = PermissibleValue(text="SCHED_E_ACCOUNT_NAME_NOT_FOUND")
    SCHED_E_CANNOT_OPEN_TASK = PermissibleValue(text="SCHED_E_CANNOT_OPEN_TASK")
    SCHED_E_INVALID_TASK = PermissibleValue(text="SCHED_E_INVALID_TASK")
    SCHED_E_NO_SECURITY_SERVICES = PermissibleValue(text="SCHED_E_NO_SECURITY_SERVICES")
    SCHED_E_SERVICE_NOT_INSTALLED = PermissibleValue(text="SCHED_E_SERVICE_NOT_INSTALLED")
    SCHED_E_SERVICE_NOT_RUNNING = PermissibleValue(text="SCHED_E_SERVICE_NOT_RUNNING")
    SCHED_E_TASK_NOT_READY = PermissibleValue(text="SCHED_E_TASK_NOT_READY")
    SCHED_E_TASK_NOT_RUNNING = PermissibleValue(text="SCHED_E_TASK_NOT_RUNNING")
    SCHED_E_TRIGGER_NOT_FOUND = PermissibleValue(text="SCHED_E_TRIGGER_NOT_FOUND")
    SCHED_E_UNKNOWN_OBJECT_VERSION = PermissibleValue(text="SCHED_E_UNKNOWN_OBJECT_VERSION")
    SCHED_E_UNSUPPORTED_ACCOUNT_OPTION = PermissibleValue(text="SCHED_E_UNSUPPORTED_ACCOUNT_OPTION")
    SCHED_S_EVENT_TRIGGER = PermissibleValue(text="SCHED_S_EVENT_TRIGGER")
    SCHED_S_TASK_DISABLED = PermissibleValue(text="SCHED_S_TASK_DISABLED")
    SCHED_S_TASK_HAS_NOT_RUN = PermissibleValue(text="SCHED_S_TASK_HAS_NOT_RUN")
    SCHED_S_TASK_NOT_SCHEDULED = PermissibleValue(text="SCHED_S_TASK_NOT_SCHEDULED")
    SCHED_S_TASK_NO_MORE_RUNS = PermissibleValue(text="SCHED_S_TASK_NO_MORE_RUNS")
    SCHED_S_TASK_NO_VALID_TRIGGERS = PermissibleValue(text="SCHED_S_TASK_NO_VALID_TRIGGERS")
    SCHED_S_TASK_READY = PermissibleValue(text="SCHED_S_TASK_READY")
    SCHED_S_TASK_RUNNING = PermissibleValue(text="SCHED_S_TASK_RUNNING")
    SCHED_S_TASK_TERMINATED = PermissibleValue(text="SCHED_S_TASK_TERMINATED")
    TASK_STATE_QUEUED = PermissibleValue(text="TASK_STATE_QUEUED")
    TASK_STATE_UNKNOWN = PermissibleValue(text="TASK_STATE_UNKNOWN")

    _defn = EnumDefinition(
        name="TaskStatusEnum",
    )

class ThreadRunningStatusEnum(EnumDefinitionImpl):

    Initialized = PermissibleValue(text="Initialized")
    Ready = PermissibleValue(text="Ready")
    Running = PermissibleValue(text="Running")
    Standby = PermissibleValue(text="Standby")
    Terminated = PermissibleValue(text="Terminated")
    Transition = PermissibleValue(text="Transition")
    Unknown = PermissibleValue(text="Unknown")
    Waiting = PermissibleValue(text="Waiting")

    _defn = EnumDefinition(
        name="ThreadRunningStatusEnum",
    )

class TimestampPrecisionEnum(EnumDefinitionImpl):

    day = PermissibleValue(text="day")
    hour = PermissibleValue(text="hour")
    minute = PermissibleValue(text="minute")
    month = PermissibleValue(text="month")
    second = PermissibleValue(text="second")
    year = PermissibleValue(text="year")

    _defn = EnumDefinition(
        name="TimestampPrecisionEnum",
    )

class TrendEnum(EnumDefinitionImpl):

    Decreasing = PermissibleValue(text="Decreasing")
    Increasing = PermissibleValue(text="Increasing")

    _defn = EnumDefinition(
        name="TrendEnum",
    )

class TriggerFrequencyEnum(EnumDefinitionImpl):

    TASK_EVENT_TRIGGER_AT_LOGON = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_LOGON")
    TASK_EVENT_TRIGGER_AT_SYSTEMSTART = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_SYSTEMSTART")
    TASK_EVENT_TRIGGER_ON_IDLE = PermissibleValue(text="TASK_EVENT_TRIGGER_ON_IDLE")
    TASK_TIME_TRIGGER_DAILY = PermissibleValue(text="TASK_TIME_TRIGGER_DAILY")
    TASK_TIME_TRIGGER_MONTHLYDATE = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDATE")
    TASK_TIME_TRIGGER_MONTHLYDOW = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDOW")
    TASK_TIME_TRIGGER_ONCE = PermissibleValue(text="TASK_TIME_TRIGGER_ONCE")
    TASK_TIME_TRIGGER_WEEKLY = PermissibleValue(text="TASK_TIME_TRIGGER_WEEKLY")

    _defn = EnumDefinition(
        name="TriggerFrequencyEnum",
    )

class TriggerTypeEnum(EnumDefinitionImpl):

    TASK_TRIGGER_BOOT = PermissibleValue(text="TASK_TRIGGER_BOOT")
    TASK_TRIGGER_EVENT = PermissibleValue(text="TASK_TRIGGER_EVENT")
    TASK_TRIGGER_IDLE = PermissibleValue(text="TASK_TRIGGER_IDLE")
    TASK_TRIGGER_LOGON = PermissibleValue(text="TASK_TRIGGER_LOGON")
    TASK_TRIGGER_REGISTRATION = PermissibleValue(text="TASK_TRIGGER_REGISTRATION")
    TASK_TRIGGER_SESSION_STATE_CHANGE = PermissibleValue(text="TASK_TRIGGER_SESSION_STATE_CHANGE")
    TASK_TRIGGER_TIME = PermissibleValue(text="TASK_TRIGGER_TIME")

    _defn = EnumDefinition(
        name="TriggerTypeEnum",
    )

class URLTransitionTypeEnum(EnumDefinitionImpl):

    link = PermissibleValue(text="link")
    typed = PermissibleValue(text="typed")
    auto_bookmark = PermissibleValue(text="auto_bookmark")
    auto_subframe = PermissibleValue(text="auto_subframe")
    manual_subframe = PermissibleValue(text="manual_subframe")
    generated = PermissibleValue(text="generated")
    auto_toplevel = PermissibleValue(text="auto_toplevel")
    form_submit = PermissibleValue(text="form_submit")
    reload = PermissibleValue(text="reload")
    keyword = PermissibleValue(text="keyword")
    keyword_generated = PermissibleValue(text="keyword_generated")

    _defn = EnumDefinition(
        name="URLTransitionTypeEnum",
    )

class UnixProcessStateEnum(EnumDefinitionImpl):

    Dead = PermissibleValue(text="Dead")
    InterruptibleSleep = PermissibleValue(text="InterruptibleSleep")
    Paging = PermissibleValue(text="Paging")
    Running = PermissibleValue(text="Running")
    Stopped = PermissibleValue(text="Stopped")
    UninterruptibleSleep = PermissibleValue(text="UninterruptibleSleep")
    Zombie = PermissibleValue(text="Zombie")

    _defn = EnumDefinition(
        name="UnixProcessStateEnum",
    )

class WhoisContactTypeEnum(EnumDefinitionImpl):

    ADMIN = PermissibleValue(text="ADMIN")
    BILLING = PermissibleValue(text="BILLING")
    TECHNICAL = PermissibleValue(text="TECHNICAL")

    _defn = EnumDefinition(
        name="WhoisContactTypeEnum",
    )

class WhoisDNSSECTypeEnum(EnumDefinitionImpl):

    Signed = PermissibleValue(text="Signed")
    Unsigned = PermissibleValue(text="Unsigned")

    _defn = EnumDefinition(
        name="WhoisDNSSECTypeEnum",
    )

class WhoisStatusTypeEnum(EnumDefinitionImpl):

    ADD_PERIOD = PermissibleValue(text="ADD_PERIOD")
    AUTO_RENEW_PERIOD = PermissibleValue(text="AUTO_RENEW_PERIOD")
    CLIENT_DELETE_PROHIBITED = PermissibleValue(text="CLIENT_DELETE_PROHIBITED")
    CLIENT_HOLD = PermissibleValue(text="CLIENT_HOLD")
    CLIENT_RENEW_PROHIBITED = PermissibleValue(text="CLIENT_RENEW_PROHIBITED")
    CLIENT_TRANSFER_PROHIBITED = PermissibleValue(text="CLIENT_TRANSFER_PROHIBITED")
    CLIENT_UPDATE_PROHIBITED = PermissibleValue(text="CLIENT_UPDATE_PROHIBITED")
    DELETE_PROHIBITED = PermissibleValue(text="DELETE_PROHIBITED")
    HOLD = PermissibleValue(text="HOLD")
    INACTIVE = PermissibleValue(text="INACTIVE")
    OK = PermissibleValue(text="OK")
    PENDING_DELETE_RESTORABLE = PermissibleValue(text="PENDING_DELETE_RESTORABLE")
    PENDING_DELETE_SCHEDULED_FOR_RELEASE = PermissibleValue(text="PENDING_DELETE_SCHEDULED_FOR_RELEASE")
    PENDING_RESTORE = PermissibleValue(text="PENDING_RESTORE")
    RENEW_PERIOD = PermissibleValue(text="RENEW_PERIOD")
    RENEW_PROHIBITED = PermissibleValue(text="RENEW_PROHIBITED")
    TRANSFER_PERIOD = PermissibleValue(text="TRANSFER_PERIOD")
    TRANSFER_PROHIBITED = PermissibleValue(text="TRANSFER_PROHIBITED")
    UPDATE_PROHIBITED = PermissibleValue(text="UPDATE_PROHIBITED")

    _defn = EnumDefinition(
        name="WhoisStatusTypeEnum",
    )

class WindowsDriveTypeEnum(EnumDefinitionImpl):

    DRIVE_CDROM = PermissibleValue(text="DRIVE_CDROM")
    DRIVE_FIXED = PermissibleValue(text="DRIVE_FIXED")
    DRIVE_NO_ROOT_DIR = PermissibleValue(text="DRIVE_NO_ROOT_DIR")
    DRIVE_RAMDISK = PermissibleValue(text="DRIVE_RAMDISK")
    DRIVE_REMOTE = PermissibleValue(text="DRIVE_REMOTE")
    DRIVE_REMOVABLE = PermissibleValue(text="DRIVE_REMOVABLE")
    DRIVE_UNKNOWN = PermissibleValue(text="DRIVE_UNKNOWN")

    _defn = EnumDefinition(
        name="WindowsDriveTypeEnum",
    )

class WindowsVolumeAttributeEnum(EnumDefinitionImpl):

    Hidden = PermissibleValue(text="Hidden")
    NoDefaultDriveLetter = PermissibleValue(text="NoDefaultDriveLetter")
    ReadOnly = PermissibleValue(text="ReadOnly")
    ShadowCopy = PermissibleValue(text="ShadowCopy")

    _defn = EnumDefinition(
        name="WindowsVolumeAttributeEnum",
    )

class WirelessNetworkSecurityModeEnum(EnumDefinitionImpl):

    WEP = PermissibleValue(text="WEP")
    WPA = PermissibleValue(text="WPA")

    _defn = EnumDefinition(
        name="WirelessNetworkSecurityModeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
                PermissibleValue(text="None") )
        setattr(cls, "WPA2-PSK",
                PermissibleValue(text="WPA2-PSK") )
        setattr(cls, "WPA2-Enterprise",
                PermissibleValue(text="WPA2-Enterprise") )
        setattr(cls, "WPA3-PSK",
                PermissibleValue(text="WPA3-PSK") )
        setattr(cls, "WPA3-Enterprise",
                PermissibleValue(text="WPA3-Enterprise") )

# Slots
class slots:
    pass

slots.list = Slot(uri=TYPES.list, name="list", curie=TYPES.curie('list'),
                   model_uri=TYPES.list, domain=None, range=Optional[Union[dict, List]])

slots.listItem = Slot(uri=TYPES.listItem, name="listItem", curie=TYPES.curie('listItem'),
                   model_uri=TYPES.listItem, domain=None, range=Optional[Union[dict, ListItem]])

slots.identifier = Slot(uri=TYPES.identifier, name="identifier", curie=TYPES.curie('identifier'),
                   model_uri=TYPES.identifier, domain=None, range=Optional[str])

slots.nativeFormatString = Slot(uri=TYPES.nativeFormatString, name="nativeFormatString", curie=TYPES.curie('nativeFormatString'),
                   model_uri=TYPES.nativeFormatString, domain=None, range=Optional[str])

slots.structuredText = Slot(uri=TYPES.structuredText, name="structuredText", curie=TYPES.curie('structuredText'),
                   model_uri=TYPES.structuredText, domain=None, range=Optional[str])

slots.entry = Slot(uri=TYPES.entry, name="entry", curie=TYPES.curie('entry'),
                   model_uri=TYPES.entry, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.hashMethod = Slot(uri=TYPES.hashMethod, name="hashMethod", curie=TYPES.curie('hashMethod'),
                   model_uri=TYPES.hashMethod, domain=None, range=Optional[str])

slots.hashValue = Slot(uri=TYPES.hashValue, name="hashValue", curie=TYPES.curie('hashValue'),
                   model_uri=TYPES.hashValue, domain=None, range=Optional[hex])

slots.key = Slot(uri=TYPES.key, name="key", curie=TYPES.curie('key'),
                   model_uri=TYPES.key, domain=None, range=Optional[str])

slots.threadNextItem = Slot(uri=TYPES.threadNextItem, name="threadNextItem", curie=TYPES.curie('threadNextItem'),
                   model_uri=TYPES.threadNextItem, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadOriginItem = Slot(uri=TYPES.threadOriginItem, name="threadOriginItem", curie=TYPES.curie('threadOriginItem'),
                   model_uri=TYPES.threadOriginItem, domain=Thread, range=Optional[Union[dict, "ThreadItem"]])

slots.threadPredecessor = Slot(uri=TYPES.threadPredecessor, name="threadPredecessor", curie=TYPES.curie('threadPredecessor'),
                   model_uri=TYPES.threadPredecessor, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadPreviousItem = Slot(uri=TYPES.threadPreviousItem, name="threadPreviousItem", curie=TYPES.curie('threadPreviousItem'),
                   model_uri=TYPES.threadPreviousItem, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadSuccessor = Slot(uri=TYPES.threadSuccessor, name="threadSuccessor", curie=TYPES.curie('threadSuccessor'),
                   model_uri=TYPES.threadSuccessor, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadTerminalItem = Slot(uri=TYPES.threadTerminalItem, name="threadTerminalItem", curie=TYPES.curie('threadTerminalItem'),
                   model_uri=TYPES.threadTerminalItem, domain=Thread, range=Optional[Union[dict, "ThreadItem"]])

slots._value = Slot(uri=TYPES._value, name="_value", curie=TYPES.curie('_value'),
                   model_uri=TYPES._value, domain=None, range=Optional[str])

slots.element = Slot(uri=COLLECTIONS.element, name="element", curie=COLLECTIONS.curie('element'),
                   model_uri=TYPES.element, domain=Collection, range=Optional[Union[dict, "Thing"]])

slots.elementOf = Slot(uri=COLLECTIONS.elementOf, name="elementOf", curie=COLLECTIONS.curie('elementOf'),
                   model_uri=TYPES.elementOf, domain=Thing, range=Optional[Union[dict, Collection]])

slots.firstItem = Slot(uri=COLLECTIONS.firstItem, name="firstItem", curie=COLLECTIONS.curie('firstItem'),
                   model_uri=TYPES.firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.firstItemOf = Slot(uri=COLLECTIONS.firstItemOf, name="firstItemOf", curie=COLLECTIONS.curie('firstItemOf'),
                   model_uri=TYPES.firstItemOf, domain=ListItem, range=Optional[Union[dict, List]])

slots.followedBy = Slot(uri=COLLECTIONS.followedBy, name="followedBy", curie=COLLECTIONS.curie('followedBy'),
                   model_uri=TYPES.followedBy, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.item = Slot(uri=COLLECTIONS.item, name="item", curie=COLLECTIONS.curie('item'),
                   model_uri=TYPES.item, domain=Bag, range=Optional[Union[dict, "CoItem"]])

slots.itemContent = Slot(uri=COLLECTIONS.itemContent, name="itemContent", curie=COLLECTIONS.curie('itemContent'),
                   model_uri=TYPES.itemContent, domain=CoItem, range=Optional[Union[dict, "CoItem"]])

slots.itemContentOf = Slot(uri=COLLECTIONS.itemContentOf, name="itemContentOf", curie=COLLECTIONS.curie('itemContentOf'),
                   model_uri=TYPES.itemContentOf, domain=CoItem, range=Optional[Union[dict, CoItem]])

slots.itemOf = Slot(uri=COLLECTIONS.itemOf, name="itemOf", curie=COLLECTIONS.curie('itemOf'),
                   model_uri=TYPES.itemOf, domain=CoItem, range=Optional[Union[dict, Bag]])

slots.lastItem = Slot(uri=COLLECTIONS.lastItem, name="lastItem", curie=COLLECTIONS.curie('lastItem'),
                   model_uri=TYPES.lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.lastItemOf = Slot(uri=COLLECTIONS.lastItemOf, name="lastItemOf", curie=COLLECTIONS.curie('lastItemOf'),
                   model_uri=TYPES.lastItemOf, domain=ListItem, range=Optional[Union[dict, List]])

slots.nextItem = Slot(uri=COLLECTIONS.nextItem, name="nextItem", curie=COLLECTIONS.curie('nextItem'),
                   model_uri=TYPES.nextItem, domain=Thing, range=Optional[Union[dict, ListItem]])

slots.precededBy = Slot(uri=COLLECTIONS.precededBy, name="precededBy", curie=COLLECTIONS.curie('precededBy'),
                   model_uri=TYPES.precededBy, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.previousItem = Slot(uri=COLLECTIONS.previousItem, name="previousItem", curie=COLLECTIONS.curie('previousItem'),
                   model_uri=TYPES.previousItem, domain=ListItem, range=Optional[Union[dict, "Thing"]])

slots._index = Slot(uri=COLLECTIONS._index, name="_index", curie=COLLECTIONS.curie('_index'),
                   model_uri=TYPES._index, domain=ListItem, range=Optional[Union[int, PositiveInteger]])

slots.size = Slot(uri=COLLECTIONS.size, name="size", curie=COLLECTIONS.curie('size'),
                   model_uri=TYPES.size, domain=Collection, range=Optional[Union[int, PositiveInteger]])

slots.confidence = Slot(uri=CORE.confidence, name="confidence", curie=CORE.curie('confidence'),
                   model_uri=TYPES.confidence, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=TYPES.constrainingVocabularyName, domain=None, range=Optional[str])

slots.constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=TYPES.constrainingVocabularyReference, domain=None, range=Optional[Union[str, IriType]])

slots.context = Slot(uri=CORE.context, name="context", curie=CORE.curie('context'),
                   model_uri=TYPES.context, domain=None, range=Optional[str])

slots.createdBy = Slot(uri=CORE.createdBy, name="createdBy", curie=CORE.curie('createdBy'),
                   model_uri=TYPES.createdBy, domain=IdentityAbstraction, range=Optional[str])

slots.definingContext = Slot(uri=CORE.definingContext, name="definingContext", curie=CORE.curie('definingContext'),
                   model_uri=TYPES.definingContext, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=TYPES.description, domain=None, range=Optional[str])

slots.endTime = Slot(uri=CORE.endTime, name="endTime", curie=CORE.curie('endTime'),
                   model_uri=TYPES.endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.externalIdentifier = Slot(uri=CORE.externalIdentifier, name="externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=TYPES.externalIdentifier, domain=None, range=Optional[str])

slots.externalReference = Slot(uri=CORE.externalReference, name="externalReference", curie=CORE.curie('externalReference'),
                   model_uri=TYPES.externalReference, domain=ExternalReference, range=Optional[str])

slots.hasFacet = Slot(uri=CORE.hasFacet, name="hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=TYPES.hasFacet, domain=None, range=Optional[str])

slots.isDirectional = Slot(uri=CORE.isDirectional, name="isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=TYPES.isDirectional, domain=None, range=Optional[Union[bool, BooleanType]])

slots.kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=TYPES.kindOfRelationship, domain=None, range=Optional[str])

slots.modifiedTime = Slot(uri=CORE.modifiedTime, name="modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=TYPES.modifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=TYPES.name, domain=None, range=Optional[str])

slots.namingAuthority = Slot(uri=CORE.namingAuthority, name="namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=TYPES.namingAuthority, domain=None, range=Optional[str])

slots.object = Slot(uri=CORE.object, name="object", curie=CORE.curie('object'),
                   model_uri=TYPES.object, domain=None, range=Optional[Union[dict, UcoObject]])

slots.objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=TYPES.objectCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.objectMarking = Slot(uri=CORE.objectMarking, name="objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=TYPES.objectMarking, domain=None, range=Optional[Union[dict, MarkingDefinitionAbstraction]])

slots.referenceURL = Slot(uri=CORE.referenceURL, name="referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=TYPES.referenceURL, domain=None, range=Optional[Union[str, IriType]])

slots.source = Slot(uri=CORE.source, name="source", curie=CORE.curie('source'),
                   model_uri=TYPES.source, domain=None, range=Optional[Union[dict, UcoObject]])

slots.specVersion = Slot(uri=CORE.specVersion, name="specVersion", curie=CORE.curie('specVersion'),
                   model_uri=TYPES.specVersion, domain=None, range=Optional[str])

slots.startTime = Slot(uri=CORE.startTime, name="startTime", curie=CORE.curie('startTime'),
                   model_uri=TYPES.startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.statement = Slot(uri=CORE.statement, name="statement", curie=CORE.curie('statement'),
                   model_uri=TYPES.statement, domain=None, range=Optional[str])

slots.tag = Slot(uri=CORE.tag, name="tag", curie=CORE.curie('tag'),
                   model_uri=TYPES.tag, domain=None, range=Optional[str])

slots.target = Slot(uri=CORE.target, name="target", curie=CORE.curie('target'),
                   model_uri=TYPES.target, domain=None, range=Optional[Union[dict, UcoObject]])

slots.value = Slot(uri=CORE.value, name="value", curie=CORE.curie('value'),
                   model_uri=TYPES.value, domain=None, range=Optional[str])

slots.AccountTypeVocab = Slot(uri=VOCABULARY.AccountTypeVocab, name="AccountTypeVocab", curie=VOCABULARY.curie('AccountTypeVocab'),
                   model_uri=TYPES.AccountTypeVocab, domain=None, range=Optional[Union[str, "AccountTypeEnum"]])

slots.ActionArgumentNameVocab = Slot(uri=VOCABULARY.ActionArgumentNameVocab, name="ActionArgumentNameVocab", curie=VOCABULARY.curie('ActionArgumentNameVocab'),
                   model_uri=TYPES.ActionArgumentNameVocab, domain=None, range=Optional[Union[str, "ActionArgumentNameEnum"]])

slots.ActionNameVocab = Slot(uri=VOCABULARY.ActionNameVocab, name="ActionNameVocab", curie=VOCABULARY.curie('ActionNameVocab'),
                   model_uri=TYPES.ActionNameVocab, domain=None, range=Optional[str])

slots.ActionRelationshipTypeVocab = Slot(uri=VOCABULARY.ActionRelationshipTypeVocab, name="ActionRelationshipTypeVocab", curie=VOCABULARY.curie('ActionRelationshipTypeVocab'),
                   model_uri=TYPES.ActionRelationshipTypeVocab, domain=None, range=Optional[Union[str, "ActionRelationshipTypeEnum"]])

slots.ActionStatusTypeVocab = Slot(uri=VOCABULARY.ActionStatusTypeVocab, name="ActionStatusTypeVocab", curie=VOCABULARY.curie('ActionStatusTypeVocab'),
                   model_uri=TYPES.ActionStatusTypeVocab, domain=None, range=Optional[Union[str, "ActionStatusTypeEnum"]])

slots.ActionTypeVocab = Slot(uri=VOCABULARY.ActionTypeVocab, name="ActionTypeVocab", curie=VOCABULARY.curie('ActionTypeVocab'),
                   model_uri=TYPES.ActionTypeVocab, domain=None, range=Optional[Union[str, "ActionTypeEnum"]])

slots.BitnessVocab = Slot(uri=VOCABULARY.BitnessVocab, name="BitnessVocab", curie=VOCABULARY.curie('BitnessVocab'),
                   model_uri=TYPES.BitnessVocab, domain=None, range=Optional[Union[str, "BitnessEnum"]])

slots.CharacterEncodingVocab = Slot(uri=VOCABULARY.CharacterEncodingVocab, name="CharacterEncodingVocab", curie=VOCABULARY.curie('CharacterEncodingVocab'),
                   model_uri=TYPES.CharacterEncodingVocab, domain=None, range=Optional[Union[str, "CharacterEncodingEnum"]])

slots.ContactAddressScopeVocab = Slot(uri=VOCABULARY.ContactAddressScopeVocab, name="ContactAddressScopeVocab", curie=VOCABULARY.curie('ContactAddressScopeVocab'),
                   model_uri=TYPES.ContactAddressScopeVocab, domain=None, range=Optional[Union[str, "ContactAddressScopeEnum"]])

slots.ContactEmailScopeVocab = Slot(uri=VOCABULARY.ContactEmailScopeVocab, name="ContactEmailScopeVocab", curie=VOCABULARY.curie('ContactEmailScopeVocab'),
                   model_uri=TYPES.ContactEmailScopeVocab, domain=None, range=Optional[Union[str, "ContactEmailScopeEnum"]])

slots.ContactPhoneScopeVocab = Slot(uri=VOCABULARY.ContactPhoneScopeVocab, name="ContactPhoneScopeVocab", curie=VOCABULARY.curie('ContactPhoneScopeVocab'),
                   model_uri=TYPES.ContactPhoneScopeVocab, domain=None, range=Optional[Union[str, "ContactPhoneEnum"]])

slots.ContactSIPScopeVocab = Slot(uri=VOCABULARY.ContactSIPScopeVocab, name="ContactSIPScopeVocab", curie=VOCABULARY.curie('ContactSIPScopeVocab'),
                   model_uri=TYPES.ContactSIPScopeVocab, domain=None, range=Optional[Union[str, "ContactSIPScopeEnum"]])

slots.ContactURLScopeVocab = Slot(uri=VOCABULARY.ContactURLScopeVocab, name="ContactURLScopeVocab", curie=VOCABULARY.curie('ContactURLScopeVocab'),
                   model_uri=TYPES.ContactURLScopeVocab, domain=None, range=Optional[Union[str, "ContactURLScopeEnum"]])

slots.DiskTypeVocab = Slot(uri=VOCABULARY.DiskTypeVocab, name="DiskTypeVocab", curie=VOCABULARY.curie('DiskTypeVocab'),
                   model_uri=TYPES.DiskTypeVocab, domain=None, range=Optional[Union[str, "DiskTypeEnum"]])

slots.EndiannessTypeVocab = Slot(uri=VOCABULARY.EndiannessTypeVocab, name="EndiannessTypeVocab", curie=VOCABULARY.curie('EndiannessTypeVocab'),
                   model_uri=TYPES.EndiannessTypeVocab, domain=None, range=Optional[Union[str, "EndiannessTypeEnum"]])

slots.HashNameVocab = Slot(uri=VOCABULARY.HashNameVocab, name="HashNameVocab", curie=VOCABULARY.curie('HashNameVocab'),
                   model_uri=TYPES.HashNameVocab, domain=None, range=Optional[Union[str, "HashNameEnum"]])

slots.LibraryTypeVocab = Slot(uri=VOCABULARY.LibraryTypeVocab, name="LibraryTypeVocab", curie=VOCABULARY.curie('LibraryTypeVocab'),
                   model_uri=TYPES.LibraryTypeVocab, domain=None, range=Optional[Union[str, "LibraryTypeEnum"]])

slots.MemoryBlockTypeVocab = Slot(uri=VOCABULARY.MemoryBlockTypeVocab, name="MemoryBlockTypeVocab", curie=VOCABULARY.curie('MemoryBlockTypeVocab'),
                   model_uri=TYPES.MemoryBlockTypeVocab, domain=None, range=Optional[Union[str, "MemoryBlockTypeEnum"]])

slots.ObservableObjectRelationshipVocab = Slot(uri=VOCABULARY.ObservableObjectRelationshipVocab, name="ObservableObjectRelationshipVocab", curie=VOCABULARY.curie('ObservableObjectRelationshipVocab'),
                   model_uri=TYPES.ObservableObjectRelationshipVocab, domain=None, range=Optional[Union[str, "ObservableObjectRelationshipEnum"]])

slots.ObservableObjectStateVocab = Slot(uri=VOCABULARY.ObservableObjectStateVocab, name="ObservableObjectStateVocab", curie=VOCABULARY.curie('ObservableObjectStateVocab'),
                   model_uri=TYPES.ObservableObjectStateVocab, domain=None, range=Optional[Union[str, "ObservableObjectStateEnum"]])

slots.PartitionTypeVocab = Slot(uri=VOCABULARY.PartitionTypeVocab, name="PartitionTypeVocab", curie=VOCABULARY.curie('PartitionTypeVocab'),
                   model_uri=TYPES.PartitionTypeVocab, domain=None, range=Optional[Union[str, "PartitionTypeEnum"]])

slots.ProcessorArchVocab = Slot(uri=VOCABULARY.ProcessorArchVocab, name="ProcessorArchVocab", curie=VOCABULARY.curie('ProcessorArchVocab'),
                   model_uri=TYPES.ProcessorArchVocab, domain=None, range=Optional[Union[str, "ProcessorArchEnum"]])

slots.RecoveredObjectStatusVocab = Slot(uri=VOCABULARY.RecoveredObjectStatusVocab, name="RecoveredObjectStatusVocab", curie=VOCABULARY.curie('RecoveredObjectStatusVocab'),
                   model_uri=TYPES.RecoveredObjectStatusVocab, domain=None, range=Optional[Union[str, "RecoveredObjectStatusEnum"]])

slots.RegionalRegistry_typeVocab = Slot(uri=VOCABULARY.RegionalRegistry_typeVocab, name="RegionalRegistry typeVocab", curie=VOCABULARY.curie('RegionalRegistry_typeVocab'),
                   model_uri=TYPES.RegionalRegistry_typeVocab, domain=None, range=Optional[Union[str, "RegionalRegistryTypeEnum"]])

slots.RegistryDatatypeVocab = Slot(uri=VOCABULARY.RegistryDatatypeVocab, name="RegistryDatatypeVocab", curie=VOCABULARY.curie('RegistryDatatypeVocab'),
                   model_uri=TYPES.RegistryDatatypeVocab, domain=None, range=Optional[Union[str, "RegistryDatatypeEnum"]])

slots.SIMFormVocab = Slot(uri=VOCABULARY.SIMFormVocab, name="SIMFormVocab", curie=VOCABULARY.curie('SIMFormVocab'),
                   model_uri=TYPES.SIMFormVocab, domain=None, range=Optional[Union[str, "SIMFormEnum"]])

slots.SIMTypeVocab = Slot(uri=VOCABULARY.SIMTypeVocab, name="SIMTypeVocab", curie=VOCABULARY.curie('SIMTypeVocab'),
                   model_uri=TYPES.SIMTypeVocab, domain=None, range=Optional[Union[str, "SIMTypeEnum"]])

slots.TaskActionTypeVocab = Slot(uri=VOCABULARY.TaskActionTypeVocab, name="TaskActionTypeVocab", curie=VOCABULARY.curie('TaskActionTypeVocab'),
                   model_uri=TYPES.TaskActionTypeVocab, domain=None, range=Optional[Union[str, "TaskActionTypeEnum"]])

slots.TaskFlagVocab = Slot(uri=VOCABULARY.TaskFlagVocab, name="TaskFlagVocab", curie=VOCABULARY.curie('TaskFlagVocab'),
                   model_uri=TYPES.TaskFlagVocab, domain=None, range=Optional[Union[str, "TaskFlagEnum"]])

slots.TaskPriorityVocab = Slot(uri=VOCABULARY.TaskPriorityVocab, name="TaskPriorityVocab", curie=VOCABULARY.curie('TaskPriorityVocab'),
                   model_uri=TYPES.TaskPriorityVocab, domain=None, range=Optional[Union[str, "TaskPriorityEnum"]])

slots.TaskStatusVocab = Slot(uri=VOCABULARY.TaskStatusVocab, name="TaskStatusVocab", curie=VOCABULARY.curie('TaskStatusVocab'),
                   model_uri=TYPES.TaskStatusVocab, domain=None, range=Optional[Union[str, "TaskStatusEnum"]])

slots.ThreadRunningStatusVocab = Slot(uri=VOCABULARY.ThreadRunningStatusVocab, name="ThreadRunningStatusVocab", curie=VOCABULARY.curie('ThreadRunningStatusVocab'),
                   model_uri=TYPES.ThreadRunningStatusVocab, domain=None, range=Optional[Union[str, "ThreadRunningStatusEnum"]])

slots.TimestampPrecisionVocab = Slot(uri=VOCABULARY.TimestampPrecisionVocab, name="TimestampPrecisionVocab", curie=VOCABULARY.curie('TimestampPrecisionVocab'),
                   model_uri=TYPES.TimestampPrecisionVocab, domain=None, range=Optional[Union[str, "TimestampPrecisionEnum"]])

slots.TrendVocab = Slot(uri=VOCABULARY.TrendVocab, name="TrendVocab", curie=VOCABULARY.curie('TrendVocab'),
                   model_uri=TYPES.TrendVocab, domain=None, range=Optional[Union[str, "TrendEnum"]])

slots.TriggerFrequencyVocab = Slot(uri=VOCABULARY.TriggerFrequencyVocab, name="TriggerFrequencyVocab", curie=VOCABULARY.curie('TriggerFrequencyVocab'),
                   model_uri=TYPES.TriggerFrequencyVocab, domain=None, range=Optional[Union[str, "TriggerFrequencyEnum"]])

slots.TriggerTypeVocab = Slot(uri=VOCABULARY.TriggerTypeVocab, name="TriggerTypeVocab", curie=VOCABULARY.curie('TriggerTypeVocab'),
                   model_uri=TYPES.TriggerTypeVocab, domain=None, range=Optional[Union[str, "TriggerTypeEnum"]])

slots.URLTransitionTypeVocab = Slot(uri=VOCABULARY.URLTransitionTypeVocab, name="URLTransitionTypeVocab", curie=VOCABULARY.curie('URLTransitionTypeVocab'),
                   model_uri=TYPES.URLTransitionTypeVocab, domain=None, range=Optional[Union[str, "URLTransitionTypeEnum"]])

slots.UnixProcessStateVocab = Slot(uri=VOCABULARY.UnixProcessStateVocab, name="UnixProcessStateVocab", curie=VOCABULARY.curie('UnixProcessStateVocab'),
                   model_uri=TYPES.UnixProcessStateVocab, domain=None, range=Optional[Union[str, "UnixProcessStateEnum"]])

slots.WhoisContactTypeVocab = Slot(uri=VOCABULARY.WhoisContactTypeVocab, name="WhoisContactTypeVocab", curie=VOCABULARY.curie('WhoisContactTypeVocab'),
                   model_uri=TYPES.WhoisContactTypeVocab, domain=None, range=Optional[Union[str, "WhoisContactTypeEnum"]])

slots.WhoisDNSSECTypeVocab = Slot(uri=VOCABULARY.WhoisDNSSECTypeVocab, name="WhoisDNSSECTypeVocab", curie=VOCABULARY.curie('WhoisDNSSECTypeVocab'),
                   model_uri=TYPES.WhoisDNSSECTypeVocab, domain=None, range=Optional[Union[str, "WhoisDNSSECTypeEnum"]])

slots.WhoisStatusTypeVocab = Slot(uri=VOCABULARY.WhoisStatusTypeVocab, name="WhoisStatusTypeVocab", curie=VOCABULARY.curie('WhoisStatusTypeVocab'),
                   model_uri=TYPES.WhoisStatusTypeVocab, domain=None, range=Optional[Union[str, "WhoisStatusTypeEnum"]])

slots.WindowsDriveTypeVocab = Slot(uri=VOCABULARY.WindowsDriveTypeVocab, name="WindowsDriveTypeVocab", curie=VOCABULARY.curie('WindowsDriveTypeVocab'),
                   model_uri=TYPES.WindowsDriveTypeVocab, domain=None, range=Optional[Union[str, "WindowsDriveTypeEnum"]])

slots.WindowsVolumeAttributeVocab = Slot(uri=VOCABULARY.WindowsVolumeAttributeVocab, name="WindowsVolumeAttributeVocab", curie=VOCABULARY.curie('WindowsVolumeAttributeVocab'),
                   model_uri=TYPES.WindowsVolumeAttributeVocab, domain=None, range=Optional[Union[str, "WindowsVolumeAttributeEnum"]])

slots.WirelessNetworkSecurityModeVocab = Slot(uri=VOCABULARY.WirelessNetworkSecurityModeVocab, name="WirelessNetworkSecurityModeVocab", curie=VOCABULARY.curie('WirelessNetworkSecurityModeVocab'),
                   model_uri=TYPES.WirelessNetworkSecurityModeVocab, domain=None, range=Optional[Union[str, "WirelessNetworkSecurityModeEnum"]])

slots.ControlledDictionary_entry = Slot(uri=TYPES.entry, name="ControlledDictionary_entry", curie=TYPES.curie('entry'),
                   model_uri=TYPES.ControlledDictionary_entry, domain=ControlledDictionary, range=Optional[Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]]])

slots.Dictionary_entry = Slot(uri=TYPES.entry, name="Dictionary_entry", curie=TYPES.curie('entry'),
                   model_uri=TYPES.Dictionary_entry, domain=Dictionary, range=Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]])

slots.DictionaryEntry_key = Slot(uri=TYPES.key, name="DictionaryEntry_key", curie=TYPES.curie('key'),
                   model_uri=TYPES.DictionaryEntry_key, domain=DictionaryEntry, range=str)

slots.DictionaryEntry_value = Slot(uri=CORE.value, name="DictionaryEntry_value", curie=CORE.curie('value'),
                   model_uri=TYPES.DictionaryEntry_value, domain=DictionaryEntry, range=str)

slots.Hash_hashValue = Slot(uri=TYPES.hashValue, name="Hash_hashValue", curie=TYPES.curie('hashValue'),
                   model_uri=TYPES.Hash_hashValue, domain=Hash, range=hex)

slots.Hash_hashMethod = Slot(uri=TYPES.hashMethod, name="Hash_hashMethod", curie=TYPES.curie('hashMethod'),
                   model_uri=TYPES.Hash_hashMethod, domain=Hash, range=str)

slots.Thread_item = Slot(uri=COLLECTIONS.item, name="Thread_item", curie=COLLECTIONS.curie('item'),
                   model_uri=TYPES.Thread_item, domain=Thread, range=Optional[Union[Union[dict, "ThreadItem"], List[Union[dict, "ThreadItem"]]]])

slots.ThreadItem_itemContent = Slot(uri=COLLECTIONS.itemContent, name="ThreadItem_itemContent", curie=COLLECTIONS.curie('itemContent'),
                   model_uri=TYPES.ThreadItem_itemContent, domain=ThreadItem, range=Optional[Union[Union[dict, "CoItem"], List[Union[dict, "CoItem"]]]])

slots.Collection_element = Slot(uri=COLLECTIONS.element, name="Collection_element", curie=COLLECTIONS.curie('element'),
                   model_uri=TYPES.Collection_element, domain=Collection, range=Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]])

slots.Collection_size = Slot(uri=COLLECTIONS.size, name="Collection_size", curie=COLLECTIONS.curie('size'),
                   model_uri=TYPES.Collection_size, domain=Collection, range=Optional[Union[int, PositiveInteger]])

slots.List_lastItem = Slot(uri=COLLECTIONS.lastItem, name="List_lastItem", curie=COLLECTIONS.curie('lastItem'),
                   model_uri=TYPES.List_lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.List_firstItem = Slot(uri=COLLECTIONS.firstItem, name="List_firstItem", curie=COLLECTIONS.curie('firstItem'),
                   model_uri=TYPES.List_firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.List_item = Slot(uri=COLLECTIONS.item, name="List_item", curie=COLLECTIONS.curie('item'),
                   model_uri=TYPES.List_item, domain=List, range=Optional[Union[Union[dict, "ListItem"], List[Union[dict, "ListItem"]]]])

slots.ListItem__index = Slot(uri=COLLECTIONS._index, name="ListItem__index", curie=COLLECTIONS.curie('_index'),
                   model_uri=TYPES.ListItem__index, domain=ListItem, range=Union[int, PositiveInteger])

slots.Annotation_object = Slot(uri=CORE.object, name="Annotation_object", curie=CORE.curie('object'),
                   model_uri=TYPES.Annotation_object, domain=Annotation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Assertion_statement = Slot(uri=CORE.statement, name="Assertion_statement", curie=CORE.curie('statement'),
                   model_uri=TYPES.Assertion_statement, domain=Assertion, range=Optional[Union[str, List[str]]])

slots.AttributedName_namingAuthority = Slot(uri=CORE.namingAuthority, name="AttributedName_namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=TYPES.AttributedName_namingAuthority, domain=AttributedName, range=Optional[str])

slots.ConfidenceFacet_confidence = Slot(uri=CORE.confidence, name="ConfidenceFacet_confidence", curie=CORE.curie('confidence'),
                   model_uri=TYPES.ConfidenceFacet_confidence, domain=ConfidenceFacet, range=Union[int, NonNegativeIntegerType])

slots.ContextualCompilation_object = Slot(uri=CORE.object, name="ContextualCompilation_object", curie=CORE.curie('object'),
                   model_uri=TYPES.ContextualCompilation_object, domain=ContextualCompilation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.ControlledVocabulary_constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="ControlledVocabulary_constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=TYPES.ControlledVocabulary_constrainingVocabularyReference, domain=ControlledVocabulary, range=Optional[Union[str, IriType]])

slots.ControlledVocabulary_constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="ControlledVocabulary_constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=TYPES.ControlledVocabulary_constrainingVocabularyName, domain=ControlledVocabulary, range=Optional[str])

slots.ControlledVocabulary_value = Slot(uri=CORE.value, name="ControlledVocabulary_value", curie=CORE.curie('value'),
                   model_uri=TYPES.ControlledVocabulary_value, domain=ControlledVocabulary, range=str)

slots.EnclosingCompilation_object = Slot(uri=CORE.object, name="EnclosingCompilation_object", curie=CORE.curie('object'),
                   model_uri=TYPES.EnclosingCompilation_object, domain=EnclosingCompilation, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ExternalReference_referenceURL = Slot(uri=CORE.referenceURL, name="ExternalReference_referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=TYPES.ExternalReference_referenceURL, domain=ExternalReference, range=Optional[Union[str, IriType]])

slots.ExternalReference_definingContext = Slot(uri=CORE.definingContext, name="ExternalReference_definingContext", curie=CORE.curie('definingContext'),
                   model_uri=TYPES.ExternalReference_definingContext, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_externalIdentifier = Slot(uri=CORE.externalIdentifier, name="ExternalReference_externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=TYPES.ExternalReference_externalIdentifier, domain=ExternalReference, range=Optional[str])

slots.Grouping_context = Slot(uri=CORE.context, name="Grouping_context", curie=CORE.curie('context'),
                   model_uri=TYPES.Grouping_context, domain=Grouping, range=Optional[Union[str, List[str]]])

slots.Relationship_endTime = Slot(uri=CORE.endTime, name="Relationship_endTime", curie=CORE.curie('endTime'),
                   model_uri=TYPES.Relationship_endTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.Relationship_isDirectional = Slot(uri=CORE.isDirectional, name="Relationship_isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=TYPES.Relationship_isDirectional, domain=Relationship, range=Union[bool, BooleanType])

slots.Relationship_kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="Relationship_kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=TYPES.Relationship_kindOfRelationship, domain=Relationship, range=Optional[str])

slots.Relationship_target = Slot(uri=CORE.target, name="Relationship_target", curie=CORE.curie('target'),
                   model_uri=TYPES.Relationship_target, domain=Relationship, range=Union[dict, "UcoObject"])

slots.Relationship_source = Slot(uri=CORE.source, name="Relationship_source", curie=CORE.curie('source'),
                   model_uri=TYPES.Relationship_source, domain=Relationship, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Relationship_startTime = Slot(uri=CORE.startTime, name="Relationship_startTime", curie=CORE.curie('startTime'),
                   model_uri=TYPES.Relationship_startTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_description = Slot(uri=DCTERMS.description, name="UcoObject_description", curie=DCTERMS.curie('description'),
                   model_uri=TYPES.UcoObject_description, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_createdBy = Slot(uri=CORE.createdBy, name="UcoObject_createdBy", curie=CORE.curie('createdBy'),
                   model_uri=TYPES.UcoObject_createdBy, domain=UcoObject, range=Optional[str])

slots.UcoObject_externalReference = Slot(uri=CORE.externalReference, name="UcoObject_externalReference", curie=CORE.curie('externalReference'),
                   model_uri=TYPES.UcoObject_externalReference, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_hasFacet = Slot(uri=CORE.hasFacet, name="UcoObject_hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=TYPES.UcoObject_hasFacet, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_modifiedTime = Slot(uri=CORE.modifiedTime, name="UcoObject_modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=TYPES.UcoObject_modifiedTime, domain=UcoObject, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_name = Slot(uri=RDFS.label, name="UcoObject_name", curie=RDFS.curie('label'),
                   model_uri=TYPES.UcoObject_name, domain=UcoObject, range=Optional[str])

slots.UcoObject_objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="UcoObject_objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=TYPES.UcoObject_objectCreatedTime, domain=UcoObject, range=Optional[Union[str, XSDDateTime]])

slots.UcoObject_objectMarking = Slot(uri=CORE.objectMarking, name="UcoObject_objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=TYPES.UcoObject_objectMarking, domain=UcoObject, range=Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]])

slots.UcoObject_specVersion = Slot(uri=CORE.specVersion, name="UcoObject_specVersion", curie=CORE.curie('specVersion'),
                   model_uri=TYPES.UcoObject_specVersion, domain=UcoObject, range=Optional[str])

slots.UcoObject_tag = Slot(uri=CORE.tag, name="UcoObject_tag", curie=CORE.curie('tag'),
                   model_uri=TYPES.UcoObject_tag, domain=UcoObject, range=Optional[Union[str, List[str]]])