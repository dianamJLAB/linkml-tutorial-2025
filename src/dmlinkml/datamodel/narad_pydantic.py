from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'https://w3id.org/narad_linkml/schema/narad/schema/',
     'description': 'NARAD extension for capability-layer semantics and '
                    'facility-specific signal bindings',
     'id': 'https://w3id.org/narad_linkml/schema/narad/schema',
     'imports': ['linkml:types'],
     'license': 'CC-BY-4.0',
     'name': 'narad',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'ncit': {'prefix_prefix': 'ncit',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'si-unit': {'prefix_prefix': 'si-unit',
                              'prefix_reference': 'http://qudt.org/vocab/unit/'},
                  'sosa': {'prefix_prefix': 'sosa',
                           'prefix_reference': 'http://www.w3.org/ns/sosa/'}},
     'source_file': 'src/dmlinkml/schema/narad_capability_linkml.yaml'} )

class DataTypeEnum(str, Enum):
    """
    Allowed data types for signal values.
    """
    None_ = "None"
    """
    A special value that may represent an unknown, missing, not applicable, or undefined value.
    """
    int = "int"
    """
    A data type comprised of numbers with no fractional part, including negative and positive values.
    """
    float = "float"
    """
    A number that can have its decimal point in any position.
    """
    double = "double"
    """
    A 64-bit floating-point value.
    """
    string = "string"
    """
    A sequence of characters used to represent text.
    """
    boolean = "boolean"
    """
    A data type with two possible values: true and false.
    """
    boolean_non_null = "boolean_non_null"
    """
    A two-value boolean data type that does not include null flavor.
    """
    date = "date"
    """
    A calendar date (year, month, day).
    """
    coded_value = "coded_value"
    """
    A code value referenced from an external coding system or ontology.
    """


class RelationshipTypeEnum(str, Enum):
    """
    Allowed edge labels in the profile-family graph projection.
    """
    HAS_SHARED_CAPABILITY = "HAS_SHARED_CAPABILITY"
    HAS_TYPE_PROFILE = "HAS_TYPE_PROFILE"
    INHERITS_CAPABILITY = "INHERITS_CAPABILITY"
    HAS_TYPE_SPECIFIC_CAPABILITY = "HAS_TYPE_SPECIFIC_CAPABILITY"
    HAS_SIGNAL = "HAS_SIGNAL"
    IMPLEMENTED_BY = "IMPLEMENTED_BY"
    BINDS_TO = "BINDS_TO"
    LOCATED_IN = "LOCATED_IN"
    CONTROLLED_BY = "CONTROLLED_BY"


class ElementKindEnum(str, Enum):
    """
    Controlled vocabulary for beamline element types.
    """
    Drift = "Drift"
    Marker = "Marker"
    BPM = "BPM"
    Corrector = "Corrector"
    Dipole = "Dipole"
    Quadrupole = "Quadrupole"
    Solenoid = "Solenoid"
    RFCavity = "RFCavity"
    Instrument = "Instrument"



