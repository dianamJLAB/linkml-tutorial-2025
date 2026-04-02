

# Slot: facility 



URI: [https://w3id.org/narad_linkml/schema/narad/schema/facility](https://w3id.org/narad_linkml/schema/narad/schema/facility)
Alias: facility

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PVBinding](PVBinding.md) | A concrete PV (Process Variable) binding for one semantic signal on a beamlin... |  no  |
| [NaradConfig](NaradConfig.md) | NARAD configuration block containing the capability layer |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/narad_linkml/schema/narad/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/narad_linkml/schema/narad/schema/facility |
| native | https://w3id.org/narad_linkml/schema/narad/schema/facility |




## LinkML Source

<details>
```yaml
name: facility
from_schema: https://w3id.org/narad_linkml/schema/narad/schema
rank: 1000
alias: facility
domain_of:
- NaradConfig
- PVBinding
range: string

```
</details>