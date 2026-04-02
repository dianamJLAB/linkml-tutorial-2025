

# Slot: signals 


_Signals within a capability._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/signals](https://w3id.org/narad_linkml/schema/narad/schema/signals)
Alias: signals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile, with its own iden... |  no  |
| [Capability](Capability.md) | A grouping of related signals for a control aspect |  no  |






## Properties

* Range: [Signal](Signal.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/signals |
| native | https://w3id.org/narad_linkml/schema/narad/schema/signals |




## LinkML Source

<details>
```yaml
name: signals
description: Signals within a capability.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
alias: signals
domain_of:
- Capability
- TypeSpecificCapability
range: Signal
multivalued: true
inlined: true
inlined_as_list: true

```
</details>