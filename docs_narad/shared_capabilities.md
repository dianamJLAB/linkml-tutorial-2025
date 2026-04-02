

# Slot: shared_capabilities 


_Named shared capabilities reused by profile types in a family._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/shared_capabilities](https://w3id.org/narad_linkml/schema/narad/schema/shared_capabilities)
Alias: shared_capabilities

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ControlProfileFamily](ControlProfileFamily.md) | A reusable family of control profiles sharing common semantics and structure |  no  |
| [ElementSemantics](ElementSemantics.md) | Semantic context referencing shared and type-specific capability names for a ... |  no  |






## Properties

* Range: [Capability](Capability.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/shared_capabilities |
| native | https://w3id.org/narad_linkml/schema/narad/schema/shared_capabilities |




## LinkML Source

<details>
```yaml
name: shared_capabilities
description: Named shared capabilities reused by profile types in a family.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
alias: shared_capabilities
domain_of:
- ControlProfileFamily
- ElementSemantics
range: Capability
multivalued: true
inlined: true

```
</details>