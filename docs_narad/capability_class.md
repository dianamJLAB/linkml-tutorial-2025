

# Slot: capability_class 


_Semantic class label for a type-specific capability (e.g. QuadrupoleStrengthCapability). Serialized as 'class' in source YAML; renamed here to avoid conflict with reserved keywords._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/capability_class](https://w3id.org/narad_linkml/schema/narad/schema/capability_class)
Alias: capability_class

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypeSpecificCapability](TypeSpecificCapability.md) | An inline capability declared within a device-type profile, with its own iden... |  no  |






## Properties

* Range: [String](String.md)



## Aliases


* class


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/capability_class |
| native | https://w3id.org/narad_linkml/schema/narad/schema/capability_class |




## LinkML Source

<details>
```yaml
name: capability_class
description: Semantic class label for a type-specific capability (e.g. QuadrupoleStrengthCapability).
  Serialized as 'class' in source YAML; renamed here to avoid conflict with reserved
  keywords.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
aliases:
- class
rank: 1000
alias: capability_class
domain_of:
- TypeSpecificCapability
range: string

```
</details>