class NaradModel(ConfiguredBaseModel):
    """
    Top-level NARAD document container.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema',
         'tree_root': True})

    narad: Optional[NaradConfig] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradModel', 'BeamlineElement']} })
    beamlines: Optional[list[Beamline]] = Field(default=[], description="""Ordered list of beamlines in this NARAD document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradModel']} })
    elements: Optional[list[BeamlineElement]] = Field(default=[], description="""Beamline element definitions (referenced by name from beamline line sequences).""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradModel']} })


class NaradConfig(ConfiguredBaseModel):
    """
    NARAD configuration block containing the capability layer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    schema_version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig']} })
    intent: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig']} })
    capability_layer: Optional[CapabilityLayer] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig']} })
    facility: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig', 'PVBinding']} })
    control_system: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig', 'Facility', 'PVBinding']} })
    signal_layer: Optional[SignalLayer] = Field(default=None, description="""Signal-layer container for facility-specific signal bindings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig']} })


class CapabilityLayer(ConfiguredBaseModel):
    """
    Capability-layer container for profile families.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    profiles: Optional[dict[str, ControlProfileFamily]] = Field(default=None, description="""Control profile families keyed by family name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapabilityLayer']} })


class SignalLayer(ConfiguredBaseModel):
    """
    Signal-layer container for facility-specific signal bindings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    facilities: Optional[dict[str, Facility]] = Field(default=None, description="""Facility identifiers for facility-specific signal bindings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SignalLayer']} })


class Facility(ConfiguredBaseModel):
    """
    A facility with specific signal bindings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    control_system: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig', 'Facility', 'PVBinding']} })
    naming_convention: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Facility']} })
    signal_definitions: Optional[SignalDefinitions] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Facility']} })


class SignalDefinitions(ConfiguredBaseModel):
    """
    Grouped EPICS signal suffix templates by semantic category.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    shared_magnet_signals: Optional[dict[str, SignalBinding]] = Field(default=None, description="""Shared magnet signal definitions keyed by signal name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SignalDefinitions']} })
    magnet_type_signals: Optional[dict[str, DeviceTypeSignalSet]] = Field(default=None, description="""Magnet-type-specific signal definition groups keyed by device type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SignalDefinitions']} })
    instrument_type_signals: Optional[dict[str, DeviceTypeSignalSet]] = Field(default=None, description="""Instrument-type-specific signal definition groups keyed by device type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SignalDefinitions']} })
    cavity_signals: Optional[dict[str, SignalBinding]] = Field(default=None, description="""Cavity signal definitions keyed by signal name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SignalDefinitions']} })


class SignalBinding(ConfiguredBaseModel):
    """
    A named EPICS suffix definition for one semantic signal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    epics_suffix: Optional[str] = Field(default=None, description="""Facility-specific EPICS suffix for a semantic signal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SignalBinding']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SignalBinding',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily']} })


class DeviceTypeSignalSet(ConfiguredBaseModel):
    """
    Signal binding set scoped to a device type (for example, Quadrupole or BPM).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    signal_bindings: Optional[dict[str, SignalBinding]] = Field(default=None, description="""Signal definitions keyed by signal name within a device type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DeviceTypeSignalSet', 'ElementNaradRef']} })


class Signal(ConfiguredBaseModel):
    """
    A named semantic signal used by a capability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['epics_pv', 'pv', 'process_variable', 'EPICS Process Variable'],
         'broad_mappings': ['qudt:QuantityKind'],
         'class_uri': 'sosa:ObservableProperty',
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    role: Optional[str] = Field(default=None, description="""The role of the signal in the control model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Signal']} })
    data_type: Optional[DataTypeEnum] = Field(default=None, description="""The data type of the signal's value.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['ncit:C42645', 'qudt:Datatype'], 'domain_of': ['Signal']} })
    units: Optional[str] = Field(default=None, description="""Units of measurement or null for unitless values.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['si-unit:Unit'], 'domain_of': ['Signal']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SignalBinding',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily']} })


class Capability(ConfiguredBaseModel):
    """
    A grouping of related signals for a control aspect.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    id: str = Field(default=..., description="""Unique identifier for the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Capability']} })
    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SignalBinding',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily']} })
    signals: Optional[list[Signal]] = Field(default=[], description="""Signals within a capability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Capability']} })


class CapabilityProfile(ConfiguredBaseModel):
    """
    A device-type profile that reuses shared capabilities and adds specific capabilities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    kind: Optional[str] = Field(default=None, description="""Kind/type of the profile family or profile instance.""", json_schema_extra = { "linkml_meta": {'aliases': ['type', 'profile_type'],
         'domain_of': ['CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SignalBinding',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily']} })
    inherits_shared_capabilities: Optional[list[str]] = Field(default=[], description="""Names of shared capabilities inherited by the profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapabilityProfile']} })
    type_specific_capabilities: Optional[list[Capability]] = Field(default=[], description="""Type-specific capabilities declared directly in a profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapabilityProfile', 'ElementSemantics']} })


class NodeLabels(ConfiguredBaseModel):
    """
    Labels used when projecting the profile model into a graph view.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    device: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NodeLabels']} })
    capability_family: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NodeLabels']} })
    profile: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NodeLabels']} })
    capability: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NodeLabels']} })
    signal: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NodeLabels']} })


class GraphProjection(ConfiguredBaseModel):
    """
    Graph projection metadata for node labels and edge categories.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    node_labels: Optional[NodeLabels] = Field(default=None, description="""Node label mapping for the graph projection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GraphProjection']} })
    relationships: Optional[list[RelationshipTypeEnum]] = Field(default=[], description="""Relationship labels used in graph projection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GraphProjection']} })


class ControlProfileFamily(ConfiguredBaseModel):
    """
    A reusable family of control profiles sharing common semantics and structure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['capability_profile_family', 'control_profile_family'],
         'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    kind: Optional[str] = Field(default=None, description="""Kind/type of the profile family or profile instance.""", json_schema_extra = { "linkml_meta": {'aliases': ['type', 'profile_type'],
         'domain_of': ['CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SignalBinding',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily']} })
    shared_capabilities: Optional[dict[str, Capability]] = Field(default=None, description="""Named shared capabilities reused by profile types in a family.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlProfileFamily', 'ElementSemantics']} })
    magnet_type_profiles: Optional[dict[str, CapabilityProfile]] = Field(default=None, description="""Magnet profile definitions keyed by profile name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlProfileFamily']} })
    instrument_type_profiles: Optional[dict[str, CapabilityProfile]] = Field(default=None, description="""Instrument profile definitions keyed by profile name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlProfileFamily']} })
    cavity_type_profiles: Optional[dict[str, CapabilityProfile]] = Field(default=None, description="""RF cavity profile definitions keyed by profile name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlProfileFamily']} })
    graph_projection: Optional[GraphProjection] = Field(default=None, description="""Optional graph projection metadata attached to a profile family.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlProfileFamily']} })


class Beamline(ConfiguredBaseModel):
    """
    An ordered sequence of beamline elements defining a beam path.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    kind: Optional[str] = Field(default=None, description="""Kind/type of the profile family or profile instance.""", json_schema_extra = { "linkml_meta": {'aliases': ['type', 'profile_type'],
         'domain_of': ['CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement']} })
    line: Optional[list[str]] = Field(default=[], description="""Ordered sequence of cross-referenced element names forming a beamline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Beamline']} })


class BeamlineElement(ConfiguredBaseModel):
    """
    A single element in a beamline with optional physics parameter blocks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema',
         'slot_usage': {'kind': {'name': 'kind', 'range': 'ElementKindEnum'},
                        'narad': {'name': 'narad', 'range': 'ElementNaradRef'}}})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    kind: Optional[ElementKindEnum] = Field(default=None, description="""Kind/type of the profile family or profile instance.""", json_schema_extra = { "linkml_meta": {'aliases': ['type', 'profile_type'],
         'domain_of': ['CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement']} })
    length: Optional[float] = Field(default=None, description="""Physical length of the element in meters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement']} })
    RFP: Optional[RFParams] = Field(default=None, description="""RF cavity physics parameters block.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement']} })
    BendP: Optional[BendParams] = Field(default=None, description="""Dipole/bend physics parameters block.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement']} })
    MagneticMultipoleP: Optional[MagneticMultipoleParams] = Field(default=None, description="""Magnetic multipole physics parameters block.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement']} })
    SolenoidP: Optional[SolenoidParams] = Field(default=None, description="""Solenoid physics parameters block.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement']} })
    narad: Optional[ElementNaradRef] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradModel', 'BeamlineElement']} })
    JLabP: Optional[JLabParams] = Field(default=None, description="""JLab-specific element parameters block.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BeamlineElement']} })


class ElementNaradRef(ConfiguredBaseModel):
    """
    NARAD semantic reference block attached to a beamline element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema',
         'slot_usage': {'signal_bindings': {'name': 'signal_bindings',
                                            'range': 'PVBinding'}}})

    capability_profile_family: Optional[str] = Field(default=None, description="""Cross-reference to the control profile family for this element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementNaradRef']} })
    capability_profile: Optional[str] = Field(default=None, description="""Cross-reference to the specific capability profile applied to this element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementNaradRef']} })
    magnet_semantics: Optional[ElementSemantics] = Field(default=None, description="""Magnet-domain semantic context for this element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementNaradRef']} })
    instrument_semantics: Optional[ElementSemantics] = Field(default=None, description="""Instrument-domain semantic context for this element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementNaradRef']} })
    cavity_semantics: Optional[ElementSemantics] = Field(default=None, description="""RF-cavity-domain semantic context for this element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementNaradRef']} })
    signal_bindings: Optional[dict[str, PVBinding]] = Field(default=None, description="""Signal definitions keyed by signal name within a device type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DeviceTypeSignalSet', 'ElementNaradRef']} })


class ElementSemantics(ConfiguredBaseModel):
    """
    Semantic context referencing shared and type-specific capability names for a beamline element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema',
         'slot_usage': {'shared_capabilities': {'name': 'shared_capabilities',
                                                'range': 'string'},
                        'type_specific_capabilities': {'name': 'type_specific_capabilities',
                                                       'range': 'string'}}})

    shared_capabilities: Optional[list[str]] = Field(default=[], description="""Named shared capabilities reused by profile types in a family.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlProfileFamily', 'ElementSemantics']} })
    type_specific_capabilities: Optional[list[str]] = Field(default=[], description="""Type-specific capabilities declared directly in a profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CapabilityProfile', 'ElementSemantics']} })


class PVBinding(ConfiguredBaseModel):
    """
    A concrete PV (Process Variable) binding for one semantic signal on a beamline element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    facility: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig', 'PVBinding']} })
    control_system: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['NaradConfig', 'Facility', 'PVBinding']} })
    pv: Optional[str] = Field(default=None, description="""The EPICS Process Variable name (e.g. MBHK101H.S).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PVBinding']} })


class RFParams(ConfiguredBaseModel):
    """
    RF cavity physics parameters (frequency, voltage, phase).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    frequency: Optional[float] = Field(default=None, description="""RF frequency in Hz.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParams']} })
    voltage: Optional[float] = Field(default=None, description="""RF voltage in volts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParams']} })
    phase: Optional[float] = Field(default=None, description="""RF phase in degrees.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RFParams']} })


class BendParams(ConfiguredBaseModel):
    """
    Dipole/bend physics parameters (entry angle, exit edge angles).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    angle_ref: Optional[float] = Field(default=None, description="""Reference bend angle in radians.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParams']} })
    e1: Optional[float] = Field(default=None, description="""Entry edge angle in radians.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParams']} })
    e2: Optional[float] = Field(default=None, description="""Exit edge angle in radians.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BendParams']} })


class MagneticMultipoleParams(ConfiguredBaseModel):
    """
    Magnetic multipole physics parameters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    kn1: Optional[float] = Field(default=None, description="""First-order magnetic multipole coefficient (quadrupole strength).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MagneticMultipoleParams']} })


class SolenoidParams(ConfiguredBaseModel):
    """
    Solenoid physics parameters.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    ksol: Optional[float] = Field(default=None, description="""Solenoid integrated field strength.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolenoidParams']} })


class JLabParams(ConfiguredBaseModel):
    """
    JLab-specific element parameters: type designation, accelerator model name, and open property map.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    jlab_type: Optional[str] = Field(default=None, description="""JLab-specific element type designation (e.g. WarmCavity, QW, HCorrector). Serialized as 'type' in source YAML; renamed here to avoid conflict with the LinkML metamodel 'type' designator used for polymorphic class selection.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'], 'domain_of': ['JLabParams']} })
    modeled_as: Optional[str] = Field(default=None, description="""Accelerator physics code model element type (e.g. RFCA, KQUAD, HKICK).""", json_schema_extra = { "linkml_meta": {'domain_of': ['JLabParams']} })
    properties: Optional[dict[str, Union[str, KeyValuePair]]] = Field(default=None, description="""Open-ended key-value property map for element-specific parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['JLabParams']} })


class KeyValuePair(ConfiguredBaseModel):
    """
    A generic key-value pair for open-ended property maps.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/narad_linkml/schema/narad/schema'})

    name: str = Field(default=..., description="""Name/identifier of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Facility',
                       'SignalBinding',
                       'DeviceTypeSignalSet',
                       'Signal',
                       'Capability',
                       'CapabilityProfile',
                       'ControlProfileFamily',
                       'Beamline',
                       'BeamlineElement',
                       'PVBinding',
                       'KeyValuePair']} })
    value: Optional[str] = Field(default=None, description="""Property value as a string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KeyValuePair']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NaradModel.model_rebuild()
NaradConfig.model_rebuild()
CapabilityLayer.model_rebuild()
SignalLayer.model_rebuild()
Facility.model_rebuild()
SignalDefinitions.model_rebuild()
SignalBinding.model_rebuild()
DeviceTypeSignalSet.model_rebuild()
Signal.model_rebuild()
Capability.model_rebuild()
CapabilityProfile.model_rebuild()
NodeLabels.model_rebuild()
GraphProjection.model_rebuild()
ControlProfileFamily.model_rebuild()
Beamline.model_rebuild()
BeamlineElement.model_rebuild()
ElementNaradRef.model_rebuild()
ElementSemantics.model_rebuild()
PVBinding.model_rebuild()
RFParams.model_rebuild()
BendParams.model_rebuild()
MagneticMultipoleParams.model_rebuild()
SolenoidParams.model_rebuild()
JLabParams.model_rebuild()
KeyValuePair.model_rebuild()
