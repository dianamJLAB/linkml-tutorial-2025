

# Slot: kind 


_Kind/type of the profile family or profile instance._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/kind](https://w3id.org/narad_linkml/schema/narad/schema/kind)
Alias: kind

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |  no  |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |  no  |
| [Beamline](Beamline.md) | An ordered sequence of beamline elements defining a beam path |  no  |
| [BeamlineElement](BeamlineElement.md) | A single element in a beamline with optional physics parameter blocks |  yes  |






## Properties

* Range: [String](String.md)



## Aliases


* type
* profile_type


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/kind |
| native | https://w3id.org/narad_linkml/schema/narad/schema/kind |




## LinkML Source

<details>
```yaml
name: kind
description: Kind/type of the profile family or profile instance.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
aliases:
- type
- profile_type
rank: 1000
alias: kind
domain_of:
- CapabilityProfile
- ControlProfileFamily
- Beamline
- BeamlineElement
range: string

```
</details>