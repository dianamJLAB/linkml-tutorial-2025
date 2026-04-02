

# Slot: jlab_type 


_JLab-specific element type designation (e.g. WarmCavity, QW, HCorrector). Serialized as 'type' in source YAML; renamed here to avoid conflict with the LinkML metamodel 'type' designator used for polymorphic class selection._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/jlab_type](https://w3id.org/narad_linkml/schema/narad/schema/jlab_type)
Alias: jlab_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [JLabParams](JLabParams.md) | JLab-specific element parameters: type designation, accelerator model name, a... |  no  |






## Properties

* Range: [String](String.md)



## Aliases


* type


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/jlab_type |
| native | https://w3id.org/narad_linkml/schema/narad/schema/jlab_type |




## LinkML Source

<details>
```yaml
name: jlab_type
description: JLab-specific element type designation (e.g. WarmCavity, QW, HCorrector).
  Serialized as 'type' in source YAML; renamed here to avoid conflict with the LinkML
  metamodel 'type' designator used for polymorphic class selection.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
aliases:
- type
rank: 1000
alias: jlab_type
domain_of:
- JLabParams
range: string

```
</details>