

# Slot: name 


_Name/identifier of the entity._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/name](https://w3id.org/narad_linkml/schema/narad/schema/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |  no  |
| [Facility](Facility.md) | A facility with specific signal bindings |  no  |
| [DeviceTypeSignalSet](DeviceTypeSignalSet.md) | Signal binding set scoped to a device type (for example, Quadrupole or BPM) |  no  |
| [Beamline](Beamline.md) | An ordered sequence of beamline elements defining a beam path |  no  |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |  no  |
| [PVBinding](PVBinding.md) | A concrete PV (Process Variable) binding for one semantic signal on a beamlin... |  no  |
| [Capability](Capability.md) | A grouping of related signals for a control aspect |  no  |
| [KeyValuePair](KeyValuePair.md) | A generic key-value pair for open-ended property maps |  no  |
| [SignalBinding](SignalBinding.md) | A named EPICS suffix definition for one semantic signal |  no  |
| [Signal](Signal.md) | A named semantic signal used by a capability |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with optional physics parameter blocks |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/name |
| native | https://w3id.org/narad_linkml/schema/narad/schema/name |




## LinkML Source

<details>
```yaml
name: name
description: Name/identifier of the entity.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
identifier: true
alias: name
domain_of:
- Facility
- SignalBinding
- DeviceTypeSignalSet
- Signal
- Capability
- CapabilityProfile
- ControlProfileFamily
- Beamline
- BeamlineElement
- PVBinding
- KeyValuePair
range: string
required: true

```
</details>