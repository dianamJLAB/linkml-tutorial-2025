# Auto generated from narad_capability_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-02T09:53:45
# Schema: narad
#
# id: https://w3id.org/narad_linkml/schema/narad/schema
# description: NARAD extension for capability-layer semantics and facility-specific signal bindings
# license: CC-BY-4.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, String

metamodel_version = "1.7.0"
version = "0.1.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCIT = CurieNamespace('ncit', 'http://purl.obolibrary.org/obo/NCIT_')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SI_UNIT = CurieNamespace('si-unit', 'http://qudt.org/vocab/unit/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/narad_linkml/schema/narad/schema/')


# Types

# Class references
class FacilityName(extended_str):
    pass


class SignalBindingName(extended_str):
    pass


class DeviceTypeSignalSetName(extended_str):
    pass


class SignalName(extended_str):
    pass


class CapabilityName(extended_str):
    pass


class TypeSpecificCapabilityId(extended_str):
    pass


class CapabilityProfileName(extended_str):
    pass


class ControlProfileFamilyName(extended_str):
    pass


class BeamlineName(extended_str):
    pass


class BeamlineElementName(extended_str):
    pass


class PVBindingName(extended_str):
    pass


class KeyValuePairName(extended_str):
    pass


@dataclass(repr=False)
class NaradModel(YAMLRoot):
    """
    Top-level NARAD document container.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/NaradModel")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NaradModel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/NaradModel")

    narad: Optional[Union[dict, "NaradConfig"]] = None
    beamlines: Optional[Union[dict[Union[str, BeamlineName], Union[dict, "Beamline"]], list[Union[dict, "Beamline"]]]] = empty_dict()
    elements: Optional[Union[dict[Union[str, BeamlineElementName], Union[dict, "BeamlineElement"]], list[Union[dict, "BeamlineElement"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.narad is not None and not isinstance(self.narad, NaradConfig):
            self.narad = NaradConfig(**as_dict(self.narad))

        self._normalize_inlined_as_list(slot_name="beamlines", slot_type=Beamline, key_name="name", keyed=True)

        self._normalize_inlined_as_list(slot_name="elements", slot_type=BeamlineElement, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NaradConfig(YAMLRoot):
    """
    NARAD configuration block containing the capability layer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/NaradConfig")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NaradConfig"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/NaradConfig")

    schema_version: Optional[str] = None
    intent: Optional[str] = None
    capability_layer: Optional[Union[dict, "CapabilityLayer"]] = None
    facility: Optional[str] = None
    control_system: Optional[str] = None
    signal_layer: Optional[Union[dict, "SignalLayer"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if self.intent is not None and not isinstance(self.intent, str):
            self.intent = str(self.intent)

        if self.capability_layer is not None and not isinstance(self.capability_layer, CapabilityLayer):
            self.capability_layer = CapabilityLayer(**as_dict(self.capability_layer))

        if self.facility is not None and not isinstance(self.facility, str):
            self.facility = str(self.facility)

        if self.control_system is not None and not isinstance(self.control_system, str):
            self.control_system = str(self.control_system)

        if self.signal_layer is not None and not isinstance(self.signal_layer, SignalLayer):
            self.signal_layer = SignalLayer(**as_dict(self.signal_layer))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapabilityLayer(YAMLRoot):
    """
    Capability-layer container for profile families.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/CapabilityLayer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CapabilityLayer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/CapabilityLayer")

    profiles: Optional[Union[dict[Union[str, ControlProfileFamilyName], Union[dict, "ControlProfileFamily"]], list[Union[dict, "ControlProfileFamily"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="profiles", slot_type=ControlProfileFamily, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalLayer(YAMLRoot):
    """
    Signal-layer container for facility-specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/SignalLayer")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SignalLayer"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/SignalLayer")

    facilities: Optional[Union[dict[Union[str, FacilityName], Union[dict, "Facility"]], list[Union[dict, "Facility"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="facilities", slot_type=Facility, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Facility(YAMLRoot):
    """
    A facility with specific signal bindings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/Facility")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Facility"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/Facility")

    name: Union[str, FacilityName] = None
    control_system: Optional[str] = None
    naming_convention: Optional[str] = None
    signal_definitions: Optional[Union[dict, "SignalDefinitions"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FacilityName):
            self.name = FacilityName(self.name)

        if self.control_system is not None and not isinstance(self.control_system, str):
            self.control_system = str(self.control_system)

        if self.naming_convention is not None and not isinstance(self.naming_convention, str):
            self.naming_convention = str(self.naming_convention)

        if self.signal_definitions is not None and not isinstance(self.signal_definitions, SignalDefinitions):
            self.signal_definitions = SignalDefinitions(**as_dict(self.signal_definitions))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalDefinitions(YAMLRoot):
    """
    Grouped EPICS signal suffix templates by semantic category.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/SignalDefinitions")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SignalDefinitions"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/SignalDefinitions")

    shared_magnet_signals: Optional[Union[dict[Union[str, SignalBindingName], Union[dict, "SignalBinding"]], list[Union[dict, "SignalBinding"]]]] = empty_dict()
    magnet_type_signals: Optional[Union[dict[Union[str, DeviceTypeSignalSetName], Union[dict, "DeviceTypeSignalSet"]], list[Union[dict, "DeviceTypeSignalSet"]]]] = empty_dict()
    instrument_type_signals: Optional[Union[dict[Union[str, DeviceTypeSignalSetName], Union[dict, "DeviceTypeSignalSet"]], list[Union[dict, "DeviceTypeSignalSet"]]]] = empty_dict()
    cavity_signals: Optional[Union[dict[Union[str, SignalBindingName], Union[dict, "SignalBinding"]], list[Union[dict, "SignalBinding"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="shared_magnet_signals", slot_type=SignalBinding, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="magnet_type_signals", slot_type=DeviceTypeSignalSet, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="instrument_type_signals", slot_type=DeviceTypeSignalSet, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="cavity_signals", slot_type=SignalBinding, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SignalBinding(YAMLRoot):
    """
    A named EPICS suffix definition for one semantic signal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/SignalBinding")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SignalBinding"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/SignalBinding")

    name: Union[str, SignalBindingName] = None
    epics_suffix: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SignalBindingName):
            self.name = SignalBindingName(self.name)

        if self.epics_suffix is not None and not isinstance(self.epics_suffix, str):
            self.epics_suffix = str(self.epics_suffix)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeviceTypeSignalSet(YAMLRoot):
    """
    Signal binding set scoped to a device type (for example, Quadrupole or BPM).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/DeviceTypeSignalSet")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DeviceTypeSignalSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/DeviceTypeSignalSet")

    name: Union[str, DeviceTypeSignalSetName] = None
    signal_bindings: Optional[Union[dict[Union[str, SignalBindingName], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DeviceTypeSignalSetName):
            self.name = DeviceTypeSignalSetName(self.name)

        self._normalize_inlined_as_dict(slot_name="signal_bindings", slot_type=SignalBinding, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Signal(YAMLRoot):
    """
    A named semantic signal used by a capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOSA["ObservableProperty"]
    class_class_curie: ClassVar[str] = "sosa:ObservableProperty"
    class_name: ClassVar[str] = "Signal"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/Signal")

    name: Union[str, SignalName] = None
    role: Optional[str] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    units: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SignalName):
            self.name = SignalName(self.name)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeEnum):
            self.data_type = DataTypeEnum(self.data_type)

        if self.units is not None and not isinstance(self.units, str):
            self.units = str(self.units)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Capability(YAMLRoot):
    """
    A grouping of related signals for a control aspect.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/Capability")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Capability"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/Capability")

    name: Union[str, CapabilityName] = None
    description: Optional[str] = None
    signals: Optional[Union[dict[Union[str, SignalName], Union[dict, Signal]], list[Union[dict, Signal]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CapabilityName):
            self.name = CapabilityName(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="signals", slot_type=Signal, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TypeSpecificCapability(YAMLRoot):
    """
    An inline capability declared within a device-type profile, with its own identifier, a semantic class label, a
    description, and a list of signals. Distinct from the shared capabilities referenced by name; these are
    profile-local definitions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/TypeSpecificCapability")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "TypeSpecificCapability"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/TypeSpecificCapability")

    id: Union[str, TypeSpecificCapabilityId] = None
    capability_class: Optional[str] = None
    description: Optional[str] = None
    signals: Optional[Union[dict[Union[str, SignalName], Union[dict, Signal]], list[Union[dict, Signal]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TypeSpecificCapabilityId):
            self.id = TypeSpecificCapabilityId(self.id)

        if self.capability_class is not None and not isinstance(self.capability_class, str):
            self.capability_class = str(self.capability_class)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="signals", slot_type=Signal, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CapabilityProfile(YAMLRoot):
    """
    A device-type profile that reuses shared capabilities and adds specific capabilities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/CapabilityProfile")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CapabilityProfile"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/CapabilityProfile")

    name: Union[str, CapabilityProfileName] = None
    kind: Optional[str] = None
    description: Optional[str] = None
    inherits_shared_capabilities: Optional[Union[str, list[str]]] = empty_list()
    type_specific_capabilities: Optional[Union[dict[Union[str, TypeSpecificCapabilityId], Union[dict, TypeSpecificCapability]], list[Union[dict, TypeSpecificCapability]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CapabilityProfileName):
            self.name = CapabilityProfileName(self.name)

        if self.kind is not None and not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.inherits_shared_capabilities, list):
            self.inherits_shared_capabilities = [self.inherits_shared_capabilities] if self.inherits_shared_capabilities is not None else []
        self.inherits_shared_capabilities = [v if isinstance(v, str) else str(v) for v in self.inherits_shared_capabilities]

        self._normalize_inlined_as_list(slot_name="type_specific_capabilities", slot_type=TypeSpecificCapability, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NodeLabels(YAMLRoot):
    """
    Labels used when projecting the profile model into a graph view.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/NodeLabels")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NodeLabels"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/NodeLabels")

    device: Optional[str] = None
    capability_family: Optional[str] = None
    profile: Optional[str] = None
    capability: Optional[str] = None
    signal: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.device is not None and not isinstance(self.device, str):
            self.device = str(self.device)

        if self.capability_family is not None and not isinstance(self.capability_family, str):
            self.capability_family = str(self.capability_family)

        if self.profile is not None and not isinstance(self.profile, str):
            self.profile = str(self.profile)

        if self.capability is not None and not isinstance(self.capability, str):
            self.capability = str(self.capability)

        if self.signal is not None and not isinstance(self.signal, str):
            self.signal = str(self.signal)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GraphProjection(YAMLRoot):
    """
    Graph projection metadata for node labels and edge categories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/GraphProjection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "GraphProjection"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/GraphProjection")

    node_labels: Optional[Union[dict, NodeLabels]] = None
    relationships: Optional[Union[Union[str, "RelationshipTypeEnum"], list[Union[str, "RelationshipTypeEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.node_labels is not None and not isinstance(self.node_labels, NodeLabels):
            self.node_labels = NodeLabels(**as_dict(self.node_labels))

        if not isinstance(self.relationships, list):
            self.relationships = [self.relationships] if self.relationships is not None else []
        self.relationships = [v if isinstance(v, RelationshipTypeEnum) else RelationshipTypeEnum(v) for v in self.relationships]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlProfileFamily(YAMLRoot):
    """
    A reusable family of control profiles sharing common semantics and structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/ControlProfileFamily")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ControlProfileFamily"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/ControlProfileFamily")

    name: Union[str, ControlProfileFamilyName] = None
    kind: Optional[str] = None
    description: Optional[str] = None
    shared_capabilities: Optional[Union[dict[Union[str, CapabilityName], Union[dict, Capability]], list[Union[dict, Capability]]]] = empty_dict()
    magnet_type_profiles: Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]] = empty_dict()
    instrument_type_profiles: Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]] = empty_dict()
    cavity_type_profiles: Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]] = empty_dict()
    graph_projection: Optional[Union[dict, GraphProjection]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ControlProfileFamilyName):
            self.name = ControlProfileFamilyName(self.name)

        if self.kind is not None and not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="shared_capabilities", slot_type=Capability, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="magnet_type_profiles", slot_type=CapabilityProfile, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="instrument_type_profiles", slot_type=CapabilityProfile, key_name="name", keyed=True)

        self._normalize_inlined_as_dict(slot_name="cavity_type_profiles", slot_type=CapabilityProfile, key_name="name", keyed=True)

        if self.graph_projection is not None and not isinstance(self.graph_projection, GraphProjection):
            self.graph_projection = GraphProjection(**as_dict(self.graph_projection))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Beamline(YAMLRoot):
    """
    An ordered sequence of beamline elements defining a beam path.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/Beamline")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Beamline"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/Beamline")

    name: Union[str, BeamlineName] = None
    kind: Optional[str] = None
    line: Optional[Union[Union[str, BeamlineElementName], list[Union[str, BeamlineElementName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BeamlineName):
            self.name = BeamlineName(self.name)

        if self.kind is not None and not isinstance(self.kind, str):
            self.kind = str(self.kind)

        if not isinstance(self.line, list):
            self.line = [self.line] if self.line is not None else []
        self.line = [v if isinstance(v, BeamlineElementName) else BeamlineElementName(v) for v in self.line]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BeamlineElement(YAMLRoot):
    """
    A single element in a beamline with optional physics parameter blocks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/BeamlineElement")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BeamlineElement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/BeamlineElement")

    name: Union[str, BeamlineElementName] = None
    kind: Optional[Union[str, "ElementKindEnum"]] = None
    length: Optional[float] = None
    RFP: Optional[Union[dict, "RFParams"]] = None
    BendP: Optional[Union[dict, "BendParams"]] = None
    MagneticMultipoleP: Optional[Union[dict, "MagneticMultipoleParams"]] = None
    SolenoidP: Optional[Union[dict, "SolenoidParams"]] = None
    narad: Optional[Union[dict, "ElementNaradRef"]] = None
    JLabP: Optional[Union[dict, "JLabParams"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, BeamlineElementName):
            self.name = BeamlineElementName(self.name)

        if self.kind is not None and not isinstance(self.kind, ElementKindEnum):
            self.kind = ElementKindEnum(self.kind)

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if self.RFP is not None and not isinstance(self.RFP, RFParams):
            self.RFP = RFParams(**as_dict(self.RFP))

        if self.BendP is not None and not isinstance(self.BendP, BendParams):
            self.BendP = BendParams(**as_dict(self.BendP))

        if self.MagneticMultipoleP is not None and not isinstance(self.MagneticMultipoleP, MagneticMultipoleParams):
            self.MagneticMultipoleP = MagneticMultipoleParams(**as_dict(self.MagneticMultipoleP))

        if self.SolenoidP is not None and not isinstance(self.SolenoidP, SolenoidParams):
            self.SolenoidP = SolenoidParams(**as_dict(self.SolenoidP))

        if self.narad is not None and not isinstance(self.narad, ElementNaradRef):
            self.narad = ElementNaradRef(**as_dict(self.narad))

        if self.JLabP is not None and not isinstance(self.JLabP, JLabParams):
            self.JLabP = JLabParams(**as_dict(self.JLabP))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementNaradRef(YAMLRoot):
    """
    NARAD semantic reference block attached to a beamline element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/ElementNaradRef")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ElementNaradRef"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/ElementNaradRef")

    capability_profile_family: Optional[Union[str, ControlProfileFamilyName]] = None
    capability_profile: Optional[Union[str, CapabilityProfileName]] = None
    magnet_semantics: Optional[Union[dict, "ElementSemantics"]] = None
    instrument_semantics: Optional[Union[dict, "ElementSemantics"]] = None
    cavity_semantics: Optional[Union[dict, "ElementSemantics"]] = None
    signal_bindings: Optional[Union[dict[Union[str, PVBindingName], Union[dict, "PVBinding"]], list[Union[dict, "PVBinding"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.capability_profile_family is not None and not isinstance(self.capability_profile_family, ControlProfileFamilyName):
            self.capability_profile_family = ControlProfileFamilyName(self.capability_profile_family)

        if self.capability_profile is not None and not isinstance(self.capability_profile, CapabilityProfileName):
            self.capability_profile = CapabilityProfileName(self.capability_profile)

        if self.magnet_semantics is not None and not isinstance(self.magnet_semantics, ElementSemantics):
            self.magnet_semantics = ElementSemantics(**as_dict(self.magnet_semantics))

        if self.instrument_semantics is not None and not isinstance(self.instrument_semantics, ElementSemantics):
            self.instrument_semantics = ElementSemantics(**as_dict(self.instrument_semantics))

        if self.cavity_semantics is not None and not isinstance(self.cavity_semantics, ElementSemantics):
            self.cavity_semantics = ElementSemantics(**as_dict(self.cavity_semantics))

        self._normalize_inlined_as_dict(slot_name="signal_bindings", slot_type=PVBinding, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementSemantics(YAMLRoot):
    """
    Semantic context referencing shared and type-specific capability names for a beamline element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/ElementSemantics")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ElementSemantics"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/ElementSemantics")

    shared_capabilities: Optional[Union[Union[str, CapabilityName], list[Union[str, CapabilityName]]]] = empty_list()
    type_specific_capabilities: Optional[Union[Union[str, TypeSpecificCapabilityId], list[Union[str, TypeSpecificCapabilityId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.shared_capabilities, list):
            self.shared_capabilities = [self.shared_capabilities] if self.shared_capabilities is not None else []
        self.shared_capabilities = [v if isinstance(v, CapabilityName) else CapabilityName(v) for v in self.shared_capabilities]

        if not isinstance(self.type_specific_capabilities, list):
            self.type_specific_capabilities = [self.type_specific_capabilities] if self.type_specific_capabilities is not None else []
        self.type_specific_capabilities = [v if isinstance(v, TypeSpecificCapabilityId) else TypeSpecificCapabilityId(v) for v in self.type_specific_capabilities]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PVBinding(YAMLRoot):
    """
    A concrete PV (Process Variable) binding for one semantic signal on a beamline element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/PVBinding")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PVBinding"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/PVBinding")

    name: Union[str, PVBindingName] = None
    facility: Optional[str] = None
    control_system: Optional[str] = None
    pv: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PVBindingName):
            self.name = PVBindingName(self.name)

        if self.facility is not None and not isinstance(self.facility, str):
            self.facility = str(self.facility)

        if self.control_system is not None and not isinstance(self.control_system, str):
            self.control_system = str(self.control_system)

        if self.pv is not None and not isinstance(self.pv, str):
            self.pv = str(self.pv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RFParams(YAMLRoot):
    """
    RF cavity physics parameters (frequency, voltage, phase).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/RFParams")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "RFParams"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/RFParams")

    frequency: Optional[float] = None
    voltage: Optional[float] = None
    phase: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.frequency is not None and not isinstance(self.frequency, float):
            self.frequency = float(self.frequency)

        if self.voltage is not None and not isinstance(self.voltage, float):
            self.voltage = float(self.voltage)

        if self.phase is not None and not isinstance(self.phase, float):
            self.phase = float(self.phase)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BendParams(YAMLRoot):
    """
    Dipole/bend physics parameters (entry angle, exit edge angles).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/BendParams")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BendParams"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/BendParams")

    angle_ref: Optional[float] = None
    e1: Optional[float] = None
    e2: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.angle_ref is not None and not isinstance(self.angle_ref, float):
            self.angle_ref = float(self.angle_ref)

        if self.e1 is not None and not isinstance(self.e1, float):
            self.e1 = float(self.e1)

        if self.e2 is not None and not isinstance(self.e2, float):
            self.e2 = float(self.e2)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MagneticMultipoleParams(YAMLRoot):
    """
    Magnetic multipole physics parameters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/MagneticMultipoleParams")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "MagneticMultipoleParams"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/MagneticMultipoleParams")

    kn1: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.kn1 is not None and not isinstance(self.kn1, float):
            self.kn1 = float(self.kn1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SolenoidParams(YAMLRoot):
    """
    Solenoid physics parameters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/SolenoidParams")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SolenoidParams"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/SolenoidParams")

    ksol: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ksol is not None and not isinstance(self.ksol, float):
            self.ksol = float(self.ksol)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JLabParams(YAMLRoot):
    """
    JLab-specific element parameters: type designation, accelerator model name, and open property map.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/JLabParams")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "JLabParams"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/JLabParams")

    jlab_type: Optional[str] = None
    modeled_as: Optional[str] = None
    properties: Optional[Union[dict[Union[str, KeyValuePairName], Union[dict, "KeyValuePair"]], list[Union[dict, "KeyValuePair"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.jlab_type is not None and not isinstance(self.jlab_type, str):
            self.jlab_type = str(self.jlab_type)

        if self.modeled_as is not None and not isinstance(self.modeled_as, str):
            self.modeled_as = str(self.modeled_as)

        self._normalize_inlined_as_dict(slot_name="properties", slot_type=KeyValuePair, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeyValuePair(YAMLRoot):
    """
    A generic key-value pair for open-ended property maps.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/KeyValuePair")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "KeyValuePair"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/narad_linkml/schema/narad/schema/KeyValuePair")

    name: Union[str, KeyValuePairName] = None
    value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, KeyValuePairName):
            self.name = KeyValuePairName(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


# Enumerations
class DataTypeEnum(EnumDefinitionImpl):
    """
    Allowed data types for signal values.
    """
    int = PermissibleValue(
        text="int",
        description="""A data type comprised of numbers with no fractional part, including negative and positive values.""",
        meaning=NCIT["C47840"])
    float = PermissibleValue(
        text="float",
        description="A number that can have its decimal point in any position.",
        meaning=NCIT["C48150"])
    double = PermissibleValue(
        text="double",
        description="A 64-bit floating-point value.",
        meaning=NCIT["C48870"])
    string = PermissibleValue(
        text="string",
        description="A sequence of characters used to represent text.",
        meaning=NCIT["C45253"])
    boolean = PermissibleValue(
        text="boolean",
        description="A data type with two possible values: true and false.",
        meaning=NCIT["C45254"])
    boolean_non_null = PermissibleValue(
        text="boolean_non_null",
        description="A two-value boolean data type that does not include null flavor.",
        meaning=NCIT["C95630"])
    date = PermissibleValue(
        text="date",
        description="A calendar date (year, month, day).",
        meaning=NCIT["C48871"])
    coded_value = PermissibleValue(
        text="coded_value",
        description="A code value referenced from an external coding system or ontology.",
        meaning=NCIT["C95637"])

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Allowed data types for signal values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="""A special value that may represent an unknown, missing, not applicable, or undefined value.""",
                meaning=NCIT["C45255"]))

class RelationshipTypeEnum(EnumDefinitionImpl):
    """
    Allowed edge labels in the profile-family graph projection.
    """
    HAS_SHARED_CAPABILITY = PermissibleValue(text="HAS_SHARED_CAPABILITY")
    HAS_TYPE_PROFILE = PermissibleValue(text="HAS_TYPE_PROFILE")
    INHERITS_CAPABILITY = PermissibleValue(text="INHERITS_CAPABILITY")
    HAS_TYPE_SPECIFIC_CAPABILITY = PermissibleValue(text="HAS_TYPE_SPECIFIC_CAPABILITY")
    HAS_SIGNAL = PermissibleValue(text="HAS_SIGNAL")
    IMPLEMENTED_BY = PermissibleValue(text="IMPLEMENTED_BY")
    BINDS_TO = PermissibleValue(text="BINDS_TO")
    LOCATED_IN = PermissibleValue(text="LOCATED_IN")
    CONTROLLED_BY = PermissibleValue(text="CONTROLLED_BY")

    _defn = EnumDefinition(
        name="RelationshipTypeEnum",
        description="Allowed edge labels in the profile-family graph projection.",
    )

class ElementKindEnum(EnumDefinitionImpl):
    """
    Controlled vocabulary for beamline element types.
    """
    Drift = PermissibleValue(text="Drift")
    Marker = PermissibleValue(text="Marker")
    BPM = PermissibleValue(text="BPM")
    Corrector = PermissibleValue(text="Corrector")
    Dipole = PermissibleValue(text="Dipole")
    Quadrupole = PermissibleValue(text="Quadrupole")
    Solenoid = PermissibleValue(text="Solenoid")
    RFCavity = PermissibleValue(text="RFCavity")
    Instrument = PermissibleValue(text="Instrument")

    _defn = EnumDefinition(
        name="ElementKindEnum",
        description="Controlled vocabulary for beamline element types.",
    )

# Slots
class slots:
    pass

slots.narad = Slot(uri=DEFAULT_.narad, name="narad", curie=DEFAULT_.curie('narad'),
                   model_uri=DEFAULT_.narad, domain=None, range=Optional[Union[dict, NaradConfig]])

slots.schema_version = Slot(uri=DEFAULT_.schema_version, name="schema_version", curie=DEFAULT_.curie('schema_version'),
                   model_uri=DEFAULT_.schema_version, domain=None, range=Optional[str])

slots.intent = Slot(uri=DEFAULT_.intent, name="intent", curie=DEFAULT_.curie('intent'),
                   model_uri=DEFAULT_.intent, domain=None, range=Optional[str])

slots.facility = Slot(uri=DEFAULT_.facility, name="facility", curie=DEFAULT_.curie('facility'),
                   model_uri=DEFAULT_.facility, domain=None, range=Optional[str])

slots.control_system = Slot(uri=DEFAULT_.control_system, name="control_system", curie=DEFAULT_.curie('control_system'),
                   model_uri=DEFAULT_.control_system, domain=None, range=Optional[str])

slots.naming_convention = Slot(uri=DEFAULT_.naming_convention, name="naming_convention", curie=DEFAULT_.curie('naming_convention'),
                   model_uri=DEFAULT_.naming_convention, domain=None, range=Optional[str])

slots.capability_layer = Slot(uri=DEFAULT_.capability_layer, name="capability_layer", curie=DEFAULT_.curie('capability_layer'),
                   model_uri=DEFAULT_.capability_layer, domain=None, range=Optional[Union[dict, CapabilityLayer]])

slots.profiles = Slot(uri=DEFAULT_.profiles, name="profiles", curie=DEFAULT_.curie('profiles'),
                   model_uri=DEFAULT_.profiles, domain=None, range=Optional[Union[dict[Union[str, ControlProfileFamilyName], Union[dict, ControlProfileFamily]], list[Union[dict, ControlProfileFamily]]]])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.name = Slot(uri=DEFAULT_.name, name="name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=URIRef)

slots.description = Slot(uri=DEFAULT_.description, name="description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.capability_class = Slot(uri=DEFAULT_.capability_class, name="capability_class", curie=DEFAULT_.curie('capability_class'),
                   model_uri=DEFAULT_.capability_class, domain=None, range=Optional[str])

slots.kind = Slot(uri=DEFAULT_.kind, name="kind", curie=DEFAULT_.curie('kind'),
                   model_uri=DEFAULT_.kind, domain=None, range=Optional[str])

slots.class = Slot(uri=DEFAULT_.class, name="class", curie=DEFAULT_.curie('class'),
                   model_uri=DEFAULT_.class, domain=None, range=Optional[str])

slots.role = Slot(uri=DEFAULT_.role, name="role", curie=DEFAULT_.curie('role'),
                   model_uri=DEFAULT_.role, domain=None, range=Optional[str])

slots.data_type = Slot(uri=DEFAULT_.data_type, name="data_type", curie=DEFAULT_.curie('data_type'),
                   model_uri=DEFAULT_.data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.units = Slot(uri=DEFAULT_.units, name="units", curie=DEFAULT_.curie('units'),
                   model_uri=DEFAULT_.units, domain=None, range=Optional[str])

slots.signals = Slot(uri=DEFAULT_.signals, name="signals", curie=DEFAULT_.curie('signals'),
                   model_uri=DEFAULT_.signals, domain=None, range=Optional[Union[dict[Union[str, SignalName], Union[dict, Signal]], list[Union[dict, Signal]]]])

slots.shared_capabilities = Slot(uri=DEFAULT_.shared_capabilities, name="shared_capabilities", curie=DEFAULT_.curie('shared_capabilities'),
                   model_uri=DEFAULT_.shared_capabilities, domain=None, range=Optional[Union[dict[Union[str, CapabilityName], Union[dict, Capability]], list[Union[dict, Capability]]]])

slots.inherits_shared_capabilities = Slot(uri=DEFAULT_.inherits_shared_capabilities, name="inherits_shared_capabilities", curie=DEFAULT_.curie('inherits_shared_capabilities'),
                   model_uri=DEFAULT_.inherits_shared_capabilities, domain=None, range=Optional[Union[str, list[str]]])

slots.type_specific_capabilities = Slot(uri=DEFAULT_.type_specific_capabilities, name="type_specific_capabilities", curie=DEFAULT_.curie('type_specific_capabilities'),
                   model_uri=DEFAULT_.type_specific_capabilities, domain=None, range=Optional[Union[dict[Union[str, TypeSpecificCapabilityId], Union[dict, TypeSpecificCapability]], list[Union[dict, TypeSpecificCapability]]]])

slots.magnet_type_profiles = Slot(uri=DEFAULT_.magnet_type_profiles, name="magnet_type_profiles", curie=DEFAULT_.curie('magnet_type_profiles'),
                   model_uri=DEFAULT_.magnet_type_profiles, domain=None, range=Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]])

slots.instrument_type_profiles = Slot(uri=DEFAULT_.instrument_type_profiles, name="instrument_type_profiles", curie=DEFAULT_.curie('instrument_type_profiles'),
                   model_uri=DEFAULT_.instrument_type_profiles, domain=None, range=Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]])

slots.cavity_type_profiles = Slot(uri=DEFAULT_.cavity_type_profiles, name="cavity_type_profiles", curie=DEFAULT_.curie('cavity_type_profiles'),
                   model_uri=DEFAULT_.cavity_type_profiles, domain=None, range=Optional[Union[dict[Union[str, CapabilityProfileName], Union[dict, CapabilityProfile]], list[Union[dict, CapabilityProfile]]]])

slots.graph_projection = Slot(uri=DEFAULT_.graph_projection, name="graph_projection", curie=DEFAULT_.curie('graph_projection'),
                   model_uri=DEFAULT_.graph_projection, domain=None, range=Optional[Union[dict, GraphProjection]])

slots.node_labels = Slot(uri=DEFAULT_.node_labels, name="node_labels", curie=DEFAULT_.curie('node_labels'),
                   model_uri=DEFAULT_.node_labels, domain=None, range=Optional[Union[dict, NodeLabels]])

slots.device = Slot(uri=DEFAULT_.device, name="device", curie=DEFAULT_.curie('device'),
                   model_uri=DEFAULT_.device, domain=None, range=Optional[str])

slots.capability_family = Slot(uri=DEFAULT_.capability_family, name="capability_family", curie=DEFAULT_.curie('capability_family'),
                   model_uri=DEFAULT_.capability_family, domain=None, range=Optional[str])

slots.profile = Slot(uri=DEFAULT_.profile, name="profile", curie=DEFAULT_.curie('profile'),
                   model_uri=DEFAULT_.profile, domain=None, range=Optional[str])

slots.capability = Slot(uri=DEFAULT_.capability, name="capability", curie=DEFAULT_.curie('capability'),
                   model_uri=DEFAULT_.capability, domain=None, range=Optional[str])

slots.signal = Slot(uri=DEFAULT_.signal, name="signal", curie=DEFAULT_.curie('signal'),
                   model_uri=DEFAULT_.signal, domain=None, range=Optional[str])

slots.relationships = Slot(uri=DEFAULT_.relationships, name="relationships", curie=DEFAULT_.curie('relationships'),
                   model_uri=DEFAULT_.relationships, domain=None, range=Optional[Union[Union[str, "RelationshipTypeEnum"], list[Union[str, "RelationshipTypeEnum"]]]])

slots.signal_layer = Slot(uri=DEFAULT_.signal_layer, name="signal_layer", curie=DEFAULT_.curie('signal_layer'),
                   model_uri=DEFAULT_.signal_layer, domain=None, range=Optional[Union[dict, SignalLayer]])

slots.facilities = Slot(uri=DEFAULT_.facilities, name="facilities", curie=DEFAULT_.curie('facilities'),
                   model_uri=DEFAULT_.facilities, domain=None, range=Optional[Union[dict[Union[str, FacilityName], Union[dict, Facility]], list[Union[dict, Facility]]]])

slots.signal_definitions = Slot(uri=DEFAULT_.signal_definitions, name="signal_definitions", curie=DEFAULT_.curie('signal_definitions'),
                   model_uri=DEFAULT_.signal_definitions, domain=None, range=Optional[Union[dict, SignalDefinitions]])

slots.epics_suffix = Slot(uri=DEFAULT_.epics_suffix, name="epics_suffix", curie=DEFAULT_.curie('epics_suffix'),
                   model_uri=DEFAULT_.epics_suffix, domain=None, range=Optional[str])

slots.shared_magnet_signals = Slot(uri=DEFAULT_.shared_magnet_signals, name="shared_magnet_signals", curie=DEFAULT_.curie('shared_magnet_signals'),
                   model_uri=DEFAULT_.shared_magnet_signals, domain=None, range=Optional[Union[dict[Union[str, SignalBindingName], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]])

slots.cavity_signals = Slot(uri=DEFAULT_.cavity_signals, name="cavity_signals", curie=DEFAULT_.curie('cavity_signals'),
                   model_uri=DEFAULT_.cavity_signals, domain=None, range=Optional[Union[dict[Union[str, SignalBindingName], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]])

slots.magnet_type_signals = Slot(uri=DEFAULT_.magnet_type_signals, name="magnet_type_signals", curie=DEFAULT_.curie('magnet_type_signals'),
                   model_uri=DEFAULT_.magnet_type_signals, domain=None, range=Optional[Union[dict[Union[str, DeviceTypeSignalSetName], Union[dict, DeviceTypeSignalSet]], list[Union[dict, DeviceTypeSignalSet]]]])

slots.instrument_type_signals = Slot(uri=DEFAULT_.instrument_type_signals, name="instrument_type_signals", curie=DEFAULT_.curie('instrument_type_signals'),
                   model_uri=DEFAULT_.instrument_type_signals, domain=None, range=Optional[Union[dict[Union[str, DeviceTypeSignalSetName], Union[dict, DeviceTypeSignalSet]], list[Union[dict, DeviceTypeSignalSet]]]])

slots.signal_bindings = Slot(uri=DEFAULT_.signal_bindings, name="signal_bindings", curie=DEFAULT_.curie('signal_bindings'),
                   model_uri=DEFAULT_.signal_bindings, domain=None, range=Optional[Union[dict[Union[str, SignalBindingName], Union[dict, SignalBinding]], list[Union[dict, SignalBinding]]]])

slots.beamlines = Slot(uri=DEFAULT_.beamlines, name="beamlines", curie=DEFAULT_.curie('beamlines'),
                   model_uri=DEFAULT_.beamlines, domain=None, range=Optional[Union[dict[Union[str, BeamlineName], Union[dict, Beamline]], list[Union[dict, Beamline]]]])

slots.elements = Slot(uri=DEFAULT_.elements, name="elements", curie=DEFAULT_.curie('elements'),
                   model_uri=DEFAULT_.elements, domain=None, range=Optional[Union[dict[Union[str, BeamlineElementName], Union[dict, BeamlineElement]], list[Union[dict, BeamlineElement]]]])

slots.line = Slot(uri=DEFAULT_.line, name="line", curie=DEFAULT_.curie('line'),
                   model_uri=DEFAULT_.line, domain=None, range=Optional[Union[Union[str, BeamlineElementName], list[Union[str, BeamlineElementName]]]])

slots.length = Slot(uri=DEFAULT_.length, name="length", curie=DEFAULT_.curie('length'),
                   model_uri=DEFAULT_.length, domain=None, range=Optional[float])

slots.RFP = Slot(uri=DEFAULT_.RFP, name="RFP", curie=DEFAULT_.curie('RFP'),
                   model_uri=DEFAULT_.RFP, domain=None, range=Optional[Union[dict, RFParams]])

slots.BendP = Slot(uri=DEFAULT_.BendP, name="BendP", curie=DEFAULT_.curie('BendP'),
                   model_uri=DEFAULT_.BendP, domain=None, range=Optional[Union[dict, BendParams]])

slots.MagneticMultipoleP = Slot(uri=DEFAULT_.MagneticMultipoleP, name="MagneticMultipoleP", curie=DEFAULT_.curie('MagneticMultipoleP'),
                   model_uri=DEFAULT_.MagneticMultipoleP, domain=None, range=Optional[Union[dict, MagneticMultipoleParams]])

slots.SolenoidP = Slot(uri=DEFAULT_.SolenoidP, name="SolenoidP", curie=DEFAULT_.curie('SolenoidP'),
                   model_uri=DEFAULT_.SolenoidP, domain=None, range=Optional[Union[dict, SolenoidParams]])

slots.JLabP = Slot(uri=DEFAULT_.JLabP, name="JLabP", curie=DEFAULT_.curie('JLabP'),
                   model_uri=DEFAULT_.JLabP, domain=None, range=Optional[Union[dict, JLabParams]])

slots.capability_profile_family = Slot(uri=DEFAULT_.capability_profile_family, name="capability_profile_family", curie=DEFAULT_.curie('capability_profile_family'),
                   model_uri=DEFAULT_.capability_profile_family, domain=None, range=Optional[Union[str, ControlProfileFamilyName]])

slots.capability_profile = Slot(uri=DEFAULT_.capability_profile, name="capability_profile", curie=DEFAULT_.curie('capability_profile'),
                   model_uri=DEFAULT_.capability_profile, domain=None, range=Optional[Union[str, CapabilityProfileName]])

slots.magnet_semantics = Slot(uri=DEFAULT_.magnet_semantics, name="magnet_semantics", curie=DEFAULT_.curie('magnet_semantics'),
                   model_uri=DEFAULT_.magnet_semantics, domain=None, range=Optional[Union[dict, ElementSemantics]])

slots.instrument_semantics = Slot(uri=DEFAULT_.instrument_semantics, name="instrument_semantics", curie=DEFAULT_.curie('instrument_semantics'),
                   model_uri=DEFAULT_.instrument_semantics, domain=None, range=Optional[Union[dict, ElementSemantics]])

slots.cavity_semantics = Slot(uri=DEFAULT_.cavity_semantics, name="cavity_semantics", curie=DEFAULT_.curie('cavity_semantics'),
                   model_uri=DEFAULT_.cavity_semantics, domain=None, range=Optional[Union[dict, ElementSemantics]])

slots.pv = Slot(uri=DEFAULT_.pv, name="pv", curie=DEFAULT_.curie('pv'),
                   model_uri=DEFAULT_.pv, domain=None, range=Optional[str])

slots.frequency = Slot(uri=DEFAULT_.frequency, name="frequency", curie=DEFAULT_.curie('frequency'),
                   model_uri=DEFAULT_.frequency, domain=None, range=Optional[float])

slots.voltage = Slot(uri=DEFAULT_.voltage, name="voltage", curie=DEFAULT_.curie('voltage'),
                   model_uri=DEFAULT_.voltage, domain=None, range=Optional[float])

slots.phase = Slot(uri=DEFAULT_.phase, name="phase", curie=DEFAULT_.curie('phase'),
                   model_uri=DEFAULT_.phase, domain=None, range=Optional[float])

slots.angle_ref = Slot(uri=DEFAULT_.angle_ref, name="angle_ref", curie=DEFAULT_.curie('angle_ref'),
                   model_uri=DEFAULT_.angle_ref, domain=None, range=Optional[float])

slots.e1 = Slot(uri=DEFAULT_.e1, name="e1", curie=DEFAULT_.curie('e1'),
                   model_uri=DEFAULT_.e1, domain=None, range=Optional[float])

slots.e2 = Slot(uri=DEFAULT_.e2, name="e2", curie=DEFAULT_.curie('e2'),
                   model_uri=DEFAULT_.e2, domain=None, range=Optional[float])

slots.kn1 = Slot(uri=DEFAULT_.kn1, name="kn1", curie=DEFAULT_.curie('kn1'),
                   model_uri=DEFAULT_.kn1, domain=None, range=Optional[float])

slots.ksol = Slot(uri=DEFAULT_.ksol, name="ksol", curie=DEFAULT_.curie('ksol'),
                   model_uri=DEFAULT_.ksol, domain=None, range=Optional[float])

slots.jlab_type = Slot(uri=DEFAULT_.jlab_type, name="jlab_type", curie=DEFAULT_.curie('jlab_type'),
                   model_uri=DEFAULT_.jlab_type, domain=None, range=Optional[str])

slots.modeled_as = Slot(uri=DEFAULT_.modeled_as, name="modeled_as", curie=DEFAULT_.curie('modeled_as'),
                   model_uri=DEFAULT_.modeled_as, domain=None, range=Optional[str])

slots.properties = Slot(uri=DEFAULT_.properties, name="properties", curie=DEFAULT_.curie('properties'),
                   model_uri=DEFAULT_.properties, domain=None, range=Optional[Union[dict[Union[str, KeyValuePairName], Union[dict, KeyValuePair]], list[Union[dict, KeyValuePair]]]])

slots.value = Slot(uri=DEFAULT_.value, name="value", curie=DEFAULT_.curie('value'),
                   model_uri=DEFAULT_.value, domain=None, range=Optional[str])

slots.elementSemantics__shared_capabilities = Slot(uri=DEFAULT_.shared_capabilities, name="elementSemantics__shared_capabilities", curie=DEFAULT_.curie('shared_capabilities'),
                   model_uri=DEFAULT_.elementSemantics__shared_capabilities, domain=None, range=Optional[Union[Union[str, CapabilityName], list[Union[str, CapabilityName]]]])

slots.elementSemantics__type_specific_capabilities = Slot(uri=DEFAULT_.type_specific_capabilities, name="elementSemantics__type_specific_capabilities", curie=DEFAULT_.curie('type_specific_capabilities'),
                   model_uri=DEFAULT_.elementSemantics__type_specific_capabilities, domain=None, range=Optional[Union[Union[str, TypeSpecificCapabilityId], list[Union[str, TypeSpecificCapabilityId]]]])

slots.BeamlineElement_kind = Slot(uri=DEFAULT_.kind, name="BeamlineElement_kind", curie=DEFAULT_.curie('kind'),
                   model_uri=DEFAULT_.BeamlineElement_kind, domain=BeamlineElement, range=Optional[Union[str, "ElementKindEnum"]])

slots.BeamlineElement_narad = Slot(uri=DEFAULT_.narad, name="BeamlineElement_narad", curie=DEFAULT_.curie('narad'),
                   model_uri=DEFAULT_.BeamlineElement_narad, domain=BeamlineElement, range=Optional[Union[dict, "ElementNaradRef"]])

slots.ElementNaradRef_signal_bindings = Slot(uri=DEFAULT_.signal_bindings, name="ElementNaradRef_signal_bindings", curie=DEFAULT_.curie('signal_bindings'),
                   model_uri=DEFAULT_.ElementNaradRef_signal_bindings, domain=ElementNaradRef, range=Optional[Union[dict[Union[str, PVBindingName], Union[dict, "PVBinding"]], list[Union[dict, "PVBinding"]]]])
