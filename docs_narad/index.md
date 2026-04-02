# narad

NARAD extension for capability-layer semantics and facility-specific signal bindings

URI: https://w3id.org/narad_linkml/schema/narad/schema

Name: narad



## Classes

| Class | Description |
| --- | --- |
| [Beamline](Beamline.md) | An ordered sequence of beamline elements defining a beam path |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with optional physics parameter blocks |
| [BendParams](BendParams.md) | Dipole/bend physics parameters (entry angle, exit edge angles) |
| [Capability](Capability.md) | A grouping of related signals for a control aspect |
| [CapabilityLayer](CapabilityLayer.md) | Capability-layer container for profile families |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |
| [DeviceTypeSignalSet](DeviceTypeSignalSet.md) | Signal binding set scoped to a device type (for example, Quadrupole or BPM) |
| [ElementNaradRef](ElementNaradRef.md) | NARAD semantic reference block attached to a beamline element |
| [ElementSemantics](ElementSemantics.md) | Semantic context referencing shared and type-specific capability names for a ... |
| [Facility](Facility.md) | A facility with specific signal bindings |
| [GraphProjection](GraphProjection.md) | Graph projection metadata for node labels and edge categories |
| [JLabParams](JLabParams.md) | JLab-specific element parameters: type designation, accelerator model name, a... |
| [KeyValuePair](KeyValuePair.md) | A generic key-value pair for open-ended property maps |
| [MagneticMultipoleParams](MagneticMultipoleParams.md) | Magnetic multipole physics parameters |
| [NaradConfig](NaradConfig.md) | NARAD configuration block containing the capability layer |
| [NaradModel](NaradModel.md) | Top-level NARAD document container |
| [NodeLabels](NodeLabels.md) | Labels used when projecting the profile model into a graph view |
| [PVBinding](PVBinding.md) | A concrete PV (Process Variable) binding for one semantic signal on a beamlin... |
| [RFParams](RFParams.md) | RF cavity physics parameters (frequency, voltage, phase) |
| [Signal](Signal.md) | A named semantic signal used by a capability |
| [SignalBinding](SignalBinding.md) | A named EPICS suffix definition for one semantic signal |
| [SignalDefinitions](SignalDefinitions.md) | Grouped EPICS signal suffix templates by semantic category |
| [SignalLayer](SignalLayer.md) | Signal-layer container for facility-specific signal bindings |
| [SolenoidParams](SolenoidParams.md) | Solenoid physics parameters |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile, with its own iden... |



## Slots

