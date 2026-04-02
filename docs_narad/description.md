

# Slot: description 



URI: [https://w3id.org/narad_linkml/schema/narad/schema/description](https://w3id.org/narad_linkml/schema/narad/schema/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |  no  |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile, with its own iden... |  no  |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |  no  |
| [Capability](Capability.md) | A grouping of related signals for a control aspect |  no  |
| [SignalBinding](SignalBinding.md) | A named EPICS suffix definition for one semantic signal |  no  |
| [Signal](Signal.md) | A named semantic signal used by a capability |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/description |
| native | https://w3id.org/narad_linkml/schema/narad/schema/description |




## LinkML Source

<details>
```yaml
name: description
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
alias: description
domain_of:
- SignalBinding
- Signal
- Capability
- TypeSpecificCapability
- CapabilityProfile
- ControlProfileFamily
range: string

```
</details>