

# Slot: data_type 


_The data type of the signal's value._





URI: [https://w3id.org/narad_linkml/schema/narad/schema/data_type](https://w3id.org/narad_linkml/schema/narad/schema/data_type)
Alias: data_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Signal](Signal.md) | A named semantic signal used by a capability |  no  |






## Properties

* Range: [DataTypeEnum](DataTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/data_type |
| native | https://w3id.org/narad_linkml/schema/narad/schema/data_type |
| broad | ncit:C42645, qudt:Datatype |




## LinkML Source

<details>
```yaml
name: data_type
description: The data type of the signal's value.
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
broad_mappings:
- ncit:C42645
- qudt:Datatype
rank: 1000
alias: data_type
domain_of:
- Signal
range: DataTypeEnum

```
</details>