| Slot | Description |
| --- | --- |
| [angle_ref](angle_ref.md) | Reference bend angle in radians |
| [beamlines](beamlines.md) | Ordered list of beamlines in this NARAD document |
| [BendP](BendP.md) | Dipole/bend physics parameters block |
| [capability](capability.md) |  |
| [capability_class](capability_class.md) | Semantic class label for a type-specific capability (e |
| [capability_family](capability_family.md) |  |
| [capability_layer](capability_layer.md) |  |
| [capability_profile](capability_profile.md) | Cross-reference to the specific capability profile applied to this element |
| [capability_profile_family](capability_profile_family.md) | Cross-reference to the control profile family for this element |
| [cavity_semantics](cavity_semantics.md) | RF-cavity-domain semantic context for this element |
| [cavity_signals](cavity_signals.md) | Cavity signal definitions keyed by signal name |
| [cavity_type_profiles](cavity_type_profiles.md) | RF cavity profile definitions keyed by profile name |
| [class](class.md) | Class label used in profile payloads (for example, QuadrupoleStrengthCapabili... |
| [control_system](control_system.md) |  |
| [data_type](data_type.md) | The data type of the signal's value |
| [description](description.md) |  |
| [device](device.md) |  |
| [e1](e1.md) | Entry edge angle in radians |
| [e2](e2.md) | Exit edge angle in radians |
| [elements](elements.md) | Beamline element definitions (referenced by name from beamline line sequences... |
| [epics_suffix](epics_suffix.md) | Facility-specific EPICS suffix for a semantic signal |
| [facilities](facilities.md) | Facility identifiers for facility-specific signal bindings |
| [facility](facility.md) |  |
| [frequency](frequency.md) | RF frequency in Hz |
| [graph_projection](graph_projection.md) | Optional graph projection metadata attached to a profile family |
| [id](id.md) | Unique identifier for the entity |
| [inherits_shared_capabilities](inherits_shared_capabilities.md) | Names of shared capabilities inherited by the profile |
| [instrument_semantics](instrument_semantics.md) | Instrument-domain semantic context for this element |
| [instrument_type_profiles](instrument_type_profiles.md) | Instrument profile definitions keyed by profile name |
| [instrument_type_signals](instrument_type_signals.md) | Instrument-type-specific signal definition groups keyed by device type |
| [intent](intent.md) |  |
| [jlab_type](jlab_type.md) | JLab-specific element type designation (e |
| [JLabP](JLabP.md) | JLab-specific element parameters block |
| [kind](kind.md) | Kind/type of the profile family or profile instance |
| [kn1](kn1.md) | First-order magnetic multipole coefficient (quadrupole strength) |
| [ksol](ksol.md) | Solenoid integrated field strength |
| [length](length.md) | Physical length of the element in meters |
| [line](line.md) | Ordered sequence of cross-referenced element names forming a beamline |
| [magnet_semantics](magnet_semantics.md) | Magnet-domain semantic context for this element |
| [magnet_type_profiles](magnet_type_profiles.md) | Magnet profile definitions keyed by profile name |
| [magnet_type_signals](magnet_type_signals.md) | Magnet-type-specific signal definition groups keyed by device type |
| [MagneticMultipoleP](MagneticMultipoleP.md) | Magnetic multipole physics parameters block |
| [modeled_as](modeled_as.md) | Accelerator physics code model element type (e |
| [name](name.md) | Name/identifier of the entity |
| [naming_convention](naming_convention.md) |  |
| [narad](narad.md) |  |
| [node_labels](node_labels.md) | Node label mapping for the graph projection |
| [phase](phase.md) | RF phase in degrees |
| [profile](profile.md) |  |
| [profiles](profiles.md) | Control profile families keyed by family name |
| [properties](properties.md) | Open-ended key-value property map for element-specific parameters |
| [pv](pv.md) | The EPICS Process Variable name (e |
| [relationships](relationships.md) | Relationship labels used in graph projection |
| [RFP](RFP.md) | RF cavity physics parameters block |
| [role](role.md) | The role of the signal in the control model |
| [schema_version](schema_version.md) |  |
| [shared_capabilities](shared_capabilities.md) | Named shared capabilities reused by profile types in a family |
| [shared_magnet_signals](shared_magnet_signals.md) | Shared magnet signal definitions keyed by signal name |
| [signal](signal.md) |  |
| [signal_bindings](signal_bindings.md) | Signal definitions keyed by signal name within a device type |
| [signal_definitions](signal_definitions.md) |  |
| [signal_layer](signal_layer.md) | Signal-layer container for facility-specific signal bindings |
| [signals](signals.md) | Signals within a capability |
| [SolenoidP](SolenoidP.md) | Solenoid physics parameters block |
| [type_specific_capabilities](type_specific_capabilities.md) | Type-specific capabilities declared directly in a profile, each with an id, c... |
| [units](units.md) | Units of measurement or null for unitless values |
| [value](value.md) | Property value as a string |
| [voltage](voltage.md) | RF voltage in volts |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [DataTypeEnum](DataTypeEnum.md) | Allowed data types for signal values |
| [ElementKindEnum](ElementKindEnum.md) | Controlled vocabulary for beamline element types |
| [RelationshipTypeEnum](RelationshipTypeEnum.md) | Allowed edge labels in the profile-family graph projection |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
