

# Slot: type_specific_capabilities 


_Type-specific capabilities declared directly in a profile, each with an id, class label, description, and signals._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/type_specific_capabilities](https://w3id.org/narad_linkml/schema/narad/schema/type_specific_capabilities)
Alias: type_specific_capabilities

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CapabilityProfile](CapabilityProfile.md) | A device-type profile that reuses shared capabilities and adds specific capab... |  no  |
| [ElementSemantics](ElementSemantics.md) | Semantic context referencing shared and type-specific capability names for a ... |  no  |






## Properties

* Range: [TypeSpecificCapability](TypeSpecificCapability.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/type_specific_capabilities |
| native | https://w3id.org/narad_linkml/schema/narad/schema/type_specific_capabilities |




## LinkML Source

<details>
```yaml
name: type_specific_capabilities
description: Type-specific capabilities declared directly in a profile, each with
  an id, class label, description, and signals.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
alias: type_specific_capabilities
domain_of:
- CapabilityProfile
- ElementSemantics
range: TypeSpecificCapability
multivalued: true
inlined: true
inlined_as_list: true

```
</details>